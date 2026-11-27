---
Document Title: Copilot Repository Instructions
Document ID: GOV-COPILOT-001
Author: Kevin Mahan
Version: 1.3.0
Created: 2026-10-08T10:12:48-05:00
Last Updated: 2026-11-26T22:19:35-06:00
---

# Copilot Repository Instructions

These instructions govern GitHub Copilot's repository work. The canonical policy documents are [Versioning](../governance/VERSIONING.md) and [Anti-Drift](../governance/ANTI_DRIFT.md). Consult both before changing repository documentation; they are authoritative for their respective subjects. The [repository changelog](../CHANGELOG.md) records completed documentation changes.

If requirements conflict, stop before editing the affected content and report the conflict. Do not silently choose between conflicting instructions or policies.

## Operating Sequence

Apply the BlitzWaffe execution model to repository modifications:

1. **Resolve:** Identify the requested operation and whether it creates, modifies, corrects, or appends content.
2. **Precheck:** Read the complete target document and applicable governance requirements. Identify dependencies and historical information to preserve.
3. **Execute:** Make only authorized changes, preserving existing content and placing new information in the appropriate document.
4. **Verify:** Compare before and after versions. Confirm no unauthorized information was removed or changed; validate structure, version, timestamps, and internal references.
5. **Commit:** Use a descriptive Git commit message. Update the document's revision history and `CHANGELOG.md` as required by the versioning policy.
6. **Recover:** If validation fails, preserve the pre-modification version, identify the failure, and correct it before proceeding. Never silently discard information.

## Before Editing Documentation

Before modifying any repository documentation:

1. Read the applicable governance documents, including both authoritative policies linked above.
2. Identify the intended and authorized modification.
3. Review the complete target document.
4. Preserve its historical information.
5. Determine whether the request concerns a new subject or an existing document.
6. Establish the required version change under [Versioning](../governance/VERSIONING.md).
7. Obtain the actual modification timestamp in the applicable time zone.
8. Execute only the authorized changes.
9. Compare the modified document with its prior version.
10. Verify historical information was preserved.
11. Update document metadata, preserving its original creation timestamp.
12. Update applicable revision records.
13. Update `CHANGELOG.md`.
14. Validate Markdown formatting and internal links.
15. Report the modifications and validation results.

Do not invent timestamps, findings, evidence, or prior revisions. Do not update a timestamp when the document's content has not changed.

## Validation Checklist

### Before editing

- [ ] Target file identified
- [ ] Complete existing content reviewed
- [ ] Applicable governance rules consulted
- [ ] Authorized modification scope established
- [ ] Current document version identified, or absence noted for a new document
- [ ] Historical information identified and protected

### After editing

- [ ] Requested changes completed and limited to authorized scope
- [ ] Existing observations and other historical information preserved
- [ ] No unauthorized deletions or unrelated restructuring
- [ ] Document version updated as required
- [ ] Modification timestamp updated only if content changed
- [ ] Original creation timestamp preserved
- [ ] Revision history updated
- [ ] `CHANGELOG.md` updated
- [ ] Markdown formatting and internal links validated
- [ ] Git diff reviewed, including every deletion and replacement

If historical observations, evidence records, or scenario content are removed unexpectedly, validation fails. Restore the affected information before committing. Intentional corrections must follow the correction procedure in [Anti-Drift](../governance/ANTI_DRIFT.md). Governance instructions do not constitute automated enforcement; do not create CI workflows or enforcement scripts unless separately authorized.

## Repository Scope and Attribution

The README describes the repository's mission and general purpose; keep operational rules in the governance documents. Do not create investigative subjects or scenarios, fabricate findings, or expand repository scope without explicit authorization. Preserve established project identifiers and author attribution as specified in [Anti-Drift](../governance/ANTI_DRIFT.md).

## Execution diagnostics and permission handling

This section is the canonical execution and recovery policy. Versioning governs metadata and revision history; Anti-Drift governs content integrity; scripts/README.md describes validators. Historical audit reports and task prompts are not independent standing policies. Report genuine conflicts before affected work; continue unrelated authorized work.

At phase start identify the session, branch, baseline, task counters, available tools and publication workflow. Inspect available capabilities without changing permissions or security settings. Do not assume authorization from repository ownership.

Keep verbose diagnostics in a temporary location outside the public repository, or in the session if private temporary storage is unavailable. Never stage, commit, push, or publish raw diagnostic logs to public branches, issues, pull requests or artifacts. Temporary logs are not managed project documentation. Retain them until diagnostic review is complete, then remove temporary copies where supported. Only sanitized change summaries belong in CHANGELOG.md.

Record each substantive operation before execution and its result immediately afterward: actual timestamp, operation, status, exit code, stdout, stderr, exact denial text when available, affected files and checkpoint. Redact secrets and personal data. Distinguish authorization denial, process failure, validation failure, Git conflict and infrastructure failure. Mark unavailable details explicitly; never invent them.

Use one independently authorized operation per tool invocation. Do not combine unrelated filesystem tests, validators, authentication checks, or publication commands in one execution request. Capture tool output directly; do not create diagnostic files or redirect output unless necessary and explicitly authorized. Read applicable governance documents in full, not just excerpts.

If authorization is denied, record the original denial and its scope immediately. Do not retry, rephrase, repackage, or bypass the denied effect, including in a new session. Where required operations remain denied, stop those operations and request authorization through the platform's supported mechanism or report the blocker. Only genuinely independent authorized work may continue. Do not infer that a denied command ran or that an unexecuted validator failed.

Run validators independently using the documented commands, without pipelines masking exit status. Use the supported agent publication workflow. Do not change Git identity unnecessarily, retry explicitly denied operations, or circumvent controls. Preserve partial work and continue independent authorized tasks where feasible. Do not restart completed work automatically.

If diagnostics cannot be accessed privately by the operator, or any required operation fails, return the complete sanitized diagnostic report in exactly one continuous fenced plain-text code block, with no nested fences, tables, or prose outside it. Include phase status, baseline, all attempted operations and results, exact available errors, last successful checkpoint, unfinished work, publication status and next required action. Escape any embedded fence sequences as plain text. Never return only PHASE BLOCKED.

Declare PHASE COMPLETE only when required work, validation and supported publication are confirmed. Otherwise report actual partial or blocked status using the diagnostic format above.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:12:48-05:00 | Initial publication of repository-wide Copilot instructions. | Kevin Mahan |
| 1.1.0 | 2026-11-26T00:23:25-06:00 | Added phase diagnostics, permission handling, managed publication and failure-reporting fallback. | Kevin Mahan |
| 1.2.0 | 2026-11-26T20:18:48-06:00 | Clarified policy authority, private temporary diagnostics, fault isolation and single-block failure reporting. | Kevin Mahan |
| 1.3.0 | 2026-11-26T22:19:35-06:00 | Required atomic execution, direct diagnostic capture and explicit denial-scope handling. | Kevin Mahan |
