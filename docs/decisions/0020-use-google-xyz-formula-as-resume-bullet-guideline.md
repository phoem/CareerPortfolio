---
type: decision
status: accepted
decision_number: 20
tags:
  - resume-writing
  - quality
  - workflow
---

# ADR 0020: Use the Google XYZ Formula as a Resume-Bullet Guideline

## Status

Accepted

## Context

CareerPortfolio needs a repeatable way to make resume bullets outcome-oriented without encouraging unsupported metrics or formulaic wording. The Google XYZ formula frames an accomplishment as an outcome (X), measured evidence or scope (Y), and the action or method that produced it (Z).

## Decision

Use the Google XYZ formula as a preferred fact-selection and editing guideline for resume bullets when the supporting outcome, measurement, and method are documented. Do not require literal XYZ wording for every bullet. Where no defensible measurement is known, use an outcome-first alternative that states the capability, the enabled result, and the technical approach.

## Consequences

Positive:

- Encourages outcomes, verified scale, and personal ownership.
- Makes technical experience more legible to recruiters and hiring managers.
- Reinforces the repository rule against invented metrics.

Trade-offs:

- Some systems and architecture work cannot honestly include a metric.
- Applying the formula mechanically can make bullets repetitive, so editorial judgment remains required.

## Related

- [ADR 0006: Store only confirmed knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0009: Centralize verified career metrics](0009-centralize-verified-career-metrics.md)
- [Resume Writing Style Guide](../STYLE_GUIDE.md)
