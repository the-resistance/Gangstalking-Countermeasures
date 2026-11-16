---
Document Title: Phase 2A Scientific Bibliography
Document ID: RSH-PHASE2A-001
Author: GitHub Copilot
Version: 1.3.0
Created: 2026-11-16T13:57:21-06:00
Last Updated: 2026-11-16T16:15:58-06:00
---

# Phase 2A Scientific Bibliography

## Current Verification Status

As of 2026-11-16, the following five source texts have been reviewed in full: NTIA ABC-MRT (S. Voran), Frey 1962, Ciglar NIME 2010, NIST TN 1515, and NIST IR 8387. `FULL_TEXT_REVIEWED` describes review of the cited source text; it does not mean that the reported experiment was independently replicated or that a capability was tested in a new experiment.

This current summary supplements, and does not rewrite, the historical Phase 2A and Phase 2A.1 checkpoints below. Earlier verification levels and access failures describe those earlier checkpoints. For the present status of each citation URL, see the [Phase 2B citation URL audit](../audits/PHASE-2B-CITATION-URL-AUDIT.md).

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

### Phase 2A.1 — Supplied-source access attempt

**Identifier:** RSH-PHASE2A-001-APP-002

**Timestamp:** 2026-11-16T14:28:32-06:00

**Author:** GitHub Copilot

**Description:** Attempted the seven supplied publisher, PubMed, NIST report/publication, and NIME URLs once each. No page or document content was retrieved; research stopped at the reported access failure as directed.

All seven requests failed with `WebFetchBlockedUrlError: failed to lookup address information: No address associated with hostname`. The failure covered the Frey publisher abstract and PubMed record; the NIST IR 8387 official PDF and publication page; the NIST TN 1515 official PDF and publication page; and the NIME 2010 conference PDF. The failed requests provide no source text for citation verification, author-list comparison, experimental conditions, results, recommendations, or limitations.

No source level is raised by this attempt. Frey's supplied 1962 citation and abstract remain **UNVERIFIED** here; the NIST IR 8387 and TN 1515 entries remain **METADATA_VERIFIED** from previously accessed indexes/catalog records only, not the named official pages or PDFs; V2 remains **ABSTRACT_REVIEWED** from the conference-maintained bibliography abstract, not the requested paper. In particular, the NIST IR 8387 publication-page author list cannot be compared with its PDF front matter, and the requested TN 1515 author attribution (Jeffrey A. Jargon and Donald C. DeGroot) was not independently checked against the report. No discrepancy can be determined from inaccessible documents. No new scientific finding or resolved lead is added; U1-U8 remain open. No incident-specific inference is made.

### Phase 2A.1 — Version normalization correction

**Identifier:** RSH-PHASE2A-001-APP-003

**Timestamp:** 2026-11-16T14:47:17-06:00

**Author:** GitHub Copilot

**Description:** Corrected the formal bibliography version for the single, still-unmerged Phase 2A.1 increment, retaining the intervening branch records for traceability.

- **Original working-branch versions:** The bibliography was successively marked 1.2.0 and 1.3.0 in commits on this PR branch, while `origin/main` remained at 1.1.0.
- **Correction:** This PR's consolidated Phase 2A.1 bibliography is version 1.2.0, one significant-content increment from the published 1.1.0.
- **Reason:** The earlier versions were unmerged intermediate work on this same increment, not separate releases from `main`. Keeping 1.3.0 as the PR's formal version fails the repository's one-increment comparison against the actual base. The former entries are retained below as a pre-merge working-branch trail; the Git commits and changelog entries are also preserved.
- **Version increment:** 1.1.0 to 1.2.0 under VERSIONING V-001. The current formal revision and changelog entry record this correction.

### Phase 2A.1 — Attached primary-source review

**Identifier:** RSH-PHASE2A-001-APP-004

**Timestamp:** 2026-11-16T14:47:17-06:00

**Author:** GitHub Copilot

**Description:** Reviewed the four supplied PDF documents. Findings below are limited to what those documents report. Reported experimental results are not independent replications, and none establishes an incident-specific application.

#### U1 — Allan H. Frey, 1962

