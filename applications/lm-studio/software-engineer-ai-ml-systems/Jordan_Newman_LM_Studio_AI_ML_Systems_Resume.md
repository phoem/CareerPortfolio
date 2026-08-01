# Jordan Newman

**Systems Software Engineer | Local AI, Runtimes, Operating Systems**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | github.com/phoem  
Willing and able to work in person in New York City

## Summary

Systems software engineer with more than 20 years centered on C; C++ has been used across that career, and periodic Python use spans approximately 20 years. Built production native runtimes, FreeBSD kernel modules, an x86 operating-system kernel, network software, and high-scale infrastructure. Brings 2+ years of hands-on experience with machine learning frameworks and model inference. This work is primarily through personal projects and includes local LLM experimentation with LM Studio, llama.cpp, Ollama, and LM Studio Bionic. Currently building Nexus, a local-first agentic control plane with TypeScript, model routing, observability, secure tools, React and Tauri clients, and auditable execution. Offers a strong understanding of operating systems and software system design, with proven problem-solving and communication skills plus deep CPU profiling, debugging, and performance expertise.

## Technical Skills

- **Languages:** C, TypeScript, Rust, C#, assembly, Go, JavaScript, Shell; long-term experience with C++ and Python.
- **Local AI and ML:** LM Studio, llama.cpp, Ollama, LM Studio Bionic; familiarity with MLX, TensorFlow, Hugging Face Transformers, and CUDA
- **Runtime and Operating Systems:** FreeBSD, Linux, x86 kernel development, system calls, processes, shared memory, Unix descriptor passing, `kqueue`, non-blocking I/O, `sendfile()`
- **Debugging and Performance:** GDB, Valgrind, Linux perf, CPU profiling and optimization, event-driven systems, concurrency, zero-copy I/O
- **Application and Platform:** React, TypeScript, Tauri, Electron, SQLite, server-sent events, MCP, Docker, Kubernetes, Terraform, Azure DevOps, CI/CD
- **Networking:** TCP/IP, HTTP, DNS, sockets, BGP4, NetFlow, packet capture, CDN architecture

## Selected AI, Runtime, and Systems Engineering

### Nexus Agentic Operating System — Creator and Engineer
*Active personal project*

- Designing a local-first agent control plane that persists tasks, approvals, audit records, and layered knowledge in SQLite and the local filesystem before introducing cloud dependencies.
- Implemented deterministic model-routing profiles with health checks, circuit breakers, budget-aware provider selection, failover, and Anthropic prompt caching.
- Built a privacy-conscious model-invocation ledger tracking tokens, latency, retries, errors, and estimated cost without retaining prompt or response content.
- Developed declarative YAML, DAG-oriented multi-agent workflows with parallel execution, conditional branches, controlled loop-back behavior, and audited task-state transitions.
- Engineered default-deny tool permissions using risk classification, human approvals, workspace grants, air-gapped network controls, canonical paths, and symlink-traversal protection.
- Built React/Tailwind and Tauri interfaces for a cohesive user and developer experience, including live events, approvals, routing simulation, usage statistics, keychain-backed secrets, and process supervision.

### PrimeHTTPD and Production CDN Runtime

- Architected PrimeHTTPD, a non-blocking HTTP/CDN runtime in C for FreeBSD with a single-process `kqueue` networking core and dedicated workers for blocking disk operations.
- Used Unix descriptor passing, `mmap()` shared worker state, least-busy scheduling, descriptor and gzip caches, and zero-copy `sendfile()` with `SF_NODISKIO` to protect the event loop from blocking I/O.
- Deployed the runtime across approximately 200 servers supporting more than 150,000 concurrent connections within infrastructure spanning 3,000-4,000 servers, 10 locations, and over 65 Gbps.
- Profiled and optimized CPU usage in systems software using GDB, Valgrind, Linux perf, and other native debugging and performance tools.

### Operating-System and Kernel Engineering

- Built TAFOS, an educational x86 kernel in C and assembly with an MBR bootloader, protected mode, interrupt descriptor table, heap allocator, port I/O, VGA output, and GDB support.
- Developed production FreeBSD kernel modules for transparent filesystem-path virtualization, execution monitoring, system protection, telemetry, and syscall instrumentation.

### Open-Source Engineering

- Contributed a merged Rust Azure Key Vault provider to `cachix/secretspec`, implementing authentication modes, validation, feature-gated integration tests, sovereign-cloud support, documentation, and maintainer-review fixes.

## Professional Experience

### Advantive — Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Contribute to Architecture Team decisions, software-system design, engineering standards, platform direction, shared libraries, documentation, developer tooling, and AI-assisted engineering workflows.
- Implement and improve Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, and security-scanning workflows across engineering teams.

### DDI System — Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Developed primarily C# desktop applications and UniVerse database connectivity; added OAuth 2.0 email support plus SellerCloud and product-catalog integrations.

### ISPRIME — Chief Executive Officer
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### Earlier Software Engineering

**DDI System — Computer Programmer** | April 2017 - March 2018  
Built ERP integrations and automated order, catalog, image, safety-data, SFTP, supplier, SellerCloud, and MultiValue/UniVerse workflows.

**Too Much Media LLC — Computer Programmer** | January 2016 - April 2017  
Developed real-time browser chat integrated with ticketing and implemented OAuth 2.0 authorization for protected customer sites.

**MFCXY, Inc. — Computer Programmer** | December 2014 - September 2015  
Developed backend and Windows desktop-client features plus middleware for cross-platform database migration.

### ISPRIME — Owner and CIO
*Weehawken, NJ | January 2001 - December 2014*

- Architected and operated production hosting and CDN infrastructure and personally built its HTTP serving, kernel, networking, security, monitoring, authentication, and operational software.
- Created technical training documentation, trained the majority of employees over the years, and mentored two beginners over several years into technical experts and company leaders.

## Additional Experience

**AJPM, LLC — Programmer / Owner** | November 2012 - December 2013  
**FatWallet.com — Systems Administrator** | December 2000 - June 2001

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPRIME full-time during rapid company growth.
