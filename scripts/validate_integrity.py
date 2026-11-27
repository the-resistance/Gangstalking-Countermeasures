#!/usr/bin/env python3
"""Detect destructive changes to historical documentation using Git comparisons."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from dataclasses import dataclass, field
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


FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
PROTECTED_MARKER_RE = re.compile(r"<!--\s*(BEGIN|END) PROTECTED:\s*([\w-]+)\s*-->")
SUPERSEDED_RE = re.compile(r"(?i)\bsupersed(?:e|ed|es)\b")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
IDENTIFIER_RE = re.compile(r"\b[A-Z]{2,6}-\d{3,8}(?:-\d{3})?\b")
NON_RECORD_PREFIXES = {"SHA", "MD", "UTF", "ISO", "RFC", "CVE", "HTTP"}
FINDING_TERMS_RE = re.compile(
    r"(?i)\b(?:finding|observation|evidence|appendment|hypothesis|conclusion|claim|statement|incident|result|verification)s?\b"
)
REVISION_TITLES = ("Revision History", "Template Revision History")
CORRECTION_TITLES = ("Correction Records", "Corrections")
UNIQUE_TITLES = (
    "Original Observation",
    "Evidence References",
    "Appendments",
    "Correction Records",
    "Corrections",
    "Revision History",
)
FIELD_LINE_RE = re.compile(r"^\s*(?:[-*+]\s+)?(\*\*|__)?([A-Za-z][A-Za-z ]*?)(?:\1)?\s*:\s*(?:\*\*|__)?\s*(.*)$")
FIELD_ALIASES = {
    "original statement": "original",
    "corrected statement": "corrected",
    "correction": "corrected",
    "reason": "reason",
    "reason for correction": "reason",
    "correction timestamp": "timestamp",
    "reference": "reference",
    "references": "reference",
    "corrects": "reference",
    "supersedes": "reference",
}


@dataclass
class Section:
    level: int
    title: str
    heading: int
    start: int
    end: int


@dataclass
class Structure:
    lines: list[str]
    kinds: list[str]
    sections: list[Section]
    problems: list[str] = field(default_factory=list)


@dataclass
class CorrectionRecord:
    line: int
    fields: dict[str, str]
    heading: str


def analyze(text: str) -> Structure:
    """Classify each line as front matter, fenced code, or text and locate validated section boundaries."""
    lines = text.splitlines()
    kinds = ["text"] * len(lines)
    problems: list[str] = []
    first = 0
    if lines and lines[0].strip() == "---":
        close = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if close is None:
            problems.append("Front matter opened at line 1 is never closed.")
        else:
            for i in range(close + 1):
                kinds[i] = "front"
            first = close + 1
    fence: tuple[str, int, int] | None = None
    headings: list[tuple[int, int, str]] = []
    for index in range(first, len(lines)):
        line = lines[index]
        match = FENCE_RE.match(line)
        if fence:
            kinds[index] = "code"
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= fence[1] and not match.group(2).strip():
                fence = None
            continue
        if match and not (match.group(1)[0] == "`" and "`" in match.group(2)):
            fence = (match.group(1)[0], len(match.group(1)), index + 1)
            kinds[index] = "code"
            continue
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((index, len(heading.group(1)), heading.group(2).strip()))
    if fence:
        problems.append(f"Code fence opened at line {fence[2]} is never closed, which hides later section boundaries.")
    sections = []
    for position, (index, level, title) in enumerate(headings):
        end = len(lines)
        for next_index, next_level, _ in headings[position + 1 :]:
            if next_level <= level:
                end = next_index
                break
        sections.append(Section(level, title, index, index + 1, end))
    for title in UNIQUE_TITLES:
        if sum(1 for section in sections if section.title == title) > 1:
            problems.append(f"Section '{title}' appears more than once (duplicate section boundaries).")
    pending: dict[str, int] = {}
    pairs: dict[str, int] = {}
    for index, line in enumerate(lines):
        for kind, name in PROTECTED_MARKER_RE.findall(line):
            if kind == "BEGIN":
                if name in pending:
                    problems.append(f"PROTECTED marker '{name}' at line {index + 1} begins before the previous one ends.")
                pending[name] = index + 1
            elif name in pending:
                del pending[name]
                pairs[name] = pairs.get(name, 0) + 1
            else:
                problems.append(f"PROTECTED marker '{name}' ends at line {index + 1} without a matching BEGIN.")
    for name, line_number in pending.items():
        problems.append(f"PROTECTED marker '{name}' begun at line {line_number} has no matching END.")
    if pairs.get("original-observation", 0) > 1:
        problems.append("Original observation has more than one protected region.")
    return Structure(lines, kinds, sections, problems)


def sections_titled(structure: Structure, titles: tuple[str, ...]) -> list[Section]:
    return [section for section in structure.sections if section.title in titles]


def split_cells(line: str) -> list[str]:
    stripped = line.strip()
    parts = re.split(r"(?<!\\)\|", stripped)
    if stripped.startswith("|"):
        parts = parts[1:]
    if stripped.endswith("|") and not stripped.endswith("\\|"):
        parts = parts[:-1]
    return [part.strip() for part in parts]


TIMESTAMP_FIELD_RE = re.compile(
    r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.(\d+))?(?:(Z)|([+-])(\d{2}):(\d{2}))"
)


def offset_timestamp(value: str) -> dt.datetime | None:
    """Parse a field that is exactly one offset-aware ISO 8601 timestamp, optionally in one balanced code span."""
    text = value.strip()
    if text.startswith("`") or text.endswith("`"):
        wrapper = re.fullmatch(r"(`{1,2})([^`]+)\1", text)
        if not wrapper:
            return None
        text = wrapper.group(2).strip()
    match = TIMESTAMP_FIELD_RE.fullmatch(text)
    if not match:
        return None
    year, month, day, hour, minute, second = (int(match.group(i)) for i in range(1, 7))
    if match.group(8):
        offset = dt.timedelta(0)
    else:
        offset_hours, offset_minutes = int(match.group(10)), int(match.group(11))
        if offset_hours > 23 or offset_minutes > 59:
            return None
        offset = dt.timedelta(hours=offset_hours, minutes=offset_minutes)
        if match.group(9) == "-":
            offset = -offset
    microsecond = int((match.group(7) or "0")[:6].ljust(6, "0"))
    try:
        return dt.datetime(year, month, day, hour, minute, second, microsecond, tzinfo=dt.timezone(offset))
    except ValueError:
        return None


def revision_table(structure: Structure) -> tuple[list[tuple[int, tuple[str, ...]]], list[str]]:
    """Return well-formed revision rows as (line number, cells) and structural problems."""
    rows: list[tuple[int, tuple[str, ...]]] = []
    problems: list[str] = []
    for section in sections_titled(structure, REVISION_TITLES):
        for index in range(section.start, section.end):
            line = structure.lines[index]
            if structure.kinds[index] != "text" or not line.strip().startswith("|"):
                continue
            cells = split_cells(line)
            if cells and cells[0].lower() == "version" or all(re.fullmatch(r":?-+:?", cell) for cell in cells if cell):
                continue
            if len(cells) != 4:
                problems.append(
                    f"Revision row at line {index + 1} is malformed (expected 4 cells, found {len(cells)}; rows may be concatenated)."
                )
            elif not SEMVER_RE.match(cells[0]):
                problems.append(f"Revision row at line {index + 1} has an invalid version '{cells[0]}'.")
            else:
                rows.append((index + 1, tuple(cells)))
    seen: set[str] = set()
    for line_number, cells in rows:
        if cells[0] in seen:
            problems.append(f"Revision row at line {line_number} is a duplicate of version {cells[0]}.")
        seen.add(cells[0])
    return rows, problems


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[>*_`]", " ", value)).strip().lower()


def innermost_section(structure: Structure, index: int) -> Section | None:
    containing = [s for s in structure.sections if s.heading < index < s.end]
    return max(containing, key=lambda section: section.level, default=None)


def block_bounds(structure: Structure, index: int) -> tuple[int, int]:
    lines = structure.lines
    if lines[index].lstrip().startswith(("|", "#")):
        return index, index + 1
    bullet = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
    start = index
    while start > 0 and lines[start - 1].strip() and not HEADING_RE.match(lines[start - 1]):
        if bullet.match(lines[start]):
            break
        start -= 1
    end = index + 1
    while end < len(lines) and lines[end].strip() and not HEADING_RE.match(lines[end]) and not bullet.match(lines[end]):
        end += 1
    return start, end


def identifiers(value: str) -> set[str]:
    return {item for item in IDENTIFIER_RE.findall(value) if item.split("-")[0] not in NON_RECORD_PREFIXES}


def parse_fields(lines: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in lines:
        match = FIELD_LINE_RE.match(line)
        label = FIELD_ALIASES.get(match.group(2).strip().lower()) if match else None
        if label:
            current = label
            fields[label] = (fields.get(label, "") + " " + match.group(3)).strip()
        elif current and line.strip():
            fields[current] = (fields[current] + " " + line.strip().lstrip(">").strip()).strip()
    return fields


def correction_records(structure: Structure) -> list[CorrectionRecord]:
    records: list[CorrectionRecord] = []
    for section in sections_titled(structure, CORRECTION_TITLES):
        children = [child for child in structure.sections if section.heading < child.heading < section.end and child.level > section.level]
        direct = [child for child in children if child.level == min(c.level for c in children)] if children else []
        if direct:
            for child in direct:
                body = structure.lines[child.start : child.end]
                records.append(CorrectionRecord(child.heading + 1, parse_fields(body), child.title))
            continue
        body = structure.lines[section.start : section.end]
        starts = [
            i
            for i, line in enumerate(body)
            if (m := FIELD_LINE_RE.match(line)) and FIELD_ALIASES.get(m.group(2).strip().lower()) == "original"
        ]
        if len(starts) > 1:
            for position, begin in enumerate(starts):
                finish = starts[position + 1] if position + 1 < len(starts) else len(body)
                records.append(CorrectionRecord(section.start + begin + 1, parse_fields(body[begin:finish]), section.title))
        else:
            records.append(CorrectionRecord(section.start + 1, parse_fields(body), section.title))
    return records


def record_problems(record: CorrectionRecord) -> list[str]:
    problems = []
    for key, label in (
        ("original", "original statement"),
        ("corrected", "corrected statement"),
        ("reason", "reason"),
    ):
        if not record.fields.get(key):
            problems.append(f"missing {label}")
    if "timestamp" not in record.fields:
        problems.append("missing correction timestamp")
    elif offset_timestamp(record.fields["timestamp"]) is None:
        problems.append("correction timestamp is not a valid offset-aware ISO 8601 timestamp")
    return problems


@dataclass
class HistoricalFinding:
    identifier: str | None
    text: str
    section: str
    line: int


LEADING_ID_RE = re.compile(r"^\s*(?:[|>]\s*)?(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*|__)?(" + IDENTIFIER_RE.pattern + r")(?:\*\*|__)?(?=$|[\s:.)\-\u2014|])")
EXCLUDED_FINDING_SECTIONS = REVISION_TITLES + CORRECTION_TITLES


def leading_identifier(value: str) -> str | None:
    match = LEADING_ID_RE.match(value)
    return match.group(1) if match and match.group(1) in identifiers(match.group(1)) else None


def historical_findings(structure: Structure) -> list[HistoricalFinding]:
    """Index findings by stable leading identifier (or heading identifier) and validated structural boundaries."""
    findings: list[HistoricalFinding] = []
    excluded = [s for s in structure.sections if s.title in EXCLUDED_FINDING_SECTIONS]
    heading_findings = {
        s.heading: leading_identifier(s.title)
        for s in structure.sections
        if leading_identifier(s.title) and not any(e.heading <= s.heading < e.end for e in excluded)
    }
    for heading, identifier in heading_findings.items():
        section = next(s for s in structure.sections if s.heading == heading)
        parents = [s for s in structure.sections if s.heading < heading < s.end and s.level < section.level]
        body = " ".join(line for i, line in enumerate(structure.lines[section.start : section.end], section.start) if structure.kinds[i] == "text")
        findings.append(HistoricalFinding(identifier, normalize(body), max(parents, key=lambda s: s.level).title if parents else "", heading + 1))
    seen: set[tuple[int, int]] = set()
    for index, line in enumerate(structure.lines):
        stripped = line.strip()
        if structure.kinds[index] != "text" or not stripped or HEADING_RE.match(line) or stripped.startswith("<!--"):
            continue
        section = innermost_section(structure, index)
        if section is None or any(e.heading <= index < e.end for e in excluded):
            continue
        own = leading_identifier(line)
        if section.heading in heading_findings and not own:
            continue
        bounds = block_bounds(structure, index)
        if bounds in seen:
            continue
        seen.add(bounds)
        block = " ".join(structure.lines[bounds[0] : bounds[1]])
        findings.append(HistoricalFinding(leading_identifier(structure.lines[bounds[0]]), normalize(block), section.title, bounds[0] + 1))
    return findings


def reference_identifiers(record: CorrectionRecord) -> set[str]:
    """Target-finding identifiers come only from the record's Reference field, never its own heading or statement."""
    return identifiers(record.fields.get("reference", ""))


