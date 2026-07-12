# ADR 0001: Adopt Google Cloud Open Knowledge Format

## Status

Accepted

## Context

CareerPortfolio needs a professional knowledge base that is readable by people, usable by AI agents, portable, diffable, and maintainable in Git. A custom YAML or database schema would add tooling and migration burden.

## Decision

Use Google Cloud's Open Knowledge Format (OKF) v0.1 for the authoritative knowledge bundle under `knowledge/`.

Knowledge concepts are Markdown files with YAML frontmatter. Every non-reserved concept requires a non-empty `type` field. `index.md` and `log.md` retain their reserved OKF meanings. Standard Markdown links express relationships, and citations are added when claims depend on external sources.

CareerPortfolio does not use separate `project.okf.yaml` files.

## Consequences

### Positive

- Knowledge remains human-readable without special tools.
- Agents can parse metadata and structured Markdown.
- Git provides history, attribution, review, and portability.
- The format can grow without a central schema registry.

### Negative

- Producers must preserve frontmatter and unknown extension fields.
- Consistency depends on documented conventions and review.
- OKF v0.1 is a draft specification and may evolve.

## References

- `docs/OKF_PORTFOLIO.md`
- `knowledge/index.md`
