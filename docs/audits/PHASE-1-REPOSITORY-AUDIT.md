---
Document Title: Phase 1 Repository Baseline Audit
Document ID: AUD-PHASE1-001
Author: GitHub Copilot
Version: 1.0.0
Created: 2026-11-16T13:33:35-06:00
Last Updated: 2026-11-16T13:35:58-06:00
---

# Phase 1 Repository Baseline Audit

## 1. Executive Summary

The repository is a documentation-led research archive, not a software application or implemented sensor-analysis platform. Its current foundation combines a manual, one research document, a reported scenario, two proposed countermeasures, evidence-handling standards and templates, documentation governance, three Python validation scripts, a generic investigation-record JSON Schema, and an architecture proposal.

Existing documentation provides careful distinctions between personal reports, hypotheses, documented sources, and independently supported findings. It describes repeatable audio observation, preservation of originals, SHA-256 recording, provenance, independent listening, and cross-references. These are primarily written standards and proposed procedures: the repository contains no populated evidence records, measurement datasets, instrument inventory, executed experiment records, or implemented audio/RF analysis pipeline.

The technical-source bibliography is notably incomplete by its own account. Allan H. Frey is named without a complete citation; the references chapter documents no specific peer-reviewed publication, patent, government document, contract, or technical publication. Accordingly, the audit does not treat the technical mechanisms raised in the repository as established incident explanations. A technology's existence does not establish its use in any particular event.

The strongest integration point is the existing shared record model in `docs/evidence-model.md` and `schemas/investigation-record.schema.json`, alongside the existing evidence standards and templates. Recommended next work is to populate source-traceable research records and define a small, reproducible audio/RF measurement protocol before considering new data stores, tooling, or broader investigation features.

## 2. Repository Baseline

| Field | Verified baseline |
|---|---|
| Repository | `the-resistance/Gangstalking-Countermeasures` |
| Branch | `copilot/phase1-repository-audit` |
| Base branch | `main` (`origin/main` fetched before branch creation) |
| Base commit SHA | `a27ee4e7b8166a2dea1600f977e97d345fbdf411` |
| Audit date | 2026-11-16 |
| Baseline worktree | Clean before report creation |

This report assesses repository contents at the stated base commit. The audit branch was created from that commit; it does not change `main`.

## 3. Complete Documentation Inventory

The table inventories every tracked file at the baseline, including non-Markdown configuration and schema files. “Not specified” means the file itself has no document ID or semantic version metadata; it is not an inferred identifier or version.

