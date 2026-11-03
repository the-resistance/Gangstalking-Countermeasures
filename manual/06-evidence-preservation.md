---
Document Title: Evidence Preservation
Document ID: MAN-EVIDENCE-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-11-03T13:35:51-06:00
Last Updated: 2026-11-03T13:35:51-06:00
---

# Evidence Preservation

This chapter points to and supplements the repository's existing [Evidence Documentation Standards](../evidence/README.md). Those standards remain authoritative. Nothing here creates evidence, replaces a required evidence record, or weakens the privacy, integrity, provenance, or missing-information requirements.

## Preserve Originals and Create Working Copies

1. Preserve an acquired original source file without editing it. Do not overwrite or rename the only original.
2. Store originals in access-controlled storage appropriate to their sensitivity. Keep a separate read-only preservation copy where practical, and perform analysis on clearly identified working copies.
3. Record the relationship between original and derivative files, including every conversion, filter, amplification, crop, or other processing step.
4. Do not claim an original, derivative, backup, or recording exists unless it has actually been acquired and identified.

## Integrity and Metadata

For an original file that is available, calculate and record its SHA-256 checksum, acquisition date and time with time zone, original filename, format, size, source device, collection method, and available metadata. Preserve metadata as received; identify fields that are unavailable rather than filling them in. A checksum can help detect a content change but does not prove the truth, source, or context of a recording.

Track later file checksums and modification times in a manifest or evidence record. Explain any difference and preserve both versions when appropriate; do not silently replace a prior hash or imply that a hash identifies who changed a file.

## Chain of Custody and Processing Logs

Maintain a dated record of each transfer or handling event when custody tracking is appropriate. Record the item identifier, person transferring and receiving it, date and time with time zone, purpose, storage or transfer method, and any known condition or integrity check. Use the [Evidence Log Template](../templates/EVIDENCE_LOG_TEMPLATE.md), including its chain-of-custody field, and add separate entries as needed; do not invent entries for unrecorded past handling.

For analysis, record the working-copy identifier, software and version, operation, parameters, operator, date, and output identifier. Preserve the original and make logs sufficient for an independent reviewer to understand or repeat the processing.

## Privacy and Forensic Review

Limit collection and access to what is necessary. Protect personally identifying or sensitive material and comply with applicable law. Public documentation should link to a controlled evidence record where appropriate rather than expose sensitive source media.

Independent digital or audio forensic review may help assess file integrity, metadata, processing, and technical limitations. Record the reviewer's methods, materials, software, findings, and limitations; do not describe an opinion as independently verified beyond what the review actually establishes.

## Related Standards and Templates

- [Evidence Documentation Standards](../evidence/README.md)
- [Evidence Log Template](../templates/EVIDENCE_LOG_TEMPLATE.md)
- [Appendment Template](../templates/APPENDMENT_TEMPLATE.md)
- [Versioning Policy](../governance/VERSIONING.md)
- [Anti-Drift Policy](../governance/ANTI_DRIFT.md)

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-03T13:35:51-06:00 | Initial publication of evidence preservation guidance referencing existing evidence governance. | Kevin Mahan |