def trace_problem(record: CorrectionRecord, historical: str | None, section: str | None = None) -> str | None:
    """Resolve the record to exactly one historical finding whose text contains its original statement."""
    if historical is None:
        return "the historical baseline is unavailable, so traceability is unverified"
    original = normalize(record.fields.get("original", ""))
    if not original:
        return "original statement is empty"
    structure = analyze(historical)
    if structure.problems:
        return "the historical baseline has malformed section boundaries, so resolution is unverified"
    findings = historical_findings(structure)
    targets = reference_identifiers(record)
    if len(targets) > 1:
        return f"conflicting references ({', '.join(sorted(targets))}) name more than one finding"
    if targets:
        target = next(iter(targets))
        matches = [f for f in findings if f.identifier == target]
        if not matches:
            return f"referenced finding {target} was not found in the historical baseline"
        if len(matches) > 1:
            return f"referenced finding {target} is a duplicate identifier in the historical baseline (ambiguous)"
        if original not in matches[0].text:
            return f"original statement does not match the historical finding {target}"
        return None
    observation = original_observation(historical)
    if "original observation" in normalize(record.fields.get("reference", "")):
        if observation is not None and original in normalize(observation):
            return None
        return "original statement does not match the historical Original Observation"
    matches = [f for f in findings if f.identifier is None and original in f.text]
    if not matches:
        return "original statement does not match any identifier-free historical finding"
    if len(matches) > 1:
        return "original statement is ambiguous: it matches more than one historical finding"
    if section is not None and matches[0].section != section:
        return f"original statement is in historical section '{matches[0].section}', not '{section}'"
    return None


