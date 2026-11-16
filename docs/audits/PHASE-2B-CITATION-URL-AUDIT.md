---
Document Title: Phase 2B Citation URL Audit
Document ID: RSH-PHASE2B-AUDIT-001
Author: GitHub Copilot
Version: 1.0.0
Created: 2026-11-16T16:05:25-06:00
Last Updated: 2026-11-16T16:15:58-06:00
---

# Phase 2B Citation URL Audit

This audit covers the 15 distinct external scientific-source URLs in the [Phase 2A bibliography](../research/PHASE-2A-SCIENTIFIC-BIBLIOGRAPHY.md). `manual/07-references.md` contains no additional external citation URLs. Repeated links to the same URL are counted once. No URL was replaced.

For URLs known from the Phase 2A.1 record to have failed DNS resolution, the blocked host was not retried. Such a failure is classified as `NETWORK_UNAVAILABLE`, not as a dead link. The five GitHub-hosted records below were checked once with an HTTP GET on 2026-11-16; their final responses were HTTP 200. URL retrieval status is distinct from the separate full-text review of supplied local PDFs documented in the bibliography's current status section.

## URL Results

### A1 — NTIA ABC-MRT technical document

- **Bibliography ID; source:** V1; S. Voran, *Conducting ABC-MRT and ABC-MRT16 Tests*, National Telecommunications and Information Administration, Institute for Telecommunication Sciences (2013; updated 2017).
- **Stable identifier:** NTIA Git revision `afaeb9a0551cb456c175bc1150a14d1edbb6c7a1`; DOI and report number not specified.
- **Original URL:** https://github.com/NTIA/ABC-MRT16/blob/afaeb9a0551cb456c175bc1150a14d1edbb6c7a1/readme.md
- **Access method and result:** One `curl -L` HTTP GET, 2026-11-16; HTTP 200.
- **Expected document retrieved / identity:** Yes; original NTIA technical-document content and its title, author, dates, and relevant context match the citation.
- **Verification level:** `VERIFIED_FULL_TEXT`.
- **Replacement URL:** None; retain the official NTIA repository locator.
- **Date checked:** 2026-11-16.

### A2 — Ciglar NIME bibliography entry

- **Bibliography ID; source:** V2 / U2; Miha Ciglar, “An Ultrasound Based Instrument Generating Audible and Tactile Sound,” *Proceedings of the International Conference on New Interfaces for Musical Expression* (2010), NIME conference-maintained bibliography.
- **Stable identifier:** DOI `10.5281/zenodo.1177745`; pages 19–22.
- **Original URL:** https://github.com/NIME-conference/NIME-bibliography/blob/f401a83a135958cb365997b8f10a2696905962ff/paper_proceedings/nime2010.bib
- **Access method and result:** One `curl -L` HTTP GET, 2026-11-16; HTTP 200.
- **Expected document retrieved / identity:** The conference bibliography entry and abstract were retrieved; title, author, conference, and abstract match. This URL is an index, not the complete paper.
- **Verification level:** `VERIFIED_ABSTRACT`.
- **Replacement URL:** None; retain the conference-maintained index.
- **Date checked:** 2026-11-16.

### A3 — NIST TN 1515 bibliographic record

- **Bibliography ID; source:** U4; Jeffrey A. Jargon and Donald C. DeGroot, *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*, NIST Technical Note 1515 (1999), NIST-Tech-Pubs index.
- **Stable identifier:** DOI `10.6028/NIST.TN.1515`; report 1515.
- **Original URL:** https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.TN.1515.ris
- **Access method and result:** One `curl -L` HTTP GET, 2026-11-16; HTTP 200.
- **Expected document retrieved / identity:** The NIST RIS index record was retrieved and matches the report identifier and title. It lists only Jargon; the reviewed report title page lists Jargon and DeGroot.
- **Verification level:** `VERIFIED_METADATA`. The author-list difference is preserved as a metadata discrepancy; the index is not substituted for the report.
- **Replacement URL:** None; retain the official NIST index and the original report citation.
- **Date checked:** 2026-11-16.

### A4 — NIST IR 8387 bibliographic record

- **Bibliography ID; source:** U7; Barbara Guttman, Douglas R. White, and Tracy Walraven, *Digital Evidence Preservation: Considerations for Evidence Handlers*, NIST Interagency Report 8387 (2022), NIST-Tech-Pubs index.
- **Stable identifier:** DOI `10.6028/NIST.IR.8387`; report 8387.
- **Original URL:** https://github.com/usnistgov/NIST-Tech-Pubs/blob/bd258f9a2e02bdb8787740eac17f6779777ea66d/bib/NIST.IR.8387.ris
- **Access method and result:** One `curl -L` HTTP GET, 2026-11-16; HTTP 200.
- **Expected document retrieved / identity:** The NIST RIS record was retrieved; title, authors, report number, and year match the reviewed report.
- **Verification level:** `VERIFIED_METADATA`. This index URL does not provide the complete report.
- **Replacement URL:** None; retain the official NIST index.
- **Date checked:** 2026-11-16.

### A5 — Ciglar NIME proceedings paper (non-www URL)

