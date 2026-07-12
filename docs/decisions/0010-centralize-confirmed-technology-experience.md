# ADR 0010: Centralize Confirmed Technology Experience

## Status

Accepted; implementation pending

## Context

Technology lists are duplicated across resumes and may omit context such as project, depth, production use, recency, and personal ownership. A flat keyword list is not enough to support accurate tailoring.

## Decision

Create a shared OKF technology-experience catalog that records confirmed technologies with contextual links to projects and roles. Entries should distinguish hands-on implementation, architecture, operation, deployment, and familiarity where known.

The catalog should be implemented when it solves an active resume or validation need rather than as speculative bulk documentation.

## Consequences

### Positive

- Improves keyword accuracy and evidence mapping.
- Reduces unsupported or context-free skill claims.
- Helps tailor skills sections by role.

### Negative

- Requires ongoing synchronization with project knowledge.
- Technology depth and recency may require additional clarification.

## Related Decisions

- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0008: Grow the Knowledge Base Incrementally](0008-grow-the-knowledge-base-incrementally.md)
