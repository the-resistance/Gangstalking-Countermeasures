"""Regression tests for historical integrity validation using isolated Git fixtures."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validate_integrity.py"
_SPEC = importlib.util.spec_from_file_location("validate_integrity", SCRIPT)
vi = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = vi
_SPEC.loader.exec_module(vi)
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


class CorrectionAssociationTests(IntegrityTestCase):
    """AUD-005: a correction must resolve to the referenced historical finding."""

    def superseded(self, text):
        return f"{text} This finding is superseded.\n"

    def test_aud005_wrong_statement_with_correct_finding_id_fails(self):
        self.assertFails(self.corrected(original="Beeping stops at night."), "INTEGRITY-010", fragment="does not match")

    def test_aud005_valid_finding_specific_correction_passes(self):
        self.assertPasses(self.corrected())
        findings = "FND-001: Beeping is periodic.\n\nFND-002: Beeping stops at night. Superseded.\n"
        current = document(
            findings=findings,
            corrections=record(cid="COR-002", reference="FND-002", original="Beeping stops at night."),
            rows=BASE_ROWS + [row("1.0.1", TS_NEW, "Corrected FND-002.")],
        )
        self.assertPasses(current)

    def test_aud005_ambiguous_historical_reference_fails(self):
        base = document(findings="Beeping is periodic.\n\nBeeping is periodic.\n")
        current = document(
            findings="Beeping is periodic. Superseded.\n\nBeeping is periodic.\n",
            corrections=record(reference="Findings section"),
        )
        self.assertFails(current, "INTEGRITY-010", base, fragment="ambiguous")

    def test_aud005_duplicate_historical_finding_ids_fail(self):
        base = document(findings="FND-001: Beeping is periodic.\n\nFND-001: Beeping stops at night.\n")
        current = document(
            findings="FND-001: Beeping is periodic. Superseded.\n\nFND-001: Beeping stops at night.\n",
            corrections=record(),
        )
        self.assertFails(current, "INTEGRITY-010", base, fragment="duplicate")

    def test_aud005_conflicting_references_fail(self):
        self.assertFails(self.corrected(reference="FND-001, FND-002"), "INTEGRITY-010", fragment="conflicting")

    def test_aud005_identifier_in_original_statement_grants_no_authority(self):
        current = document(
            findings=SUPERSEDED_FINDINGS,
            corrections=record(reference=None, original="FND-001: Beeping is periodic."),
        )
        self.assertFails(current, "INTEGRITY-010")

    def test_aud005_correction_record_identifier_is_not_a_target(self):
        self.assertFails(self.corrected(cid="FND-001", reference="FND-002"), "INTEGRITY-010")

    def test_aud005_reference_to_unknown_historical_finding_fails(self):
        current = document(
            findings=SUPERSEDED_FINDINGS.replace("FND-001", "FND-009"),
            corrections=record(reference="FND-009", original="Beeping is periodic."),
        )
        self.assertFails(current, "INTEGRITY-010", fragment="not found")

    def test_aud005_identifier_free_finding_moved_to_other_section_fails(self):
        base = document(findings="Beeping is periodic.\n")
        current = document(findings="No findings recorded.\n", appendment_extra="\n## Notes\n\nBeeping is periodic. Superseded.\n")
        current += "\n## Correction Records\n\n" + record(reference="Notes section")
        self.assertFails(current, "INTEGRITY-010", base, fragment="section")

    def test_aud005_heading_style_findings_resolve_by_heading_identifier(self):
        base = document(findings="### FND-001\n\nBeeping is periodic.\n\nMore detail.\n\n### FND-002\n\nBeeping stops at night.\n")
        findings = base.split("\n## Evidence")[0].split("## Findings\n\n")[1].replace("More detail.", "More detail. Superseded.")
        good = document(findings=findings, corrections=record())
        self.assertPasses(good, base)
        wrong = document(findings=findings, corrections=record(original="Beeping stops at night."))
        self.assertFails(wrong, "INTEGRITY-010", base, fragment="does not match")

    def test_aud005_unavailable_baseline_is_not_verified_traceability(self):
        fields = {"original": "Beeping is periodic."}
        self.assertFalse(vi.record_traceable(vi.CorrectionRecord(1, fields, "COR-001"), None))

    def test_aud006_correction_timestamp_with_prose_fails_validation(self):
        self.assertFails(self.corrected(timestamp=f"recorded {TS_NEW} (approximately)"), "INTEGRITY-010", fragment="timestamp")


class StrictTimestampTests(unittest.TestCase):
    """AUD-006: the whole field must be exactly one offset-aware timestamp."""

    def test_aud006_leading_prose_is_rejected(self):
        self.assertIsNone(vi.offset_timestamp("on 2026-11-27T10:00:00-06:00"))

    def test_aud006_trailing_prose_is_rejected(self):
        self.assertIsNone(vi.offset_timestamp("2026-11-27T10:00:00-06:00 approx."))

    def test_aud006_multiple_timestamps_are_rejected(self):
        self.assertIsNone(vi.offset_timestamp("2026-11-27T10:00:00-06:00 2026-11-28T10:00:00-06:00"))

    def test_aud006_valid_utc_timestamp_is_accepted(self):
        parsed = vi.offset_timestamp("2026-11-27T16:00:00Z")
        self.assertEqual(parsed.utcoffset().total_seconds(), 0)

    def test_aud006_fractional_seconds_and_offset_are_accepted(self):
        parsed = vi.offset_timestamp(" `2026-11-27T10:00:00.123456-06:00` ")
        self.assertEqual(parsed.microsecond, 123456)
        self.assertEqual(parsed.utcoffset().total_seconds(), -6 * 3600)

    def test_aud006_malformed_wrappers_are_rejected(self):
        for value in ("`2026-11-27T10:00:00Z", "2026-11-27T10:00:00Z`", "``2026-11-27T10:00:00Z`", "```2026-11-27T10:00:00Z```", "`` `2026-11-27T10:00:00Z` ``", "'2026-11-27T10:00:00Z'"):
            with self.subTest(value=value):
                self.assertIsNone(vi.offset_timestamp(value))

    def test_aud006_naive_timestamp_is_rejected(self):
        self.assertIsNone(vi.offset_timestamp("2026-11-27T10:00:00"))

    def test_aud006_impossible_dates_and_times_are_rejected(self):
        for value in ("2026-02-30T10:00:00Z", "2026-13-01T10:00:00Z", "2026-11-27T24:00:00Z", "2026-11-27T10:60:00Z", "2026-11-27T10:00:60Z"):
            with self.subTest(value=value):
                self.assertIsNone(vi.offset_timestamp(value))

    def test_aud006_invalid_offset_components_are_rejected(self):
        for value in ("2026-11-27T10:00:00+24:00", "2026-11-27T10:00:00-06:60", "2026-11-27T10:00:00+99:99"):
            with self.subTest(value=value):
                self.assertIsNone(vi.offset_timestamp(value))


class AdministrativeClassificationTests(IntegrityTestCase):
    """AUD-007: only unambiguous administrative revision rows are exempt."""

    def admin(self, description, timestamp=TS_NEW, extra_rows=()):
        rows = BASE_ROWS + [row("1.1.0", timestamp, description)] + list(extra_rows)
        return document(rows=rows, version="1.1.0")

    def test_aud007_valid_administrative_revision_passes(self):
        self.assertPasses(self.admin("Superseded the earlier table formatting."))
        self.assertPasses(self.admin("Formatting guidance was superseded; historical content unchanged."))

    def test_aud007_substantive_change_disguised_as_administrative_fails(self):
        self.assertFails(self.admin("Formatting update superseded the earlier beep schedule."), "INTEGRITY-010")

    def test_aud007_every_supersession_occurrence_is_evaluated(self):
        description = "Superseded the earlier table formatting; superseded the earlier beep schedule."
        self.assertFails(self.admin(description), "INTEGRITY-010")

    def test_aud007_administrative_wording_mixed_with_finding_change_fails(self):
        self.assertFails(self.admin("Superseded the earlier table formatting; corrected finding FND-001."), "INTEGRITY-010")

    def test_aud007_invalid_revision_metadata_is_not_exempt(self):
        self.assertFails(self.admin("Superseded the earlier table formatting.", timestamp="2026-11-27T10:00:00"), "INTEGRITY-010")
        self.assertFails(self.admin("Superseded the earlier table formatting.", timestamp="not a timestamp"), "INTEGRITY-010")

    def test_aud007_duplicate_version_row_is_not_exempt(self):
        duplicate = row("1.1.0", TS_NEW, "Superseded the earlier table formatting.")
        self.assertFails(self.admin("Superseded the earlier table formatting.", extra_rows=[duplicate]), "INTEGRITY-010")

    def test_aud007_ambiguous_administrative_classification_fails(self):
        for description in ("Superseded earlier text.", "Superseded the earlier version.", "Superseded."):
            with self.subTest(description=description):
                self.assertFails(self.admin(description), "INTEGRITY-010")

    def test_aud007_malformed_row_is_not_exempt(self):
        joined = row("1.1.0", TS_NEW, "Superseded the earlier table formatting.") + row("1.2.0", TS_NEW, "Second.")
        self.assertFails(document(rows=BASE_ROWS + [joined], version="1.2.0"), "INTEGRITY-010")


if __name__ == "__main__":
    unittest.main()
