#!/usr/bin/env python3
"""Check repository documentation structure, identifiers, and local references."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

METADATA_FIELDS = (
    "Document Title",
    "Document ID",
    "Author",
    "Version",
    "Created",
    "Last Updated",
)
SCENARIO_FIELDS = (
    "Scenario Number",
    "Original Observation Date",
    "Original Observation Time",
    "Time Zone",
    "Category",
)
COUNTERMEASURE_FIELDS = (
    "Countermeasure Number",
    "Category",
    "Associated Scenarios",
)
SCENARIO_SECTIONS = (
    "Scenario Overview",
    "Original Observation",
    "Environmental Context",
    "Chronological Event Record",
    "Observed Patterns",
    "Hypotheses",
    "Investigative Questions",
    "Evidence References",
    "Associated Countermeasures",
    "Investigation Results",
    "Verification",
    "Appendments",
    "Revision History",
)
COUNTERMEASURE_SECTIONS = (
    "Objective",
    "Applicable Conditions",
    "Technical Basis",
    "Required Equipment",
    "Preparation",
    "Procedure",
    "Expected Results",
    "Evidence Collection",
    "Effectiveness Evaluation",
    "Limitations",
    "Safety Considerations",
    "Related Scenarios",
    "Appendments",
    "Revision History",
)
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
SCENARIO_NAME_RE = re.compile(r"^(\d{3})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
COUNTERMEASURE_NAME_RE = re.compile(
    r"^(\d{3})-[a-z0-9]+(?:-[a-z0-9]+)*(?:-countermeasure)?\.md$"
)
LINK_RE = re.compile(r"(?<!!) \[[^\]]*\]\(([^)]+)\)", re.VERBOSE)


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.errors: list[tuple[Path, str, str, int | None, str]] = []
        self.documents: dict[Path, tuple[str, dict[str, str], list[str]]] = {}
        self.document_ids: dict[str, Path] = {}
        self.scenarios: dict[str, Path] = {}
        self.countermeasures: dict[str, Path] = {}
        self.evidence_ids: dict[str, Path] = {}
        self.appendment_ids: dict[tuple[Path, str], int] = {}

    def error(
        self,
        path: Path,
        rule: str,
        message: str,
        line: int | None = None,
        action: str = "Review the document and correct the reported issue.",
    ) -> None:
        self.errors.append((path, rule, message, line, action))

    @staticmethod
    def parse_front_matter(text: str) -> tuple[dict[str, str], int]:
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return {}, 0
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                values: dict[str, str] = {}
                for line in lines[1:index]:
                    match = re.match(r"^([A-Za-z][A-Za-z0-9 _-]*):\s*(.*)$", line)
                    if match:
                        values[match.group(1)] = match.group(2).strip().strip("\"'")
                return values, index + 1
        return {}, 0

    @staticmethod
    def parse_visible_metadata(text: str) -> dict[str, str]:
        values: dict[str, str] = {}
        for line in text.splitlines():
            match = re.match(r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.*?)\s*$", line)
            if match:
                values[match.group(1)] = match.group(2)
        return values if values.get("Document ID") else {}

    def run(self) -> int:
        markdown = sorted(
            path
            for path in self.root.rglob("*.md")
            if ".git" not in path.parts and path.name != "CHANGELOG.md"
        )
        for path in markdown:
            text = path.read_text(encoding="utf-8")
            metadata, _ = self.parse_front_matter(text)
            relative = path.relative_to(self.root)
            if relative == Path("README.md"):
                metadata = metadata or self.parse_visible_metadata(text)
            self.documents[path] = (text, metadata, text.splitlines())
            for identifier in re.findall(
                r"<!-- BEGIN EVIDENCE: (EV-\d{8}-\d{3}) -->", text
            ):
                if identifier in self.evidence_ids:
                    self.error(
                        path,
                        "DOC-002",
                        f"Evidence ID '{identifier}' is also used by {self.relative(self.evidence_ids[identifier])}.",
                        self.find_line(text.splitlines(), identifier),
                        "Assign each evidence item a unique permanent identifier.",
                    )
                else:
                    self.evidence_ids[identifier] = path
            appendment_identifiers = re.findall(
                r"<!-- BEGIN APPENDMENT: (APP-[A-Z0-9-]+) -->", text
            )
            for identifier in appendment_identifiers:
                key = (path, identifier)
                self.appendment_ids[key] = self.appendment_ids.get(key, 0) + 1
                if self.appendment_ids[key] > 1:
                    self.error(
                        path,
                        "DOC-002",
                        f"Appendment ID '{identifier}' is duplicated in this document.",
                        self.find_line(text.splitlines(), identifier),
                        "Assign a unique appendment identifier within its parent document.",
                    )
            if relative == Path("README.md"):
                if metadata:
                    for field in METADATA_FIELDS:
                        if not metadata.get(field):
                            self.error(
                                path,
                                "DOC-001",
                                f"Required visible metadata field '{field}' is missing.",
                                None,
                                "Complete the README metadata fields under governance/VERSIONING.md.",
                            )
                    document_id = metadata.get("Document ID", "")
                    if document_id in self.document_ids:
                        self.error(
                            path,
                            "DOC-002",
                            f"Document ID '{document_id}' is also used by {self.relative(self.document_ids[document_id])}.",
                            None,
                            "Assign a unique permanent document identifier.",
                        )
                    elif document_id:
                        self.document_ids[document_id] = path
                continue
            if not metadata:
                self.error(
                    path,
                    "DOC-001",
                    "Required YAML front matter is missing or malformed.",
                    1,
                    "Add the required document metadata under governance/VERSIONING.md.",
                )
                continue
            for field in METADATA_FIELDS:
                if not metadata.get(field):
                    self.error(
                        path,
                        "DOC-001",
                        f"Required metadata field '{field}' is missing or empty.",
                        1,
                        "Add the missing field using the governed metadata format.",
                    )
            document_id = metadata.get("Document ID", "")
            if document_id:
                if document_id in self.document_ids:
                    self.error(
                        path,
                        "DOC-002",
                        f"Document ID '{document_id}' is also used by "
                        f"{self.relative(self.document_ids[document_id])}.",
                        1,
                        "Assign a unique permanent document identifier.",
                    )
                else:
                    self.document_ids[document_id] = path

        self.collect_catalog()
        self.validate_documents()
        self.validate_indexes()
        self.validate_links()
        self.report()
        return 1 if self.errors else 0

    def collect_catalog(self) -> None:
        scenario_dir = self.root / "scenarios"
        if scenario_dir.is_dir():
            for path in sorted(scenario_dir.glob("*.md")):
                if path.name == "INDEX.md":
                    continue
                match = SCENARIO_NAME_RE.fullmatch(path.name)
                if not match:
                    self.error(
                        path,
                        "DOC-003",
                        "Scenario filename does not follow NNN-descriptive-subject.md.",
                        1,
                        "Use a three-digit permanent scenario number and lowercase hyphenated subject.",
                    )
                    continue
                metadata = self.documents.get(path, ("", {}, []))[1]
                number = match.group(1)
                expected = f"SCN-{number}"
                if metadata.get("Scenario Number") != expected:
                    self.error(
                        path,
                        "DOC-010",
                        f"Scenario Number must match its filename ({expected}).",
                        1,
                        "Keep the filename, Scenario Number, and Document ID aligned.",
                    )
                if metadata.get("Document ID") != expected:
                    self.error(
                        path,
                        "DOC-010",
                        f"Document ID must match its permanent scenario identifier ({expected}).",
                        1,
                        "Use the assigned permanent scenario identifier.",
                    )
                self.add_catalog_id(self.scenarios, expected, path)

        countermeasure_dir = self.root / "countermeasures"
        if countermeasure_dir.is_dir():
            for path in sorted(countermeasure_dir.glob("*.md")):
                if path.name == "INDEX.md":
                    continue
                match = COUNTERMEASURE_NAME_RE.fullmatch(path.name)
                if not match:
                    self.error(
                        path,
                        "DOC-004",
                        "Countermeasure filename does not follow the NNN-descriptive-name convention.",
                        1,
                        "Use a three-digit permanent number and lowercase hyphenated name; an optional -countermeasure suffix is accepted.",
                    )
                    continue
                metadata = self.documents.get(path, ("", {}, []))[1]
                expected = f"CM-{match.group(1)}"
                if metadata.get("Countermeasure Number") != expected:
                    self.error(
                        path,
                        "DOC-010",
                        f"Countermeasure Number must match its filename ({expected}).",
                        1,
                        "Keep the filename, Countermeasure Number, and Document ID aligned.",
                    )
                if metadata.get("Document ID") != expected:
                    self.error(
                        path,
                        "DOC-010",
                        f"Document ID must match its permanent countermeasure identifier ({expected}).",
                        1,
                        "Use the assigned permanent countermeasure identifier.",
                    )
                self.add_catalog_id(self.countermeasures, expected, path)

    def add_catalog_id(
        self, catalog: dict[str, Path], identifier: str, path: Path
    ) -> None:
        if identifier in catalog:
            self.error(
                path,
                "DOC-002",
                f"Identifier '{identifier}' is also used by {self.relative(catalog[identifier])}.",
                1,
                "Assign a unique permanent identifier; never reuse an identifier.",
            )
        else:
            catalog[identifier] = path

    def validate_documents(self) -> None:
        for path, (text, metadata, lines) in self.documents.items():
            if not metadata:
                continue
            relative = path.relative_to(self.root)
            is_template = relative.parts[:1] == ("templates",)
            is_scenario = relative.parent == Path("scenarios") and path.name != "INDEX.md"
            is_countermeasure = (
                relative.parent == Path("countermeasures") and path.name != "INDEX.md"
            )
            if is_scenario or (is_template and "SCENARIO_TEMPLATE" in path.name):
                for field in SCENARIO_FIELDS:
                    if not self.has_document_field(text, metadata, field):
                        self.error(
                            path,
                            "DOC-001",
                            f"Required scenario metadata field '{field}' is missing.",
                            self.find_line(lines, field),
                            "Add the field to scenario metadata; use an approved missing-data designation when unknown.",
                        )
                self.require_sections(path, lines, SCENARIO_SECTIONS)
            if is_countermeasure or (
                is_template and "COUNTERMEASURE_TEMPLATE" in path.name
            ):
                for field in COUNTERMEASURE_FIELDS:
                    if not self.has_document_field(text, metadata, field):
                        self.error(
                            path,
                            "DOC-001",
                            f"Required countermeasure metadata field '{field}' is missing.",
                            self.find_line(lines, field),
                            "Add the required countermeasure metadata field.",
                        )
                self.require_sections(path, lines, COUNTERMEASURE_SECTIONS)
            if is_template:
                for policy in (
                    "governance/VERSIONING.md",
                    "governance/ANTI_DRIFT.md",
                ):
                    if policy not in text:
                        self.error(
                            path,
                            "DOC-005",
                            f"Template does not reference {policy}.",
                            None,
                            "Add a relative link to the authoritative governance document.",
                        )

            if is_scenario or is_countermeasure:
                required_ids = (
                    re.findall(r"(?<![A-Z])CM-\d{3}(?!\d)", text)
                    if is_scenario
                    else re.findall(r"(?<![A-Z])SCN-\d{3}(?!\d)", text)
                )
                catalog = self.countermeasures if is_scenario else self.scenarios
                for identifier in sorted(set(required_ids)):
                    if identifier not in catalog:
                        self.error(
                            path,
                            "DOC-007",
                            f"Reference to unknown identifier '{identifier}'.",
                            self.find_line(lines, identifier),
                            "Correct the identifier or link only to an existing catalog document.",
                        )
            if is_scenario:
                begin = "<!-- BEGIN PROTECTED: original-observation -->"
                end = "<!-- END PROTECTED: original-observation -->"
                observation = self.section_text(lines, "Original Observation")
                if observation is not None and (begin not in observation or end not in observation):
                    self.error(
                        path,
                        "DOC-008",
                        "Published scenario Original Observation lacks stable protected-section markers.",
                        self.find_line(lines, "## Original Observation"),
                        "Wrap the preserved source text in matching BEGIN/END PROTECTED markers.",
                    )

    @staticmethod
    def has_document_field(
        text: str, metadata: dict[str, str], field: str
    ) -> bool:
        return bool(metadata.get(field)) or bool(
            re.search(
                rf"(?m)^\s*{re.escape(field)}:\s*\S.*$",
                text,
            )
        )

    def require_sections(
        self, path: Path, lines: list[str], sections: tuple[str, ...]
    ) -> None:
        headings = {match.group(1).strip() for line in lines if (match := re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line))}
        for section in sections:
            if section not in headings and not (
                section == "Hypotheses" and "Investigative Hypotheses" in headings
            ):
                self.error(
                    path,
                    "DOC-005",
                    f"Required section '## {section}' is missing.",
                    None,
                    "Restore the required section heading without removing historical content.",
                )

    @staticmethod
    def section_text(lines: list[str], title: str) -> str | None:
        for index, line in enumerate(lines):
            match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if not match or match.group(2).strip() != title:
                continue
            level = len(match.group(1))
            end = next(
                (
                    pos
                    for pos in range(index + 1, len(lines))
                    if (heading := re.match(r"^(#{1,6})\s+", lines[pos]))
                    and len(heading.group(1)) <= level
                ),
                len(lines),
            )
            return "\n".join(lines[index + 1 : end])
        return None

    def validate_indexes(self) -> None:
        for directory, catalog, prefix, rule in (
            ("scenarios", self.scenarios, "SCN-", "DOC-012"),
            ("countermeasures", self.countermeasures, "CM-", "DOC-012"),
        ):
            path = self.root / directory / "INDEX.md"
            if not path.is_file():
                self.error(
                    path,
                    rule,
                    "Required library index is missing.",
                    None,
                    "Create the authorized index and list only existing documents.",
                )
                continue
            text = path.read_text(encoding="utf-8")
            for line_number, line in enumerate(text.splitlines(), 1):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if not cells or not cells[0].startswith(prefix):
                    continue
                identifier = cells[0]
                if identifier not in catalog:
                    self.error(
                        path,
                        rule,
                        f"Index references unknown {identifier}.",
                        line_number,
                        "Remove the fictional entry or link to an existing document.",
                    )
                    continue
                links = LINK_RE.findall(line)
                target = self.resolve_link(path, links[0]) if links else None
                if target != catalog[identifier]:
                    self.error(
                        path,
                        rule,
                        f"Index link for {identifier} does not point to its existing document.",
                        line_number,
                        "Use a relative Markdown link to the matching document.",
                    )

    def validate_links(self) -> None:
        for path, (text, _, _) in self.documents.items():
            for match in LINK_RE.finditer(text):
                raw_target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
                if raw_target.startswith(("http://", "https://", "mailto:", "data:")):
                    continue
                target = self.resolve_link(path, raw_target)
                if target is None:
                    self.error(
                        path,
                        "DOC-006",
                        f"Relative Markdown link target '{raw_target}' does not exist.",
                        text.count("\n", 0, match.start()) + 1,
                        "Correct the relative path or remove the broken reference.",
                    )
                    continue
                anchor = raw_target.split("#", 1)[1] if "#" in raw_target else ""
                if anchor and target.is_file() and not self.anchor_exists(target, anchor):
                    self.error(
                        path,
                        "DOC-006",
                        f"Markdown link anchor '#{anchor}' does not exist in {self.relative(target)}.",
                        text.count("\n", 0, match.start()) + 1,
                        "Correct the heading anchor or link to an existing section.",
                    )

    def resolve_link(self, source: Path, target: str) -> Path | None:
        path_part = target.split("#", 1)[0]
        if not path_part:
            return source if source.is_file() else None
        result = (source.parent / path_part).resolve()
        try:
            result.relative_to(self.root)
        except ValueError:
            return None
        return result if result.is_file() else None

    @staticmethod
    def anchor_exists(path: Path, anchor: str) -> bool:
        text = path.read_text(encoding="utf-8")
        heading = anchor.lower().replace("-", " ")
        return any(
            re.sub(r"[^a-z0-9 -]", "", match.group(1).lower()).strip().replace(" ", "-")
            == anchor.lower()
            for line in text.splitlines()
            if (match := re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line))
        ) or heading in text.lower()

    @staticmethod
    def find_line(lines: list[str], text: str) -> int | None:
        for index, line in enumerate(lines, 1):
            if text in line:
                return index
        return None

    def relative(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root))
        except ValueError:
            return str(path)

    def report(self) -> None:
        if not self.errors:
            print("Documentation structure and reference validation passed.")
            return
        for path, rule, message, line, action in self.errors:
            location = self.relative(path)
            if line is not None:
                location += f":{line}"
            print(f"{location}: {rule}: {message} Suggested action: {action}")
        print(f"Documentation validation failed with {len(self.errors)} error(s).")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    return Validator(args.root).run()


if __name__ == "__main__":
    sys.exit(main())