| File path | Document ID / version | Purpose |
|---|---|---|
| `README.md` | README-001 / 1.2.0 | Mission, principles, authorship, and top-level navigation. |
| `MANUAL.md` | MAN-ROOT-001 / 1.1.0 | Navigation across manual chapters and supporting records. |
| `manual/00-introduction.md` | MAN-INTRO-001 / 1.0.0 | Scope, investigative principles, and attribution cautions. |
| `manual/01-research-objectives.md` | MAN-OBJECTIVES-001 / 1.0.0 | Goals for observation, measurement, research, preservation, and review. |
| `manual/02-observations.md` | MAN-OBSERVATIONS-001 / 1.0.0 | Index of report categories summarized from RSH-001. |
| `manual/03-terminology.md` | MAN-TERMS-001 / 1.0.0 | Working terms, alternatives, and verification criteria. |
| `manual/04-technology-research.md` | MAN-TECH-001 / 1.0.0 | Technical topics, evidence-status labels, and research limits. |
| `manual/05-investigative-methodology.md` | MAN-METHODS-001 / 1.0.0 | Proposed observation, recording, listening, and reporting methods. |
| `manual/06-evidence-preservation.md` | MAN-EVIDENCE-001 / 1.0.0 | Supplementary evidence preservation and forensic-review guidance. |
| `manual/07-references.md` | MAN-REFERENCES-001 / 1.0.0 | Reference categories and expressly identified research leads/gaps. |
| `research/001-voice-to-skull-v2k.md` | RSH-001 / 1.0.0 (front matter; working draft 0.1 in body) | Author's reported experiences, technical topics, proposed models, and research objectives. |
| `scenarios/INDEX.md` | IDX-SCENARIOS-001 / 1.1.1 | Published scenario index. |
| `scenarios/001-audible-beeping-transitioning.md` | SCN-001 / 1.0.2 | One reported scenario; source, repeatability, and relationship remain unresolved. |
| `countermeasures/INDEX.md` | IDX-COUNTERMEASURES-001 / 1.1.0 | Published countermeasure index. |
| `countermeasures/001-independent-observation.md` | CM-001 / 1.0.0 | Proposed independent observation and sound-source identification procedure. |
| `countermeasures/002-pre-transition-auditory-masking.md` | CM-002 / 1.0.0 | Proposed evaluation of perceived disruption under safe playback conditions. |
| `evidence/README.md` | EVD-STANDARDS-001 / 1.2.0 | Evidence IDs, provenance, integrity, privacy, and missing-information rules. |
| `templates/EVIDENCE_LOG_TEMPLATE.md` | TPL-EVIDENCE-001 / 1.1.2 | Reusable evidence-item record including hash and custody fields. |
| `templates/APPENDMENT_TEMPLATE.md` | TPL-APPENDMENT-001 / 1.1.1 | Append-only additions and auditable correction structure. |
| `templates/SCENARIO_TEMPLATE.md` | TPL-SCENARIO-001 / 1.1.0 | Scenario structure separating original observation, hypotheses, and later additions. |
| `templates/COUNTERMEASURE_TEMPLATE.md` | TPL-COUNTERMEASURE-001 / 1.0.1 | Procedure template covering basis, safety, limitations, and evaluation. |
| `docs/evidence-model.md` | EVD-MODEL-001 / 1.0.0 | Shared evidence states, record types, identifiers, and provenance guidance. |
| `docs/architecture/README.md` | ARCH-001 / 1.0.0 | Prior audit snapshot and staged architecture proposal; not an implementation. |
| `schemas/investigation-record.schema.json` | No document ID/version specified | JSON Schema 2020-12 envelope for claims, sources, entities, relationships, evidence, events, instruments, experiments, and conclusions. |
| `governance/ANTI_DRIFT.md` | GOV-ANTIDRIFT-001 / 1.0.0 | Historical preservation, append-first edits, corrections, and scope controls. |
| `governance/VERSIONING.md` | GOV-VERSIONING-001 / 1.0.0 | Document metadata, semantic versioning, timestamps, revision histories, and changelog rules. |
| `.github/copilot-instructions.md` | GOV-COPILOT-001 / 1.0.0 | Repository-specific work sequence and documentation safeguards. |
| `CHANGELOG.md` | No document ID/version required | Reverse-chronological ledger of completed documentation changes. |
| `scripts/README.md` | GOV-VALIDATION-001 / 1.0.1 | Validator use, rules, and Git comparison behavior. |
| `scripts/validate_documentation.py` | No document ID/version specified | Checks documentation structure, identifiers, links, and indexes. |
| `scripts/validate_versions.py` | No document ID/version specified | Checks version metadata, timestamps, revision histories, and changelog. |
| `scripts/validate_integrity.py` | No document ID/version specified | Checks historical observations, evidence, appendments, identifiers, and revisions against Git. |
| `.github/workflows/documentation-validation.yml` | No document ID/version specified | Read-only CI workflow invoking the three documentation validators. |

The baseline contains the directories covered by the inventory above. `docs/audits/` did not exist before this report. There are no baseline files under a top-level `schemas` collection beyond the one listed schema, or separate RF, acoustic, or equipment data collections.

## 4. Current Technical Architecture

**Verified repository facts**

