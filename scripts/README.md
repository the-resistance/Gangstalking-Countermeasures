---
Document Title: Documentation Validation Tools
Document ID: GOV-VALIDATION-001
Author: Kevin Mahan
Version: 1.2.0
Created: 2026-10-08T10:36:37-05:00
Last Updated: 2026-11-27T04:14:59-06:00
---

# Documentation Validation Tools

These Python 3 standard-library scripts inspect documentation without changing files. Run them from the repository root:

```sh
python3 scripts/validate_documentation.py
python3 scripts/validate_versions.py
python3 scripts/validate_integrity.py
```

Each script exits with `0` on success and `1` on failure. Reports identify a file, rule, issue, and corrective action. Structural, version, and integrity checks are separate so failures can be diagnosed at the appropriate layer.

## Git Comparison

The version and integrity validators compare changed files with a Git baseline. By default they use `HEAD^` when available and perform static checks when there is no prior commit. Supply `--base <revision>` to select a comparison point. An all-zero SHA explicitly indicates an initial push with no prior revision. The validators inspect committed, staged, unstaged, and untracked files; they do not repair or rewrite content.

The integrity validator uses stable `Original Observation` sections and matching `BEGIN/END PROTECTED`, `BEGIN/END EVIDENCE`, and `BEGIN/END APPENDMENT` markers. Preserve the complete original content and identifiers inside these boundaries. A potential destructive edit is reported for review; complex corrections still require a human to verify compliance with the [Anti-Drift Policy](../governance/ANTI_DRIFT.md).

## Validation Rules

- `validate_documentation.py` checks metadata presence, unique document identifiers, scenario/countermeasure naming, required sections, references, relative Markdown links, and index entries. Countermeasure filenames may use `NNN-descriptive-name.md` or the optional `NNN-descriptive-name-countermeasure.md` suffix.
- `validate_versions.py` checks semantic versions, offset-aware ISO 8601 timestamps, revision history, creation timestamp preservation, and valid version increments for changed documents. A changed document normally needs one valid increment from the baseline version. When a branch legitimately accumulates several documented increments (for example `1.3.0` to `1.4.0` to `1.5.0`), `VERSION-007` accepts the change only if the revision history contains a continuous chain of valid increments that starts at the baseline version, ends at the current version, preserves the baseline revision entries unchanged, and records every intermediate revision later than the baseline's `Last Updated`. Undocumented jumps, missing intermediate revisions, invalid transitions, regressions, and altered baseline history are still rejected.
- `validate_integrity.py` compares changed documentation with Git history and reports removed or altered observations, evidence records, appendments, identifiers, scenario files, and revision history. Static checks also report malformed section boundaries (`INTEGRITY-011`: unclosed front matter or code fences, unbalanced `PROTECTED` markers, duplicated protected sections) and malformed revision tables (`INTEGRITY-012`: concatenated rows, invalid or duplicate versions), and a changed document must keep every baseline revision row unchanged and in order.

## INTEGRITY-010 Correction Records

`INTEGRITY-010` applies to changed documents that already exist in the baseline. It uses validated Markdown section boundaries (front matter, fenced code, and headings) rather than a document-wide word search:

- A single-line, well-formed Revision History table row (four cells, semantic version, offset-aware timestamp) that uses supersession wording in a sentence that does not concern a finding, observation, evidence, appendment, claim, statement, or an identifier such as `FND-001` is administrative and is not a finding correction.
- Every other use, including prose placed under a Revision History heading, malformed rows, and revision rows that concern a finding, requires a complete correction record.
- A record lives under a `Correction Records` (or `Corrections`) heading, either as one subsection per record or as consecutive blocks beginning with an `Original statement` field. Required fields: `Original statement`, `Corrected statement` (or `Correction`), `Reason`, and `Correction timestamp` (offset-aware ISO 8601). Add `Reference` (or `Corrects`) with the finding identifier.
- A record satisfies a finding only if it is linked to it: it names an identifier found in the finding, or, when the finding has no identifier, its original statement appears in the finding. The original statement must also be traceable to the baseline document. A record for one finding never satisfies another.
- A modified `Original Observation` still requires a complete record that preserves the original text (`INTEGRITY-008`).

The validator cannot judge whether a correction is factually justified; that remains a human review under [AD-005](../governance/ANTI_DRIFT.md). `governance/ANTI_DRIFT.md` itself uses supersession wording in rule text outside a revision row, so editing that document currently requires human review of a reported `INTEGRITY-010` result.

## Structured Document Editing

Existing validators enforce: front matter and revision-table structure, creation timestamp preservation, version increments, revision/metadata agreement, changelog entry format, protected-record preservation, and baseline revision-row preservation. They do not detect an omitted `CHANGELOG.md` entry for a specific document, review each deletion for you, or verify that a new revision row was written on its own line beyond rejecting concatenated rows; confirm those with `git diff` before publication.

See the [Versioning Policy](../governance/VERSIONING.md) and [Anti-Drift Policy](../governance/ANTI_DRIFT.md) for the authoritative documentation requirements. Automated checks identify integrity risks; they do not guarantee historical accuracy.

## Regression Tests

Run the standard-library regression tests for the version and integrity validators from the repository root. Each integrity test builds an isolated temporary Git repository and never touches production records:

```sh
python3 -m unittest discover -s scripts/tests
```

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:36:37-05:00 | Initial publication of documentation validation tool guidance. | Kevin Mahan |
| 1.0.1 | 2026-10-08T11:11:19-05:00 | Documented both accepted countermeasure filename forms used by repository architecture and scenario modules. | Kevin Mahan |
| 1.1.0 | 2026-11-26T23:00:11-06:00 | Documented cumulative revision-chain validation for VERSION-007 and the validator regression tests. | Kevin Mahan |
| 1.2.0 | 2026-11-27T04:14:59-06:00 | Documented INTEGRITY-010 section-aware correction records, INTEGRITY-011 and INTEGRITY-012 structural checks, structured-editing enforcement limits, and the integrity regression tests. | Kevin Mahan |
