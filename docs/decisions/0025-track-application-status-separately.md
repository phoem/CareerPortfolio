# ADR 0025: Track Application Status Separately from Preparation Status

## Status

Accepted

## Context

CareerPortfolio records resume-tailoring stages such as evidence gathering and submission ready, but those stages do not prove whether an application was submitted. Historical application packages predate explicit lifecycle tracking, so treating them as not applied would replace missing knowledge with an unsupported claim.

Application status also changes independently of resume content. Storing lifecycle fields in `APPLICATION.json` would cause status-only edits to trigger unnecessary DOCX/PDF generation because application manifests intentionally participate in incremental artifact selection.

The portfolio needs both an authoritative record beside each posting and a complete cross-portfolio view without maintaining two independently editable sources of truth.

## Decision

Each application package must contain an authoritative `APPLICATION_STATUS.json`. Existing packages default to `unknown` unless their status is confirmed. Future packages default to `not_applied` unless they are created for an already-submitted application with a confirmed later state.

The controlled lifecycle states are `unknown`, `not_applied`, `applied`, `interviewing`, `offer_received`, and `closed`. Closed applications may record the controlled outcomes `not_selected`, `withdrawn`, `offer_declined`, or `accepted`.

Confirmed transitions may be retained in a history array with the date the information was recorded, its source, and a note. Unknown event dates are omitted or described as unknown; they are never inferred from the record date.

`applications/STATUS.json` is a generated master index built from every package manifest and status file. Package status files remain authoritative. A repository script refreshes the master index and a dedicated CI workflow rejects missing, invalid, or stale status records.

Preparation state remains separate in application-package documentation and `applications/QUEUE.md`. Status-only files are excluded from resume-artifact workflow triggers.

## Consequences

### Positive

- Distinguishes prepared materials from confirmed submissions.
- Preserves uncertainty for historical applications.
- Provides one complete portfolio-wide status view.
- Prevents the master index from becoming a second editable source of truth.
- Avoids unnecessary artifact generation after status-only updates.
- Retains confirmed lifecycle transitions without inventing event dates.

### Negative

- Every application package gains one small metadata file.
- Contributors must refresh the master index after a status change.
- Historical packages remain unknown until Jordan or reliable records confirm them.

## Related Decisions

- [ADR 0005: Create Targeted Application Packages from Real Job Listings](0005-create-targeted-application-packages.md)
- [ADR 0006: Store Only Confirmed Knowledge and Preserve Uncertainty](0006-store-only-confirmed-knowledge.md)
- [ADR 0015: Organize Targeted Applications by Company and Posting](0015-organize-targeted-applications-by-company-and-posting.md)
- [ADR 0017: Use Incremental Artifact Builds and Scoped Validation](0017-use-incremental-artifact-builds-and-scoped-validation.md)