- The project is Markdown documentation with Python standard-library documentation validators; no application source modules, dependency manifest, build system, or dedicated test suite are present in the tracked baseline. `docs/architecture/README.md` makes the same boundary explicit.
- `MANUAL.md` links the chapters, RSH-001, scenario and countermeasure indexes, evidence standards and template, record model, schema, architecture proposal, validators, and governance.
- Scenario, countermeasure, and evidence guidance uses stable IDs and relative cross-references. Evidence standards require actual evidence before creating an evidence record and define missing-information labels.
- `schemas/investigation-record.schema.json` defines an extensible record envelope with a stable ID, type, evidence state, state rationale, and provenance. Type-specific fields cover claims, sources, entities, relationships, evidence, events, instruments, experiments, and conclusions.
- `docs/architecture/README.md` explicitly distinguishes the shared vocabulary/schema from future, unimplemented capture, analysis, correlation, legal research, and validation modules.
- The CI workflow runs structural, version, and historical-integrity checks with repository history and read-only contents permission.

**Assessment**

The architecture is a documentation and data-contract foundation, not a functioning technical investigation system. It can describe intended entities and methods, but the repository currently has no populated machine-readable investigation records, schema validator, evidence manifest processor, measurement acquisition code, or reproducibility fixtures. The report therefore describes capabilities of the documented model separately from capabilities implemented in code.

## 5. Research Coverage Matrix

Coverage describes what the repository documents, not whether a mechanism was used in any event. Priorities: **P1** = foundational source or protocol gap; **P2** = focused technical gap; **P3** = later or conditional work.

