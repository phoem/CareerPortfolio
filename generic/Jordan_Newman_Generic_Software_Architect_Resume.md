# Jordan Newman - Generic Software Architect Resume

**Software Architect | Distributed Systems, Infrastructure, Security, DevOps**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | github.com/phoem  
*Selected public repositories are available. The most significant engineering repositories are private; access is available upon request.*

## Summary

Software architect and hands-on systems engineer with experience designing production software and infrastructure across CDN, hosting, enterprise software, security, backend platforms, and DevOps. Architected systems operating across approximately 3,000-4,000 servers, 10 CDN locations, and more than 65 Gbps of peak traffic. Combines technical leadership with deep implementation experience in C, FreeBSD, networking, kernel development, reliability, and performance engineering.

## Technical Skills
- **Languages:** C, C++, Go, Python, C#, Objective-C, PHP, Perl, JavaScript, Node.js, Shell, Visual Basic
- **Systems:** FreeBSD, Linux, kernel modules, system calls, operating systems, kqueue, sendfile(), GDB, TCP/IP, non-blocking I/O
- **Networking/Security:** HTTP, DNS, CDN architecture, socket programming, DDoS detection/mitigation, packet capture, libpcap, IPFW, authentication, telemetry
- **Cloud/DevOps:** Azure DevOps, Docker, Kubernetes, Terraform, CI/CD, security scanning, deployment automation
- **Databases/Web:** MySQL, MultiValue/Universe, OAuth/OAuth2, SMTP OAuth, React, jQuery, PHP, web services

## Selected Technical Highlights

- Architected the custom HTTP serving and CDN software platform for infrastructure spanning thousands of servers and multiple points of presence.
- Designed high-availability, DDoS mitigation, traffic analysis, telemetry, authentication, and operational-control systems.
- Created a kernel-aware event-driven server architecture using kqueue, sendfile(), non-blocking sockets, I/O workers, and FreeBSD-specific optimizations.
- Designed a transparent FreeBSD kernel pathname-virtualization layer for multi-tenant hosting without application changes or chroot jails.
- Standardized Kubernetes, Terraform, Azure DevOps, CI/CD, and security-scanning practices across engineering teams.

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
- Served as a member of the Architecture Team, collaborating with fellow architects and the architecture lead to make technical decisions, define engineering standards, guide platform direction, and develop shared libraries, documentation, and AI-assisted engineering workflows.

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

**Infrastructure Leadership**
- Architected and operated hosting and CDN infrastructure spanning approximately 3,000-4,000 servers, 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.

**Systems Software Engineering**
- Designed and built PrimeHTTPD, a high-performance, non-blocking, kqueue-based HTTP/CDN server in C for FreeBSD; deployed it across approximately 200 servers and supported more than 150,000 concurrent connections.
- Leveraged sendfile(), SF_NODISKIO, TCP_NODELAY, TCP_NOPUSH, O_NONBLOCK, accept_filter_http, persistent connections, and dedicated I/O workers to keep disk operations from blocking the networking event loop.
- Developed production FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.

**Security and Networking**
- Built DDoS detection and mitigation systems, packet and DNS analysis tools, monitoring, telemetry, authentication, deployment, and security software used across production infrastructure.

### FatWallet.com - Systems Administrator
*Wisconsin / Remote | December 2000 - June 2001*

- Rebuilt production infrastructure to resolve performance and stability issues without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** - Computer Science coursework; left during first semester to pursue ISPrime full-time during rapid company growth.
