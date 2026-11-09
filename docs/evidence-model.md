---
Document Title: Evidence Record Model
Document ID: EVD-MODEL-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-11-08T20:12:00-06:00
Last Updated: 2026-11-08T20:12:00-06:00
---

# Evidence Record Model

The [JSON Schema](../schemas/investigation-record.schema.json) defines a common record envelope for future machine-readable investigation data. A record is a description with provenance, not proof that its contents are true. This model supplements the existing [evidence documentation standards](../evidence/README.md); it does not replace them or create records for evidence that has not been collected.

## Evidence States

Every record has exactly one current `evidence_state` and a non-empty `evidence_state_reason`:

| State | Meaning |
|---|---|
| `OBSERVED` | Directly recorded or measured; the method and limits still matter. |
| `REPRODUCED` | Repeated under documented, reasonably controlled conditions. |
| `CORRELATED` | Independently measured events show a documented temporal or statistical association. |
| `MECHANISM_SUPPORTED` | Evidence supports a known physical or technical mechanism as an explanation. |
| `ATTRIBUTION_CANDIDATE` | A possible source or actor is identified, but the link is not established. |
| `ATTRIBUTION_SUPPORTED` | Independent evidence materially links a source to an event. |
| `CLAIM_ONLY` | The statement exists as an allegation, testimony, filing, social-media statement, or other claim without independent substantiation in the record. |
| `CONTRADICTED` | Identified evidence materially conflicts with the statement; this does not automatically establish an alternative explanation. |
| `UNRESOLVED` | Available information is insufficient to classify the matter more specifically. |

These labels are not a mandatory linear progression. Records may remain unresolved, and a change of state requires new evidence and a recorded rationale. A patent, lawsuit, report, or observed capability does not alone establish deployment, causation, intent, or attribution. Correlation is not causation. Preserve the underlying source and its context.

## Record Types and Provenance

The schema supports `claim`, `source`, `entity`, `relationship`, `evidence`, `event`, `instrument`, `experiment`, and `conclusion` records. Each record includes a stable identifier, state, state rationale, and one or more provenance entries. Provenance locators may refer to another record, a primary document and page or paragraph, an actual measurement, or an access-controlled evidence item. Do not put sensitive evidence contents or unnecessary precise location data in public records.

Relationship records identify both endpoints and a predicate, and carry their own provenance and evidence state. Keep different relationship assertions separate when their support differs. For example, a documented organizational relationship and an allegation about that organization must not be collapsed into one edge or promoted to an established fact.

Use the existing `EV-YYYYMMDD-NNN` identifier format for evidence items. Other record types use the prefixes `CLM`, `SRC`, `ENT`, `REL`, `EVT`, `INS`, `EXP`, and `CON`. JSON Lines collections should contain one schema-conforming record per line; there are no such collections or runtime schema validators yet.

`confidence` is optional and is not a substitute for the evidence state. If used in future records, its scale and method must be documented. Unknown facts should use the existing missing-information designations rather than fabricated values.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-08T20:12:00-06:00 | Initial publication of the shared evidence-state vocabulary and record-model guidance. | Kevin Mahan |
