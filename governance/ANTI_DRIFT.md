---
Document Title: Documentation Anti-Drift Policy
Document ID: GOV-ANTIDRIFT-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-10-08T10:12:48-05:00
Last Updated: 2026-10-08T10:12:48-05:00
---

# Documentation Anti-Drift Policy

This document is the canonical authority for preserving historical content, document integrity, project terminology, and authorized modifications. Apply version and timestamp requirements from the [Versioning Policy](VERSIONING.md).

## AD-001 — Content Preservation

Previously documented observations must remain preserved. Do not delete historical content merely because newer information becomes available. Add new information in a way that extends, rather than erases, the existing record.

## AD-002 — Append-First Policy

Use append-only modifications for historical observations and evidence records. Clearly distinguish the original record from later additions, for example:

- Original observation
- Appendment 001
- Appendment 002

Each appendment must include a unique identifier, timestamp, author, description, and supporting evidence if available. Do not silently replace or alter earlier appendments. Do not imply evidence exists when it does not.

## AD-003 — Preserve Original Wording

Preserve the substance and meaning of author-provided observations. Do not silently reinterpret them. Put additional analysis in a separate, clearly identified section rather than inserting it into the original observation record.

## AD-004 — No Destructive Summarization

Do not shorten historical records to improve readability or replace detailed observations with condensed summaries. A summary may be added as a separate section, but the original detailed information must remain accessible.

## AD-005 — Correction Procedure

Corrections are permitted only with an auditable record that includes:

1. The original statement being corrected.
2. The correction.
3. The reason for the correction.
4. The correction timestamp.
5. A document version increment under the [Versioning Policy](VERSIONING.md).
6. A revision history entry.
7. Preservation of the previous wording in Git history or a correction record.

Never silently alter historical facts. Where appropriate, mark the previous statement as superseded.

## AD-006 — Subject Isolation

Keep each independent investigative subject separately documented. Do not merge unrelated scenarios or unrelated countermeasures into one document. Related subjects may cross-reference each other. Each scenario must have a stable unique identifier.

## AD-007 — No Fabrication

Never invent observations, incidents, witnesses, recordings, evidence, timestamps, technical findings, verification results, or source identifications. Identify missing information as missing. Distinguish clearly among:

- Reported
- Observed
- Hypothesized
- Corroborated
- Verified
- Unresolved

Claims of coordination or intentional conduct require supporting evidence.

## AD-008 — Terminology Preservation

Preserve established project terminology and exact capitalization for formally defined identifiers:

- Khalisti
- BlitzWaffe
- Aggressive Strategic Reasoning Core
- ASRC
- BlitzWaffe Program Dismantlement
- Observation & Countermeasure Field Manual

Do not automatically rename established projects, files, or identifiers.

## AD-009 — Pre-Modification Comparison

Before editing an existing document:

1. Read the complete document.
2. Identify its current Git revision or otherwise capture its prior state.
3. Identify the authorized modification.
4. Identify affected sections.
5. Confirm unrelated sections will remain unchanged.
6. Apply only the authorized modification.
7. Inspect the Git diff.
8. Verify all deletions and replacements.
9. Restore accidentally removed information.
10. Proceed only after validation passes.

## AD-010 — Historical Recovery

Git history must provide a recovery path. If a modification removes historical information accidentally, identify the affected revision, recover the missing content, and restore it without destroying subsequent legitimate additions. Document the recovery operation.

## AD-011 — No Unauthorized Expansion

Do not create investigative subjects without explicit instruction. Do not fabricate scenarios, create speculative incident records, expand a hypothesis into a finding without sufficient evidence, or introduce unrelated research areas into existing documents.

## AD-012 — Governance Protection

Governance files are subject to the versioning and anti-drift requirements. A governance change must preserve prior revisions, include accurate timestamps, identify affected rules, explain the change, increment the document version, and update `CHANGELOG.md`. Do not silently weaken existing protections.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:12:48-05:00 | Initial publication of documentation anti-drift policy. | Kevin Mahan |
