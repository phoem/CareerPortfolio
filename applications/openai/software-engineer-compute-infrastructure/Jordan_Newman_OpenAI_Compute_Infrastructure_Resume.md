# Jordan Newman

**Systems Software Engineer | Compute Infrastructure, Networking, Reliability**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | github.com/phoem  
*Selected public repositories are available. The most significant engineering repositories are private; access is available upon request.*

## Summary

Systems software and infrastructure engineer with deep experience building and operating production runtimes, networking platforms, kernel software, observability tools, and automation. Architected infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic. Built a high-concurrency FreeBSD HTTP/CDN runtime in C with event-driven networking, inter-process descriptor passing, shared-memory worker scheduling, kernel-assisted zero-copy I/O, caching, and production authentication and routing features. Combines low-level implementation depth with long-term ownership of demanding 24/7 infrastructure.

## Technical Skills

- **Languages:** C, C++, Go, Python, C#, Objective-C, PHP, Perl, JavaScript, Node.js, Shell, Visual Basic
- **Systems:** FreeBSD, Linux, operating-system internals, kernel modules, system calls, kqueue, mmap, signals, sendmsg(), sendfile(), GDB, non-blocking I/O
- **Networking:** TCP/IP, HTTP, DNS, CDN architecture, socket programming, packet capture, libpcap, IPFW, DDoS detection and mitigation
- **Infrastructure:** Distributed systems, production reliability, observability, incident diagnosis, deployment automation, Docker, Kubernetes, Terraform, Azure DevOps, CI/CD
- **Platforms and Security:** Authentication systems, OAuth/OAuth2, security scanning, telemetry, MySQL, MultiValue/Universe

## Selected Technical Highlights

- Architected and operated multi-location hosting and CDN infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic.
- Designed and deployed PrimeHTTPD, a custom event-driven HTTP/CDN runtime in C for FreeBSD, across approximately 200 production servers supporting more than 150,000 concurrent connections.
- Kept the latency-sensitive networking path in one main process and delegated only potentially blocking disk operations to a configurable pool of I/O workers.
- Built inter-process job dispatch and file/socket descriptor transfer with `sendmsg()`, allowing worker processes to perform blocking opens or disk-backed sends and return descriptor ownership when complete.
- Used a primary `kqueue`, HTTP accept filtering, persistent connections, non-blocking sockets, `sendfile()`, and `SF_NODISKIO` to minimize blocking, copies, context switching, and per-connection overhead.
- Implemented shared `mmap()` worker-state telemetry and least-busy-worker assignment, giving the main process continuous visibility into worker activity.
- Built file-descriptor and in-memory gzip caches plus chunked encoding, ETags, conditional GETs, hot configuration reloads, authentication integration, and wildcard/PCRE2 rewrite support.
- Developed packet, DNS, monitoring, deployment, authentication, security, and DDoS systems used to operate and defend 24/7 production infrastructure.
- Implemented Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, security-scanning, shared-library, and AI-assisted engineering workflows in modern enterprise environments.

## Selected Systems Projects

### PrimeHTTPD

High-performance, non-blocking HTTP and CDN server written in C for FreeBSD.

- Designed around one main event-driven process with a primary `kqueue`; only the main process accepted connections.
- Used FreeBSD HTTP accept filtering so accept readiness was reported only when HTTP traffic was waiting.
- Delegated blocking file opens and disk-backed transfers to configurable I/O workers.
- Passed jobs, open file descriptors, client sockets, offsets, and byte counts with `sendmsg()`.
- Used `sendfile()` with `SF_NODISKIO`; operations that could block were transferred to workers and descriptors were returned after completion.
- Shared worker status through `mmap()` and selected the least-busy worker for new work.
- Supported persistent connections, gzip caching, file-descriptor caching, chunked transfer encoding, ETags, conditional requests, PrimeAuth basic/cookie authentication, wildcard rewrites, PCRE2 rewrites, and `SIGUSR1` configuration reloads.

### VirtualDir

Designed and developed a FreeBSD kernel module that intercepted filesystem-related system calls and transparently remapped paths from configuration, enabling shared physical layouts without chroot jails. Built the companion `vdcli` runtime-management tool.

### PrimeDump and PrimeDNSTop

Built real-time packet and DNS analysis tools using libpcap. Decoded Ethernet, IP, TCP, UDP, ICMPv6, and RFC 1035 DNS traffic; ranked source/domain activity, detected recursion attacks, and integrated operational views with IPFW-based mitigation workflows.

### TAFOS

Developed an educational x86 operating-system kernel in C and assembly with a custom MBR bootloader, protected-mode transition, IDT, heap allocator, port I/O, VGA output, and GDB debugging support.

## Professional Experience

### Advantive — Senior Development Specialist
*Remote / Tampa Bay, FL | July 2022 – Present*

- Implemented and improved Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, and security-scanning workflows across engineering teams.
- Serve on the Architecture Team, collaborating on technical decisions, engineering standards, platform direction, shared libraries, documentation, and AI-assisted engineering workflows.
- Build durable developer and platform improvements intended to reduce repeated work and improve consistency across teams.

### DDI Systems — Senior Development Specialist
*Manalapan, NJ | November 2021 – July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPrime LLC — CEO
*Weehawken, NJ | April 2018 – January 2020*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI Systems — Computer Programmer
*Manalapan, NJ | April 2017 – April 2018*

- Built ERP integrations and automated order, catalog, image, SDS, SFTP, SellerCloud, Essendant, and MultiValue/Universe data workflows.

### Too Much Media LLC — Computer Programmer
*Morganville, NJ | January 2016 – April 2017*

- Developed real-time browser chat integrated with ticketing systems and implemented OAuth 2.0 authorization for protected sites.

### MFCXY, Inc. — Computer Programmer
*Chicago, IL | December 2014 – September 2015*

- Developed backend and Windows client features and middleware for cross-platform database migration.

### AJPM, LLC — Programmer / Owner
*New Jersey / Remote | November 2012 – December 2013*

- Built automated purchasing, inventory, repair, resale, and financial workflow software.

### ISPrime Inc. — CIO / Partner
*Weehawken, NJ | March 2001 – December 2014*

- Architected and operated hosting and CDN infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Designed and built PrimeHTTPD, a high-performance event-driven HTTP/CDN server in C for FreeBSD, deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
- Built the runtime's non-blocking network core, I/O-worker architecture, descriptor-passing protocol, shared-memory worker state, kernel-assisted transfer path, caches, authentication integration, request routing, and HTTP protocol features.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.
- Built DDoS detection and mitigation systems, packet and DNS analysis tools, telemetry, monitoring, authentication, deployment, and security software for 24/7 production operations.
- Diagnosed performance, reliability, network, and abuse incidents across software and infrastructure layers and converted operational findings into lasting tooling and system improvements.

### FatWallet.com — Systems Administrator
*Wisconsin / Remote | December 2000 – June 2001*

- Rebuilt production infrastructure to resolve performance and stability problems without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPrime full-time during rapid company growth.