- **Citation:** Allan H. Frey, “Human auditory system response to modulated electromagnetic energy,” *Journal of Applied Physiology* 17, no. 4 (1962): 689–692. DOI: `10.1152/jappl.1962.17.4.689`. The article's title, author, journal citation, and pagination appear on p. 689. [Publisher abstract](https://journals.physiology.org/doi/abs/10.1152/jappl.1962.17.4.689); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/13895081/); [publisher full-text locator](https://journals.physiology.org/doi/10.1152/jappl.1962.17.4.689).
- **Verification level:** FULL_TEXT_REVIEWED. The supplied four-page article was read (journal pp. 689–692). The abstract printed on p. 689 was also checked; direct access to the supplied web records was unavailable.
- **Reported findings:** Frey reports that modulated RF exposure produced sound perceptions in normal-hearing and deaf human subjects, describes the perceptions as varying with carrier frequency and modulation, and reports a response several hundred feet from the antenna in the abstract (p. 689). The article reports subjective matching attempts and says a pulsed audio signal with high-frequency components produced the closest match (p. 690). Its threshold discussion reports that peak, rather than average, power density was the critical factor in the tested conditions (p. 691).
- **Method and conditions:** The paper describes human-subject observations using pulse-modulated transmitters across carrier frequencies including 425, 1,310, 2,982, and 8,900 MHz, with varied pulse widths, repetition rates, and duty cycles (Table 1, p. 690). The abstract reports approximately 80 dB ambient acoustic noise and approximately 275 mW/cm² peak power density for perception at 425 and 1,310 MHz, with average power density as low as 400 μW/cm² (p. 689). Threshold observations used earplugs to reduce ambient acoustic noise; a sound-level meter and earplug attenuation are described on p. 690. A sound-matching procedure with a variable audio bandpass filter is described on pp. 690–691.
- **Limitations:** The paper says its transmitter values are conservative and not precise because measurements were not made in ideal laboratory environments (p. 689). It does not report a sample size or a controlled, blinded protocol in this article; the authors refer readers to a separate paper for a longer series of studies and measurement instruments (p. 689). The proposed approximately 3 μW/cm² threshold in an anechoic room is explicitly a theoretical extrapolation from assumptions about noise attenuation, not a measured result (p. 692). The authors state that evidence for possible detector sites is inconclusive and interpretations are deliberately omitted pending additional data (p. 692).
- **Classification:** DOCUMENTED SCIENCE for the bounded, author-reported human observations and threshold discussion. This is not independent replication, a demonstrated mechanism, or evidence of any particular exposure or event.
- **Repository cross-reference:** RSH-001 sections 3.1 and 6; Phase 1 audit sections 5–7.

#### U2 — Miha Ciglar, NIME 2010