| Subject | Existing coverage | Supporting files | Missing information | Priority |
|---|---|---|---|---|
| RF modulation/demodulation | Audio demodulation and possible unintended electronic detection are research topics; no RF capture or result documented. | `manual/04-technology-research.md`; `research/001-voice-to-skull-v2k.md` | Traceable sources, signal model, instrument/setup limits, controlled protocol, actual data. | P1 |
| Pulse-width modulation (PWM) | No specific PWM coverage identified in reviewed research chapters. | `manual/04-technology-research.md` (general EMI/demodulation context only) | Definition, applicable source literature, relevance criteria, and tests. | P2 |
| Passive intermodulation | No specific coverage identified. | None specific; general topic context in `manual/04-technology-research.md` | Source-backed explanation and bounded measurement protocol. | P2 |
| Nonlinear electrical junctions | Not specifically documented. | None specific | Traceable literature and testable, instrument-appropriate conditions. | P2 |
| Electromagnetic interference | Listed as a possible mechanism; not tied to incident measurements or a cited technical publication. | `manual/04-technology-research.md`; `research/001-voice-to-skull-v2k.md` | Source citations, device-specific checks, RF environment and control records. | P1 |
| Microwave auditory effect | Named as the Frey effect; RSH-001 describes pulsed RF auditory sensations under certain conditions, while the reference index says the underlying publication is incompletely cited. | `research/001-voice-to-skull-v2k.md`; `manual/04-technology-research.md`; `manual/07-references.md` | Complete primary citation and contextual review; no event-specific exposure evidence. | P1 |
| RF-induced acoustic phenomena | RF auditory effects and possible audio mechanisms appear as research topics. | `manual/04-technology-research.md`; RSH-001 | Terminology, source-backed mechanism boundaries, competing explanations, measurement criteria. | P1 |
| Software-defined radio (SDR) acquisition | No SDR acquisition method or data record is documented. | No specific supporting file | Acquisition requirements, calibration/metadata, lawful and safe protocol, sample data. | P1 |
| Directional audio | Mentioned as relevant background; specific systems and references are not supplied. | `manual/04-technology-research.md`; RSH-001 | Source-supported capability descriptions, measurement conditions, limits, and event evidence. | P2 |
| Parametric ultrasonic speakers | RSH-001 broadly mentions systems using ultrasonic carriers and nonlinear acoustic propagation; no cited device or study. | RSH-001; `manual/04-technology-research.md` | Peer-reviewed/technical sources and bounded capability characterization. | P1 |
| Ultrasonic demodulation | Not separately treated as a research topic. | No specific supporting file | Traceable sources, definitions, measurement procedure, and confounds. | P2 |
| Mechanical vibration | Listed as a possible environmental mechanism; no measurements. | `manual/03-terminology.md`; RSH-001 | Instrumented measurements, equipment specification, controls, and source citations. | P2 |
| Acoustic resonance | Listed as a possible mechanism, without an associated measurement or source. | `manual/03-terminology.md`; `manual/04-technology-research.md`; RSH-001 | Source-backed theory, environmental parameters, and reproducible protocol. | P2 |
| Environmental sound propagation | Environmental sound sources are considered broadly; propagation conditions are not systematically covered. | `manual/05-investigative-methodology.md`; CM-001 | Acoustic environment characterization, geometry, distance, and measurement limits. | P2 |
| Speech-like artifacts | Noise interpretation, processing, high gain, and playback artifacts are discussed as alternatives; no preserved recording is documented. | `manual/03-terminology.md`; `manual/04-technology-research.md`; RSH-001 | Test materials, blinded outcomes, actual source recordings and analysis. | P1 |
| Auditory perception in noise | Ambiguous noise and speech-like pattern perception are acknowledged; no cited study or repository listening result. | `manual/03-terminology.md`; `manual/04-technology-research.md`; RSH-001 | Traceable perceptual literature and preregistered/blinded protocol. | P1 |
| Original recording preservation | Written standards require preserving originals and analyzing copies; no actual audio item is recorded in the baseline. | `manual/05-investigative-methodology.md`; `manual/06-evidence-preservation.md`; `evidence/README.md`; evidence template | Real acquisition examples, controlled storage implementation, validation of derivative links. | P1 |
| WAV and IQ acquisition | WAV/audio metadata is discussed generally; IQ capture is not documented. | `manual/05-investigative-methodology.md`; evidence template | Separate audio and IQ acquisition fields, sampling/device metadata, calibration and format guidance. | P1 |
| Spectral analysis | Mentioned as descriptive analysis; no analysis software, dataset, or output is included. | `manual/05-investigative-methodology.md` | Repeatable parameters, tool/version records, fixtures, and limits on interpretation. | P1 |
| Filtering and gain controls | Guidance says document transformations/settings and analyze copies. | `manual/05-investigative-methodology.md`; `manual/06-evidence-preservation.md` | Filter/gain specification schema, reproducible examples, and comparative results. | P2 |
| Processing artifact identification | Compression, AGC, encoding, and playback are possible confounds, not demonstrated findings. | `manual/04-technology-research.md`; `manual/05-investigative-methodology.md`; RSH-001 | Instrumented baseline and artifact characterization sources/tests. | P1 |
| Independent listening tests | Proposed blinded independent listening and recordkeeping are described. | `manual/05-investigative-methodology.md`; RSH-001 | Listener protocol details, consent/privacy process, analysis criteria, and actual test records. | P1 |
| Blind transcription | Listeners' independent word interpretations are suggested, but a formal transcription protocol is not specified. | `manual/05-investigative-methodology.md`; `manual/03-terminology.md` | Instructions, blinding, agreement metric, and handling of indeterminate audio. | P2 |
| Timestamp synchronization | Recording and clock offsets are called out; CM-001 suggests clock comparison. | `manual/05-investigative-methodology.md`; CM-001 | Common timebase, uncertainty field, drift procedure, and synchronized sample records. | P2 |
| Metadata and chain of custody | Evidence standard/template and preservation chapter specify metadata, hashes, processing history, and custody notes. | `evidence/README.md`; `manual/06-evidence-preservation.md`; `templates/EVIDENCE_LOG_TEMPLATE.md` | No actual chain-of-custody records or automated manifest checks. | P1 |
| HackRF One | No device-specific record or guidance identified. | None | Manufacturer/model-specific capability and limits sourced from authoritative documentation; calibration and safe acquisition protocol. | P2 |
| SDR software | No named SDR package or workflow identified. | None specific | Source-traceable versions, settings, acquisition format, and reproducible workflow. | P2 |
| RF measurement equipment | Generic instrument record type exists; no RF measurement inventory or measurement method. | `docs/evidence-model.md`; schema | Frequency range, bandwidth, calibration, antenna/probe, uncertainty, and actual records. | P1 |
| Acoustic measurement equipment | Generic instrument type exists; no acoustic instrument inventory or measurement method. | `docs/evidence-model.md`; schema | Microphone/calibrator specifications, placement, calibration, units, uncertainty, and records. | P1 |
| Directional audio systems | General directional audio topic; no equipment inventory or tested system. | `manual/04-technology-research.md`; RSH-001 | Traceable product/technical sources and experimentally bounded capability. | P2 |
| Bluetooth audio security | Bluetooth playback is an untested alternative in a personal report; no security analysis. | RSH-001; `manual/02-observations.md` | Relevant threat model, standards/source references, and a reasoned scope before testing. | P3 |
| Relevant patents | Patents named as a category, but no patent number or verified claim. | `manual/07-references.md`; RSH-001 | Search strategy, patent records, claim-level attribution, and separation from demonstrated capability. | P1 |
| Government research publications | No specific historical government document is cited; named programs are explicitly not established links. | `manual/07-references.md`; `manual/04-technology-research.md` | Primary documents, provenance, context, and documented relationships. | P1 |
| Documented research contracts | No contract identifier, agency, performer, statement of work, or result documented. | `manual/07-references.md`; `manual/04-technology-research.md` | Verifiable contract records and claim-by-claim links to research outcomes. | P2 |

