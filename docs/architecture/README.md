---
Document Title: Investigation Framework Architecture
Document ID: ARCH-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-11-08T20:12:00-06:00
Last Updated: 2026-11-08T20:12:00-06:00
---

# Investigation Framework Architecture

## Audit Snapshot

This proposal is based on the repository state at commit `44ceb12f5bc7599d23bba9b2a2c49de3d02c794c` on branch `copilot/repository-wide-audit-upgrade`. The working tree was clean. No local `main` branch or remote-tracking `origin/main` reference was available, so a merge base with `main` could not be determined. The repository has no production application modules, build system, or dedicated test suite. Its three Python standard-library scripts validate documentation structure, versions, and historical integrity.

Existing material includes an evidence standard and templates, a research document and manual, one scenario, two countermeasures, and documentation governance. The manual discusses audio observation, alternative hypotheses, repeatability, and evidence preservation. RF, network, legal, entity-graph, instrument, and cross-domain analysis implementations are not present. No evidence records or instrument inventory are currently published. The three existing documentation validators passed during this audit.

These are inventory findings, not claims about events or mechanisms. Existing reports, hypotheses, and technical references retain their documented status.

## Proposed Architecture

Build the framework in small, independently reviewable layers. Preserve existing records and terminology; additions should link to existing evidence rather than duplicate it.

1. **Shared record model:** use the JSON Schema at [`schemas/investigation-record.schema.json`](../../schemas/investigation-record.schema.json) for claims, sources, entities, relationships, evidence, events, instruments, experiments, and conclusions. Store future normalized collections as one JSON object per line, partitioned by record type where useful.
2. **Evidence integrity and event packages:** add capture manifests, timestamps, hashes, derivative relationships, processing history, and privacy controls before introducing sensor-specific capture. Raw originals remain immutable; no precise location is collected by default.
3. **Domain adapters and experiments:** integrate audio, RF, network, location, and environmental measurements as separate modules that emit records using the shared model. Reuse existing procedures and templates; do not claim a capability until there is an implementation and validation.
4. **Correlation and analysis:** correlate independently recorded observations with explicit time uncertainty, control periods, methods, and limitations. Report statistical association separately from causal mechanism and attribution.
5. **Legal and organizational research:** model each source-backed claim and relationship independently, preserving the source locator, exact scope, and evidence state. A filing's allegation is not a court finding, and technical capability is not evidence of deployment.
6. **Validation and reporting:** add deterministic fixtures and validators for schema conformance, provenance links, hashes, timestamps, instrument limits, and relationship integrity as corresponding data and implementations are introduced.

## Implementation Boundaries

The current deliverable establishes only the shared evidence vocabulary and record schema. It does not implement capture, RF or audio processing, packet analysis, correlation, legal research, instrument validation, custody automation, or a full entity graph. No dependencies or runtime modules are introduced by this proposal.

Keep high-rate acquisition and signal processing in C or C++ when those modules are authorized and justified. Use existing repository tooling where appropriate; do not add Python for convenience. Laboratory transmission, if ever separately authorized, must be opt-in, lawful, and constrained; uncontrolled jamming is out of scope.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-08T20:12:00-06:00 | Initial audit snapshot and staged architecture proposal for a provenance-first investigation framework. | Kevin Mahan |
