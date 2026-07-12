# ADR 0004: Maintain Three Canonical Generic Resumes

## Status

Accepted

## Context

A single generic resume cannot effectively emphasize all of Jordan Newman's relevant experience. Systems, architecture, and general senior software roles value different evidence and framing.

## Decision

Maintain three canonical reusable resumes:

1. Senior Software Engineer.
2. Software Architect.
3. Backend / Infrastructure Engineer.

All three draw from the same verified knowledge base but emphasize different aspects of the same facts. Targeted resumes should begin from the closest canonical version rather than from whichever resume was edited most recently.

## Consequences

### Positive

- Reduces repetitive rewriting.
- Preserves distinct market positioning.
- Improves consistency across targeted applications.

### Negative

- Improvements may need selective propagation across multiple files.
- All three must remain synchronized with the knowledge base.

## Related Decisions

- [ADR 0003: Knowledge Before Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0005: Create Targeted Application Packages](0005-create-targeted-application-packages.md)