## 6. Scientific Bibliography Assessment

**Repository facts.** `manual/07-references.md` explicitly states that Allan H. Frey is named in RSH-001 without complete bibliographic details. It reports no other specific peer-reviewed publication in the reviewed research document and no identified specific historical government publication, patent, technical publication, institution/program relationship, or government contract. RSH-001 presents technical topics and statements, but does not supply a complete traceable bibliography for them. `manual/04-technology-research.md` appropriately labels unsupported topics as leads or hypotheses and cautions that publication, patent, contract, or capability does not establish incident deployment.

| Requested source area | Baseline finding | Classification/status |
|---|---|---|
| Peer-reviewed publications | No complete external peer-reviewed citation identified in `manual/07-references.md`. | No source assessed; research gap. |
| Allan H. Frey research | Named in RSH-001; exact publication and findings remain to be identified and checked, per the references chapter. | Research lead, not a traceable citation in this repository. |
| Ultrasonic audio research | Parametric/directional audio is mentioned, but no specific study is cited. | Research hypothesis / lead. |
| RF demodulation research | RF auditory/demodulation topics appear without a specific reference or captured signal. | Research hypothesis / lead. |
| Auditory perception research | Ambiguous noise and speech-like interpretation are acknowledged; no study is cited. | Research lead. |
| Audio forensic methodologies | The manual specifies proposed preservation, analysis, and independent review practices but cites no external methodology standard or source. | Documented repository procedure, not an externally validated forensic standard. |
| Relevant patents | Patent category is noted; no number, title, assignee, filing, or grant is identified. | No patent claim assessed. |
| Historical government programmes | The references chapter says no specific document is cited and explicitly rejects inferring a connection from program names. | No documentary relationship established. |
| Government-funded research contracts | No contract number, agency, performer, statement of work, or result identified. | No contract assessed. |