def record_traceable(record: CorrectionRecord, historical: str | None, section: str | None = None) -> bool:
    return trace_problem(record, historical, section) is None


def corrections_preserve_original(text: str, original: str) -> bool:
    target = normalize(original)
    return any(
        not record_problems(record) and target and target in normalize(record.fields["original"])
        for record in correction_records(analyze(text))
    )


ADMIN_TERM = r"(?:formatting|format|layout|table|metadata|template|guidance|headings?|markdown|links?|navigation|style|numbering|whitespace|front\s+matter)"
ADMIN_QUALIFIER = r"(?:earlier|previous|prior|old|existing)"
ADMIN_SENTENCE_RES = (
    re.compile(
        rf"(?:(?:version\s+\d+\.\d+\.\d+|this\s+(?:revision|update))\s+)?supersed(?:e|ed|es)\s+(?:the\s+)?(?:{ADMIN_QUALIFIER}\s+)?"
        rf"{ADMIN_TERM}(?:\s+{ADMIN_TERM})?(?:\s+(?:of|in|for|on)\s+(?:this|the)\s+(?:table|document|file|section|page|template))?[.;!?]*",
        re.IGNORECASE,
    ),
    re.compile(
        rf"(?:the\s+)?(?:{ADMIN_QUALIFIER}\s+)?{ADMIN_TERM}(?:\s+{ADMIN_TERM})?\s+(?:(?:was|were|is|are)\s+)?supersed(?:e|ed|es)[.;!?]*",
        re.IGNORECASE,
    ),
)


