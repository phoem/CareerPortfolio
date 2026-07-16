# ADR 0019: Maintain an Append-Only LinkedIn Change Log

## Status

Accepted

## Context

LinkedIn profile changes are externally visible and may affect professional positioning. A completion message in chat is temporary and does not provide a durable record of what was added, removed, updated, reordered, attempted, approved, or verified.

## Decision

Maintain `linkedin/CHANGELOG.md` as an append-only audit trail for the manual LinkedIn workflow.

Every attempted or successful LinkedIn edit must record an ISO 8601 timestamp with an explicit UTC offset, profile URL, field, action, exact before and intended after state when available, approval scope, result, verification status, notification-setting observation when relevant, errors or warnings, and related CareerPortfolio knowledge or commit references.

Failed and partially completed attempts are logged as well as successful changes. Corrections to the log are added as new entries rather than silently rewriting history. Authentication material, private messages, cookies, tokens, recovery information, and unnecessary browser captures are prohibited.

## Consequences

### Positive

- provides a durable history of externally visible profile changes;
- supports auditing, rollback planning, and synchronization with CareerPortfolio;
- distinguishes approved intent from the final verified LinkedIn state;
- preserves useful failure and warning information.

### Negative

- exact before and after text increases repository content and must be reviewed for appropriate disclosure;
- every publishing session requires a follow-up repository update;
- append-only corrections may leave superseded entries that readers must interpret chronologically.

## Related Decisions

- [ADR 0003: Record Knowledge Before Generating Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0018: Use an Approval-Gated LinkedIn Profile Workflow](0018-use-an-approval-gated-linkedin-profile-workflow.md)
