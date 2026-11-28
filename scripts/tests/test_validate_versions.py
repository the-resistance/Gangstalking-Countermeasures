"""Regression tests for VERSION-007 revision-chain validation."""

from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validate_versions.py"
spec = importlib.util.spec_from_file_location("validate_versions", SCRIPT)
validate_versions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_versions)

BASE_ROWS = [
    ("1.0.0", "2026-10-08T09:39:41-05:00", "Initial.", "Kevin Mahan"),
    ("1.3.0", "2026-11-16T16:28:42-06:00", "Third.", "Kevin Mahan"),
]
FULL_ROWS = BASE_ROWS + [
    ("1.4.0", "2026-11-25T21:29:28-06:00", "Fourth.", "Kevin Mahan"),
    ("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.", "Kevin Mahan"),
]
BASE_UPDATED = "2026-11-16T16:28:42-06:00"


def transition(new_version, rows, old_version="1.3.0", old_rows=BASE_ROWS):
    return validate_versions.validate_version_transition(
        old_version, BASE_UPDATED, list(old_rows), new_version, list(rows)
    )


class VersionTransitionTests(unittest.TestCase):
    def test_single_increment_is_valid(self):
        self.assertEqual(transition("1.4.0", FULL_ROWS[:3]), [])

    def test_documented_cumulative_chain_is_valid(self):
        self.assertEqual(transition("1.5.0", FULL_ROWS), [])

    def test_cumulative_chain_across_patch_and_major_is_valid(self):
        rows = BASE_ROWS + [
            ("1.3.1", "2026-11-20T10:00:00-06:00", "Patch.", "A"),
            ("2.0.0", "2026-11-21T10:00:00-06:00", "Major.", "A"),
        ]
        self.assertEqual(transition("2.0.0", rows), [])

    def test_undocumented_jump_is_rejected(self):
        rows = BASE_ROWS + [("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.", "A")]
        self.assertTrue(any("1.3.0 -> 1.5.0" in p for p in transition("1.5.0", rows)))

    def test_missing_intermediate_revision_is_rejected(self):
        rows = BASE_ROWS + [
            ("1.4.0", "2026-11-25T21:29:28-06:00", "Fourth.", "A"),
            ("1.6.0", "2026-11-26T22:34:15-06:00", "Skipped 1.5.0.", "A"),
        ]
        self.assertTrue(any("1.4.0 -> 1.6.0" in p for p in transition("1.6.0", rows)))

    def test_version_regression_and_no_increment_are_rejected(self):
        self.assertTrue(transition("1.2.0", BASE_ROWS))
        self.assertTrue(transition("1.3.0", BASE_ROWS))

    def test_invalid_transition_in_chain_is_rejected(self):
        rows = BASE_ROWS + [
            ("1.3.5", "2026-11-25T21:29:28-06:00", "Jump.", "A"),
            ("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.", "A"),
        ]
        self.assertTrue(any("1.3.0 -> 1.3.5" in p for p in transition("1.5.0", rows)))

    def test_chain_missing_baseline_version_is_rejected(self):
        rows = [row for row in FULL_ROWS if row[0] != "1.3.0"]
        self.assertTrue(any("absent from the revision history" in p for p in transition("1.5.0", rows)))

    def test_altered_baseline_history_is_rejected(self):
        rows = list(FULL_ROWS)
        rows[0] = ("1.0.0", "2026-10-08T09:39:41-05:00", "Rewritten.", "Kevin Mahan")
        self.assertTrue(any("baseline revision history" in p for p in transition("1.5.0", rows)))

    def test_chain_not_ending_at_current_version_is_rejected(self):
        self.assertTrue(transition("1.5.0", FULL_ROWS[:3]))

    def test_fabricated_intermediate_before_baseline_is_rejected(self):
        rows = BASE_ROWS + [
            ("1.4.0", "2026-11-01T00:00:00-06:00", "Backdated.", "A"),
            ("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.", "A"),
        ]
        self.assertTrue(any("not later than the baseline" in p for p in transition("1.5.0", rows)))


class EndToEndTests(unittest.TestCase):
    def run_git(self, root, *args):
        subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@example.com", "-c", "commit.gpgsign=false", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
        )

    def document(self, version, updated, rows):
        table = "\n".join(f"| {v} | {t} | {d} | Kevin Mahan |" for v, t, d in rows)
        return (
            "---\nDocument Title: Doc\nDocument ID: DOC-001\nAuthor: Kevin Mahan\n"
            f"Version: {version}\nCreated: 2026-10-08T09:00:00-05:00\nLast Updated: {updated}\n---\n\n"
            "# Doc\n\nBody.\n\n## Revision History\n\n"
            "| Version | Timestamp | Description | Author |\n|---|---|---|---|\n" + table + "\n"
        )

    def validate(self, rows_after):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_git(root, "init", "-q")
            (root / "CHANGELOG.md").write_text(
                "| 2026-11-01T00:00:00-06:00 | `doc.md` | N/A | 1.0.0 | Created. | A |\n", encoding="utf-8"
            )
            first = [
                ("1.0.0", "2026-10-08T09:00:00-05:00", "Initial."),
                ("1.3.0", "2026-11-16T16:28:42-06:00", "Third."),
            ]
            (root / "doc.md").write_text(self.document("1.3.0", "2026-11-16T16:28:42-06:00", first), encoding="utf-8")
            self.run_git(root, "add", ".")
            self.run_git(root, "commit", "-q", "-m", "base")
            base = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True, check=True
            ).stdout.strip()
            version, updated = rows_after[-1][0], rows_after[-1][1]
            text = self.document(version, updated, first + rows_after) + "\nChanged.\n"
            (root / "doc.md").write_text(text, encoding="utf-8")
            return subprocess.run(
                ["python3", str(SCRIPT), "--root", str(root), "--base", base], capture_output=True, text=True
            )

    def test_cumulative_increment_passes_end_to_end(self):
        result = self.validate(
            [("1.4.0", "2026-11-25T21:29:28-06:00", "Fourth."), ("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.")]
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_undocumented_jump_fails_end_to_end(self):
        result = self.validate([("1.5.0", "2026-11-26T22:34:15-06:00", "Fifth.")])
        self.assertEqual(result.returncode, 1)
        self.assertIn("VERSION-007", result.stdout)


class TimestampTests(unittest.TestCase):
    def test_strict_timestamp_rejections(self):
        for value in ("2026-11-27 10:00:00Z", "2026-11-27T10:00Z",
                      "2026-11-27T10:00:00+06:60", "2026-02-30T10:00:00Z",
                      "2026-11-27T10:00:00", "2026-11-27T10:00:00+24:00",
                      "on 2026-11-27T10:00:00Z", "2026-11-27T10:00:00Z approx."):
            with self.subTest(value=value):
                self.assertIsNone(validate_versions.iso_timestamp(value))

    def test_strict_timestamp_acceptance(self):
        for value in ("2026-11-27T10:00:00Z", "2026-11-27T10:00:00-06:00",
                      "2026-11-27T10:00:00.123456+05:30", "`2026-11-27T10:00:00Z`"):
            with self.subTest(value=value):
                self.assertIsNotNone(validate_versions.iso_timestamp(value))


if __name__ == "__main__":
    unittest.main()
