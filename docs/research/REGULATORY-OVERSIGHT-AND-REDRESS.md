---
Document Title: Regulatory Oversight and Redress
Document ID: RSH-ETHICS-001
Author: Kevin Mahan
Version: 1.2.0
Created: 2026-11-26T22:33:31-06:00
Last Updated: 2026-11-27T03:33:28-06:00
---

# Regulatory Oversight and Redress

## Authorship and AI-Assistance Disclosure

Kevin Mahan is the document owner of record, consistent with repository attribution. Version 1.0.0 was drafted with AI assistance (GitHub Copilot), and its revision-history entry, which names GitHub Copilot, is preserved unchanged. Version 1.1.0 corrects the ownership metadata and records source-verification status; the 1.1.0 changes were also prepared with AI assistance. Version 1.2.0 integrates source-review records supplied by the document owner from an external AI-assisted review (ChatGPT, 2026-11-27); it was likewise prepared with AI assistance (GitHub Copilot), and GitHub Copilot did not itself access the sources (Section 9.2). AI-assisted drafting does not substitute for review by the document owner or by qualified legal and ethics reviewers, and this disclosure does not claim that any such review has occurred.

This document formalizes the ethics and accountability themes stated in the [Author's Statement and Research Abstract](../../README.md#authors-statement-and-research-abstract) of the repository README. It is a governance-oriented research document. It is not legal advice, a legal opinion, an incident report, or a finding about any person, institution, or technology. It creates no investigative subject, scenario, or evidence record.

## 1. Purpose, Scope, and Status Labels

The README abstract states that the initiative examines "civil liability, regulatory oversight, informed consent, human-subject protections, institutional accountability, and lawful redress," and that its purpose is "education, transparency, human dignity, and lawful, nonviolent accountability—not retaliation." This document organizes those themes so that readers can separate what is legally required, what is an ethical principle, and what this archive proposes.

Every statement below carries one of these labels (version 1.1.0 refined the legal labels of version 1.0.0; no ethical position was changed):

| Label | Meaning |
|---|---|
| **VERIFIED LEGAL REQUIREMENT** | A requirement whose primary text has been reviewed and recorded in Section 9.1. None exists in this document yet. |
| **CONDITIONAL LEGAL APPLICABILITY** | A legal requirement that may exist but is unverified here, and whose applicability depends on jurisdiction, actor, funding, and facts. It is not a statement that the requirement applies to this archive or to anyone. |
| **ETHICAL PRINCIPLE** | A widely discussed normative principle or the author's stated conviction. It is not a legal obligation, and does not create enforceable legal rights, liability, or proof of misconduct, unless a law separately adopts it. |
| **PROPOSED SAFEGUARD** | A practice proposed for this archive. It is not a legal requirement and has not been implemented or independently reviewed. |
| **UNRESOLVED QUESTION** | A matter that cannot be classified on the evidence available. |

Version 1.0.0 used an `ESTABLISHED LEGAL REQUIREMENT` label for statements that were not verified against primary texts. Those statements are now classified under the labels above; the original wording of 1.0.0 remains available in Git history (commit bb0bb79).

### Source and verification limits

No primary legal text, statute, regulation, court decision, or regulatory guidance has been reviewed in full for this repository. An attempt to access the four primary sources named in Section 9 failed (see Section 9.1), so every source remains `UNVERIFIED`: its text, current version, and applicability have not been checked here. This document does not cite specific statute sections, case law, or agency rules, and it does not state what the law requires in any particular jurisdiction. Research-ethics instruments do not by themselves create enforceable legal rights, establish liability, or prove misconduct. Consult a qualified attorney and the primary texts before relying on any legal point.

**Version 1.2.0 update:** The paragraph above records the state at version 1.1.0 and is preserved. Since then, the document owner supplied an external, AI-assisted review (ChatGPT, 2026-11-27) confirming access to the four sources at claim-level scope. That review is not independent Copilot verification, is not exhaustive provision verification, and does not change the limits stated above on legal effect. Current classifications are in Section 9.2.

Hypotheses and findings are kept separate throughout, as required by the [Anti-Drift Policy](../../governance/ANTI_DRIFT.md) (AD-007) and the [Evidence Record Model](../evidence-model.md).

## 2. Research Ethics

- **ETHICAL PRINCIPLE:** Research should respect persons, seek to benefit and avoid harm, and distribute burdens and benefits fairly. These three themes are commonly associated with the Belmont Report (Section 9).
- **ETHICAL PRINCIPLE (author's stated conviction):** All human beings are fundamentally equal; the ability to observe, influence, or exercise power does not establish the ethical or legal right to do so ([README abstract](../../README.md#authors-statement-and-research-abstract)). The same abstract states that knowledge should support education and transparency, not domination or retaliation.
- **PROPOSED SAFEGUARD:** State a research question's scope, evidence basis, and limits before drawing conclusions. Consider alternative explanations explicitly, as the README requires, and record null and contradicting results.
- **PROPOSED SAFEGUARD:** Do not target, locate, identify, confront, or retaliate against any person or institution on the basis of an unverified hypothesis. The repository's stated approach is lawful and nonviolent.
- **PROPOSED SAFEGUARD:** Disclose the author's perspective and any personal stake. The archive is partly based on the author's own reported experiences, which are reports, not independent findings.

## 3. Informed Consent

- **CONDITIONAL LEGAL APPLICABILITY (unverified):** Where research with human subjects is governed by a regulation or institutional policy, informed consent may be required. The content of any such requirement has not been verified here, and whether any such rule applies to this archive is an `UNRESOLVED QUESTION`. See Section 9 and the applicability caution there.
- **ETHICAL PRINCIPLE:** Voluntary, informed consent is a core principle of human-subject research, reflected in the Nuremberg Code and the Declaration of Helsinki (Section 9). It also underlies the author's stated concern about non-consensual influence and observation.
- **PROPOSED SAFEGUARD:** Do not recruit or involve third parties as subjects, and do not record, measure, or test other people, without their documented, informed, and voluntary agreement and a lawful basis. The archive currently contains no such participant studies.
- **PROPOSED SAFEGUARD:** Any future experiment involving other people must first be separately authorized, described in a written protocol, reviewed independently, and permit withdrawal at any time.

## 4. Human-Subject Protections

- **ETHICAL PRINCIPLE:** The repository's research addresses technologies whose hypothesized misuse could cause psychological, social, and economic harm (README abstract). The same potential for harm applies to any experiment that exposes a person to audio, radio-frequency, or other stimuli.
- **UNRESOLVED QUESTION:** No legal requirement governing exposure of persons to experimental stimuli has been identified or verified for this archive. The [architecture proposal](../architecture/README.md) states that laboratory transmission, if ever separately authorized, must be opt-in, lawful, and constrained, and that uncontrolled jamming is out of scope. That is a repository boundary, not a statement of law.
- **PROPOSED SAFEGUARD:** Do not expose any person, including the author, to a stimulus or exposure for experimental purposes under this archive without prior written protocol, risk review, independent oversight (Section 7), and applicable legal and medical advice.
- **PROPOSED SAFEGUARD:** Treat reported distress as a matter for qualified medical or mental-health care. Documentation of an experience does not replace care, and care does not invalidate documentation.

## 5. Privacy and Individual Rights

- **CONDITIONAL LEGAL APPLICABILITY (unverified):** Laws governing recording, interception, surveillance, and personal data may vary by jurisdiction, including rules on who must consent to a recording. The [Evidence Documentation Standards](../../evidence/README.md) already require that recording, observation, storage, and evidence collection comply with applicable law. This document does not verify or state which laws apply.
- **ETHICAL PRINCIPLE:** Individuals have an interest in privacy and in not being observed, impersonated, or falsely attributed communications without justification (README abstract).
- **PROPOSED SAFEGUARD:** Do not publish sensitive personal information, identifying details of third parties, or precise location data. Keep sensitive originals in access-controlled storage, as stated in the evidence standards and the [Evidence Record Model](../evidence-model.md).
- **PROPOSED SAFEGUARD:** Use the existing missing-information designations (`NOT RECORDED`, `NOT AVAILABLE`, `NOT APPLICABLE`, `PENDING VERIFICATION`) rather than inferring identities or facts.
- **PROPOSED SAFEGUARD:** Name individuals or organizations only where a source-backed relationship exists, record the exact scope of the source, and keep allegations separate from established facts.

## 6. Evidentiary Standards

The repository's existing vocabulary applies and is not changed here:

- The [Evidence Record Model](../evidence-model.md) defines the evidence states (`OBSERVED`, `REPRODUCED`, `CORRELATED`, `MECHANISM_SUPPORTED`, `ATTRIBUTION_CANDIDATE`, `ATTRIBUTION_SUPPORTED`, `CLAIM_ONLY`, `CONTRADICTED`, `UNRESOLVED`). A patent, lawsuit, report, or observed capability does not alone establish deployment, causation, intent, or attribution. Correlation is not causation.
- The README abstract states that technological capability, actual deployment, responsible-party attribution, causation, and damages each "require separate evidentiary support."
- The [Evidence Documentation Standards](../../evidence/README.md) require preserved originals, recorded provenance, transformations, and SHA-256 hashes where originals are available. A matching hash supports file integrity; it does not establish that the recorded event is true or identify its source.
- The [Phase 2A bibliography](PHASE-2A-SCIENTIFIC-BIBLIOGRAPHY.md) and [Phase 2B citation audit](../audits/PHASE-2B-CITATION-URL-AUDIT.md) record that full-text review of a source is not independent experimental replication.

**CONDITIONAL LEGAL APPLICABILITY (unverified):** Legal standards of proof and rules of evidence may differ by forum and jurisdiction. This archive's evidence states are research classifications, not legal standards, and do not predict how a court or agency would treat any material.

**PROPOSED SAFEGUARD:** Before any claim of misconduct is stated beyond `CLAIM_ONLY`, require identified, independent, and preserved evidence for each element: capability, deployment, attribution, causation, and damages. Treat each element separately.

## 7. Institutional Accountability and Independent Oversight

- **ETHICAL PRINCIPLE (author's stated conviction):** Concentrated power without accountability can encourage moral overreach and erosion of human boundaries (README abstract).
- **UNRESOLVED QUESTION:** No legal requirement or responsible institution has been identified here. This document identifies no specific institution as responsible for any event. A documented capability, program, patent, or filing does not establish that an institution deployed a technology or acted unlawfully.
- **PROPOSED SAFEGUARD:** When an institution is discussed, rely on identifiable primary or authoritative sources, state exactly what each source says, and keep a documented organizational relationship separate from any allegation about that organization, as the Evidence Record Model requires for relationship records.
- **PROPOSED SAFEGUARD (independent oversight):** Seek review by people independent of the author before any conclusion is promoted above a hypothesis. Qualified reviewers might include a relevant technical expert, an audio-forensics or RF specialist, a research-ethics reviewer, and an attorney. The Phase 1 audit notes that no independent review record or workflow exists yet. Any reviewer's method, materials, findings, and limitations should be recorded as a separate, attributed record. No such review has been performed.

## 8. Lawful Reporting and Redress

- **CONDITIONAL LEGAL APPLICABILITY (unverified):** Avenues for reporting and remedies may depend on jurisdiction and facts. Possibilities that may exist include reports to law enforcement, complaints to regulators, and civil claims. Their availability, requirements, and deadlines have not been verified here, and no specific avenue is asserted. Research-ethics instruments do not by themselves create a right to redress.
- **ETHICAL PRINCIPLE:** Accountability should be sought through lawful, nonviolent means, consistent with the README statement that the purpose is accountability, not retaliation.
- **PROPOSED SAFEGUARD:** Before reporting or filing, consult a qualified attorney about jurisdiction, applicable law, and time limits. Report only what is supported, labeled with its evidence state.
- **PROPOSED SAFEGUARD:** Provide originals and records under appropriate controls, keeping preserved originals unaltered, and describe the limits of the evidence honestly, including alternative explanations and gaps.
- **PROPOSED SAFEGUARD:** Do not use this archive to harass, threaten, or publicly accuse an identified person or institution without source-backed support and legal advice.

## 9. Instruments Named for Orientation (UNVERIFIED in this archive)

These are listed so that readers can locate the primary texts. Their contents have not been reviewed for this document and nothing here summarizes them as binding on the author or any institution.

| Instrument | Type | Relevance | Status in this archive |
|---|---|---|---|
| The Belmont Report (1979, United States) | Ethical principles for human-subject research | Respect for persons, beneficence, justice | `UNVERIFIED`; not reviewed |
| The Nuremberg Code (1947) | Ethical principles | Voluntary consent in human experimentation | `UNVERIFIED`; not reviewed |
| Declaration of Helsinki (World Medical Association) | Ethical principles | Medical research involving human participants | `UNVERIFIED`; not reviewed; current version not checked |
| 45 CFR Part 46, "Protection of Human Subjects" (United States, HHS regulation) | Regulation containing multiple subparts | Part 46 as a whole is not the Common Rule. The Common Rule is commonly understood to be the baseline policy codified at Subpart A of Part 46 and adopted by other federal departments and agencies in their own regulations; the other subparts address additional matters. | `UNVERIFIED`; not reviewed. Subpart structure and the Subpart A relationship are stated from general knowledge and must be confirmed against the primary text. Coverage is limited to defined categories of research, and whether any part applies to this independent archive is an `UNRESOLVED QUESTION`. |

Research-ethics instruments in this table are not self-executing sources of enforceable rights against any person, and none establishes liability or proves misconduct. Legal effect, if any, depends on a law or regulation that adopts the instrument and on applicability to the actor and research concerned.

### 9.1 Source Verification Records

An attempt to access each primary source on 2026-11-26 (America/Chicago), after the request received at 22:37:01-06:00 and before this revision at 22:37:23-06:00, failed for all four. The exact error for each was: `WebFetchBlockedUrlError: failed to lookup address information: No address associated with hostname`. It was classified as an infrastructure (DNS resolution) failure, not an authorization denial or a content result. The exact per-attempt access timestamps were not captured. Because no source text was retrieved, no document was reviewed and no proposition is supported. A resolvable URL alone would not have established verification. Fields below that depend on reading the source are `NOT AVAILABLE`.

| Field | Belmont Report | 45 CFR Part 46 | Declaration of Helsinki | Nuremberg Code |
|---|---|---|---|---|
| Issuing authority | `NOT AVAILABLE` (not confirmed from source) | `NOT AVAILABLE` (not confirmed from source) | `NOT AVAILABLE` (not confirmed from source) | `NOT AVAILABLE` (not confirmed from source) |
| Document title | `NOT AVAILABLE` | `NOT AVAILABLE` | `NOT AVAILABLE` | `NOT AVAILABLE` |
| Publication or revision date | `NOT AVAILABLE`. The requested 2024 Helsinki revision is unconfirmed. | `NOT AVAILABLE`; current-version date unconfirmed | `NOT AVAILABLE`; the requested 2024 revision is unconfirmed | `NOT AVAILABLE` |
| Primary source URL (supplied by the document owner) | https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46 | https://www.wma.net/policies-post/wma-declaration-of-helsinki/ | https://history.nih.gov/display/history/Nuremberg+Code |
| Actual access outcome | Failed: DNS resolution error | Failed: DNS resolution error | Failed: DNS resolution error | Failed: DNS resolution error |
| Sections reviewed | None | None | None | None |
| Supported propositions | None | None | None | None |
| Applicability limitations | Unconfirmed; an ethical statement, not by itself an enforceable legal instrument | Unconfirmed; see Section 9 on Part 46 versus Subpart A; scope-dependent | Unconfirmed; an ethical statement of a professional body, not by itself an enforceable legal instrument | Unconfirmed; a historical ethical statement, not by itself an enforceable legal instrument |
| Verification status | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` |

The applicability limitations above are cautions stated from general knowledge, not findings from the sources.

### 9.2 Source Register and Current Verification Classification (version 1.2.0)

Section 9.1 is a historical record of the 2026-11-26 failed-access checkpoint and is not rewritten. This section records the later state. The sources below were reported accessible in an external AI-assisted review (ChatGPT, 2026-11-27) supplied by the document owner. GitHub Copilot did not access these sources for this revision and has not independently verified any of them. The URLs below are those supplied in the source register and differ for SRC-001 and SRC-004 from the URLs recorded in Section 9.1.

| ID | Source | Issuer and date (as supplied) | URL | Type | Current classification |
|---|---|---|---|---|---|
| SRC-001 | Belmont Report | National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research, April 18, 1979 | https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html | Ethical guidance | `EXTERNALLY REVIEWED (ChatGPT, 2026-11-27)`; `NOT INDEPENDENTLY VERIFIED BY COPILOT` |
| SRC-002 | 45 CFR Part 46, Protection of Human Subjects | Federal regulation; eCFR displayed currency 2026-11-24 | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46 | Federal regulation | `EXTERNALLY REVIEWED (ChatGPT, 2026-11-27)`; `NOT INDEPENDENTLY VERIFIED BY COPILOT`; applicability `UNRESOLVED` |
| SRC-003 | WMA Declaration of Helsinki | World Medical Association, October 2024 revision | https://www.wma.net/policies-post/wma-declaration-of-helsinki/ | Professional medical research ethics | `EXTERNALLY REVIEWED (ChatGPT, 2026-11-27)`; `NOT INDEPENDENTLY VERIFIED BY COPILOT` |
| SRC-004 | Nuremberg Code | USA v. Karl Brandt et al., August 19, 1947 | https://encyclopedia.ushmm.org/content/en/article/the-nuremberg-code | Historical judicial and research ethics instrument | `EXTERNALLY REVIEWED (ChatGPT, 2026-11-27)`; `NOT INDEPENDENTLY VERIFIED BY COPILOT` |

For SRC-004, the registered URL is an encyclopedia article presenting the text, not the original judicial record; this document does not state that the original record was reviewed.

**Claim-level review scope.** Review is recorded only for the provisions listed below. Accessibility of a source is not exhaustive verification of its provisions, and provisions not listed were not reviewed. Where this document's support for a statement is insufficient, the preliminary classification is retained.

| ID | Provisions in review scope |
|---|---|
| SRC-001 | A (research and practice boundaries); B.1 (autonomy, additional protections); B.2 (beneficence, harm reduction); B.3 (justice, equitable distribution); C.1 (informed consent); C.2 (risk and benefit assessment); C.3 (equitable participant selection) |
| SRC-002 | Subparts A (Common Rule), B (pregnancy and fetal protections), C (prisoner protections), D (children's protections), E (IRB registration); 46.101 (applicability); 46.102 (definitions); 46.104 (exemptions); 46.109-113 (IRB review and oversight); 46.116 (informed consent and exceptions); 46.117 (consent documentation and waivers); 46.123 (federal support termination) |
| SRC-003 | Paragraphs 1-2 (scope, ethical responsibility); 6-9 (participant rights); 15 (research-related injury); 16-18 (risk assessment, monitoring); 19-20 (vulnerability); 21-22 (scientific rigor, protocols); 23 (independent ethics review); 24 (privacy, confidentiality); 25-32 (consent, qualified exceptions); 35-36 (registration, reporting) |
| SRC-004 | Principles 1-10: voluntary consent; social value; scientific justification; avoiding unnecessary suffering; restrictions on anticipated fatal or disabling harm, subject to the historical text's qualified exception; proportionate risk; protective preparations; qualified personnel; participant termination rights; researcher termination responsibility |

**SRC-002 distinctions.** These four concepts are separate and must not be conflated:

- *Regulatory applicability* (46.101): whether Part 46 covers given research at all. Subpart A is the Common Rule baseline; Subparts B-E address additional matters.
- *Exemption* (46.104): research within a covered scope that is excluded from some requirements.
- *Consent waiver or alteration* (46.116): conditional exceptions to informed-consent requirements.
- *Documentation waiver* (46.117): conditional waiver of the requirement to document consent, which is distinct from waiving consent itself.

The conditions for each are not detailed here (Section 11).

### 9.3 Comparative Framework

This matrix is limited to the provisions in the review scope of Section 9.2. "Not itemized" means the dimension is not explicitly addressed by the provisions in review scope; it does not assert that the instrument as a whole is silent. Entries marked (preliminary) are not supported at provision level by the review record.

| Dimension | SRC-001 Belmont | SRC-002 45 CFR 46 | SRC-003 Helsinki | SRC-004 Nuremberg |
|---|---|---|---|---|
| Autonomy and consent | B.1; C.1 | 46.116; 46.117 | 6-9; 25-32 | Principle 1 |
| Risk minimization | B.2; C.2 | 46.109-113 (preliminary; criteria not itemized) | 15; 16-18 | Principles 4, 5, 6, 7 |
| Independent ethics oversight | Not itemized | 46.109-113; Subpart E | 23 | Not itemized; Principle 8 addresses qualified personnel only |
| Equitable participant selection | B.3; C.3 | Subparts B, C, D (additional protections); 46.109-113 (preliminary) | 19-20 | Not itemized |
| Privacy and confidentiality | Not itemized | Not itemized (preliminary) | 24 | Not itemized |
| Scientific validity | Not itemized | Not itemized (preliminary) | 21-22 | Principles 2, 3, 8 |
| Withdrawal rights | Not itemized (preliminary; related to C.1) | Not itemized (preliminary; related to 46.116) | Not itemized (preliminary; related to 25-32) | Principle 9 |
| Termination safeguards | Not itemized | 46.113 (preliminary); 46.123 | 16-18 (monitoring; preliminary) | Principle 10 |

Only SRC-002 is a regulation, and its legal effect is limited to research within its applicability. SRC-001, SRC-003, and SRC-004 are ethical or historical instruments that do not independently create enforceable legal obligations.

### 9.4 Applicability Matrix

| ID | Statement | Classification |
|---|---|---|
| ETH-001 | Participant autonomy | `ETHICAL PRINCIPLE` |
| ETH-002 | Harm minimization | `ETHICAL PRINCIPLE` |
| ETH-003 | Informed consent principles | `ETHICAL PRINCIPLE` |
| REG-001 | Oversight of covered research | `CONDITIONAL LEGAL APPLICABILITY`; limited to research covered by SRC-002 |
| REG-002 | Conditional consent exceptions | `CONDITIONAL LEGAL APPLICABILITY`; conditions not detailed here |
| REG-003 | Part 46 versus Subpart A | `CONDITIONAL LEGAL APPLICABILITY`; Part 46 as a whole is not the Common Rule, which is Subpart A |
| LAW-001 | Part 46 applies universally | `INCORRECT` |
| LAW-002 | All instruments independently establish enforceable legal obligations | `INCORRECT` |
| LAW-003 | Applicability to specific events | `UNRESOLVED` |
| LAW-004 | Availability of legal remedies | `UNRESOLVED` |
| EVD-001 | Occurrence of alleged misconduct | `NOT ESTABLISHED` |
| EVD-002 | Responsibility of any party | `NOT ESTABLISHED` |

Source verification does not establish that any alleged activity occurred. This document identifies and accuses no individual, organization, or institution.

## 10. Distinction Between Hypotheses and Findings

- A **hypothesis** is a proposed explanation that remains open to testing, such as the README's hypothesized harms or any suspected unauthorized use of a technology. It is labeled `CLAIM_ONLY` or `UNRESOLVED` until evidence supports a more specific state.
- A **finding** requires identified evidence, recorded method and limits, and a rationale for the evidence state. Independent verification is a separate, higher bar.
- Reported experiences, such as those in [RSH-001](../../research/001-voice-to-skull-v2k.md) and [SCN-001](../../scenarios/001-audible-beeping-transitioning.md), are reports. Suspected misconduct is not an established finding (README abstract).
- This document makes no finding about capability, deployment, attribution, causation, damages, intent, or liability, and none should be inferred from it.

## 11. Open Items and Missing Information

- Primary legal and ethics texts in Section 9 have not been obtained or reviewed; access failed on 2026-11-26 (Section 9.1). Outstanding research requirement: retrieve and review each source in full from an environment with network access, then record issuing authority, title, publication or revision date, access timestamp, sections reviewed, supported propositions, applicability limits, and verification status.
- Confirm the current Declaration of Helsinki revision (the document owner requested the 2024 version) and the current version of 45 CFR Part 46, including its subpart structure and the Subpart A relationship.
- Confirm the original issuing authorities and dates of the Belmont Report and Nuremberg Code from the sources.
- Whether any human-subject regulation, institutional review requirement, or privacy law applies to this archive remains an `UNRESOLVED QUESTION`.
- No independent ethics review, legal review, or oversight record exists.
- No jurisdiction-specific reporting or redress pathway has been identified or verified.
- Version 1.2.0 outstanding requirements: detailed regulatory exceptions (the conditions for exemptions, consent waivers, and documentation waivers under SRC-002); jurisdiction-specific applicability; independent legal and ethics review; independent factual corroboration. Independent Copilot or human verification of the externally reviewed sources (Section 9.2) and provision-level review beyond the recorded scope also remain outstanding.

## Related Documents

- [README — Author's Statement and Research Abstract](../../README.md#authors-statement-and-research-abstract)
- [Research and Investigative Field Manual](../../MANUAL.md)
- [Evidence Documentation Standards](../../evidence/README.md)
- [Evidence Record Model](../evidence-model.md)
- [Investigation Framework Architecture](../architecture/README.md)
- [Phase 1 Repository Baseline Audit](../audits/PHASE-1-REPOSITORY-AUDIT.md)
- [Phase 2A Scientific Bibliography](PHASE-2A-SCIENTIFIC-BIBLIOGRAPHY.md)
- [Versioning Policy](../../governance/VERSIONING.md) and [Anti-Drift Policy](../../governance/ANTI_DRIFT.md)

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-26T22:33:31-06:00 | Initial publication formalizing the README ethics and accountability abstract, separating legal requirements, ethical principles, and proposed safeguards without reviewing primary legal texts. | GitHub Copilot |
| 1.1.0 | 2026-11-26T22:37:23-06:00 | Corrected ownership metadata to Kevin Mahan and added AI-assistance disclosure; reclassified unverified legal statements; distinguished 45 CFR Part 46 from Subpart A (Common Rule); recorded failed access to four primary sources and their unverified status; added outstanding research requirements. | Kevin Mahan |
| 1.2.0 | 2026-11-27T03:33:28-06:00 | Integrated externally reviewed research ethics sources (SRC-001 to SRC-004; ChatGPT, 2026-11-27, not independently verified by Copilot); added source register, claim-level review scope, comparative framework, and applicability matrix; preserved Section 9.1 failed-access record; retained outstanding requirements. | Kevin Mahan |
