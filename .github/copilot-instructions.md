---
Document Title: Copilot Repository Instructions
Document ID: GOV-COPILOT-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-10-08T10:12:48-05:00
Last Updated: 2026-10-08T10:12:48-05:00
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

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:12:48-05:00 | Initial publication of repository-wide Copilot instructions. | Kevin Mahan |
