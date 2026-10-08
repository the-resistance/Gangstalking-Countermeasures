---
Document Title: Documentation Validation Tools
Document ID: GOV-VALIDATION-001
Author: Kevin Mahan
Version: 1.0.1
Created: 2026-10-08T10:36:37-05:00
Last Updated: 2026-10-08T11:11:19-05:00
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
- `validate_versions.py` checks semantic versions, offset-aware ISO 8601 timestamps, revision history, creation timestamp preservation, and valid version increments for changed documents.
- `validate_integrity.py` compares changed documentation with Git history and reports removed or altered observations, evidence records, appendments, identifiers, scenario files, and revision history.

See the [Versioning Policy](../governance/VERSIONING.md) and [Anti-Drift Policy](../governance/ANTI_DRIFT.md) for the authoritative documentation requirements. Automated checks identify integrity risks; they do not guarantee historical accuracy.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:36:37-05:00 | Initial publication of documentation validation tool guidance. | Kevin Mahan |
| 1.0.1 | 2026-10-08T11:11:19-05:00 | Documented both accepted countermeasure filename forms used by repository architecture and scenario modules. | Kevin Mahan |
