# Jordan Newman

**Systems & Infrastructure Engineer | Compute Platforms, Networking, Reliability**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

*Selected public repositories are available. The most significant engineering repositories are private; access is available upon request.*

## Summary

Systems software and infrastructure engineer with deep experience building and operating distributed production platforms, high-performance network services, observability systems, developer tooling, and agent infrastructure. Architected and operated infrastructure spanning approximately 3,000-4,000 servers, 10 locations, and more than 65 Gbps of peak traffic. Built a C/FreeBSD HTTP/CDN runtime deployed across approximately 200 servers and supporting more than 150,000 concurrent connections. Brings comfort with ambiguity, strong ownership, and a bias toward practical, durable solutions. Interested in building infrastructure that directly enables frontier AI research and product impact.

## Technical Skills

- **Systems & Performance:** C, C++, FreeBSD, Linux, operating systems, kernel modules, system calls, `kqueue`, `sendfile()`, shared memory, descriptor passing, non-blocking I/O, GDB, Valgrind, Linux `perf`
- **Networking & Reliability:** TCP/IP, HTTP, DNS, BGP4, CDN architecture, socket programming, packet capture, libpcap, NetFlow, SNMP, IPFW, DDoS mitigation, observability, incident diagnosis
- **Infrastructure & Platforms:** Distributed systems, storage I/O, Docker, Kubernetes, Terraform, Azure DevOps, Azure Pipelines, GitHub Actions, CI/CD, deployment automation, security scanning
- **Agent & Developer Infrastructure:** TypeScript, Node.js, Python, Go, Rust, LLM routing, Model Context Protocol (MCP), declarative DAG workflows, permissioned tools, human approvals, CLI tools, APIs, audit trails
- **Additional Languages & Data:** C#, JavaScript, Shell, Objective-C, PHP, Perl, Visual Basic, MySQL, MultiValue/Universe

## Selected Infrastructure Highlights

- Architected and operated 24/7 hosting and CDN infrastructure spanning approximately 3,000-4,000 servers, 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Designed and deployed PrimeHTTPD, a high-performance C/FreeBSD HTTP/CDN runtime, across approximately 200 production servers supporting more than 150,000 concurrent connections.
- Built event-driven networking, kernel-assisted zero-copy I/O, worker scheduling, descriptor-passing, shared-memory telemetry, caching, authentication, request routing, and operational reload capabilities.
- Designed production packet, DNS, NetFlow, BGP, DDoS, monitoring, health-check, deployment, authentication, and security systems for large-scale infrastructure operations.
- Built Nexus, a local-first agentic control plane with sandboxed task workspaces, default-deny tool permissions, declarative workflows, human approval gates, model routing, and auditable execution state.
- Support about 12 engineering teams with reusable Azure Pipelines, templates, deployment gates, and self-hosted runners that reduce manual work and enable quicker releases.

## Selected Systems Projects

### PrimeHTTPD — High-Concurrency C/FreeBSD Runtime

- Built a non-blocking HTTP/CDN server around one primary `kqueue` process, keeping latency-sensitive connection handling in the event loop.
- Delegated potentially blocking file operations and disk-backed transfers to configurable workers.
- Passed jobs, files, and client sockets with `sendmsg()` descriptor passing; shared worker state through `mmap()` and assigned work to the least-busy worker.
- Used `sendfile()`, `SF_NODISKIO`, `TCP_NODELAY`, `TCP_NOPUSH`, `O_NONBLOCK`, and FreeBSD HTTP accept filters to optimize host, network, and storage-I/O behavior.
- Implemented persistent connections, descriptor and gzip caches, chunked encoding, ETags, conditional requests, authentication, wildcard and PCRE2 rewrites, and signal-driven configuration reloads.

### Nexus — Agent Infrastructure and Developer Platform

- Designed and built a TypeScript local-first control plane for agentic workloads with DAG workflows, LLM routing, MCP integrations, permissioned tools, human approvals, scheduled execution, and an append-only audit trail.
- Implemented sandboxed task workspaces, per-task permissions and budgets, SQLite/local-filesystem state, live event streaming, a CLI, React operations interface, and Tauri desktop client.

### Network, Fleet Observability, and Kernel Systems

- Built PrimeDump and PrimeDNSTop with libpcap for packet- and DNS-level visibility, including Ethernet/IP/TCP/UDP/ICMPv6 decoding, RFC 1035 query parsing, source/domain ranking, recursion-attack detection, and IPFW mitigation workflows.
- Built PrimeFlow for NetFlow v5 collection and PrimeBGP for BGP4 systems work; developed production health-check and monitoring software including `sitecheck`, `slugd`, and `php-seclogd`.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache; profiled and optimized CPU-intensive systems using GDB, Valgrind, and Linux `perf`.

## Professional Experience

### Advantive — Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Serve on the Architecture Team, contributing to technical decisions, engineering standards, shared libraries, platform direction, developer tooling, and documentation.
- Support about 12 teams with reusable Azure Pipelines, templates, deployment gates, and self-hosted runners that reduce manual work, save developer time, and enable quicker releases.
- Implement and improve Docker, Kubernetes, Terraform, CI/CD, security-scanning, and AI-assisted engineering workflows.

### DDI Systems — Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPrime LLC — CEO
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI Systems — Computer Programmer
*Manalapan, NJ | April 2017 - March 2018*

- Built ERP integrations and automated order, catalog, image, SDS, SFTP, SellerCloud, Essendant, and MultiValue/Universe data workflows.

### Too Much Media LLC — Computer Programmer
*Morganville, NJ | January 2016 - April 2017*

- Developed real-time browser chat integrated with ticketing systems and implemented OAuth 2.0 authorization for protected sites.

### MFCXY, Inc. — Computer Programmer
*Chicago, IL | December 2014 - September 2015*

- Developed backend and Windows client features and middleware for cross-platform database migration.

### AJPM, LLC — Programmer / Owner
*New Jersey / Remote | November 2012 - December 2013*

- Built automated purchasing, inventory, repair, resale, and financial workflow software.

### ISPrime Inc. — CIO / Partner
*Weehawken, NJ | January 2001 - December 2014*

- Led major technical projects and as many as 10 employees, taking unclear problems through architecture, hands-on implementation, production operation, and long-term improvement.
- Architected and operated hosting, CDN, network, and datacenter infrastructure spanning approximately 3,000-4,000 servers, 10 locations, and more than 65 Gbps of peak traffic.
- Helped design and operate multi-provider transit, direct and exchange peering, and private inter-PoP fiber connectivity.
- Designed and built PrimeHTTPD and its network core, I/O workers, scheduling protocol, shared-memory telemetry, kernel-assisted transfers, caches, authentication, routing, and HTTP features.
- Built DDoS defenses and packet, DNS, BGP, NetFlow, monitoring, health-check, deployment, authentication, and security tooling for demanding 24/7 production operations.
- Diagnosed complex behavior across operating-system, storage, networking, and workload layers, turning operational findings into durable systems and clearer abstractions.

### FatWallet.com — Systems Administrator
*Wisconsin / Remote | December 2000 - June 2001*

- Rebuilt production infrastructure to resolve performance and stability problems without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPrime full-time during rapid company growth.