def sentence_spans(text: str) -> list[tuple[int, int]]:
    spans, start = [], 0
    for boundary in re.finditer(r"[.;!?]+(?=\s|$)", text):
        spans.append((start, boundary.end()))
        start = boundary.end()
    if text[start:].strip():
        spans.append((start, len(text)))
    return [(a, b) for a, b in spans if text[a:b].strip()]


def valid_revision_rows(structure: Structure) -> dict[int, tuple[str, ...]]:
    """Well-formed revision rows (four cells, unique semantic version, offset-aware timestamp, author) by line number."""
    rows, _ = revision_table(structure)
    versions = [cells[0] for _, cells in rows]
    return {
        number: cells
        for number, cells in rows
        if versions.count(cells[0]) == 1 and offset_timestamp(cells[1]) is not None and cells[2] and cells[3]
    }


def is_administrative_revision(
    structure: Structure, index: int, match: re.Match[str], rows: dict[int, tuple[str, ...]] | None = None
) -> bool:
    """A validated revision-table row whose supersession is unambiguously formatting or metadata and whose row concerns no finding."""
    section = innermost_section(structure, index)
    if section is None or section.title not in REVISION_TITLES or structure.kinds[index] != "text":
        return False
    cells = (valid_revision_rows(structure) if rows is None else rows).get(index + 1)
    if cells is None:
        return False
    line = structure.lines[index]
    description = cells[2]
    offset = line.find(description, line.find(cells[1]) + len(cells[1]))
    if offset < 0 or FINDING_TERMS_RE.search(description) or identifiers(description):
        return False
    start = match.start() - offset
    for begin, finish in sentence_spans(description):
        if begin <= start < finish:
            return any(pattern.fullmatch(description[begin:finish].strip()) for pattern in ADMIN_SENTENCE_RES)
    return False


