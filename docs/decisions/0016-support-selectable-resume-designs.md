# ADR 0016: Support Selectable Resume Designs

## Status

Accepted

## Context

CareerPortfolio needs to support more than one visual resume design without duplicating factual resume content. A user may want to change the repository default, apply a design to every future rebuild of one application, or request a different design for only the next build.

## Decision

Store reusable rendering designs under `designs/<design-name>/` and select the repository default through `designs/default.json`.

Application packages may use:

- `DESIGN.json` for a persistent override affecting all future builds of that application;
- `DESIGN_NEXT.json` for a one-build override that takes precedence and is removed after successful generation.

Design resolution order is:

1. application `DESIGN_NEXT.json`;
2. application `DESIGN.json`;
3. repository `designs/default.json`.

Design files control presentation only. Resume facts and wording remain in the canonical Markdown sources and knowledge base. Unknown design names are errors rather than silent fallbacks.

## Consequences

### Positive

- separates factual content from presentation;
- supports safe experimentation without changing the global default;
- makes persistent job-specific branding possible;
- allows a new design to become the repository default explicitly;
- preserves ATS-safe and human-oriented variants as reusable templates.

### Negative

- every design must be tested for DOCX, PDF, ATS parsing, and visual quality;
- one-build overrides introduce state that generation must consume carefully;
- future designs may require additional rendering features or assets.

## Related Decisions

- [ADR 0003: Record Knowledge Before Generating Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
- [ADR 0015: Organize Targeted Applications by Company and Posting](0015-organize-targeted-applications-by-company-and-posting.md)
