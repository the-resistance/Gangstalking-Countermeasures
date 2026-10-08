---
Document Title: Evidence Documentation Standards
Document ID: EVD-STANDARDS-001
Author: Kevin Mahan
Version: 1.1.0
Created: 2026-10-08T10:37:13-05:00
Last Updated: 2026-10-08T10:42:49-05:00
---

# Evidence Documentation Standards

Use this directory to organize traceable references to supporting information for investigations. Evidence records support careful evaluation; a record alone does not establish the truth or cause of an event. Follow the [Versioning Policy](../governance/VERSIONING.md), [Anti-Drift Policy](../governance/ANTI_DRIFT.md), and [Evidence Log Template](../templates/EVIDENCE_LOG_TEMPLATE.md).

## Evidence Categories

Records may describe photographs, audio or video recordings, technical measurements, device diagnostics, witness observations, environmental measurements, public research documents, and original incident notes. These are categories, not records of evidence currently held.

Assign a stable identifier in the format `EV-YYYYMMDD-NNN`, using the actual acquisition date and a unique sequence for that date. Do not invent dates or reuse identifiers. Link evidence to its associated scenario when one exists.

## Integrity and Provenance

1. Preserve available original source files without editing them.
2. Record acquisition date and time, time zone, collection method, and available source metadata.
3. Preserve available metadata; do not claim missing metadata was captured.
4. Identify the associated scenario, source device, original filename, file format, and file size when known.
5. Distinguish original files from edited or processed derivatives and record each transformation.
6. Maintain traceable references between evidence records, scenarios, and related evidence.
7. When an original file is available, record its SHA-256 hash. A matching hash can help establish that file content has not changed; it does not independently establish the truth of the recorded event.
8. Explicitly identify unavailable evidence or information rather than filling gaps with assumptions.

Keep original materials in access-controlled storage appropriate to their sensitivity. Public documentation should distinguish material preserved for private investigation from material suitable for public release. Do not automatically publish sensitive personal information or commit sensitive media or personally identifying information. Ensure recording, observation, storage, and evidence collection comply with applicable law.

When a record is published in Markdown, wrap its complete contents in matching machine-readable markers: `<!-- BEGIN EVIDENCE: EV-YYYYMMDD-NNN -->` and `<!-- END EVIDENCE: EV-YYYYMMDD-NNN -->`. The same permanent identifier must appear in both markers. These boundaries allow integrity checks to detect deleted or altered historical records.

## Missing Information

Use one of `NOT RECORDED`, `NOT AVAILABLE`, `NOT APPLICABLE`, or `PENDING VERIFICATION` when a field cannot be established. Choose the designation that accurately describes the gap; do not use it to imply verification.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:37:13-05:00 | Initial publication of evidence organization, integrity, provenance, and privacy standards. | Kevin Mahan |
| 1.1.0 | 2026-10-08T10:42:49-05:00 | Established stable evidence record boundaries for automated historical integrity checks. | Kevin Mahan |
