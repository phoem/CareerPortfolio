# Jordan Newman

**Systems Software Engineer | Compute Infrastructure, Networking, Reliability**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://github.com/phoem
*Selected public repositories are available. The most significant engineering repositories are private; access is available upon request.*

## Summary

Systems software and infrastructure engineer with deep experience building and operating production runtimes, networking platforms, kernel software, observability tools, and automation. Architected infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic. Built a high-concurrency FreeBSD HTTP/CDN runtime in C with event-driven networking, inter-process descriptor passing, shared-memory worker scheduling, kernel-assisted zero-copy I/O, caching, authentication, and request routing. Combines low-level implementation depth with long-term ownership of demanding 24/7 infrastructure and an interest in systems that directly enable frontier AI research and products.

## Technical Skills

- **Languages:** C, C++, Go, Python, C#, Objective-C, PHP, Perl, JavaScript, Node.js, Shell, Visual Basic
- **Systems:** FreeBSD, Linux, operating systems, distributed systems, kernel modules, system calls, kqueue, mmap, signals, sendmsg(), sendfile(), GDB, non-blocking I/O, worker scheduling, hardware-aware performance optimization
- **Networking:** TCP/IP, HTTP, DNS, CDN architecture, socket programming, packet capture, libpcap, IPFW, DDoS detection and mitigation
- **Infrastructure:** Reliability engineering, observability, incident diagnosis, storage I/O, infrastructure tooling, developer experience, deployment automation, Docker, Kubernetes, Terraform, Azure DevOps, CI/CD
- **Platforms and Security:** Authentication systems, OAuth/OAuth2, security scanning, telemetry, MySQL, MultiValue/Universe

## Selected Technical Highlights

- Architected and operated multi-location hosting and CDN infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic.
- Designed and deployed PrimeHTTPD, a custom event-driven HTTP/CDN runtime in C for FreeBSD, across approximately 200 production servers supporting more than 150,000 concurrent connections.
- Kept the latency-sensitive network path in one primary `kqueue` process and delegated potentially blocking file operations and disk-backed transfers to configurable I/O workers.
- Transferred jobs, files, and client sockets with `sendmsg()` descriptor passing; used shared `mmap()` telemetry for least-busy-worker scheduling and operational visibility.
- Developed packet, DNS, monitoring, deployment, authentication, security, and DDoS systems used to operate and defend 24/7 production infrastructure.
- Implemented Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, security-scanning, shared-library, and AI-assisted engineering workflows in modern enterprise environments.

## Selected Systems Projects

### PrimeHTTPD

High-performance, non-blocking HTTP and CDN server written in C for FreeBSD.

- Designed one main event-driven process around a primary `kqueue`; only that process accepted connections, using FreeBSD HTTP accept filtering to surface request-bearing connections.
- Delegated blocking file opens and disk-backed `sendfile()` transfers to configurable I/O workers, passing jobs, descriptors, offsets, and byte counts with `sendmsg()`.
- Shared worker status through `mmap()` and selected the least-busy worker for new work.
- Supported persistent connections, descriptor and gzip caches, chunked encoding, ETags, conditional requests, PrimeAuth, wildcard/PCRE2 rewrites, and `SIGUSR1` reloads.

### VirtualDir

Designed and developed a FreeBSD kernel module that intercepted filesystem-related system calls and transparently remapped paths from configuration, enabling shared physical layouts without chroot jails. Built the companion `vdcli` runtime-management tool.

### PrimeDump and PrimeDNSTop

Built real-time packet and DNS analysis tools using libpcap. Decoded Ethernet, IP, TCP, UDP, ICMPv6, and RFC 1035 DNS traffic; ranked source/domain activity, detected recursion attacks, and integrated operational views with IPFW-based mitigation workflows.

### TAFOS

Developed an educational x86 operating-system kernel in C and assembly with a custom MBR bootloader, protected-mode transition, IDT, heap allocator, port I/O, VGA output, and GDB debugging support.

## Professional Experience

### Advantive — Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 – Present*

- Implemented and improved Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, and security-scanning workflows across engineering teams.
- Serve on the Architecture Team, collaborating on technical decisions, engineering standards, platform direction, shared libraries, developer tooling, documentation, and AI-assisted engineering workflows.

### DDI System — Senior Development Specialist
*Manalapan, NJ | October 2021 – July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPRIME — Chief Executive Officer
*Weehawken, NJ | March 2018 – December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI System — Computer Programmer
*Manalapan, NJ | April 2017 – March 2018*

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

### ISPRIME — Owner and CIO
*Weehawken, NJ | January 2001 – December 2014*

- Architected and operated hosting and CDN infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Designed and built PrimeHTTPD, a high-performance event-driven HTTP/CDN server in C for FreeBSD, deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
- Built the runtime's network core, I/O workers, descriptor-passing protocol, shared-memory worker state, kernel-assisted transfers, caches, authentication, routing, and HTTP features.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.
- Built DDoS detection and mitigation systems, packet and DNS analysis tools, telemetry, monitoring, authentication, deployment, and security software for 24/7 production operations.
- Debugged complex system behavior across software, storage, networking, and workload layers, turning production findings into robust, durable tooling and system improvements.

### FatWallet.com — Systems Administrator
*Wisconsin / Remote | December 2000 – June 2001*

- Rebuilt production infrastructure to resolve performance and stability problems without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPrime full-time during rapid company growth.
