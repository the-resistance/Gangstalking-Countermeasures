---
Document Title: Phase 2A Scientific Bibliography
Document ID: RSH-PHASE2A-001
Author: GitHub Copilot
Version: 1.2.0
Created: 2026-11-16T13:57:21-06:00
Last Updated: 2026-11-16T14:23:36-06:00
---

# Phase 2A Scientific Bibliography

## Scope and Methodology

This controlled increment addresses source gaps identified in the [Phase 1 audit](../audits/PHASE-1-REPOSITORY-AUDIT.md), especially its research coverage matrix and bibliography assessment. It covers the existing technical topics in [RSH-001](../../research/001-voice-to-skull-v2k.md) and the [technology research chapter](../../manual/04-technology-research.md). It does not report an experiment, incident finding, equipment deployment, or investigation record.

Verification was attempted on 2026-11-16. The authoritative publication or index was consulted for bibliographic identity, and relevant source text was reviewed before a technical statement was classified as documented. A source's own experimental conditions and limits are kept separate from any incident-specific question. The bibliography below contains **two verified references**: one primary technical document and one conference publication checked against its conference index and abstract only. The eight explicitly numbered leads are **UNVERIFIED** for their substantive findings. The NIST index records cited for two leads verify bibliographic metadata only, not the contents of those reports.

## Source Verification Criteria

Acceptable sources include original peer-reviewed or conference papers, university or official research publications, original reports, and recognized standards. A complete entry identifies the authors, exact title, date, publisher or institution, applicable volume and pages, a stable identifier and authoritative locator, the relevant finding or method, conditions, limitations, classification, and repository topic. Where a field is inapplicable or unavailable, it is identified as such rather than guessed. The relevant text must be checked, not just a search result or generated citation; bibliographic metadata alone cannot verify a finding. Standards and guidance are not experiments.

## Verified Primary-Source Bibliography

### V1 — Speech intelligibility and the modified rhyme test

