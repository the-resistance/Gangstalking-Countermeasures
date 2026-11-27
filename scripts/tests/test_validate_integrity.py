"""Regression tests for historical integrity validation using isolated Git fixtures."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validate_integrity.py"
CREATED = "2026-10-08T09:00:00-05:00"
TS_BASE = "2026-11-01T09:00:00-06:00"
TS_NEW = "2026-11-27T10:00:00-06:00"
AUTHOR = "Kevin Mahan"
FINDINGS = "FND-001: Beeping is periodic.\n\nFND-002: Beeping stops at night.\n"
SUPERSEDED_FINDINGS = "FND-001: Beeping is periodic. This finding is superseded.\n\nFND-002: Beeping stops at night.\n"


def row(version, timestamp, description):
    return f"| {version} | {timestamp} | {description} | {AUTHOR} |"


BASE_ROWS = [row("1.0.0", TS_BASE, "Initial.")]
NEW_ROW = row("1.1.0", TS_NEW, "Version 1.1.0 superseded the earlier formatting of this table.")


def record(
    cid="COR-001",
    reference="FND-001",
    original="Beeping is periodic.",
    corrected="Beeping is irregular.",
    reason="A longer log showed variance.",
    timestamp=TS_NEW,
):
    lines = [f"### {cid}", ""]
    for label, value in (
        ("Reference", reference),
        ("Original statement", original),
        ("Corrected statement", corrected),
        ("Reason", reason),
        ("Correction timestamp", timestamp),
    ):
        if value is not None:
            lines.append(f"- **{label}:** {value}")
    return "\n".join(lines) + "\n"


def document(
    observation="The beep occurred at 10:00.",
    findings=FINDINGS,
    evidence="Evidence text.",
    appendment="Appendment text.",
    corrections=None,
    rows=BASE_ROWS,
    version="1.0.0",
    end_marker=True,
    revision_prose="",
    appendment_extra="",
):
    parts = [
        f"---\nDocument Title: Fixture\nDocument ID: DOC-001\nAuthor: {AUTHOR}\nVersion: {version}\n"
        f"Created: {CREATED}\nLast Updated: {TS_BASE}\n---\n\n# Fixture\n"
    ]
    if observation is not None:
        end = "<!-- END PROTECTED: original-observation -->\n" if end_marker else ""
        parts.append(
            "\n## Original Observation\n\n<!-- BEGIN PROTECTED: original-observation -->\n"
            f"{observation}\n{end}"
        )
    parts.append(f"\n## Findings\n\n{findings}")
    parts.append(
        "\n## Evidence References\n\n<!-- BEGIN EVIDENCE: EV-20261101-001 -->\n"
        f"{evidence}\n<!-- END EVIDENCE: EV-20261101-001 -->\n"
    )
    parts.append("\n## Appendments\n\n")
    if appendment is not None:
        parts.append(f"<!-- BEGIN APPENDMENT: APP-001 -->\n{appendment}\n<!-- END APPENDMENT: APP-001 -->\n")
    parts.append(appendment_extra)
    if corrections is not None:
        parts.append(f"\n## Correction Records\n\n{corrections}")
    parts.append(
        "\n## Revision History\n\n"
        + (revision_prose + "\n\n" if revision_prose else "")
        + "| Version | Timestamp | Description | Author |\n|---------|-----------|-------------|--------|\n"
        + "\n".join(rows)
        + "\n"
    )
    return "".join(parts)


class IntegrityTestCase(unittest.TestCase):
    def git(self, root, *args):
        subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@example.com", "-c", "commit.gpgsign=false", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
        )

    def run_validator(self, current, base=None):
        base = document() if base is None else base
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.git(root, "init", "-q")
            (root / "doc.md").write_text(base, encoding="utf-8")
            self.git(root, "add", ".")
            self.git(root, "commit", "-q", "-m", "base")
            (root / "doc.md").write_text(current, encoding="utf-8")
            return subprocess.run(
                ["python3", str(SCRIPT), "--root", str(root), "--base", "HEAD"], capture_output=True, text=True
            )

    def assertPasses(self, current, base=None):
        result = self.run_validator(current, base)
        self.assertEqual(result.returncode, 0, result.stdout)

    def assertFails(self, current, rule, base=None, fragment=""):
        result = self.run_validator(current, base)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(rule, result.stdout)
        self.assertIn(fragment, result.stdout)

    def corrected(self, **kwargs):
        return document(
            findings=SUPERSEDED_FINDINGS,
            corrections=record(**kwargs),
            rows=BASE_ROWS + [row("1.0.1", TS_NEW, "Corrected FND-001.")],
        )


class SupersededDetectionTests(IntegrityTestCase):
    def test_int_001_administrative_superseded_reference_passes(self):
        self.assertPasses(document(rows=BASE_ROWS + [NEW_ROW], version="1.1.0"))

    def test_int_002_superseded_finding_without_correction_fails(self):
        self.assertFails(document(findings=SUPERSEDED_FINDINGS), "INTEGRITY-010")

    def test_int_003_complete_linked_correction_passes(self):
        self.assertPasses(self.corrected())

    def test_int_004_missing_original_statement_fails(self):
        self.assertFails(self.corrected(original=None), "INTEGRITY-010", fragment="original statement")

    def test_int_005_missing_correction_reason_fails(self):
        self.assertFails(self.corrected(reason=None), "INTEGRITY-010", fragment="reason")

    def test_int_006_missing_or_invalid_timestamp_fails(self):
        self.assertFails(self.corrected(timestamp=None), "INTEGRITY-010", fragment="timestamp")
        self.assertFails(self.corrected(timestamp="2026-11-27T10:00:00"), "INTEGRITY-010", fragment="timestamp")
        self.assertFails(self.corrected(timestamp="yesterday"), "INTEGRITY-010", fragment="timestamp")

    def test_int_013_unrelated_correction_reference_fails(self):
        current = document(
            findings=SUPERSEDED_FINDINGS,
            corrections=record(cid="COR-002", reference="FND-002", original="Beeping stops at night."),
        )
        self.assertFails(current, "INTEGRITY-010")

    def test_complete_correction_for_other_finding_does_not_satisfy_second_finding(self):
        findings = "FND-001: Beeping is periodic. This finding is superseded.\n\nFND-002: Beeping stops at night. Superseded.\n"
        self.assertFails(document(findings=findings, corrections=record()), "INTEGRITY-010", fragment="FND-002")

    def test_missing_corrected_statement_fails(self):
        self.assertFails(self.corrected(corrected=None), "INTEGRITY-010", fragment="corrected statement")

    def test_untraceable_original_statement_fails(self):
        self.assertFails(self.corrected(original="Something never recorded."), "INTEGRITY-010")

    def test_finding_without_identifier_links_by_original_statement(self):
        base = document(findings="Beeping is periodic.\n")
        findings = "Beeping is periodic. This finding is superseded.\n"
        passing = document(findings=findings, corrections=record(reference="Findings section"), version="1.0.1")
        self.assertPasses(passing, base)
        unrelated = record(reference="Findings section", original="The beep occurred at 10:00.")
        self.assertFails(document(findings=findings, corrections=unrelated), "INTEGRITY-010", base)

    def test_superseded_prose_under_revision_heading_is_not_exempt(self):
        current = document(revision_prose="FND-001 is superseded by newer measurements.", rows=BASE_ROWS)
        self.assertFails(current, "INTEGRITY-010")

    def test_revision_row_superseding_a_finding_requires_correction(self):
        rows = BASE_ROWS + [row("1.1.0", TS_NEW, "Finding FND-001 superseded by a newer measurement.")]
        self.assertFails(document(rows=rows, version="1.1.0"), "INTEGRITY-010")

    def test_revision_row_superseding_a_finding_passes_with_linked_correction(self):
        rows = BASE_ROWS + [row("1.1.0", TS_NEW, "Finding FND-001 superseded by a newer measurement.")]
        current = document(rows=rows, version="1.1.0", corrections=record())
        self.assertPasses(current)

    def test_impossible_calendar_timestamp_fails(self):
        self.assertFails(self.corrected(timestamp="2026-13-45T10:00:00-06:00"), "INTEGRITY-010", fragment="timestamp")

    def test_modified_observation_requires_complete_correction(self):
        changed = "The beep occurred at 11:00."
        original = "The beep occurred at 10:00."
        self.assertFails(document(observation=changed), "INTEGRITY-008")
        record_text = record(reference="Original Observation", original=original, corrected=changed)
        self.assertPasses(document(observation=changed, corrections=record_text, version="1.0.1"))
        incomplete = record(reference="Original Observation", original=original, corrected=changed, reason=None)
        self.assertFails(document(observation=changed, corrections=incomplete), "INTEGRITY-008")


class HistoricalPreservationTests(IntegrityTestCase):
    def test_int_007_removed_protected_observation_fails(self):
        self.assertFails(document(observation=None), "INTEGRITY-002")

    def test_int_008_modified_protected_evidence_fails(self):
        self.assertFails(document(evidence="Altered evidence."), "INTEGRITY-008")

    def test_int_009_removed_appendment_fails(self):
        self.assertFails(document(appendment=None), "INTEGRITY-004")

    def test_int_010_altered_historical_revision_row_fails(self):
        self.assertFails(document(rows=[row("1.0.0", TS_BASE, "Rewritten.")]), "INTEGRITY-012", fragment="altered")

    def test_removed_historical_revision_row_fails(self):
        base = document(rows=BASE_ROWS + [row("1.1.0", TS_NEW, "Second.")], version="1.1.0")
        self.assertFails(document(rows=BASE_ROWS, version="1.1.0"), "INTEGRITY-012", base)

    def test_int_011_concatenated_revision_rows_fail(self):
        joined = BASE_ROWS[0] + row("1.1.0", TS_NEW, "Second.")
        self.assertFails(document(rows=[joined]), "INTEGRITY-012", fragment="malformed")

    def test_int_012_duplicate_revision_version_fails(self):
        self.assertFails(document(rows=BASE_ROWS + [row("1.0.0", TS_NEW, "Duplicate.")]), "INTEGRITY-012", fragment="duplicate")

    def test_int_014_malformed_section_boundaries_fail(self):
        self.assertFails(document(end_marker=False), "INTEGRITY-011")
        self.assertFails(document(findings="```\nFND-001: Beeping is periodic.\n"), "INTEGRITY-011", fragment="fence")

    def test_duplicate_protected_section_headings_fail(self):
        current = document(appendment_extra="\n## Original Observation\n\nShadow section.\n")
        self.assertFails(current, "INTEGRITY-011", fragment="duplicate")

    def test_int_015_administrative_revision_with_preserved_history_passes(self):
        extra = "\n<!-- BEGIN APPENDMENT: APP-002 -->\nSecond appendment.\n<!-- END APPENDMENT: APP-002 -->\n"
        current = document(
            rows=BASE_ROWS + [row("1.1.0", TS_NEW, "Superseded formatting guidance; historical content unchanged.")],
            version="1.1.0",
            appendment_extra=extra,
        )
        self.assertPasses(current)

    def test_appended_revision_row_without_other_changes_passes(self):
        self.assertPasses(document(rows=BASE_ROWS + [row("1.1.0", TS_NEW, "Added note.")], version="1.1.0"))


if __name__ == "__main__":
    unittest.main()
