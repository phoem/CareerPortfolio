# Jordan Newman - Generic Senior Software Engineer Resume

**Senior Software Engineer | Systems, Backend, Security, Infrastructure**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

*Selected public repositories are available. The most significant engineering repositories are private; access is available upon request.*

## Summary

Senior software engineer specializing in systems software, distributed infrastructure, networking, security, and performance engineering. Built production systems spanning high-performance HTTP/CDN serving, FreeBSD kernel modules, observability, deployment automation, and enterprise integrations. Combines deep C and operating-system expertise with modern cloud delivery, developer tooling, and agentic AI systems.

## Technical Skills
- **Languages:** C, C++, C#, Go, Python, Rust, TypeScript, JavaScript, Node.js, Shell, Objective-C, PHP, Perl, Visual Basic
- **Systems:** FreeBSD, Linux, kernel modules, system calls, operating systems, kqueue, sendfile(), GDB, TCP/IP, non-blocking I/O
- **Networking/Security:** HTTP, DNS, CDN architecture, socket programming, DDoS detection/mitigation, packet capture, libpcap, IPFW, authentication, telemetry
- **Cloud/DevOps:** Azure DevOps, Azure Pipelines, GitHub Actions, Docker, Kubernetes, Terraform, CI/CD, security scanning, deployment automation
- **AI/Developer Tooling:** LLM APIs and routing, MCP, agentic workflows, CLI tools, GitHub automation, auditable task execution
- **Databases/Web:** MySQL, MultiValue/Universe, OAuth/OAuth2, SMTP OAuth, React, jQuery, PHP, web services

## Selected Technical Highlights

- Built and operated infrastructure spanning approximately 3,000-4,000 servers, 10 CDN locations, and more than 65 Gbps of peak traffic.
- Designed the custom HTTP/CDN server and supporting software platform used for high-traffic production workloads.
- Built non-blocking event-driven systems around kqueue, zero-copy sendfile(), kernel-aware I/O, and dedicated disk I/O workers.
- Developed production FreeBSD kernel modules, DDoS mitigation systems, packet analyzers, DNS monitoring, authentication, and telemetry software.
- Built Nexus, a local-first agentic control plane with LLM routing, MCP integrations, declarative workflows, permissioned tools, and auditable task state.

## Selected Systems Projects

- **PrimeHTTPD:** Built a non-blocking C/FreeBSD HTTP/CDN server using `kqueue`, `sendfile()`, persistent connections, caching, and specialized I/O workers.
- **VirtualDir:** Built a FreeBSD kernel module that transparently remapped filesystem paths from runtime configuration; included the `vdcli` management tool.
- **PrimeDump:** Built a libpcap-based real-time traffic analyzer decoding Ethernet, IP, TCP, UDP, and ICMPv6 with ncurses views and IPFW integration.
- **PrimeDNSTop:** Built a DNS traffic monitor parsing UDP/53 and RFC 1035 queries to detect recursion attacks and rank source and domain activity.
- **Nexus:** Building a local-first agentic control plane with LLM routing, MCP integrations, declarative workflows, permissioned tools, and auditable task state.

## Professional Experience

### Advantive - Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Serve on the Architecture Team, contributing to technical decisions, engineering standards, shared libraries, platform direction, and documentation.
- Support about 12 teams with reusable Azure Pipelines, templates, deployment gates, and self-hosted runners that reduce manual work and enable quicker releases.
- Implement and improve Docker, Kubernetes, Terraform, CI/CD, security-scanning, developer-tooling, and AI-assisted engineering workflows.

### DDI Systems - Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPrime LLC - CEO
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI Systems - Computer Programmer
*Manalapan, NJ | April 2017 - March 2018*

- Built ERP integrations and automated order, catalog, image, SDS, SFTP, SellerCloud, Essendant, and MultiValue/Universe data workflows.

### Too Much Media LLC - Computer Programmer
*Morganville, NJ | January 2016 - April 2017*

- Developed real-time browser chat integrated with ticketing systems and implemented OAuth 2.0 authorization for protected sites.

### MFCXY, Inc. - Computer Programmer
*Chicago, IL | December 2014 - September 2015*

- Developed backend and Windows client features and middleware for cross-platform database migration.

### AJPM, LLC - Programmer / Owner
*New Jersey / Remote | November 2012 - December 2013*

- Built automated purchasing, inventory, repair, resale, and financial workflow software.

### ISPrime Inc. - CIO / Partner
*Weehawken, NJ | January 2001 - December 2014*

**Infrastructure Leadership**
- Architected and operated hosting and CDN infrastructure spanning approximately 3,000-4,000 servers, 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Led major technical projects and as many as 10 employees, taking unclear problems through architecture, hands-on implementation, and production operation.

**Systems Software Engineering**
- Designed and built PrimeHTTPD, a high-performance, non-blocking, kqueue-based HTTP/CDN server in C for FreeBSD; deployed it across approximately 200 servers and supported more than 150,000 concurrent connections.
- Leveraged sendfile(), SF_NODISKIO, TCP_NODELAY, TCP_NOPUSH, O_NONBLOCK, accept_filter_http, persistent connections, and dedicated I/O workers to keep disk operations from blocking the networking event loop.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.

**Security and Networking**
- Built DDoS defenses, packet and DNS analysis, authentication, deployment, and production health-check and monitoring software including `sitecheck`, `slugd`, and `php-seclogd`.

### FatWallet.com - Systems Administrator
*Wisconsin / Remote | December 2000 - June 2001*

- Rebuilt production infrastructure to resolve performance and stability issues without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** - Computer Science coursework; left during first semester to pursue ISPrime full-time during rapid company growth.