- **Citation:** S. Voran. *Conducting ABC-MRT and ABC-MRT16 Tests*. National Telecommunications and Information Administration, Institute for Telecommunication Sciences, 2013; updated March 2, 2017. Original technical documentation; journal volume, issue, pages, DOI, and report number are not specified.
- **Stable identifier and verified locator:** Git revision `afaeb9a0551cb456c175bc1150a14d1edbb6c7a1`, [original NTIA document, Background and Prepare SUT Recordings](https://github.com/NTIA/ABC-MRT16/blob/afaeb9a0551cb456c175bc1150a14d1edbb6c7a1/readme.md). The author, title, dates, and relevant context were checked in that document.
- **Relevant method and finding:** The document describes the human modified rhyme test as a six-alternative word-identification task with scores corrected for guessing. It describes ABC-MRT and ABC-MRT16 as algorithms intended to estimate such scores from test recordings, and reports deviations for subsets of reference material across 139 conditions.
- **Conditions:** Its reference recordings are mono linear PCM, 16 bits per sample at 48,000 samples per second, with four talkers and 1,200 files. The reported subset deviations are relative to the 1,200-file ABC-MRT results, not necessarily to human listener scores. The document gives quiet and specified noise conditions as examples, not as proof that any particular example was among the 139.
- **Limitations:** This is the author's technical documentation, not the separately cited conference papers or the text of ANSI S3.2. The described scores concern the specified test material and system conditions; they do not establish intelligibility, words, speaker identity, or a cause in an unrelated recording. The underlying data and independently replicated results were not reviewed.
- **Classification:** **DOCUMENTED SCIENCE** for the source's bounded description of the test and reported comparison; this does not certify performance in other conditions.
- **Repository topic:** Speech perception and intelligibility in noise; independent listening in RSH-001 sections 3.5 and 7.3.

### V2 — Ultrasonic sound generation in a musical interface

- **Citation:** Miha Ciglar. "An Ultrasound Based Instrument Generating Audible and Tactile Sound." *Proceedings of the International Conference on New Interfaces for Musical Expression*, Sydney, Australia, 2010, pp. 19-22. ISSN `2220-4806`; DOI `10.5281/zenodo.1177745`. Volume and issue are not specified in the index.
- **Verified locator:** [Conference bibliography, 2010 proceedings entry and abstract](https://github.com/NIME-conference/NIME-bibliography/blob/f401a83a135958cb365997b8f10a2696905962ff/paper_proceedings/nime2010.bib). Citation metadata and the abstract were checked against this conference-maintained index; the DOI destination and full paper were not accessed.
- **Relevant method:** The indexed abstract describes an interactive musical instrument using airborne ultrasound and discusses audible sound generation by self-demodulation during propagation in air.
- **Conditions:** The abstract identifies airborne ultrasound and the instrument context, but does not state carrier frequency, exposure, distance, quantitative performance, controls, or independent replication.
- **Limitations:** Only the abstract, not the full paper or underlying results, was reviewed. It does not establish practical range, intelligibility, reproduction, or use in an incident. The abstract's tactile application is not the subject of this bibliography.
- **Classification:** **RESEARCH HYPOTHESIS** for applying the abstract-described method to repository questions; no experimental performance is independently established here.
- **Repository topic:** Parametric ultrasonic and directional audio in RSH-001 section 3.3.

## Microwave Auditory Research

**U1 — UNVERIFIED:** Allan H. Frey's original microwave auditory publications, RF-induced hearing, pulse conditions, proposed mechanisms, and reproducibility. The repository names Frey but does not supply a checked primary citation. Publisher and PubMed access failed during this review; neither an exact citation nor experimental details are asserted here. No event-specific RF exposure is established.

## Ultrasonic and Directional Audio Research

**U2 — UNVERIFIED:** Further primary literature and experimental results on parametric acoustic arrays, ultrasonic carrier modulation, nonlinear propagation, self-demodulation, and limitations. V2's abstract was reviewed, but its full paper and quantitative experimental conditions were not accessible; no range, intelligibility, or deployment claim is made.

## RF Demodulation and Nonlinear Effects

**U3 — UNVERIFIED:** Nonlinear junction detection and unintentional RF demodulation, including device-specific electromagnetic interference. No primary source or relevant device measurement was reviewed.

**U4 — UNVERIFIED:** Passive intermodulation. The official NIST bibliographic index lists Jeffrey A. Jargon, *Comparison of passive intermodulation measurements for the U.S. wireless industry*, 1999, technical note 1515, DOI `10.6028/NIST.TN.1515`; see the [NIST index record](https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.TN.1515.ris). The index labels the publisher and series as National Bureau of Standards/NBS, so publication identity and attribution should be checked against the report itself. The report, findings, setup, and limitations were not accessible; the indexed DOI was not resolved.

## Auditory Perception Research

V1 describes a specific speech-intelligibility test and automated estimate; it does not establish how an individual interpreted an ambiguous recording.

**U5 — UNVERIFIED:** Peer-reviewed primary studies of auditory pareidolia, speech perception in ambiguous noise, and perceptual bias. No source-specific experimental result was reviewed.

**U6 — UNVERIFIED:** Primary literature on blinded listening, transcription agreement, and signal detection theory as applied to ambiguous audio. V1's described six-choice task is not a substitute for verification of those methods or their application to open-ended recordings.

## Audio Forensic Standards and Methods

**U7 — UNVERIFIED:** The NIST index lists Barbara Guttman, Douglas R. White, and Tracy Walraven, *Digital evidence preservation: considerations for evidence handlers*, 2022, NIST IR 8387, DOI `10.6028/NIST.IR.8387`; see the [NIST index record](https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.IR.8387.ris). The report's text, recommendations, applicability to original and processed audio, and limitations were not accessible; the indexed DOI was not resolved. This is a report lead, not a verified standard.

**U8 — UNVERIFIED:** Published audio forensic standards and primary methods addressing original versus processed audio, spectral interpretation, processing artifacts, provenance, and chain of custody. No specific standard text was reviewed, and no compliance is asserted.

The existing [evidence model](../evidence-model.md) and [preservation chapter](../../manual/06-evidence-preservation.md) are repository guidance, not external forensic-standard verification. A hash can establish a file comparison, not the truth, origin, or cause of its contents.

## Evidence Classification Matrix

These are classifications of statements, not an automatic conversion to the separate evidence states in the [record model](../evidence-model.md).

| Classification | Bounded application |
|---|---|
| DOCUMENTED SCIENCE | V1's source-described test and bounded subset comparison. |
| EXPERIMENTALLY DEMONSTRATED CAPABILITY | None independently established by this review; an experiment and its conditions require direct verification. |
| PATENT CLAIM | None reviewed; a patent claim alone does not demonstrate a working or deployed device. |
| RESEARCH HYPOTHESIS | Applying V2's abstract-described method or another technical explanation to a specific incident remains a hypothesis until supported by appropriate evidence. |
| PERSONAL OBSERVATION | The reports in RSH-001 remain personal observations, not independent technical measurements. |
| UNVERIFIED CLAIM | U1-U8 are leads, not established findings; unsupported attribution, intent, or deployment claims remain unverified. |

Published capabilities, proposed mechanisms, personal observations, and claims about specific events are distinct. A publication cannot by itself establish use in an event, a perpetrator, intent, or government involvement.

## Research Gaps and Unresolved Questions

The Phase 1 audit's primary Frey citation gap remains unresolved, as do the experimental ultrasonic, RF, perceptual-bias, and forensic-standard gaps above. Independent replication, experimental parameters, and restrictions on generalization require review of the actual publications. No recording, source signal, exposure, or incident-specific attribution was examined. Synthetic speech, voice cloning, resonance, and historical institutional relationships remain outside the verified source coverage of this increment.

## Source Verification Limitations

Direct DNS access to PubMed, Crossref, DOI, and NIST web sites failed; an additional browser attempt to PubMed was blocked. The official NTIA, NIST, and NIME conference GitHub repositories were accessible. V1 was reviewed in the original technical document; V2 was reviewed only through its conference index and abstract; the two NIST records were metadata only. The DOI destinations, V2 full paper, full report texts, original Frey paper, and relevant standards were not accessed. This is a limited source review, not an exhaustive literature search or a completed resolution of the Phase 1 bibliography gap.

## Cross-Reference Mapping

| Repository topic | Source or lead | Boundary |
|---|---|---|
| RSH-001 sections 3.1 and 6, RF auditory hypothesis | U1 | No paper or event-specific exposure verified. |
| RSH-001 sections 3.3 and 3.2, directional audio and EMI | V2, U2-U4 | V2's abstract describes an ultrasonic method; no experimental performance or incident-specific device verified. |
| RSH-001 sections 3.5 and 7.3, perception and listening | V1, U5-U6 | V1 concerns a specified intelligibility test, not open-ended incident transcription. |
| RSH-001 sections 7.4-7.5 and preservation chapter | U7-U8 | External forensic report and standards text not reviewed. |
| Phase 1 audit sections 5-7 | V1-V2, U1-U8 | Two sources reviewed at different levels; remaining source gaps explicitly retained. |

## Phase 2A.1 — Source Verification Follow-up

**Identifier:** RSH-PHASE2A-001-APP-001

**Timestamp:** 2026-11-16T14:23:36-06:00

**Author:** GitHub Copilot

**Description:** A further attempt to obtain the primary publications and clarify the existing source-access record. The earlier sections remain the historical Phase 2A review; this follow-up states the later review's results and does not retroactively change them.

### Verification levels and existing sources

`FULL_TEXT_REVIEWED` means the source text itself was reviewed; `ABSTRACT_REVIEWED` means only its abstract was reviewed; `METADATA_VERIFIED` means bibliographic identity was checked against an authoritative record, without verification of findings; `UNVERIFIED` means the required identity or source content has not been independently checked. A full-text review is not independent replication, and a standard or guidance document is not an experiment.

| Source | Level | Scope and limitation |
|---|---|---|
| V1 | FULL_TEXT_REVIEWED | The original NTIA technical documentation was reviewed in Phase 2A; the separate conference papers, underlying data, and independent replication were not reviewed. |
| V2 | ABSTRACT_REVIEWED | The conference-maintained index and abstract were reviewed; the paper's full text and quantitative results remain inaccessible. Its [conference paper URL](https://nime.org/proceedings/2010/nime2010_019.pdf) was attempted in this follow-up. |
| U4 report | METADATA_VERIFIED | NIST's index was previously checked; a separate U.S. Government Publishing Office (GPO) catalog record confirms the title, 1999 date, NIST technical note number and DOI, but is not the report text. |
| U7 report | METADATA_VERIFIED | The NIST index lists three authors; the publication page and report PDF could not be consulted to confirm whether the author list is complete or to review recommendations. |

These are four previously recorded sources or source leads at different levels, not four full-text findings. This follow-up adds no newly verified source and does not resolve any U1-U8 lead in full.

### U1 — Frey citation candidates

The supplied 1962 starting point is Allan H. Frey, "Human auditory system response to modulated electromagnetic energy," *Journal of Applied Physiology* 17, no. 4 (1962): 689-692, DOI `10.1152/jappl.1962.17.4.689`; [publisher](https://journals.physiology.org/doi/10.1152/jappl.1962.17.4.689) and [PubMed record](https://pubmed.ncbi.nlm.nih.gov/13895081/). **UNVERIFIED in this follow-up:** both sites failed to open, so the supplied bibliographic details and abstract could not be independently checked here. Abstract findings and full-text findings are therefore both **not reviewed**, and no experimental conditions, mechanisms, or outcomes are asserted. The title and locator are research starting points, not proof of a particular incident. Repository cross-reference: RSH-001 sections 3.1 and 6.

An earlier 1961 publication was also sought through PubMed and publication searches; no authoritative original or index record was accessible to verify its identity or findings. U1 remains open for both publications, experimental context, and reproducibility.

### U4 — Additional catalog corroboration

The [GPO catalog record](https://github.com/usgpo/cataloging-records/blob/26924f888be05df779f7d6d80a425fc35bca7b28/NIST_Collection/CSV/nist_technical_note.csv) lists "Comparison of passive intermodulation measurements for the U.S. wireless industry," 1999, NIST technical note 1515, DOI `10.6028/NIST.TN.1515`, and links to a [government-hosted PDF](https://www.govinfo.gov/content/pkg/GOVPUB-C13-394f7814a03d3b046fdffe2d99e68c05/pdf/GOVPUB-C13-394f7814a03d3b046fdffe2d99e68c05.pdf). The NIST index above attributes the report to Jeffrey A. Jargon; the GPO row checked here does not list an author. **METADATA_VERIFIED** applies only to these catalog fields; the discrepancy in the earlier NIST index's publisher/series labels is not resolved by the GPO record's series label alone. The PDF was inaccessible. Findings, measurement setup, conditions, and limitations remain **UNVERIFIED**, and no passive-intermodulation mechanism or device-specific outcome is inferred. Repository cross-reference: RSH-001 section 3.2 and Phase 1 audit section 5.

### U7 — Report access and authorship

The [NIST index record](https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.IR.8387.ris) lists Barbara Guttman, Douglas R. White, and Tracy Walraven, *Digital Evidence Preservation: Considerations for Evidence Handlers*, NIST IR 8387 (2022), DOI `10.6028/NIST.IR.8387`. This remains **METADATA_VERIFIED** from the index only. The [official publication page](https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers) and [official PDF](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8387.pdf) were not accessible; completeness of authorship against those sources, report recommendations, conditions of applicability, and limitations remain **UNVERIFIED**. No report-specific handling recommendation or standards compliance is claimed. Repository cross-reference: RSH-001 sections 7.4-7.5 and the [preservation chapter](../../manual/06-evidence-preservation.md).

### Remaining leads and access boundaries

| Lead | Follow-up status |
|---|---|
| U1 | Open: supplied 1962 citation and earlier 1961 source require authoritative verification; neither abstract nor full text was reviewed here. |
| U2 | Open: V2 remains abstract-only; the NIME full paper and further primary parametric-array literature require review of actual source text and conditions. |
| U3 | Open: no original nonlinear-junction or device-specific demodulation study was reviewed. |
| U4 | Open: report identity has index-level support, but its text, setup, results, and publisher/series discrepancy require review. |
| U5 | Open: no original study of speech perception in ambiguous noise or auditory pareidolia was reviewed. |
| U6 | Open: no primary study of blinded listening, transcription agreement, or signal detection theory for ambiguous audio was reviewed. |
| U7 | Open: author-list completeness and report recommendations require the official publication page and report text. |
| U8 | Open: no audio-forensic standard text or primary method was reviewed; the SWGDE documents site was inaccessible. |

Attempts to access the publisher, PubMed, Crossref, NIST, NIME, Zenodo, GPO PDF, acoustics publisher, and SWGDE sites failed because their hostnames could not be resolved in this environment. A separate browser attempt was blocked for PubMed and the NIST publication page. The conference bibliography, NIST index, and GPO catalog were accessible through their maintained GitHub repositories. These access failures do not establish that the source documents do not exist. Source-specific findings are not substituted from secondary summaries. Established mechanisms, hypotheses about application, and personal observations remain distinct; no source alone establishes any incident, perpetrator, deployment, or attribution.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-16T13:57:21-06:00 | Initial limited bibliography with one reviewed technical source and explicitly unverified research leads. | GitHub Copilot |
| 1.1.0 | 2026-11-16T14:10:33-06:00 | Added a conference-indexed ultrasonic audio reference with abstract-only verification and explicit limitations. | GitHub Copilot |
| 1.2.0 | 2026-11-16T14:23:36-06:00 | Appended source-verification levels, attempted primary-source access, government catalog corroboration, and remaining research gaps. | GitHub Copilot |