- **Citation:** Miha Ciglar, “An Ultrasound Based Instrument Generating Audible and Tactile Sound,” *Proceedings of the 2010 Conference on New Interfaces for Musical Expression (NIME 2010)*, Sydney, Australia, June 2010, pp. 19–22. ISSN `2220-4806`; DOI `10.5281/zenodo.1177745`. Title, author, conference, and pagination appear on pp. 19 and 22. [Original conference PDF](https://www.nime.org/proceedings/2010/nime2010_019.pdf).
- **Verification level:** FULL_TEXT_REVIEWED. All four proceedings pages (pp. 19–22) of the supplied paper were reviewed.
- **Reported method and findings:** The paper describes a prototype with 97 piezoelectric transducers on a spherical surface, resonant at 40 kHz, driven by an amplitude-modulated carrier and focused at a fixed point approximately 25 cm from the transducers (p. 19). It describes airborne nonlinear propagation as producing audible components alongside tactile feedback at the focal point (pp. 19–20). For hand-position sensing, it added three 50 kHz transmitter/receiver elements and analyzed reflected-signal amplitudes; Figure 2 reports a 1024-point FFT with 192 kHz sampling (p. 21). The authors report that the 50 kHz amplitudes varied with hand position and could be used as control parameters (p. 21).
- **Experimental conditions and limitations:** Audio generation used an Edirol FA101 interface at 192 kHz and Pure Data; the 40 kHz array was driven through a 100 W amplifier, reported to operate at full power, with a 2.2 μF coupling capacitor (p. 21). The authors state that they lacked measuring equipment to determine the load impedance, that amplifier and transducer impedances were not matched, and that further measurements were needed to optimize power transfer (pp. 21–22). The hand-position experiments were limited to receiver-amplitude analysis and simple mappings to oscillator pitch; the paper says no particular synthesis engine was designed (p. 21, footnote). It supplies no calibrated sound-pressure, beam-range, exposure, intelligibility, or controlled-listener measurements. Its qualitative description is not an independent replication or evidence of use outside the musical prototype.
- **Classification:** DOCUMENTED SCIENCE for the source-described prototype and qualitative observations, bounded by the reported apparatus and missing quantitative characterization. It does not establish a general-purpose capability or any incident-specific application.
- **Repository cross-reference:** RSH-001 section 3.3; Phase 1 audit sections 5–7.

#### U4 — Jeffrey A. Jargon and Donald C. DeGroot, NIST TN 1515

- **Citation:** Jeffrey A. Jargon and Donald C. DeGroot, *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*, NIST Technical Note 1515, October 1999, 48 pp. DOI: `10.6028/NIST.TN.1515`. Both authors and the title appear on the report title page (PDF p. 3) and paper title page (PDF p. 7); the report abstract is on PDF p. 7. [Official report PDF](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1515.pdf); [NIST publication record](https://www.nist.gov/publications/comparison-passive-intermodulation-measurements-u-s-wireless-industry).
- **Verification level:** FULL_TEXT_REVIEWED. The supplied PDF's title and abstract, methodology, results, discussion and conclusions, and participant/form appendices were reviewed. The report identifies itself as 48 pages; the 52-page PDF also includes front matter and publication material.
- **Method:** NIST organized a round-robin comparison using four two-port artifacts with DIN 7-16 connectors and deliberately varied nonlinearities: three diode-modified adapters and a diode-modified cable assembly (printed pp. 4–5). Ten companies contributed 19 data sets across AMPS, GSM, PCS, and DCS bands over about nine months (abstract, PDF p. 7; printed pp. 5–6). The protocol used two continuous-wave sources at +43 dBm (20 W) each, measured third-order intermodulation products in receive bands, and allowed forward and/or reflected configurations (printed pp. 4–5 and Appendix A, pp. 41–42). Appendix A asked participants to report environmental conditions, systems, loads, and uncertainty bounds where available (pp. 41–42).
- **Reported findings:** The report says most participant measurements were within two standard deviations of ensemble means, while some showed substantial discrepancies (printed pp. 9–10). Results varied by artifact, band, and forward/reflected configuration; the electrically long blue artifact showed configuration and frequency dependence, and the white artifact was less repeatable than the others (pp. 6–9). NIST's own artifacts and systems remained stable within 2.9 dB standard deviation for up to five months (p. 9).
- **Limitations:** This was a bounded interlaboratory comparison of four designed artifacts and selected commercial communications bands, not an unrestricted survey of passive devices or an incident investigation. The DCS results had only two participants and were not statistically summarized (p. 8). One GSM participant's values were over 30 dB below the others and were excluded from figures and mean/standard-deviation calculations (p. 7). The report anonymizes companies, and its reported agreement/disagreement is specific to the instruments, artifacts, bands, and protocol. It does not establish that passive intermodulation occurred in any other device or event.
- **Metadata discrepancy:** The [previously consulted NIST-Tech-Pubs RIS index](https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.TN.1515.ris) lists Jargon but not DeGroot; the original report title page lists **both Jeffrey A. Jargon and Donald C. DeGroot** (PDF pp. 3 and 7). The supplied NIST publication page could not be accessed, so its author list could not be compared directly with the PDF.
- **Classification:** DOCUMENTED SCIENCE for this source's reported measurement intercomparison, limited to its stated sample and protocol.
- **Repository cross-reference:** RSH-001 section 3.2; Phase 1 audit sections 5–7.

#### U7 — Guttman, White, and Walraven, NIST IR 8387

- **Citation:** Barbara Guttman, Douglas R. White, and Tracy Walraven, *Digital Evidence Preservation: Considerations for Evidence Handlers*, NIST Interagency Report 8387, September 2022. DOI: `10.6028/NIST.IR.8387`. The complete three-author list appears on the report cover and title page (PDF pp. 1–2) and in NIST's recommended citation (PDF p. 3). [Official report PDF](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8387.pdf); [NIST publication record](https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers).
- **Verification level:** FULL_TEXT_REVIEWED. All pages of the supplied 22-page PDF, including front matter, abstract, body, and references, were reviewed.
- **Reported guidance:** The report addresses preservation of physical media, digital images/files, other digital objects, and law-enforcement-generated digital evidence; it identifies evidence-management professionals as its primary audience and limits acquisition discussion to areas overlapping preservation (abstract, PDF p. 4; printed p. 1). For digital files, it recommends documenting source and transfer/creation, storing hashes or signatures separately in a secure location, maintaining backups and access controls/logging, and considering long-term storage and file-format preservation (printed pp. 7–11). It describes physical-media, transfer, storage, and radio-isolation considerations (printed pp. 3–5).
- **Limitations:** This is preservation guidance, not an experiment, audio-forensic standard, or validation of a specific collection process. Acquisition is outside scope except where it overlaps preservation (abstract and printed p. 1). Recommendations are directed to evidence-management settings; the report does not determine the authenticity, truth, origin, or cause of a file's contents.
- **Author comparison:** The PDF front matter names Guttman, White, and Walraven (PDF pp. 1–3), matching the author list in the [previously accessed NIST-Tech-Pubs RIS index](https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.IR.8387.ris). The official publication page supplied for comparison could not be accessed in this environment, so direct page-to-PDF comparison and any webpage discrepancy remain unverified. No discrepancy appears between the PDF and the accessible index.
- **Classification:** DOCUMENTED TECHNICAL GUIDANCE; not experimental evidence.
- **Repository cross-reference:** RSH-001 sections 7.4–7.5; `manual/06-evidence-preservation.md`; Phase 1 audit sections 6–7.

#### Current source levels and remaining leads

| Source or lead | Current level/status |
|---|---|
| V1 — Voran, NTIA ABC-MRT technical document | FULL_TEXT_REVIEWED, as documented in the Phase 2A entry. |
| V2 — Ciglar, NIME 2010 | FULL_TEXT_REVIEWED; the earlier Phase 2A access was limited to the conference abstract. |
| U1 — Frey | 1962 article FULL_TEXT_REVIEWED; earlier 1961 publication and its findings remain UNVERIFIED. The broader U1 lead is narrowed, not fully resolved. |
| U2 — Parametric/directional audio | Ciglar paper FULL_TEXT_REVIEWED; further primary literature and broader performance limits remain open. |
| U3 — Nonlinear junction detection and unintentional RF demodulation | UNVERIFIED; TN 1515 concerns a bounded passive-intermodulation comparison and does not resolve this lead. |
| U4 — Passive intermodulation | NIST TN 1515 FULL_TEXT_REVIEWED; metadata author discrepancy recorded above. Broader device/application questions remain open. |
| U5 — Speech perception and auditory pareidolia | UNVERIFIED; no primary source reviewed in these attachments. |
| U6 — Blinded listening and signal detection | UNVERIFIED; no primary source reviewed in these attachments. |
| U7 — Digital evidence preservation | NIST IR 8387 FULL_TEXT_REVIEWED. PDF author list verified; direct comparison with the official publication webpage remains blocked. It is guidance, not a standard. |
| U8 — Audio forensic standards and methods | UNVERIFIED; these attachments do not contain a reviewed audio-forensic standard. |

#### Access and inference boundary

The four supplied PDFs were available locally and reviewed directly. Direct requests to the Frey publisher/PubMed pages and the two NIST publication pages failed with DNS-resolution errors; therefore no claim is made about the inaccessible web-page author lists or page abstracts. The PDF contents, not those failed requests, support the full-text classifications above. No source establishes an incident, exposure, device, perpetrator, deployment, intent, or attribution.

| Evidence classification update | Bounded application |
|---|---|
| DOCUMENTED SCIENCE | Frey's reported human observations, Ciglar's bounded prototype account, and the TN 1515 interlaboratory measurements, each with the conditions and limitations above. |
| DOCUMENTED TECHNICAL GUIDANCE | NIST IR 8387's evidence-preservation considerations; this is not experimental evidence or a forensic standard. |
| EXPERIMENTALLY DEMONSTRATED CAPABILITY | No generalized or independently replicated capability is established by these reviews. |

## Pre-merge Working-Branch Revision Trail

The following two revision records were present in commits on this unmerged branch. They are retained as an audit trail, but are not separate releases from `main`; APP-003 documents their consolidation into the formal 1.2.0 increment.

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.2.0 | 2026-11-16T14:23:36-06:00 | Appended source-verification levels, attempted primary-source access, government catalog corroboration, and remaining research gaps. | GitHub Copilot |
| 1.3.0 | 2026-11-16T14:28:32-06:00 | Appended the supplied-source access failures and preserved the existing verification levels and unresolved leads. | GitHub Copilot |

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-16T13:57:21-06:00 | Initial limited bibliography with one reviewed technical source and explicitly unverified research leads. | GitHub Copilot |
| 1.1.0 | 2026-11-16T14:10:33-06:00 | Added a conference-indexed ultrasonic audio reference with abstract-only verification and explicit limitations. | GitHub Copilot |
| 1.2.0 | 2026-11-16T14:47:17-06:00 | Consolidated Phase 2A.1 source reviews, access limitations, and the formal version correction into one increment from 1.1.0. | GitHub Copilot |
| 1.3.0 | 2026-11-16T16:15:58-06:00 | Added a current source-review status summary and linked the separate citation URL audit while preserving the Phase 2A and Phase 2A.1 checkpoint records. | GitHub Copilot |
