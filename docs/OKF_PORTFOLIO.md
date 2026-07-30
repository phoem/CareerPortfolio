# OKF Knowledge Conventions

This repository uses the [Google Cloud Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) for the professional-knowledge bundle under `knowledge/`.

## What OKF Means Here

OKF is a directory tree of Markdown concept documents with YAML frontmatter. It is human-readable, agent-readable, diffable, and portable.

This repository does **not** use `project.okf.yaml` files. The Markdown concept document itself is the knowledge record.

## Bundle Root

`knowledge/` is the OKF knowledge-bundle root.

- `knowledge/index.md` provides progressive-disclosure navigation and declares `okf_version: "0.2"`.
- `knowledge/log.md` records meaningful knowledge changes.
- Concept directories contain one or more Markdown concept documents.

## Concept Frontmatter

Every non-reserved Markdown concept must begin with YAML frontmatter and include `type`.

Recommended template:

```yaml
---
type: Software Project
title: Project Name
description: One-sentence project summary.
tags: [systems, networking]
generated:
  by: human/jordan-newman
  at: 2026-07-30T00:00:00Z
verified:
  - by: human/jordan-newman
    at: 2026-07-30T00:00:00Z
status: active
owner: Jordan Newman
evidence_status: confirmed
---
```

Standard OKF fields:

- `type` — required concept type;
- `title` — display name;
- `description` — one-sentence summary;
- `resource` — canonical URI when known;
- `tags` — cross-cutting categorization;
- `sources` — structured provenance for externally supported claims;
- `generated` — who or what produced the current content and when;
- `verified` — who or what confirmed the content against its sources or authoritative record;
- `status` — lifecycle state;
- `stale_after` — optional freshness boundary when the knowledge can reasonably expire.

Repository extensions:

- `owner` — the person whose work is documented;
- `evidence_status` — normally `confirmed`; use another value only when uncertainty is explicitly documented;
- `deployment` — optional short production-use summary;
- documentation-maturity fields may be retained as repository extensions when they do not conflict with OKF lifecycle semantics.

Unknown fields must be preserved during edits.

## v0.1 Migration Rules

- Replace legacy `timestamp` with `generated.at`; preserve the old value when it accurately represents the last meaningful content update.
- Add `generated.by` using the most accurate known actor. Do not imply that an AI agent authored historical content when it did not.
- Add `verified` only when a person, source, or deterministic check actually confirmed the content.
- Move external provenance from body `# Citations` lists into frontmatter `sources` with stable IDs.
- Use source-keyed Markdown footnotes when a particular claim needs claim-level attribution.
- Do not add `stale_after` mechanically. Use it only for knowledge whose freshness can reasonably expire.
- Preserve repository-specific metadata and all unknown fields.

## Trust and Provenance

`generated` describes authorship or production of the current concept. `verified` describes confirmation. These are distinct.

For Jordan-confirmed professional history, a typical verification record is:

```yaml
verified:
  - by: human/jordan-newman
    at: 2026-07-30T00:00:00Z
```

For external sources:

```yaml
sources:
  - id: pcworld-dns-attack
    url: https://example.com/article
    title: Article title
    author: Publisher or author when known
    usage_count: 1
```

Do not use an external publication as proof of Jordan's personal contribution unless the concept separately documents that ownership.

## Evidence Quality

Concepts should make the quality and limits of important evidence visible in prose or a dedicated `Evidence` section. Use the smallest amount of structure that keeps the distinction clear.

Useful classifications include:

- **Exact** — a value, date, implementation detail, or outcome known precisely from a reliable record or direct confirmation.
- **Estimated** — an explicitly approximate value or range; preserve words such as `approximately`, `about`, or `estimated` in downstream wording.
- **Externally supported** — a claim supported by a publication, repository, benchmark record, or other frontmatter `sources` entry.
- **Qualitative** — a confirmed fact without a defensible numeric measure.
- **Resume-safe wording** — an optional concise wording variant that faithfully preserves the underlying evidence classification and personal ownership.

Do not encode a metric as exact merely because it appears precise in an old resume.

## Concept Types

Types are descriptive, not centrally registered. Preferred values include:

- `Software Project`
- `Kernel Module`
- `Infrastructure Platform`
- `Embedded System`
- `Operating System Project`
- `Technical Metric`
- `Resume Evidence`
- `Professional Profile`
- `Interview Story`
- `Reference`
- `Attested Computation`

Agents must tolerate and preserve other useful types.

## Links and Relationships

Use normal Markdown links to connect related concepts. Prefer bundle-relative links beginning with `/` when practical.

Example:

```markdown
PrimeHTTPD was part of the [CDN platform](/CDN_Platform/README.md) and worked alongside [VirtualDir](/VirtualDir/README.md).
```

Relationship meaning is expressed in prose, consistent with OKF.

## Open Questions

Use an `Open Questions` section in the nearest relevant concept to preserve missing details that could materially strengthen future resumes, application evidence maps, or interviews.

Open questions should:

- ask for a specific implementation, ownership, scale, performance, reliability, or outcome detail;
- remain clearly separated from confirmed factual sections;
- avoid speculative answers or implied claims;
- be removed, answered, or rewritten when Jordan provides the missing information;
- trigger a `knowledge/log.md` entry when the answer produces a meaningful knowledge change.

Do not create a parallel missing-knowledge database unless repeated use demonstrates that concept-local questions are insufficient.

## Attested Computation

Use `type: Attested Computation` only when a knowledge claim is produced by a repeatable computation whose runtime, parameters, executor, and attester are documented. Resume claims should not be converted into attested computations merely to appear more formal.

## Accuracy and Incremental Growth

- Only confirmed facts belong in factual sections.
- Estimates and ranges must remain estimates and ranges.
- Missing information belongs in `Open Questions`, not invented prose.
- Documentation grows as job requirements make additional details relevant.
- Update the OKF concept before adding newly learned facts to a resume.
- Keep `generated`, `verified`, `sources`, lifecycle, and freshness metadata current whenever a meaningful knowledge change is made.