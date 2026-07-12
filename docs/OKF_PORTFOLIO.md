# OKF Knowledge Conventions

This repository uses the [Google Cloud Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) for the professional-knowledge bundle under `knowledge/`.

## What OKF Means Here

OKF is a directory tree of Markdown concept documents with YAML frontmatter. It is human-readable, agent-readable, diffable, and portable.

This repository does **not** use `project.okf.yaml` files. The Markdown concept document itself is the knowledge record.

## Bundle Root

`knowledge/` is the OKF knowledge-bundle root.

- `knowledge/index.md` provides progressive-disclosure navigation.
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
timestamp: 2026-07-12T00:00:00Z
status: partial
owner: Person Name
evidence_status: confirmed
---
```

Standard OKF fields:

- `type` — required concept type;
- `title` — display name;
- `description` — one-sentence summary;
- `resource` — canonical URI when known;
- `tags` — cross-cutting categorization;
- `timestamp` — last meaningful knowledge update.

Repository extensions:

- `status` — documentation maturity such as `partial`, `documented`, or `interview-ready`;
- `owner` — the person whose work is documented;
- `evidence_status` — normally `confirmed`; use another value only when uncertainty is explicitly documented;
- `deployment` — optional short production-use summary.

Unknown fields must be preserved during edits.

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

Agents must tolerate and preserve other useful types.

## Links and Relationships

Use normal Markdown links to connect related concepts. Prefer bundle-relative links beginning with `/` when practical.

Example:

```markdown
PrimeHTTPD was part of the [CDN platform](/CDN_Platform/README.md) and worked alongside [VirtualDir](/VirtualDir/README.md).
```

Relationship meaning is expressed in prose, consistent with OKF.

## Citations

When a claim relies on published or external evidence, include a numbered `# Citations` section. Personal recollection and directly supplied project facts do not require external citations, but the concept should clearly distinguish estimates from exact values.

## Accuracy and Incremental Growth

- Only confirmed facts belong in factual sections.
- Estimates and ranges must remain estimates and ranges.
- Missing information belongs in `Open Questions`, not invented prose.
- Documentation grows as job requirements make additional details relevant.
- Update the OKF concept before adding newly learned facts to a resume.