The audit assessed source traceability against the files present, not the truth or quality of uncited external publications. No external publication, patent database, government archive, or contracting database was independently searched for this report. A source should be marked **DOCUMENTED SCIENCE** only after a specific source and relevant claim are verified; a patent remains **PATENT CLAIM** unless independent evidence supports more. A demonstrable capability remains **EXPERIMENTALLY DEMONSTRATED CAPABILITY**, not evidence of use in a particular event. Repository observations remain **PERSONAL OBSERVATION**; unsupported explanatory statements remain **RESEARCH HYPOTHESIS** or **UNVERIFIED CLAIM**, as appropriate.

## 7. Evidence and Forensic Capabilities

**Documented capabilities and controls**

- `evidence/README.md` defines stable `EV-YYYYMMDD-NNN` IDs, source metadata, derivatives, scenario links, SHA-256 use for available originals, privacy limits, and explicit missing-information labels.
- `templates/EVIDENCE_LOG_TEMPLATE.md` includes source device, filename, format, size, hash, storage reference, collection method, corroboration, verification, custody, and related evidence fields.
- `manual/06-evidence-preservation.md` directs preservation of originals, analysis of working copies, logging of transformations, and recording of custody events when appropriate.
- `manual/05-investigative-methodology.md` describes baseline recording, device settings, independent devices, audio/spectral review, blind listening, alternatives, repeatability, and limitations.
- `docs/evidence-model.md` and the schema provide provenance-bearing evidence, event, instrument, experiment, source, and conclusion record types. The evidence-specific schema permits a SHA-256 field matching 64 hexadecimal characters.
- `scripts/validate_integrity.py` checks historical documentation markers and changes in protected content; it is not an evidence-file hash verifier.

**Current limits**

No evidence record, original WAV, IQ file, hash manifest, custody log, audio measurement, RF measurement, listening-test result, or independent expert report is present in the baseline inventory. The evidence schema's hash field is optional, and the repository has no machine-readable schema-validation or media-integrity tool. The written protocol is a capability to document a method, not evidence that the method has been executed or validated.

## 8. Architectural Gaps

1. **No populated shared records:** the schema/model are design artifacts without data instances or a validator.
2. **Limited domain fields:** the generic instrument record requires only manufacturer and model; it does not standardize calibration, bandwidth, sample rate, antenna/microphone, units, uncertainty, or acquisition settings.
3. **No dedicated acquisition specification:** audio capture is discussed in prose; IQ, SDR, RF, acoustic, and synchronized multimodal capture do not have structured protocols.
4. **No experiment execution records:** the schema allows experiment records, but there are no experiment records, protocol fixtures, result datasets, or null-result examples.
5. **No executable provenance chain:** written guidance calls for hashes and derivatives, but no tool validates file hashes, custody transitions, related record IDs, or transformation graphs.
6. **No source registry populated:** sources and documentary relationships are supported abstractly by the model, while cited external sources and source-to-claim links are absent.
7. **No independent review workflow:** independent review is recommended, but no review record or structured reviewer method/materials/findings/limitations record exists.
8. **No domain-specific reproducibility checks:** the validators protect documentation form and historical text, not scientific methods, record semantics, measurement quality, or reproducibility.

## 9. Duplication and Anti-Drift Risks