- **Bibliography ID; source:** V2 / U2; Miha Ciglar, “An Ultrasound Based Instrument Generating Audible and Tactile Sound,” NIME 2010, pp. 19–22.
- **Stable identifier:** DOI `10.5281/zenodo.1177745`.
- **Original URL:** https://nime.org/proceedings/2010/nime2010_019.pdf
- **Access method and result:** The Phase 2A.1 record reports one web request and DNS-resolution failure; not retried.
- **Expected document retrieved / identity:** Not from this URL. A supplied local copy of the four-page paper was reviewed and matches the citation; the URL destination itself was not confirmed.
- **Verification level:** `NETWORK_UNAVAILABLE` for this URL; the local source review is recorded separately as `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the original proceedings locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A6 — Ciglar NIME proceedings paper (www URL)

- **Bibliography ID; source:** V2 / U2; Miha Ciglar, “An Ultrasound Based Instrument Generating Audible and Tactile Sound,” NIME 2010, pp. 19–22.
- **Stable identifier:** DOI `10.5281/zenodo.1177745`.
- **Original URL:** https://www.nime.org/proceedings/2010/nime2010_019.pdf
- **Access method and result:** This exact URL was not requested. The non-www proceedings hostname failed DNS resolution in the prior review; the host was not retried.
- **Expected document retrieved / identity:** Not from this URL. A supplied local copy of the four-page paper was reviewed and matches the citation; the www URL destination remains unconfirmed.
- **Verification level:** `UNVERIFIED` for this URL; the local source review is separately `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the original proceedings locator.
- **Date checked:** 2026-11-16 (related non-www host attempt; exact URL untested).

### A7 — GPO catalog record for NIST TN 1515

- **Bibliography ID; source:** U4; *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*, U.S. Government Publishing Office catalog record.
- **Stable identifier:** NIST Technical Note 1515; DOI `10.6028/NIST.TN.1515`.
- **Original URL:** https://github.com/usgpo/cataloging-records/blob/26924f888be05df779f7d6d80a425fc35bca7b28/NIST_Collection/CSV/nist_technical_note.csv
- **Access method and result:** One `curl -L` HTTP GET, 2026-11-16; HTTP 200.
- **Expected document retrieved / identity:** The GPO catalog data was retrieved; title, year, report number, DOI, and government PDF locator match the cited report. The row does not list an author.
- **Verification level:** `VERIFIED_METADATA`; this is a catalog record, not the report text.
- **Replacement URL:** None; retain this official catalog record as corroboration.
- **Date checked:** 2026-11-16.

### A8 — GPO-hosted NIST TN 1515 PDF

- **Bibliography ID; source:** U4; Jeffrey A. Jargon and Donald C. DeGroot, *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*, NIST Technical Note 1515.
- **Stable identifier:** DOI `10.6028/NIST.TN.1515`; report 1515.
- **Original URL:** https://www.govinfo.gov/content/pkg/GOVPUB-C13-394f7814a03d3b046fdffe2d99e68c05/pdf/GOVPUB-C13-394f7814a03d3b046fdffe2d99e68c05.pdf
- **Access method and result:** The Phase 2A.1 record reports a failed request due to DNS resolution; not retried.
- **Expected document retrieved / identity:** Not from this URL. A supplied local copy of the report was reviewed and its title page matches the citation; the government-hosted URL was not confirmed.
- **Verification level:** `NETWORK_UNAVAILABLE` for this URL; local report review is separately `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the government-hosted locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A9 — Official NIST TN 1515 PDF

- **Bibliography ID; source:** U4; Jeffrey A. Jargon and Donald C. DeGroot, *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*, NIST Technical Note 1515.
- **Stable identifier:** DOI `10.6028/NIST.TN.1515`; report 1515.
- **Original URL:** https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1515.pdf
- **Access method and result:** The Phase 2A.1 record reports a failed NIST-host request due to DNS resolution; not retried.
- **Expected document retrieved / identity:** Not from this URL. A supplied local copy of the report was reviewed and matches the citation; this exact destination remains unconfirmed.
- **Verification level:** `NETWORK_UNAVAILABLE` for this URL; local report review is separately `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the original official NIST locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A10 — NIST TN 1515 publication page

- **Bibliography ID; source:** U4; NIST publication record for *Comparison of Passive Intermodulation Measurements for the U.S. Wireless Industry*.
- **Stable identifier:** DOI `10.6028/NIST.TN.1515`; report 1515.
- **Original URL:** https://www.nist.gov/publications/comparison-passive-intermodulation-measurements-u-s-wireless-industry
- **Access method and result:** The Phase 2A.1 record reports a failed NIST-host request due to DNS resolution; not retried.
- **Expected document retrieved / identity:** No publication-page content retrieved. The report's title and authors were confirmed from the supplied local report, not this page.
- **Verification level:** `NETWORK_UNAVAILABLE`.
- **Replacement URL:** None; retain the official NIST publication-page locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A11 — Frey publisher abstract URL

