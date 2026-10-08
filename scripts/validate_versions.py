#!/usr/bin/env python3
"""Validate document metadata and version changes against a Git baseline."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
REVISION_RE = re.compile(
    r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
)
CHANGELOG_RE = re.compile(
    r"^\|\s*([^|]+)\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|$"
)
REQUIRED = ("Document Title", "Document ID", "Author", "Version", "Created", "Last Updated")


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        text=True,
        capture_output=True,
        check=check,
    )


def front_matter(text: str) -> tuple[dict[str, str], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            result: dict[str, str] = {}
            for line in lines[1:end]:
                match = re.match(r"^([A-Za-z][A-Za-z0-9 _-]*):\s*(.*)$", line)
                if match:
                    result[match.group(1)] = match.group(2).strip().strip("\"'")
            return result, end + 1
    return {}, 0


def document_metadata(text: str, relative: str) -> tuple[dict[str, str], int]:
    metadata, end = front_matter(text)
    if metadata or relative != "README.md":
        return metadata, end
    visible: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.*?)\s*$", line)
        if match:
            visible[match.group(1)] = match.group(2)
    return (visible, 0) if visible.get("Document ID") else ({}, 0)


def iso_timestamp(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None


def revision_rows(text: str) -> list[tuple[str, str, str, str]]:
    rows = []
    for line in text.splitlines():
        match = REVISION_RE.match(line)
        if match:
            rows.append(tuple(part.strip() for part in match.groups()))
    return rows


def document_revision_history(text: str) -> str:
    lines = text.splitlines()
    headings = [
        index
        for index, line in enumerate(lines)
        if re.match(r"^##\s+(?:Template )?Revision History\s*$", line)
    ]
    return "\n".join(lines[headings[-1] + 1 :]) if headings else ""


def version_tuple(value: str) -> tuple[int, int, int] | None:
    if not VERSION_RE.fullmatch(value):
        return None
    return tuple(int(part) for part in value.split("."))  # type: ignore[return-value]


def is_valid_increment(old: str, new: str) -> bool:
    previous = version_tuple(old)
    current = version_tuple(new)
    if previous is None or current is None or current <= previous:
        return False
    major, minor, patch = previous
    return current in (
        (major, minor, patch + 1),
        (major, minor + 1, 0),
        (major + 1, 0, 0),
    )


def normalize_for_content_comparison(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for end in range(1, len(lines)):
            if lines[end].strip() == "---":
                for index in range(1, end):
                    if re.match(r"^(Version|Last Updated):", lines[index]):
                        lines[index] = ""
                break
    normalized = []
    for line in lines:
        if REVISION_RE.match(line):
            continue
        normalized.append(line)
    return "\n".join(normalized).strip()


def determine_baseline(root: Path, requested: str | None) -> str | None:
    if requested and set(requested) == {"0"}:
        print("Version validation: initial history has no prior baseline; static checks only.")
        return None
    if requested:
        result = git(root, "rev-parse", "--verify", f"{requested}^{{commit}}", check=False)
        if result.returncode:
            raise ValueError(f"Requested Git baseline is unavailable: {requested}")
        resolved = result.stdout.strip()
        merge_base = git(root, "merge-base", resolved, "HEAD", check=False)
        if merge_base.returncode:
            raise ValueError(f"Requested Git baseline has no common ancestor with HEAD: {requested}")
        return merge_base.stdout.strip()
    result = git(root, "rev-parse", "--verify", "HEAD^", check=False)
    if result.returncode:
        print("Version validation: initial history has no prior commit; static checks only.")
        return None
    return result.stdout.strip()


def changed_paths(root: Path, baseline: str | None) -> set[str]:
    changed: set[str] = set()
    if baseline:
        merge_base = git(root, "merge-base", baseline, "HEAD", check=False)
        base = merge_base.stdout.strip() if merge_base.returncode == 0 else baseline
        for args in (
            ("diff", "--name-only", f"{base}...HEAD"),
            ("diff", "--name-only", base),
            ("diff", "--cached", "--name-only", base),
        ):
            result = git(root, *args, check=False)
            if result.returncode:
                raise ValueError(f"Unable to compare Git baseline {base}: {result.stderr.strip()}")
            changed.update(line for line in result.stdout.splitlines() if line)
    else:
        result = git(root, "ls-files", "--cached", "--others", "--exclude-standard", check=False)
        if result.returncode:
            raise ValueError(f"Unable to list repository files: {result.stderr.strip()}")
        changed.update(line for line in result.stdout.splitlines() if line)
    untracked = git(root, "ls-files", "--others", "--exclude-standard")
    changed.update(line for line in untracked.stdout.splitlines() if line)
    return changed


def content_at(root: Path, revision: str, path: str) -> str | None:
    result = git(root, "show", f"{revision}:{path}", check=False)
    return result.stdout if result.returncode == 0 else None


def validate_changelog(root: Path) -> list[tuple[str, str]]:
    path = root / "CHANGELOG.md"
    errors: list[tuple[str, str]] = []
    if not path.is_file():
        return [("CHANGELOG.md", "VERSION-010: repository changelog is missing.")]
    rows: list[tuple[datetime, str, str]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = CHANGELOG_RE.match(line)
        if not match:
            continue
        timestamp, document, previous, new, description, author = (
            part.strip() for part in match.groups()
        )
        parsed = iso_timestamp(timestamp)
        if parsed is None:
            errors.append(("CHANGELOG.md", f"VERSION-010:{line_number}: changelog timestamp is not valid offset-aware ISO 8601."))
            continue
        if not document or not description or not author:
            errors.append(("CHANGELOG.md", f"VERSION-010:{line_number}: changelog entry requires a document, change summary, and author."))
        if previous != "N/A" and version_tuple(previous) is None:
            errors.append(("CHANGELOG.md", f"VERSION-010:{line_number}: previous version is not semantic or N/A."))
        if new != "N/A" and version_tuple(new) is None:
            errors.append(("CHANGELOG.md", f"VERSION-010:{line_number}: new version is not semantic or N/A."))
        rows.append((parsed, timestamp, str(line_number)))
    if not rows:
        errors.append(("CHANGELOG.md", "VERSION-010: no timestamped changelog entries were found."))
    for earlier, later in zip(rows, rows[1:]):
        if earlier[0] < later[0]:
            errors.append(("CHANGELOG.md", f"VERSION-010:{later[2]}: entries are not in reverse chronological order."))
    return errors


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
    errors: list[tuple[str, str]] = []
    try:
        baseline = determine_baseline(root, args.base)
        changes = changed_paths(root, baseline)
    except (ValueError, subprocess.CalledProcessError) as error:
        print(f"VERSION-008: {error}")
        return 1

    markdown = sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and path.name != "CHANGELOG.md"
    )
    for path in markdown:
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        metadata, _ = document_metadata(text, relative)
        if relative == "README.md" and not metadata:
            continue
        if not metadata:
            errors.append((relative, "VERSION-001: required document metadata is missing."))
            continue
        for field in REQUIRED:
            if not metadata.get(field):
                errors.append((relative, f"VERSION-001: required field '{field}' is missing."))
        version = metadata.get("Version", "")
        if version_tuple(version) is None:
            errors.append((relative, f"VERSION-001: invalid semantic version '{version}'."))
        created = iso_timestamp(metadata.get("Created", ""))
        updated = iso_timestamp(metadata.get("Last Updated", ""))
        if created is None:
            errors.append((relative, "VERSION-002: Created is not a valid offset-aware ISO 8601 timestamp."))
        if updated is None:
            errors.append((relative, "VERSION-003: Last Updated is not a valid offset-aware ISO 8601 timestamp."))
        if created and updated and updated < created:
            errors.append((relative, "VERSION-004: Last Updated is earlier than Created."))
        rows = revision_rows(document_revision_history(text))
        matching = [row for row in rows if row[0] == version]
        if not rows:
            errors.append((relative, "VERSION-005: revision history table is missing."))
        elif not matching:
            errors.append((relative, f"VERSION-005: revision history does not contain current version {version}."))
        elif metadata.get("Last Updated") and not any(
            row[1] == metadata["Last Updated"] for row in matching
        ):
            errors.append((relative, "VERSION-005: current version's revision timestamp does not match Last Updated."))
        previous_revision_time: datetime | None = None
        for revision_version, timestamp, description, author in rows:
            revision_time = iso_timestamp(timestamp)
            if revision_time is None:
                errors.append((relative, f"VERSION-005: revision {revision_version} has an invalid offset-aware ISO 8601 timestamp."))
                continue
            if not description or not author:
                errors.append((relative, f"VERSION-005: revision {revision_version} must include a description and author."))
            if previous_revision_time and revision_time < previous_revision_time:
                errors.append((relative, f"VERSION-005: revision history is not chronological at version {revision_version}."))
            previous_revision_time = revision_time

        if relative not in changes:
            continue
        previous_text = content_at(root, baseline, relative) if baseline else None
        if previous_text is None:
            recorded_versions = [row[0] for row in rows if version_tuple(row[0]) is not None]
            unique_versions = list(dict.fromkeys(recorded_versions))
            if not unique_versions or unique_versions[0] != "1.0.0":
                errors.append((relative, "VERSION-006: new documents must begin their revision history at 1.0.0."))
            if unique_versions and unique_versions[-1] != version:
                errors.append((relative, f"VERSION-005: latest revision history version does not match metadata version {version}."))
            for earlier, later in zip(unique_versions, unique_versions[1:]):
                if not is_valid_increment(earlier, later):
                    errors.append((relative, f"VERSION-006: revision history has invalid version progression from {earlier} to {later}."))
            continue
        previous, _ = document_metadata(previous_text, relative)
        if not previous:
            if relative != "README.md":
                errors.append((relative, "VERSION-008: existing document has no readable prior metadata."))
                continue
            history = git(
                root,
                "log",
                "--follow",
                "--reverse",
                "--format=%aI",
                baseline,
                "--",
                relative,
                check=False,
            )
            original_timestamp = (
                iso_timestamp(history.stdout.splitlines()[0])
                if history.returncode == 0 and history.stdout.splitlines()
                else None
            )
            current_created = created
            if (
                original_timestamp is None
                or current_created is None
                or current_created.astimezone(timezone.utc)
                != original_timestamp.astimezone(timezone.utc)
            ):
                errors.append((relative, "VERSION-009: README creation timestamp does not match its original Git creation record."))
            previous = {
                "Created": metadata.get("Created", ""),
                "Version": "1.0.0",
                "Last Updated": "",
            }
        if previous.get("Created") != metadata.get("Created"):
            errors.append((relative, "VERSION-009: original Created timestamp changed."))
        substantive = normalize_for_content_comparison(previous_text) != normalize_for_content_comparison(text)
        if substantive:
            old_version = previous.get("Version", "")
            if not is_valid_increment(old_version, version):
                errors.append((relative, f"VERSION-007: substantive change requires one valid version increment from {old_version}; found {version}."))
            if previous.get("Last Updated") == metadata.get("Last Updated"):
                errors.append((relative, "VERSION-008: substantive change did not update Last Updated."))
            if not any(
                row[0] == version
                and row[1] == metadata.get("Last Updated")
                and row[3] == metadata.get("Author")
                for row in rows
            ):
                errors.append((relative, "VERSION-008: revision history must record the new version, modification timestamp, and author."))
        elif version != previous.get("Version"):
            errors.append((relative, "VERSION-007: version changed without a substantive content change."))

    errors.extend(validate_changelog(root))
    if errors:
        for path, message in errors:
            print(f"{path}: {message} Suggested action: correct metadata or revision history using governance/VERSIONING.md.")
        print(f"Version validation failed with {len(errors)} error(s).")
        return 1
    print("Document version and timestamp validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
