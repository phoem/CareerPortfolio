# Jordan Newman

**Software Engineer | Research Infrastructure, Distributed Systems, Platform Architecture**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

## Summary

Hands-on software architect and infrastructure engineer with 20+ years of experience designing, building, and operating production distributed systems. Architected 24/7 infrastructure spanning approximately 3,000-4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic. Personally built a high-concurrency C/FreeBSD runtime from first principles and took it through production at scale. Combines low-level systems depth with current architecture-team work in shared platforms, developer tooling, infrastructure as code, CI/CD, and AI-assisted engineering workflows.

## Core Capabilities

- **Infrastructure and architecture:** Distributed systems, production infrastructure, platform engineering, reliability, scalability, observability, developer tooling, infrastructure as code
- **Systems engineering:** C, C++, Go, Python, FreeBSD, Linux, kernel modules, system calls, `kqueue`, shared memory, inter-process communication, non-blocking I/O, GDB
- **Networking and operations:** TCP/IP, HTTP, DNS, CDN architecture, socket programming, packet analysis, libpcap, IPFW, DDoS detection and mitigation, incident diagnosis
- **Modern delivery:** Terraform, Kubernetes, Docker, Azure DevOps, CI/CD, deployment automation, security scanning, C#

## Selected Impact

- Architected and operated a multi-location hosting and CDN platform spanning approximately 3,000-4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic.
- Designed and implemented PrimeHTTPD, a production event-driven HTTP/CDN runtime in C for FreeBSD, deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
- Established a non-blocking runtime architecture using one primary `kqueue` process, configurable I/O workers, `sendmsg()` descriptor passing, shared `mmap()` worker state, least-busy-worker dispatch, and `sendfile()` with `SF_NODISKIO`.
- Built the monitoring, telemetry, deployment, authentication, packet/DNS analysis, security, and DDoS systems needed to operate and defend customer-facing infrastructure around the clock.

## Independent Delivery and Technical Leadership

- Independently scoped and delivered complex technical projects from initial requirements and architecture through hands-on coding, production deployment, and long-term operation.
- Make architectural decisions and define engineering standards, shared libraries, and platform direction that other engineers and teams build upon.
- Use written technical documentation and cross-team collaboration to communicate decisions and establish alignment across engineering teams.
- Operated effectively in fast-changing startup environments with high autonomy and ownership, combining executive accountability with hands-on systems engineering during rapid company growth.

## Selected Systems Engineering

- **PrimeHTTPD:** Built persistent connections, descriptor and gzip caches, chunked encoding, ETags, conditional requests, authentication integration, and signal-driven configuration reloads around a high-concurrency event core.
- Added wildcard and PCRE2 request rewriting and integrated the runtime with PrimeAuth for HTTP Basic and cookie authentication.
- **VirtualDir:** Designed and developed a production FreeBSD kernel module and management utility that intercepted filesystem-related system calls and transparently remapped paths.
- Enabled shared physical layouts without chroot jails; deployed VirtualDir on approximately 30 servers for approximately 5-8 years.
- **PrimeDump and PrimeDNSTop:** Built libpcap-based packet and DNS analysis tools that decoded Ethernet, IP, TCP, UDP, ICMPv6, and RFC 1035 traffic for troubleshooting, abnormal-activity detection, and DDoS investigation.
- **KeepClean and StatCache:** Developed production FreeBSD kernel modules for execution monitoring, system-asset protection, user-space telemetry, and filesystem performance instrumentation.
- **TAFOS:** Developed an educational x86 operating-system kernel in C and assembly with a custom MBR bootloader, protected-mode transition, interrupt descriptor table, heap allocator, port I/O, VGA output, and GDB debugging.

## Professional Experience

### Advantive - Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Serve on the Architecture Team, collaborating on technical decisions, engineering standards, platform direction, shared libraries, documentation, and developer tooling used across engineering teams.
- Implement and improve Terraform, Kubernetes, Docker, Azure DevOps, CI/CD, security-scanning, and AI-assisted engineering workflows that support shared platform delivery.

### DDI System - Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPRIME - Chief Executive Officer
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### ISPRIME - Owner and CIO
*Weehawken, NJ | January 2001 - December 2014*

- Held architectural and operational responsibility for a 24/7 distributed hosting and CDN platform spanning approximately 3,000-4,000 servers, about 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Personally architected and implemented PrimeHTTPD in C for FreeBSD, delivering the serving runtime from first-principles design through production deployment across approximately 200 servers.
- Kept latency-sensitive networking non-blocking with `kqueue`, HTTP accept filters, persistent connections, and kernel-assisted `sendfile()` transfers; delegated file opens and disk-backed sends to configurable worker processes.
- Designed the worker protocol around Unix-domain `sendmsg()` descriptor passing and shared `mmap()` activity state, enabling least-busy-worker assignment and operational visibility.
- Implemented descriptor and gzip caches, chunked encoding, ETags, conditional requests, authentication integration, wildcard/PCRE2 rewrites, and signal-driven configuration reloads.
- Developed production FreeBSD kernel modules, including VirtualDir for transparent filesystem path virtualization, plus packet and DNS analysis tools used for troubleshooting and attack investigation.
- Built monitoring, telemetry, authentication, deployment, infrastructure-management, DDoS detection and mitigation, and security software in response to production operational needs.
- Acted as a technical lead and mentor across ISPRIME, creating internal training documentation and training most employees; personally guided two beginners over several years into technical experts and eventual company leaders.

### Earlier Software and Systems Experience

- **DDI System - Computer Programmer** | Manalapan, NJ | April 2017 - March 2018: Built ERP integrations and automated order, catalog, image, SDS, SFTP, SellerCloud, Essendant, and MultiValue/Universe workflows.
- **Too Much Media LLC - Computer Programmer** | Morganville, NJ | January 2016 - April 2017: Developed real-time browser chat integrated with ticketing and implemented OAuth 2.0 authorization.
- **MFCXY, Inc. - Computer Programmer** | Chicago, IL | December 2014 - September 2015: Developed backend and Windows-client features and cross-platform database-migration middleware.
- **AJPM, LLC - Programmer / Owner** | New Jersey / Remote | November 2012 - December 2013: Built software for purchasing, inventory, repair, resale, and financial workflows.
- **FatWallet.com - Systems Administrator** | Wisconsin / Remote | December 2000 - June 2001: Rebuilt production infrastructure to resolve performance and stability problems without customer-facing downtime and added automated availability and health alerting.

## Education

**Brookdale Community College** - Computer Science coursework; left during the first semester to pursue ISPRIME full-time during rapid company growth.
