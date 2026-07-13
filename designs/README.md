# Resume Designs

The `designs/` directory stores reusable rendering templates and the repository default design.

## Default design

`designs/default.json` selects the design used when no more-specific override exists.

```json
{
  "design": "classic-ats"
}
```

Each named design lives in `designs/<design-name>/design.json` and may later include supporting assets, templates, examples, or implementation files.

## Application-level selection

Each application package may contain either or both of these files:

- `DESIGN.json` — persistent override used for every future rebuild of that application.
- `DESIGN_NEXT.json` — one-build override used only for the next successful generation; it takes precedence over `DESIGN.json` and is removed after generation.

Example persistent override:

```json
{
  "design": "classic-ats",
  "scope": "persistent",
  "applies_to": ["resume", "cover_letter"]
}
```

Example one-build override:

```json
{
  "design": "modern-light",
  "scope": "next-build",
  "applies_to": ["resume"]
}
```

## Resolution order

1. `DESIGN_NEXT.json` in the application directory.
2. `DESIGN.json` in the application directory.
3. `designs/default.json`.

A design override must name an existing directory under `designs/`. Unknown designs are errors; the generator must not silently fall back to another design.

Generic resumes use the repository default until per-resume overrides are implemented.
