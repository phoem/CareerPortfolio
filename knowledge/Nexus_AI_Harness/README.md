---
type: Personal Software Project
title: Nexus Agentic Operating System
description: Local-first control plane for permissioned AI agents, approval workflows, layered knowledge, and auditable task execution.
tags: [ai, agents, local-first, security, workflows, tauri, react, typescript, sqlite, mcp, personal-project]
generated:
  at: 2026-08-01T00:00:00Z
status: active
owner: Jordan Newman
evidence_status: confirmed
---

# Nexus Agentic Operating System

## Summary

Nexus is a local-first agentic operating system and control plane Jordan Newman is building for running AI agents with permissioned tools, human approval flows, layered knowledge, and auditable task execution. Its initial operating boundary uses SQLite and the local filesystem so core execution does not require a cloud dependency.

“Agentic operating system” describes a control plane and operating environment for agents; it is not a claim that Nexus is a hardware-hosting kernel or a replacement for Windows, macOS, or Linux.

## Personal Ownership

Jordan designed and is building Nexus. He also migrated its desktop shell from Electron to Tauri early in development.

## Core Engine and Workflow Runtime

- Task lifecycle state machine covering creation, planning, queuing, execution, completion, and failure.
- Audit logging for every task-state transition.
- Declarative YAML, DAG-oriented workflow definitions.
- Multi-agent execution with sub-tasks, parallel branches, conditional `when` guards, branching, and controlled loop-back constructs.
- Human approval engine with persisted approval records, response tracking, standing approvals, and conflict resolution.

## Default-Deny Permission System

Every tool call passes through permission evaluation that accounts for:

- tool category and `LOW`, `MEDIUM`, or `HIGH` risk classification;
- mandatory approval requirements;
- workspace-scoped grants;
- air-gapped network blocking;
- resource and path scoping, including canonical path resolution and symlink-traversal protection;
- agent-specific `permissions` and `tools` declarations in YAML.

## Tools and Connectors

Implemented tool categories include:

- filesystem reads and atomic writes using temporary-file replacement;
- approval-gated shell execution;
- database query and write operations;
- GitHub repository, issue, file, and pull-request operations;
- OAuth 2.0 Gmail and Calendar operations;
- structured code editing, Git commands, test execution, and builds;
- Open Knowledge Format reads, queries, and writes against per-repository `.nexus/knowledge/` bundles;
- per-workspace Graphify MCP server discovery and registration.

Tool access varies by risk and agent configuration. Filesystem access inside an approved workspace can be allowed by default, while high-risk operations such as shell execution require approval.

## Security and Audit Architecture

- Immutable `AuditLog` rows on terminal tool-call state changes.
- Persisted `Agent`, `Task`, `ToolCall`, `Approval`, and `Event` records with timestamps, actor identifiers, and client-type metadata.
- Secret references stored separately from secret values; values are resolved at execution time from operating-system keyring storage or external vaults.
- No prompt or response content stored in the model-usage ledger.

## Knowledge System

- Per-repository Open Knowledge Format bundles under `.nexus/knowledge/`.
- Scanning and synchronization into a central knowledge vault.
- Per-workspace Graphify MCP registration to synchronize the knowledge graph.
- Optional AI-driven enrichment that resolves placeholder concepts into detailed `.ai.md` files through the same model-provider abstraction used for agent tasks.

## Observability and Model Routing

- Model-invocation ledger tracking token use, latency, retry counts, errors, and estimated cost without retaining prompt or response content.
- Anthropic automatic prompt-caching support with configurable time-to-live behavior.
- Opt-in deterministic routing profiles with provider health and circuit breakers, budget-aware selection, failover policies, and a Web UI route simulator.

## Clients and User Experience

### Command-Line Client

The standalone `nexusctl` HTTP client can operate tasks, approvals, workflows, scheduled jobs, knowledge scanning and enrichment, configuration, model-routing simulation and health, and security simulation.

### Web Application

A React and Tailwind single-page application provides task creation, live server-sent events, approval cards, artifact panels, a workflow canvas, knowledge exploration, AI-usage statistics, configuration editing, and sidebar navigation.

### Desktop Application

The Tauri desktop application provides a system tray, workspace selection, notifications, operating-system keychain integration, local file and URL opening, and launch and supervision of the local Nexus Core process.

## Electron-to-Tauri Architecture Decision

Jordan replaced the original Electron shell with Tauri early in development because Tauri offered:

- a smaller application bundle;
- lower memory use and faster startup;
- a smaller runtime footprint;
- a stricter capability-based security model better aligned with Nexus's default-deny design.

## Confirmed Technologies and Protocols

- TypeScript;
- React and Tailwind CSS;
- Electron in the original desktop implementation;
- Tauri in the current desktop implementation;
- SQLite and the local filesystem;
- YAML workflow definitions;
- server-sent events;
- OAuth 2.0;
- MCP integrations;
- Open Knowledge Format bundles.

## Evidence Quality

- Jordan directly confirmed the implemented architecture and his ownership on 2026-08-01.
- Nexus is an active personal project; its production-user count, release status, public availability, repository visibility, supported operating systems, test coverage, and measured performance are not yet documented.
- Named model runtimes and ML frameworks must not be described as Nexus integrations until Jordan confirms the direct connection.
- The Tauri footprint, startup, memory, and security advantages explain the architecture decision; no project-specific before-and-after measurements are currently documented.

## Resume-Ready Descriptions

- Designing and building Nexus, a local-first agentic control plane with declarative multi-agent workflows, human approvals, default-deny tool permissions, layered knowledge, model routing, and auditable task execution.
- Built a React/Tailwind operations interface and Tauri desktop client with live event streaming, approval workflows, operating-system keychain integration, and local process supervision.
- Migrated the desktop shell from Electron to Tauri to reduce runtime and bundle footprint, improve startup behavior, and adopt a stricter capability-based security model.

## Related Concepts

- [Local AI and ML Experience](../Local_AI_ML_Experience/README.md)
- [Performance Profiling Experience](../Performance_Profiling_Experience/README.md)
- [Open Source Contributions](../Open_Source_Contributions/README.md)

## Open Questions

- Which local-model runtimes and ML frameworks are integrated directly into Nexus?
- What languages and major components make up Nexus Core and the model-provider layer?
- Is Nexus public, deployed, or used by anyone besides Jordan?
- Which operating systems are currently supported?
- Are there project-specific bundle-size, memory, startup, latency, test-coverage, or reliability measurements?