- **Bibliography ID; source:** U1; Allan H. Frey, “Human Auditory System Response to Modulated Electromagnetic Energy,” *Journal of Applied Physiology* 17, no. 4 (1962), pp. 689–692.
- **Stable identifier:** DOI `10.1152/jappl.1962.17.4.689`.
- **Original URL:** https://journals.physiology.org/doi/abs/10.1152/jappl.1962.17.4.689
- **Access method and result:** The Phase 2A.1 record reports publisher-host DNS failure; this exact abstract path was not separately retried.
- **Expected document retrieved / identity:** No content from this URL. The supplied local article includes the cited title, author, journal, and pagination; this abstract URL was not confirmed.
- **Verification level:** `NETWORK_UNAVAILABLE`.
- **Replacement URL:** None; retain the publisher's original locator.
- **Date checked:** 2026-11-16 (publisher host checked in prior attempt).

### A12 — Frey PubMed record

- **Bibliography ID; source:** U1; Allan H. Frey, “Human Auditory System Response to Modulated Electromagnetic Energy,” PubMed record.
- **Stable identifier:** PMID `13895081`; DOI `10.1152/jappl.1962.17.4.689`.
- **Original URL:** https://pubmed.ncbi.nlm.nih.gov/13895081/
- **Access method and result:** The Phase 2A.1 record reports one request and DNS-resolution failure; not retried.
- **Expected document retrieved / identity:** No PubMed record content retrieved. The supplied local paper's bibliographic identity was reviewed; PubMed identity was not checked from this URL.
- **Verification level:** `NETWORK_UNAVAILABLE`.
- **Replacement URL:** None; retain the authoritative PubMed locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A13 — Frey publisher full-text locator

- **Bibliography ID; source:** U1; Allan H. Frey, “Human Auditory System Response to Modulated Electromagnetic Energy,” *Journal of Applied Physiology*.
- **Stable identifier:** DOI `10.1152/jappl.1962.17.4.689`.
- **Original URL:** https://journals.physiology.org/doi/10.1152/jappl.1962.17.4.689
- **Access method and result:** The Phase 2A.1 record reports publisher-host DNS failure; this exact path was not separately retried.
- **Expected document retrieved / identity:** No content from this URL. The supplied local four-page article matches the citation; the publisher URL destination was not confirmed.
- **Verification level:** `NETWORK_UNAVAILABLE` for this URL; local article review is separately `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the publisher's original locator.
- **Date checked:** 2026-11-16 (publisher host checked in prior attempt).

### A14 — Official NIST IR 8387 PDF

- **Bibliography ID; source:** U7; Barbara Guttman, Douglas R. White, and Tracy Walraven, *Digital Evidence Preservation: Considerations for Evidence Handlers*, NIST IR 8387 (2022).
- **Stable identifier:** DOI `10.6028/NIST.IR.8387`; report 8387.
- **Original URL:** https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8387.pdf
- **Access method and result:** The Phase 2A.1 record reports a failed NIST-host request due to DNS resolution; not retried.
- **Expected document retrieved / identity:** Not from this URL. The supplied local 22-page NIST report was reviewed and its author list and report identifier match; this URL destination itself was not confirmed.
- **Verification level:** `NETWORK_UNAVAILABLE` for this URL; local report review is separately `FULL_TEXT_REVIEWED`.
- **Replacement URL:** None; retain the original official NIST locator.
- **Date checked:** 2026-11-16 (prior attempt).

### A15 — NIST IR 8387 publication page

- **Bibliography ID; source:** U7; NIST publication record for *Digital Evidence Preservation: Considerations for Evidence Handlers*.
- **Stable identifier:** DOI `10.6028/NIST.IR.8387`; report 8387.
- **Original URL:** https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers
- **Access method and result:** The Phase 2A.1 record reports a failed NIST-host request due to DNS resolution; not retried.
- **Expected document retrieved / identity:** No publication-page content retrieved. The supplied report matches the citation; author-list comparison against this page remains unverified.
- **Verification level:** `NETWORK_UNAVAILABLE`.
- **Replacement URL:** None; retain the official NIST publication-page locator.
- **Date checked:** 2026-11-16 (prior attempt).

## Summary and Limits

| Result | URLs |
|---|---:|
| `VERIFIED_FULL_TEXT` | 1 |
| `VERIFIED_ABSTRACT` | 1 |
| `VERIFIED_METADATA` | 3 |
| `NETWORK_UNAVAILABLE` | 9 |
| `UNVERIFIED` | 1 |
| URLs replaced | 0 |

Five URL destinations returned the expected NTIA document or authoritative conference/catalog metadata. Nine publisher, government-host, conference-paper, PubMed, or NIST-page destinations remain inaccessible from the recorded environment. Separately, all five source texts named in the bibliography's current status were reviewed from supplied documents; this does not establish that each blocked URL serves the reviewed copy or that reported experiments were independently replicated.

No inaccessible URL was labeled a dead link, and no third-party mirror was substituted. All original DOI and publication provenance in the bibliography is preserved.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-11-16T16:15:58-06:00 | Initial URL-by-URL audit of the bibliography's 15 distinct external citation URLs, preserving inaccessible official locators and distinguishing URL access from local full-text review. | GitHub Copilot |
