# Jordan Newman - Netflix Distributed Systems Engineer - Compute Runtime Resume

**Distributed Systems Engineer | Compute Runtime, Systems Software, Infrastructure**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | github.com/phoem

## Summary

Distributed systems and systems software engineer with deep experience building production runtime, networking, kernel, and infrastructure software. Architected and operated systems spanning approximately 3,000-4,000 servers, 10 locations, and more than 65 Gbps of peak traffic. Built a non-blocking FreeBSD HTTP/CDN runtime in C, specialized I/O workers, kernel modules, DDoS defenses, telemetry, deployment automation, and modern container and infrastructure-as-code workflows. Brings hands-on depth from kernel interfaces through large-scale production operations.

## Technical Skills
- **Languages:** C, C++, Go, Python, C#, Objective-C, PHP, Perl, JavaScript, Node.js, Shell, Visual Basic
- **Systems:** FreeBSD, Linux, kernel modules, system calls, operating systems, kqueue, sendfile(), GDB, TCP/IP, non-blocking I/O
- **Networking/Security:** HTTP, DNS, CDN architecture, socket programming, DDoS detection/mitigation, packet capture, libpcap, IPFW, authentication, telemetry
- **Cloud/DevOps:** Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, security scanning, deployment automation
- **Databases/Web:** MySQL, MultiValue/Universe, OAuth/OAuth2, SMTP OAuth, React, jQuery, PHP, web services

## Selected Technical Highlights

- Designed and deployed PrimeHTTPD, a custom event-driven compute and HTTP serving runtime across approximately 200 production FreeBSD servers.
- Supported more than 150,000 concurrent connections using kqueue, persistent connections, non-blocking sockets, zero-copy sendfile(), and FreeBSD-specific TCP and accept-filter optimizations.
- Separated latency-sensitive event processing from blocking disk work through dedicated I/O workers and SF_NODISKIO-aware handling.
- Architected and operated distributed production infrastructure spanning thousands of servers and multiple geographic locations.
- Built observability, traffic analysis, DNS monitoring, authentication, deployment, security, and DDoS mitigation systems for 24/7 infrastructure.
- Implemented Kubernetes, Docker, Terraform, Azure DevOps, CI/CD, and security-scanning workflows in modern engineering environments.

## Selected Systems Projects

- **PrimeHTTPD:** Architected and implemented a high-performance, non-blocking, kqueue-based HTTP/CDN server in C for FreeBSD. Used sendfile(), SF_NODISKIO, TCP_NODELAY, TCP_NOPUSH, O_NONBLOCK, accept_filter_http, persistent connections, and dedicated I/O workers.
- **VirtualDir:** Designed and developed a FreeBSD kernel module that intercepted filesystem-related syscalls and transparently remapped paths from configuration, enabling shared physical layouts without chroot jails; included the vdcli runtime management tool.
- **PrimeDump:** Built a libpcap-based real-time traffic analyzer decoding Ethernet, IP, TCP, UDP, and ICMPv6 with ncurses views and IPFW integration.
- **PrimeDNSTop:** Built a DNS traffic monitor parsing UDP/53 and RFC 1035 queries to detect recursion attacks and rank source and domain activity.
- **TAFOS:** Developed an educational x86 operating-system kernel in C and assembly with a custom MBR bootloader, protected mode, IDT, heap allocator, port I/O, VGA output, and GDB support.

## Professional Experience

### Advantive - Senior Development Specialist
*Remote / Tampa Bay, FL | July 2022 - Present*

- Implemented Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, and security-scanning workflows across engineering teams.
- Partnered with architecture teams to standardize deployment practices and developed shared libraries, documentation, and AI-assisted engineering workflows.

### DDI Systems - Senior Development Specialist
*Manalapan, NJ | November 2021 - July 2022*

- Modernized legacy VB.NET components in C# and integrated Microsoft Office 365 SMTP OAuth for secure customer-facing workflows.

### ISPrime LLC - CEO
*Weehawken, NJ | April 2018 - January 2020*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### DDI Systems - Computer Programmer
*Manalapan, NJ | April 2017 - April 2018*

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
*Weehawken, NJ | March 2001 - December 2014*

- Architected and operated hosting and CDN infrastructure spanning approximately 3,000-4,000 servers, 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Designed and built PrimeHTTPD, a high-performance, non-blocking, kqueue-based HTTP/CDN server in C for FreeBSD; deployed it across approximately 200 servers and supported more than 150,000 concurrent connections.
- Leveraged sendfile(), SF_NODISKIO, TCP_NODELAY, TCP_NOPUSH, O_NONBLOCK, accept_filter_http, persistent connections, and dedicated I/O workers to keep disk operations from blocking the networking event loop.
- Built DDoS detection and mitigation systems, packet and DNS analysis tools, monitoring, telemetry, authentication, deployment, and security software used across production infrastructure.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.

### FatWallet.com - Systems Administrator
*Wisconsin / Remote | December 2000 - June 2001*

- Rebuilt production infrastructure to resolve performance and stability issues without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** - Computer Science coursework; left during first semester to pursue ISPrime full-time during rapid company growth.
