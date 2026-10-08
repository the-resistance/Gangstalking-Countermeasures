---
Document Title: Documentation Versioning Policy
Document ID: GOV-VERSIONING-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-10-08T10:12:48-05:00
Last Updated: 2026-10-08T10:12:48-05:00
---

# Documentation Versioning Policy

This document is the canonical authority for versions, timestamps, revision histories, and the repository changelog. Apply it to managed Markdown documents: authored project documentation, including governance files. `README.md` may use visible Markdown metadata instead of YAML front matter to preserve its public-facing presentation. `CHANGELOG.md` is the repository-level change ledger and does not require its own version or revision history; entries in it must follow rule V-006.

## V-001 — Semantic Versioning

Each managed document has its own independent `MAJOR.MINOR.PATCH` version:

- **MAJOR** — a major restructuring or other breaking change to the document.
- **MINOR** — significant new content that does not constitute a major restructuring.
- **PATCH** — minor corrections that do not add significant content.

Use `1.0.0` for a document's initial publication. Increment only the relevant document's version when its content changes. Examples: `1.0.0` initial publication, `1.1.0` significant new content, `1.1.1` minor correction, `2.0.0` major restructuring.

## V-002 — Document Metadata

Each managed document must identify its title, ID, author, version, creation timestamp, and last substantive modification timestamp. Use this YAML front matter format:

```yaml
---
Document Title: Document title
Document ID: DOC-001
Author: Kevin Mahan
Version: 1.0.0
Created: 2026-10-08T10:12:48-05:00
Last Updated: 2026-10-08T10:12:48-05:00
---
```

The timestamp above illustrates format only; it is not a timestamp to reuse. Use actual timestamps. Use the `America/Chicago` time zone unless explicitly instructed otherwise, and include the correct UTC offset for the timestamp (including daylight-saving time when applicable). For `README.md`, visible Markdown metadata may be used instead of front matter.

Apply these requirements to new documents when they are created. For a pre-existing document without this metadata, add it as part of the next explicitly authorized substantive edit; do not modify unrelated documents solely to retrofit metadata. Use reliable records for historical timestamps and follow V-003 when the original creation time cannot be established.

## V-003 — Timestamp Requirements

Preserve a document's original creation timestamp, most recent substantive modification timestamp, original observation timestamp where applicable, and historical revision timestamps. When content changes, update `Last Updated`, preserve `Created`, and record the change in the revision history. Do not change timestamps merely because a document was opened or inspected, and do not claim a modification unless the content actually changed.

Never invent a timestamp. If an existing document's creation time cannot be established from reliable records, identify the missing information rather than presenting an assumed time as fact. The timestamp of a revision must reflect when that revision is actually made.

## V-004 — Revision History

Every managed document must contain a revision history with `Version`, `Timestamp`, `Description`, and `Author` fields. Add each subsequent revision as a new chronological record; never erase prior revision entries.

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | Actual ISO 8601 timestamp with offset | Initial publication | Kevin Mahan |

The example row describes required fields, not a historical record to copy.

## V-005 — Independent Versioning

Changing one document does not require version changes to unrelated documents. Update only documents whose content actually changed. An index or navigation document may also need an update when its linked content changes; version that document only if its own content changes.

## V-006 — Changelog

Maintain [`CHANGELOG.md`](../CHANGELOG.md) as the repository-level record, ordered in reverse chronological order. Each entry must identify:

- Date and timestamp
- Modified document
- Previous version, if applicable
- New version
- Specific change summary
- Author

Describe the actual modification; do not use vague entries such as “Updated documentation.” For an initial publication, identify the new version and state that no previous version applies.

## V-007 — Git Traceability

Each completed modification must be traceable through Git history. Use descriptive commit messages, such as `docs: establish governance framework`, `docs(scenario-001): append observation`, or `docs: correct documentation metadata`. Do not amend or rewrite published historical commits solely to conceal earlier revisions.

## Revision History

| Version | Timestamp | Description | Author |
|---------|-----------|-------------|--------|
| 1.0.0 | 2026-10-08T10:12:48-05:00 | Initial publication of documentation versioning policy. | Kevin Mahan |