- **Intentional overlap:** RSH-001, `manual/02-observations.md`, `manual/03-terminology.md`, and `manual/04-technology-research.md` share topics and summaries. The manual explicitly identifies these as navigation/synthesis, links back to RSH-001, and cautions that summaries do not replace original records. Future edits should preserve this source-of-truth relationship.
- **Repeated methodological guidance:** `manual/05-investigative-methodology.md`, `manual/06-evidence-preservation.md`, `evidence/README.md`, and `templates/EVIDENCE_LOG_TEMPLATE.md` repeat preservation and provenance concepts for different operational purposes. Divergent updates could produce inconsistent requirements.
- **Parallel schemas of record:** Markdown scenario/evidence templates and the JSON schema both model evidence-related concepts. There are no instances or mapping rules showing which representation is authoritative for a given record; duplication is a risk, not a demonstrated conflict.
- **Potentially confusing version labels:** RSH-001 front matter says version 1.0.0 while its body retains “Version 0.1 — Working Draft” and “END OF WORKING DRAFT — VERSION 0.1.” Both appear preserved in one document, but readers may confuse document revision with source-draft status.
- **Prior architecture snapshot is historical:** `docs/architecture/README.md` describes the state at a previous branch/commit in its “Audit Snapshot.” It is useful provenance, but must not be read as a current audit of this `main` baseline.
- **Governance protection is explicit:** `governance/ANTI_DRIFT.md` requires preserving observations and appendments, maintaining permanent IDs, separating subjects, and not fabricating records. `governance/VERSIONING.md` requires independent versions, actual timestamps, revision entries, and a changelog entry. The validators implement some but not all human-review requirements.

No duplicate identifier or contradictory policy was established by this content review. The listed items are maintenance risks and integration concerns, not findings of actual record corruption.

## 10. Recommended Integration Points

1. Use `schemas/investigation-record.schema.json` as the existing common envelope; extend it only where an authorized, concrete record requires typed fields. Avoid a competing database or schema.
2. Link source-backed technical claims through `source`, `claim`, and `relationship` records with exact locators and independent evidence states; retain Markdown chapters as readable synthesis and research leads.
3. Extend the existing evidence template/model with explicit audio and IQ acquisition metadata only after defining the requirements; preserve `evidence/README.md` as the policy authority.
4. Represent instruments through existing `instrument` records and experiments through existing `experiment` records; add calibration, settings, uncertainty, controls, and protocol version in a documented, schema-validated manner.
5. Link measurement/evidence records to event and experiment records using `related_record_ids` or appropriate relationship records; preserve original media in controlled storage and reference rather than commit sensitive files.
6. Record independent reviews and reproducibility outcomes as source-backed records or scoped additions to existing record types before introducing new parallel catalogs.
7. Keep the three existing documentation validators for documentation/governance checks; treat any future schema, hash, and record-link validation as complementary checks, not replacements.

## 11. Recommended Phase 2 Scope

Phase 2 should remain evidence- and source-first, with no inference about the cause of an individual event:

1. Build a verified bibliography beginning with the exact Allan H. Frey primary reference already named as incomplete; add peer-reviewed RF auditory, ultrasonic audio, auditory perception, and audio-forensics sources only after checking bibliographic identity and claim context.
2. Create source records and narrowly scoped claims with stable locators and evidence classifications. Explicitly separate documented science, experimentally demonstrated capability, patent claim, research hypothesis, personal observation, and unverified claim.
3. Define a minimal audio acquisition/analysis protocol around preserved originals, metadata, hash, clock uncertainty, processing logs, blinded listening/transcription, and null results; specify IQ/RF acquisition separately rather than implying it from audio guidance.
4. Define instrument and experiment field requirements using the existing model/schema, then add a small set of non-sensitive example records and validate them. Examples must be clearly marked as fixtures, not observations.
5. Decide how source Markdown, record instances, evidence files, and derived analysis outputs link together, without duplicating source-of-truth content.

These are recommendations, not authorization to implement Phase 2 or to create investigative findings.

## 12. Dependencies and Blockers

- **Source verification:** exact primary and peer-reviewed source documents are absent from the repository and must be obtained and reviewed before making source-backed technical claims.
- **Measurement requirements:** an authorized scope must determine whether and how any RF, acoustic, audio, or SDR measurement is pursued; no equipment or measurement data is inventoried.
- **Privacy and lawful handling:** source media and any future observations may be sensitive; existing evidence standards require controlled storage and lawful collection.
- **Architecture decisions:** future record formats and field requirements should extend the existing schema/model, but current documents do not specify storage or schema-validation tooling.
- **No blocker to this baseline report:** previous-session artifacts named in the task prompt are not prerequisites and were not needed.

