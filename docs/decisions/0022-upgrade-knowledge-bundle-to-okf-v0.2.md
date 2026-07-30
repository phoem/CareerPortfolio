---
type: decision
status: accepted
decision_number: 22
tags:
  - knowledge
  - okf
  - provenance
  - trust
---

# ADR 0022: Upgrade the Knowledge Bundle to OKF v0.2

## Status

Accepted

## Context

CareerPortfolio adopted Open Knowledge Format v0.1 as the representation for professional knowledge. OKF v0.2 supersedes v0.1 and adds standard provenance, authorship, verification, lifecycle, freshness, and attestation fields while preserving the Markdown-plus-YAML structure and the required `type` field.

The repository already distinguishes confirmed facts, estimates, external support, and unknown information. Adopting v0.2 makes those trust signals more interoperable and queryable without replacing the existing evidence-quality rules.

## Decision

Upgrade `knowledge/` to target OKF v0.2.

- Declare `okf_version: "0.2"` in `knowledge/index.md`.
- Use `generated.at` instead of the legacy `timestamp` field for new and migrated concepts.
- Record the most accurate known producer in `generated.by`.
- Use `verified` only when a person, source, or deterministic process actually confirms the concept.
- Store external provenance in frontmatter `sources` with stable IDs rather than relying on body-only citation lists.
- Use lifecycle and freshness fields only when meaningful; do not add `stale_after` mechanically to historical career facts.
- Preserve repository-specific and unknown metadata during migration.
- Keep evidence classification, personal ownership, estimates, resume-safe wording, and open questions in the concept body where that remains clearer than frontmatter.
- Update knowledge metadata whenever meaningful concept content changes.

## Consequences

Positive:

- Authorship, verification, provenance, lifecycle, and freshness become machine-queryable.
- External evidence can be linked to individual claims through stable source IDs.
- The repository remains compatible with the current OKF specification while retaining its factual-accuracy model.
- Consumers can distinguish who produced knowledge from who confirmed it.

Trade-offs:

- Existing concepts require incremental frontmatter migration.
- Historical authorship may not always be reconstructable precisely; migrations must use honest actors and avoid invented provenance.
- Optional v0.2 fields can create false confidence if populated mechanically, so omission remains preferable to unsupported metadata.

## Related

- [ADR 0001: Adopt Google Cloud Open Knowledge Format](0001-adopt-google-cloud-open-knowledge-format.md)
- [ADR 0003: Record knowledge before generating artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store only confirmed knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0021: Require application evidence maps and explicit evidence quality](0021-require-application-evidence-maps-and-explicit-evidence-quality.md)
- [OKF Knowledge Conventions](../OKF_PORTFOLIO.md)