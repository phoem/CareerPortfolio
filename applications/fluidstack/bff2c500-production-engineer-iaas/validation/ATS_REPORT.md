# ATS Readiness Report

- **Validated:** 2026-08-13T06:05:44+00:00
- **Validator:** CareerPortfolio ATS Validator v0.2.2
- **Score type:** Targeted readiness
- **Overall score:** 64/100
- **Disposition:** Not Ready
- **Autonomous revision pass:** 0 of 3

## Category Scores

| Category | Score | Weight |
|---|---:|---:|
| Artifact parseability and structure | 100 | 25% |
| Required-information completeness | 100 | 10% |
| Required job-requirement evidence | 16 | 30% |
| Preferred job-requirement evidence | 42 | 15% |
| Language and keyword quality | 80 | 10% |
| Human readability and positioning | 97 | 10% |

## Critical Failures

- None detected.

## Artifact parseability and structure

- DOCX token coverage versus Markdown: 99.3%.
- PDF token coverage versus Markdown: 99.3%.

## Required-information completeness

- Contact details, conventional sections, and work-history dates are present.

## Required job-requirement evidence

- Missing: You treat toil as a bug. If something requires a human to do it twice, you build the thing that makes it not require a human. (matched: human, build).
- Missing: You design APIs that age well. You've felt the pain of a leaky abstraction at scale and you don't repeat it. (matched: design, apis).
- Missing: You move toward ambiguity, not away from it. You walk into the fog, build the map, and explain it to everyone else. (matched: into, build).
- Missing: You learn at a steep slope. You reach real competence in an unfamiliar domain fast. We value this over existing expertise. (matched: real).
- Missing: You carry a pager without flinching. You run the incident, write the postmortem, fix the systemic cause, and move on. (matched: without, incident).
- Adjacent: You're fluent with AI tooling. LLM APIs, MCP servers, and agentic frameworks, and you drive Claude Code, Cursor, or similar every day. (matched: ai, llm, apis, mcp, servers, agentic, frameworks, code).
- Adjacent: You've shipped production services that other teams depend on at scale, and you're comfortable in any language using AI coding tools. (matched: production, teams, ai, tools.).

## Preferred job-requirement evidence

- Direct: Distributed systems and data pipeline engineering. (matched: distributed, systems, data, pipeline).
- Missing: Time-series observability stacks (Prometheus, Thanos, VictoriaMetrics). (matched: observability).
- Adjacent: API design and versioning at scale. (matched: api, design).
- Missing: Workflow and orchestration engines (Temporal, Cadence). (matched: workflow).
- Missing: BMC/Redfish or hardware telemetry. (matched: none).
- Direct: Go, Python, and Postgres. (matched: go, python).

## Language and keyword quality

- Qualification-language token coverage: 22.2%.

## Human readability and positioning

- 1 bullets are long enough to hinder scanning.

## Requirement-to-Evidence Matrix

| Type | Strength | Requirement | Matched terms |
|---|---|---|---|
| Required | Missing | You treat toil as a bug. If something requires a human to do it twice, you build the thing that makes it not require a human. | human, build |
| Required | Missing | You design APIs that age well. You've felt the pain of a leaky abstraction at scale and you don't repeat it. | design, apis |
| Required | Missing | You move toward ambiguity, not away from it. You walk into the fog, build the map, and explain it to everyone else. | into, build |
| Required | Missing | You learn at a steep slope. You reach real competence in an unfamiliar domain fast. We value this over existing expertise. | real |
| Required | Missing | You carry a pager without flinching. You run the incident, write the postmortem, fix the systemic cause, and move on. | without, incident |
| Required | Adjacent | You're fluent with AI tooling. LLM APIs, MCP servers, and agentic frameworks, and you drive Claude Code, Cursor, or similar every day. | ai, llm, apis, mcp, servers, agentic, frameworks, code |
| Required | Adjacent | You've shipped production services that other teams depend on at scale, and you're comfortable in any language using AI coding tools. | production, teams, ai, tools. |
| Preferred | Direct | Distributed systems and data pipeline engineering. | distributed, systems, data, pipeline |
| Preferred | Missing | Time-series observability stacks (Prometheus, Thanos, VictoriaMetrics). | observability |
| Preferred | Adjacent | API design and versioning at scale. | api, design |
| Preferred | Missing | Workflow and orchestration engines (Temporal, Cadence). | workflow |
| Preferred | Missing | BMC/Redfish or hardware telemetry. | None |
| Preferred | Direct | Go, Python, and Postgres. | go, python |

## Artifact Versions

- `resume`: `9eab38f266eda7619c903c41432ac5d536932c5be0e764e7df3870d175bc3c86`
- `docx`: `709fd25190b5d1c4d97097db0a3fb4de0265abb12355eadfabd0b549a3d76500`
- `pdf`: `81a1e8a547557b0973120cc5ea30768f5807e143f7f1cb0ec8532724c57f2544`
- `job`: `519df57152a39adc8c59e4217326bcea0146ac3c1570a26e06189554a3dcef03`

## Recommended Next Action

- Revise the lowest-scoring fixable categories, regenerate artifacts, and rerun validation. Stop after three autonomous passes or earlier when a stop condition is reached.
