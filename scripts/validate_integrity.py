#!/usr/bin/env python3
"""Detect destructive changes to historical documentation using Git comparisons."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

MARKER_RE = {
    "evidence": re.compile(
        r"<!-- BEGIN EVIDENCE: (EV-(?:\d{8}-\d{3}|YYYYMMDD-NNN)) -->.*?<!-- END EVIDENCE: \1 -->",
        re.DOTALL,
    ),
    "appendment": re.compile(
        r"<!-- BEGIN APPENDMENT: (APP-[A-Z0-9-]+) -->.*?<!-- END APPENDMENT: \1 -->",
        re.DOTALL,
    ),
}


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        text=True,
        capture_output=True,
        check=check,
    )


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        visible: dict[str, str] = {}
        for line in lines:
            match = re.match(r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.*?)\s*$", line)
            if match:
                visible[match.group(1)] = match.group(2)
        return visible
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            values: dict[str, str] = {}
            for line in lines[1:end]:
                match = re.match(r"^([A-Za-z][A-Za-z0-9 _-]*):\s*(.*)$", line)
                if match:
                    values[match.group(1)] = match.group(2).strip().strip("\"'")
            return values
    return {}


def git_content(root: Path, revision: str, path: str) -> str | None:
    result = git(root, "show", f"{revision}:{path}", check=False)
    return result.stdout if result.returncode == 0 else None


def revision_base(root: Path, requested: str | None) -> str | None:
    if requested and set(requested) == {"0"}:
        print("Integrity validation: initial history has no prior baseline; static checks only.")
        return None
    if requested:
        resolved = git(root, "rev-parse", "--verify", f"{requested}^{{commit}}", check=False)
        if resolved.returncode:
            raise ValueError(f"Requested Git baseline is unavailable: {requested}")
        merge_base = git(root, "merge-base", resolved.stdout.strip(), "HEAD", check=False)
        if merge_base.returncode:
            raise ValueError(f"Requested Git baseline has no common ancestor with HEAD: {requested}")
        return merge_base.stdout.strip()
    parent = git(root, "rev-parse", "--verify", "HEAD^", check=False)
    if parent.returncode:
        print("Integrity validation: initial history has no prior commit; static checks only.")
        return None
    return parent.stdout.strip()


def changed_paths(root: Path, base: str | None) -> set[str]:
    changed: set[str] = set()
    if base:
        for args in (
            ("diff", "--name-only", f"{base}...HEAD"),
            ("diff", "--name-only", base),
            ("diff", "--cached", "--name-only", base),
        ):
            result = git(root, *args, check=False)
            if result.returncode:
                raise ValueError(f"Unable to compare Git baseline {base}: {result.stderr.strip()}")
            changed.update(path for path in result.stdout.splitlines() if path)
    else:
        result = git(root, "ls-files", "--cached", "--others", "--exclude-standard", check=False)
        if result.returncode:
            raise ValueError(f"Unable to list repository files: {result.stderr.strip()}")
        changed.update(path for path in result.stdout.splitlines() if path)
    untracked = git(root, "ls-files", "--others", "--exclude-standard")
    changed.update(path for path in untracked.stdout.splitlines() if path)
    return changed


def markdown_section(text: str, title: str) -> str | None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not match or match.group(2).strip() != title:
            continue
        level = len(match.group(1))
        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            next_heading = re.match(r"^(#{1,6})\s+", lines[next_index])
            if next_heading and len(next_heading.group(1)) <= level:
                end = next_index
                break
        return "\n".join(lines[index + 1 : end]).strip()
    return None


def original_observation(text: str) -> str | None:
    section = markdown_section(text, "Original Observation")
    if section is None:
        return None
    begin = "<!-- BEGIN PROTECTED: original-observation -->"
    end = "<!-- END PROTECTED: original-observation -->"
    if begin in section and end in section:
        return section.split(begin, 1)[1].split(end, 1)[0].strip()
    return section


def corrections_preserve_original(text: str, original: str) -> bool:
    correction = markdown_section(text, "Correction Records")
    if correction is None:
        correction = markdown_section(text, "Corrections")
    if correction is None:
        return False
    labels = (
        re.search(r"(?i)original statement", correction),
        re.search(r"(?i)reason", correction),
        re.search(r"(?i)correction timestamp", correction),
    )
    return all(labels) and original and original in correction


def marker_records(text: str, kind: str) -> dict[str, str]:
    return {match.group(1): match.group(0) for match in MARKER_RE[kind].finditer(text)}


def historical_ids(root: Path, base: str, directory: str) -> tuple[set[str], set[str]]:
    current_ids: set[str] = set()
    listing = git(root, "ls-tree", "-r", "--name-only", base, "--", directory)
    for path in listing.stdout.splitlines():
        if not path.endswith(".md") or path.endswith("/INDEX.md"):
            continue
        text = git_content(root, base, path) or ""
        fields = front_matter(text)
        current_ids.update(
            value
            for value in (
                fields.get("Document ID", ""),
                fields.get("Scenario Number", ""),
                fields.get("Countermeasure Number", ""),
            )
            if re.fullmatch(r"(?:SCN|CM)-\d{3}", value)
        )
    log = git(root, "log", "--all", "-p", "--", f"{directory}/*.md", check=False)
    ever_ids = set(
        re.findall(r"(?m)^\+\s*(?:Document ID|Scenario Number|Countermeasure Number):\s*((?:SCN|CM)-\d{3})\s*$", log.stdout)
    )
    return current_ids, ever_ids


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--base",
        default=None,
        help="Git base revision; omitted uses HEAD^ when available, all-zero SHA means no baseline.",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[tuple[str, str, str | None, str]] = []

    def report(path: str, rule: str, message: str, action: str, text: str | None = None, term: str | None = None) -> None:
        line = None
        if text is not None and term:
            position = text.find(term)
            if position >= 0:
                line = text.count("\n", 0, position) + 1
        errors.append((path, rule, f"{message}" + (f" (line {line})" if line else ""), action))

    try:
        base = revision_base(root, args.base)
        changed = changed_paths(root, base)
    except (ValueError, subprocess.CalledProcessError) as error:
        print(f"INTEGRITY-001: {error} Suggested action: provide a valid fetched Git baseline.")
        return 1

    for directory, rule in (("scenarios", "INTEGRITY-006"), ("countermeasures", "INTEGRITY-006")):
        current_ids, ever_ids = historical_ids(root, base, directory) if base else (set(), set())
        prefix = "SCN-" if directory == "scenarios" else "CM-"
        for path in sorted((root / directory).glob("*.md")) if (root / directory).is_dir() else []:
            if path.name == "INDEX.md":
                continue
            text = path.read_text(encoding="utf-8")
            metadata = front_matter(text)
            identifier = metadata.get("Document ID", "")
            if base and identifier.startswith(prefix) and identifier not in current_ids and identifier in ever_ids:
                report(
                    path.relative_to(root).as_posix(),
                    rule,
                    f"Identifier {identifier} was used in repository history and is retired or reassigned.",
                    "Assign a never-used permanent identifier; do not reuse retired identifiers.",
                    text,
                    identifier,
                )

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts or path.name == "CHANGELOG.md":
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        metadata = front_matter(text)
        if metadata and not re.search(r"(?m)^##\s+(?:Template )?Revision History\s*$", text):
            report(relative, "INTEGRITY-007", "Revision history section is missing.", "Restore the revision history section.", text, "Document ID")
        for kind, pattern in MARKER_RE.items():
            if path.parent == root / "templates":
                continue
            begins = len(re.findall(rf"<!-- BEGIN {kind.upper()}:", text))
            ends = len(re.findall(rf"<!-- END {kind.upper()}:", text))
            records = len(marker_records(text, kind))
            if begins != records or ends != records:
                report(
                    relative,
                    "INTEGRITY-003" if kind == "evidence" else "INTEGRITY-004",
                    f"{kind.title()} preservation markers are incomplete or mismatched.",
                    "Restore matching stable BEGIN/END markers and preserve the complete original record.",
                    text,
                    f"<!-- BEGIN {kind.upper()}:",
                )

    if base:
        for relative in sorted(changed):
            if not relative.endswith(".md") or relative == "CHANGELOG.md":
                continue
            old = git_content(root, base, relative)
            current_path = root / relative
            current = current_path.read_text(encoding="utf-8") if current_path.is_file() else None
            if old is None:
                continue
            if current is None:
                if relative.startswith(("scenarios/", "countermeasures/")) and not relative.endswith("/INDEX.md"):
                    report(
                        relative,
                        "INTEGRITY-001",
                        "Previously published scenario or countermeasure document was removed.",
                        "Restore the document; retire it only through an explicitly authorized, auditable correction.",
                    )
                continue
            old_meta, new_meta = front_matter(old), front_matter(current)
            if old_meta.get("Document ID") and old_meta.get("Document ID") != new_meta.get("Document ID"):
                report(
                    relative,
                    "INTEGRITY-005",
                    "Established Document ID changed.",
                    "Restore the original identifier; identifiers are permanent and must not be renumbered.",
                    current,
                    "Document ID:",
                )
            if relative.startswith("scenarios/") and not relative.endswith("/INDEX.md"):
                old_number = old_meta.get("Scenario Number")
                new_number = new_meta.get("Scenario Number")
                if old_number and old_number != new_number:
                    report(
                        relative,
                        "INTEGRITY-006",
                        f"Scenario number changed from {old_number} to {new_number}.",
                        "Restore the permanent scenario number; do not renumber published scenarios.",
                        current,
                        "Scenario Number:",
                    )

            old_observation = original_observation(old)
            new_observation = original_observation(current)
            if old_observation is not None and new_observation is None:
                report(
                    relative,
                    "INTEGRITY-002",
                    "Original Observation section was removed.",
                    "Restore the historical section; corrections must follow governance/ANTI_DRIFT.md.",
                    current,
                )
            elif old_observation is not None and old_observation != new_observation:
                if not corrections_preserve_original(current, old_observation):
                    report(
                        relative,
                        "INTEGRITY-008",
                        "Protected original observation was changed or replaced, potentially by a summary.",
                        "Restore the exact historical text, or add an auditable correction record preserving it and identifying the reason and timestamp.",
                        current,
                        "## Original Observation",
                    )

            for kind, rule in (("evidence", "INTEGRITY-003"), ("appendment", "INTEGRITY-004")):
                old_records = marker_records(old, kind)
                new_records = marker_records(current, kind)
                for identifier, old_record in old_records.items():
                    if identifier not in new_records:
                        report(
                            relative,
                            rule,
                            f"Historical {kind} record {identifier} was removed.",
                            "Restore the complete record with its stable identifier; append new information instead of replacing it.",
                            current,
                            identifier,
                        )
                    elif new_records[identifier] != old_record:
                        report(
                            relative,
                            "INTEGRITY-008",
                            f"Protected {kind} record {identifier} was modified.",
                            "Restore the original record and add subsequent information as a separate appendment.",
                            current,
                            identifier,
                        )

            for heading, rule in (
                ("Original Observation", "INTEGRITY-002"),
                ("Evidence References", "INTEGRITY-003"),
                ("Appendments", "INTEGRITY-004"),
            ):
                before = markdown_section(old, heading)
                after = markdown_section(current, heading)
                if before is not None and after is None:
                    report(
                        relative,
                        rule,
                        f"Historical '{heading}' section was removed.",
                        "Restore the section and its historical records; do not delete protected history.",
                        current,
                        f"## {heading}",
                    )
            if re.search(r"(?i)\bsupersed(?:e|ed|es)\b", current):
                correction = markdown_section(current, "Correction Records") or markdown_section(current, "Corrections") or ""
                if not all(
                    re.search(pattern, correction, re.IGNORECASE)
                    for pattern in ("original statement", "reason", "correction timestamp")
                ):
                    report(
                        relative,
                        "INTEGRITY-010",
                        "A finding is described as superseded without required correction references.",
                        "Document the original statement, correction, reason, and correction timestamp under a correction section.",
                        current,
                        "supersed",
                    )

    if errors:
        for path, rule, message, action in errors:
            print(f"{path}: {rule}: {message} Suggested action: {action}")
        print(f"Integrity validation failed with {len(errors)} error(s).")
        return 1
    print("Historical integrity validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