def superseded_problems(structure: Structure, historical: str | None) -> list[tuple[int, str]]:
    """Return (line, message) for supersession claims that lack a complete, linked correction record."""
    records = correction_records(structure)
    correction_ranges = [(s.heading, s.end) for s in sections_titled(structure, CORRECTION_TITLES)]
    revision_rows = valid_revision_rows(structure)
    results: list[tuple[int, str]] = []
    reported_blocks: set[tuple[int, int]] = set()
    for index, line in enumerate(structure.lines):
        matches = list(SUPERSEDED_RE.finditer(line))
        if (
            not matches
            or structure.kinds[index] == "front"
            or all(is_administrative_revision(structure, index, match, revision_rows) for match in matches)
        ):
            continue
        number = index + 1
        inside = None
        for begin, finish in correction_ranges:
            if begin < index < finish:
                inside = max((r for r in records if begin < r.line - 1 < finish and r.line <= number), key=lambda r: r.line, default=None)
        if inside is not None:
            problems = record_problems(inside)
            if not problems:
                trace = trace_problem(inside, historical)
                problems = [trace] if trace else []
            if problems:
                results.append((number, f"Correction record at line {inside.line} is incomplete: {'; '.join(problems)}."))
            continue
        bounds = block_bounds(structure, index)
        if bounds in reported_blocks:
            continue
        reported_blocks.add(bounds)
        block = " ".join(structure.lines[bounds[0] : bounds[1]])
        section = innermost_section(structure, index)
        heading_id = leading_identifier(section.title) if section else None
        leading = leading_identifier(structure.lines[bounds[0]]) or heading_id
        ids = {leading} if leading else set()
        section_title = section.title if section else ""
        linked = [
            record
            for record in records
            if (ids and ids & reference_identifiers(record))
            or (not ids and not reference_identifiers(record) and record.fields.get("original") and normalize(record.fields["original"]) in normalize(block))
        ]
        label = ", ".join(sorted(ids)) if ids else "the statement at this location"
        if not linked:
            hints = [f"record at line {r.line}: {'; '.join(record_problems(r))}" for r in records if record_problems(r)]
            suffix = f" Incomplete records: {'; '.join(hints)}." if hints else ""
            results.append((number, f"A finding ({label}) is described as superseded without a correction record linked to it.{suffix}"))
            continue
        valid = [r for r in linked if not record_problems(r) and record_traceable(r, historical, None if ids else section_title)]
        if not valid:
            detail = "; ".join(
                f"record at line {r.line}: "
                + ("; ".join(record_problems(r)) or trace_problem(r, historical, None if ids else section_title) or "unresolved")
                for r in linked
            )
            results.append((number, f"Correction for {label} is incomplete or untraceable ({detail})."))
    return results


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
    log = git(root, "log", "-p", base, "--", f"{directory}/*.md", check=False)
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
        if path.parent != root / "templates":
            structure = analyze(text)
            for problem in structure.problems:
                report(
                    relative,
                    "INTEGRITY-011",
                    f"Malformed section boundaries: {problem}",
                    "Repair the boundary so headings, fences, and PROTECTED markers are balanced without removing content.",
                )
            for problem in revision_table(structure)[1]:
                report(
                    relative,
                    "INTEGRITY-012",
                    problem,
                    "Keep one complete four-cell row per line and one row per version; append rather than rewrite revisions.",
                )
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

            old_rows, old_row_problems = revision_table(analyze(old))
            current_rows = revision_table(analyze(current))[0]
            if old_rows and not old_row_problems:
                before_rows = [cells for _, cells in old_rows]
                after_rows = [cells for _, cells in current_rows]
                if after_rows[: len(before_rows)] != before_rows:
                    removed = len(after_rows) < len(before_rows)
                    report(
                        relative,
                        "INTEGRITY-012",
                        "Historical revision row was " + ("removed or reordered." if removed else "altered or reordered."),
                        "Restore every baseline revision row unchanged and append new revisions after them.",
                        current,
                        "Revision History",
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
            for line_number, message in superseded_problems(analyze(current), old):
                report(
                    relative,
                    "INTEGRITY-010",
                    f"{message} (line {line_number})",
                    "Add a correction record with the original statement, corrected statement, reason, offset-aware correction timestamp, and a reference to this finding; administrative revision rows are not affected.",
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
