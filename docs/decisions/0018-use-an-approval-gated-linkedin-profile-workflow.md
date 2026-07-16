# ADR 0018: Use an Approval-Gated LinkedIn Profile Workflow

## Status

Accepted

## Context

CareerPortfolio should help keep Jordan Newman's LinkedIn profile aligned with verified professional knowledge. Reading and editing LinkedIn requires an authenticated interactive session, and profile changes are externally visible. An unattended scheduled process or GitHub Action would not provide an appropriate human review boundary.

## Decision

Use a manually invoked, two-phase LinkedIn workflow:

1. perform a read-only profile review and present exact proposed changes with supporting CareerPortfolio evidence;
2. stop for explicit field-level approval, then publish and verify only the approved changes through Jordan's authenticated browser session.

CareerPortfolio remains the factual source of truth. LinkedIn-only claims are not promoted into the knowledge base without Jordan's confirmation. The workflow must not access or store credentials or modify unrelated account, network, messaging, privacy, or job-search settings.

The workflow is documented in `docs/workflows/LINKEDIN_PROFILE_WORKFLOW.md`. It is not implemented as an unattended GitHub Action.

## Consequences

### Positive

- keeps externally visible changes under Jordan's control;
- creates a clear separation between recommendation and publication;
- grounds LinkedIn wording in verified CareerPortfolio evidence;
- supports post-save verification and an optional audit record;
- avoids storing LinkedIn authentication material in the repository.

### Negative

- Jordan must be available for approval and authentication;
- LinkedIn interface changes may require workflow adaptation;
- profile synchronization is intentionally manual rather than continuous;
- field-by-field verification takes longer than bulk editing.

## Related Decisions

- [ADR 0003: Record Knowledge Before Generating Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0008: Grow the Knowledge Base Incrementally](0008-grow-the-knowledge-base-incrementally.md)
