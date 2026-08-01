# Jordan Newman

**Software Engineer | Desktop Products, Systems, Agentic AI**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | github.com/phoem  
Willing and able to work in person in New York City

## Summary

Product-minded senior software engineer with more than 20 years of experience working across application interfaces, backend systems, operating systems, security, and production infrastructure. Currently building Nexus, a local-first agentic control plane with a React Web UI, Tauri desktop client, multi-agent workflows, default-deny tool permissions, human approvals, layered knowledge, and auditable execution. Combines hands-on React, TypeScript, Electron, Tauri, C#, C++, and C experience with deep system-design and performance-engineering judgment. Two-plus years of hands-on ML-framework and local-model experimentation, including LM Studio, llama.cpp, Ollama, and LM Studio Bionic.

## Technical Skills

- **Application Engineering:** React, TypeScript, Tailwind CSS, Tauri, Electron, C#, C++, C, Rust, Python, Objective-C, desktop applications, cross-stack development
- **Agentic AI and Local Models:** agent workflows, tool calling, human-in-the-loop approvals, model routing, MCP, LM Studio, llama.cpp, Ollama, LM Studio Bionic, MLX, Hugging Face Transformers, TensorFlow
- **Systems and Data:** Linux, FreeBSD, SQLite, local-first architecture, process supervision, server-sent events, HTTP, TCP/IP, non-blocking I/O, MultiValue/UniVerse
- **Security and Delivery:** default-deny permissions, OAuth 2.0, operating-system keyrings, audit logging, GitHub, CI/CD, Docker, Kubernetes, Terraform, Azure DevOps
- **Debugging and Performance:** GDB, Valgrind, Linux perf, CPU profiling and optimization, system design, architecture

## Selected Product and Systems Engineering

### Nexus Agentic Operating System — Creator and Engineer
*Active personal project*

- Designing and building a local-first control plane for permissioned AI agents; task execution, approval state, audit records, and layered knowledge remain on the user's machine through SQLite and the local filesystem before any cloud dependency is introduced.
- Built a declarative YAML, DAG-oriented workflow runtime supporting sub-tasks, parallel agents, conditional branches, controlled loop-back execution, and a full task state machine with audit logging on every transition.
- Engineered default-deny tool execution around risk levels, mandatory and standing approvals, workspace-scoped grants, air-gapped network controls, canonical path resolution, and symlink-traversal protection.
- Delivered a React/Tailwind operations interface with live server-sent events, task and approval experiences, artifact views, workflow canvas, knowledge explorer, AI-usage statistics, model-routing simulation, and configuration editing.
- Built the Tauri desktop client with system-tray controls, workspace selection, notifications, keychain-backed secret handling, file and URL opening, and local process supervision; migrated from Electron for a smaller footprint, faster startup, lower memory use, and stricter capability-based security.
- Implemented deterministic model-routing profiles with health checks, circuit breakers, budget-aware selection, failover, prompt caching, and a privacy-conscious invocation ledger tracking tokens, latency, retries, errors, and estimated cost without retaining prompt or response content.

### Open-Source Engineering

- Contributed a merged Rust Azure Key Vault provider to `cachix/secretspec`, implementing multiple Azure authentication modes, validation, feature-gated integration tests, sovereign-cloud support, documentation, and maintainer-review fixes across 14 changed files.

### PrimeHTTPD and CDN Platform

- Architected and implemented a high-performance HTTP/CDN server in C for FreeBSD, combining a single-process `kqueue` networking core with dedicated workers for blocking disk I/O, Unix descriptor passing, shared-memory scheduling, and zero-copy `sendfile()` transfers.
- Deployed PrimeHTTPD across approximately 200 servers supporting more than 150,000 concurrent connections as part of infrastructure spanning approximately 3,000-4,000 servers, 10 locations, and more than 65 Gbps of peak traffic.

## Professional Experience

### Advantive — Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Contribute to Architecture Team decisions, engineering standards, platform direction, reusable libraries, documentation, developer tooling, and AI-assisted engineering workflows.
- Implement and improve Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, and security-scanning workflows across engineering teams.

### DDI System — Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Developed and maintained Inform's primarily C# desktop applications, including WebCom and PrintCom connectivity to a UniVerse database backend.
- Added OAuth 2.0 support for email and implemented SellerCloud and product-catalog integrations.

### ISPRIME — Chief Executive Officer
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI System — Computer Programmer
*Manalapan, NJ | April 2017 - March 2018*

- Built ERP integrations and automated order, catalog, image, safety-data, SFTP, SellerCloud, supplier, and MultiValue/UniVerse workflows.

### Too Much Media LLC — Computer Programmer
*Morganville, NJ | January 2016 - April 2017*

- Developed real-time browser chat integrated with ticketing workflows and implemented OAuth 2.0 authorization for protected customer sites.

### MFCXY, Inc. — Computer Programmer
*Chicago, IL | December 2014 - September 2015*

- Developed backend and Windows desktop-client features plus middleware for cross-platform database migration.

### ISPRIME — Owner and CIO
*Weehawken, NJ | January 2001 - December 2014*

- Architected and operated the production hosting and CDN platform and personally built its HTTP serving, kernel, networking, security, monitoring, authentication, and operational software.
- Created employee training documentation, trained the majority of employees over the years, and personally mentored two beginners over several years into technical experts and eventual company leaders.

## Additional Experience

**AJPM, LLC — Programmer / Owner** | November 2012 - December 2013  
**FatWallet.com — Systems Administrator** | December 2000 - June 2001

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPRIME full-time during rapid company growth.
