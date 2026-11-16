---
Document Title: Phase 2A Scientific Bibliography
Document ID: RSH-PHASE2A-001
Author: GitHub Copilot
Version: 1.0.0
Created: 2026-11-16T13:57:21-06:00
Last Updated: 2026-11-16T13:57:21-06:00
---

# Phase 2A Scientific Bibliography

## Scope and Methodology

This controlled increment addresses source gaps identified in the [Phase 1 audit](../audits/PHASE-1-REPOSITORY-AUDIT.md), especially its research coverage matrix and bibliography assessment. It covers the existing technical topics in [RSH-001](../../research/001-voice-to-skull-v2k.md) and the [technology research chapter](../../manual/04-technology-research.md). It does not report an experiment, incident finding, equipment deployment, or investigation record.

Verification was attempted on 2026-11-16. The authoritative publication or index was consulted for bibliographic identity, and relevant source text was reviewed before a technical statement was classified as documented. A source's own experimental conditions and limits are kept separate from any incident-specific question. The bibliography below contains **one verified primary technical document**; the eight explicitly numbered leads are **UNVERIFIED** for their substantive findings. The NIST index records cited for two leads verify bibliographic metadata only, not the contents of those reports.

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

## Microwave Auditory Research

**U1 — UNVERIFIED:** Allan H. Frey's original microwave auditory publications, RF-induced hearing, pulse conditions, proposed mechanisms, and reproducibility. The repository names Frey but does not supply a checked primary citation. Publisher and PubMed access failed during this review; neither an exact citation nor experimental details are asserted here. No event-specific RF exposure is established.

## Ultrasonic and Directional Audio Research

**U2 — UNVERIFIED:** Primary literature on parametric acoustic arrays, ultrasonic carrier modulation, nonlinear propagation, self-demodulation, and experimental limitations. No primary paper or relevant experimental context was accessible and verified in this review; no range, intelligibility, or deployment claim is made.

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
| RESEARCH HYPOTHESIS | An incident-specific technical explanation remains a hypothesis until supported by appropriate evidence. |
| PERSONAL OBSERVATION | The reports in RSH-001 remain personal observations, not independent technical measurements. |
| UNVERIFIED CLAIM | U1-U8 are leads, not established findings; unsupported attribution, intent, or deployment claims remain unverified. |

Published capabilities, proposed mechanisms, personal observations, and claims about specific events are distinct. A publication cannot by itself establish use in an event, a perpetrator, intent, or government involvement.

## Research Gaps and Unresolved Questions

The Phase 1 audit's primary Frey citation gap remains unresolved, as do the ultrasonic, RF, perceptual-bias, and forensic-standard gaps above. Independent replication, experimental parameters, and restrictions on generalization require review of the actual publications. No recording, source signal, exposure, or incident-specific attribution was examined. Synthetic speech, voice cloning, resonance, and historical institutional relationships remain outside the verified source coverage of this increment.

## Source Verification Limitations

Direct DNS access to PubMed, Crossref, DOI, and NIST web sites failed; an additional browser attempt to PubMed was blocked. The official NTIA and NIST GitHub repositories were accessible. V1 was reviewed in the original technical document, while the two NIST records were metadata only. The DOI destinations, paywalled or full report texts, original Frey paper, and relevant standards were not accessed. This is a limited source review, not an exhaustive literature search or a completed resolution of the Phase 1 bibliography gap.

## Cross-Reference Mapping

| Repository topic | Source or lead | Boundary |
|---|---|---|
| RSH-001 sections 3.1 and 6, RF auditory hypothesis | U1 | No paper or event-specific exposure verified. |
| RSH-001 sections 3.3 and 3.2, directional audio and EMI | U2-U4 | No applicable experimental result or device verified. |
| RSH-001 sections 3.5 and 7.3, perception and listening | V1, U5-U6 | V1 concerns a specified intelligibility test, not open-ended incident transcription. |
| RSH-001 sections 7.4-7.5 and preservation chapter | U7-U8 | External forensic report and standards text not reviewed. |
| Phase 1 audit sections 5-7 | V1, U1-U8 | One source reviewed; remaining source gaps explicitly retained. |

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-16T13:57:21-06:00 | Initial limited bibliography with one reviewed technical source and explicitly unverified research leads. | GitHub Copilot |
