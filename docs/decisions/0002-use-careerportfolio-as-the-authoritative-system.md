# ADR 0002: Use CareerPortfolio as the Authoritative Professional System

## Status

Accepted

## Context

The repository began as a collection of resumes, but the useful information now includes project history, architecture, verified metrics, role-specific evidence, workflow rules, and application packages. Resumes alone are too narrow and duplicate important facts.

## Decision

Treat `phoem/CareerPortfolio` as the authoritative system for Jordan Newman's professional knowledge and career artifacts.

The repository contains the curated source knowledge, canonical resumes, targeted application packages, workflow documentation, and generated deliverables. Resumes are outputs of the system rather than the sole source of truth.

## Consequences

### Positive

- Important experience is retained independently of any single resume.
- Future applications can reuse verified evidence.
- The repository can support interview preparation and other career artifacts later.

### Negative

- Repository maintenance extends beyond editing resumes.
- Structural decisions require documentation and consistency checks.

## Related Decisions

- [ADR 0003: Knowledge Before Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0004: Maintain Three Canonical Generic Resumes](0004-maintain-three-canonical-generic-resumes.md)