## 13. Prioritized Action Matrix

| Priority | Action | Existing integration point | Completion evidence |
|---|---|---|---|
| P1 | Verify and document exact primary citation for Allan H. Frey's microwave auditory research and the claim it supports. | `manual/07-references.md`; schema source/claim records | Traceable bibliographic record, claim locator, and explicit limits. |
| P1 | Establish an evidence-status/source-linking convention for scientific claims and research leads. | `manual/04-technology-research.md`; `docs/evidence-model.md` | Each claim has a source or is expressly marked as a research hypothesis, personal observation, or unverified claim. |
| P1 | Specify a minimal audio preservation and analysis protocol with blind listening, timestamp uncertainty, transformations, and null outcomes. | `manual/05-investigative-methodology.md`; evidence template | Versioned protocol with required fields and a reproducible test fixture, not an asserted incident result. |
| P1 | Define RF/IQ acquisition and instrument metadata needs before acquiring or interpreting RF data. | Schema instrument/experiment/evidence types; `docs/architecture/README.md` | Documented, reviewed acquisition requirements and instrument limits; no deployment inference. |
| P1 | Validate machine-readable records and their provenance links once concrete record examples are authorized. | `schemas/investigation-record.schema.json`; `docs/evidence-model.md` | Valid and invalid test fixtures with deterministic validation output. |
| P2 | Add focused sourced research on ultrasonic audio, RF demodulation, perception, and audio-forensic methods. | `manual/04-technology-research.md`; `manual/07-references.md` | Reviewed primary/peer-reviewed sources and bounded claim associations. |
| P2 | Extend instrument/experiment records for calibration, uncertainty, and acquisition settings. | Existing schema and evidence model | Explicit field definitions, backward-compatibility review, and passing validation fixtures. |
| P2 | Establish manifest verification for actual media and derivative relationships if a need and safe storage design are approved. | Evidence standards/template; architecture proposal | Tested hash/manifest verification that distinguishes integrity from truth or attribution. |
| P3 | Assess Bluetooth security, specific SDR/equipment models, patents, and government contracts only where source-backed scope justifies them. | `manual/07-references.md`; source records | Traceable records and stated relevance; no assumed link to an event. |

## 14. Audit Limitations

- The audit is a repository-content baseline review at the base commit in Section 2; it is not a scientific literature review, external source verification, forensic examination, RF survey, acoustic measurement, legal opinion, or expert assessment.
- Bibliography findings are limited to what is documented in tracked repository files. No external repositories, patent databases, government archives, contract databases, or third-party sites were searched for this report.
- The technical matrix assesses presence or absence of repository coverage, not the validity of the underlying mechanisms.
- The report does not verify whether any reported event occurred or establish a cause, technology, source, actor, deployment, or intent.
- “Missing” refers to absence from the audited repository baseline, not proof that information does not exist elsewhere.
- The audit does not execute or validate equipment procedures; it reviews their written description and the repository's documentation tooling.

## 15. Final Verification Summary

At baseline, the audit confirmed the repository and commit SHA in Section 2, reviewed all 33 tracked files, read the governance policies, and found no existing `docs/audits/` directory. The report is non-empty and all 15 required sections are present. `scripts/validate_documentation.py`, `scripts/validate_versions.py --base origin/main`, and `scripts/validate_integrity.py --base origin/main` passed; `git diff --check` passed. At the time of this report validation, only this report and its required `CHANGELOG.md` entry were modified. Commit, push, and draft-PR status are reported after those actions and are not represented here as completed.

## Revision History

| Version | Timestamp | Description | Author |
|---|---|---|---|
| 1.0.0 | 2026-11-16T13:35:58-06:00 | Initial Phase 1 repository baseline audit, including completed documentation validation. | GitHub Copilot |
