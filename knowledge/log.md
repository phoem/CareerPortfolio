# Knowledge Base Update Log

## 2026-07-31

* **PrimeBGP**: Added confirmed design and implementation ownership for a passive BGP4 speaker that accepted peering sessions, processed route updates, and stored prefixes in an in-memory red-black tree for policy-based rerouting.
* **PrimeFlow**: Added confirmed design and implementation ownership for a NetFlow v5 collector daemon with a modular processing pipeline and companion `pcap`-based flow generator.
* **Network infrastructure**: Recorded ISPRIME familiarity with Cisco, Juniper, and Foundry equipment; SNMP and NetFlow monitoring; and hands-on datacenter design, setup, migration, and operations.
* **Evidence boundaries**: Left languages, individual-tool deployment scale, routing topology, device models, specific configuration ownership, and unconfirmed protocols as open questions.
* **ISPRIME mentoring**: Recorded that Jordan created internal training documentation and trained the majority of ISPRIME employees over the years.
* **Leadership development**: Recorded that Jordan personally mentored two beginners over several years into technical experts and eventual ISPRIME leaders.
* **Evidence boundary**: Preserved trainee counts, leadership titles, training topics, and the mentees' later IT careers as qualitative or open details rather than inventing specifics.

## 2026-07-30

* **Advantive role**: Added confirmed current-role responsibilities covering Architecture Team participation, platform engineering, developer tooling, Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, security scanning, shared libraries, documentation, and AI-assisted engineering workflows.
* **Evidence boundary**: Recorded that current evidence supports qualitative platform-workflow claims but not Kubernetes scheduler/control-plane ownership or quantified team impact.
* **OKF migration**: Upgraded the `knowledge/` bundle declaration and all indexed concepts from OKF v0.1 timestamp metadata to OKF v0.2 `generated.at` metadata.
* **Evidence boundaries**: Added or clarified evidence-quality sections for project, platform, technology-experience, career-timeline, and profile concepts without changing the underlying factual claims.
* **Governance**: Added ADR 0022 and updated the OKF conventions to cover v0.2 provenance, verification, freshness, structured sources, claim-level source footnotes, and attested computation.
* **PrimeHTTPD clarification**: Recorded that PrimeHTTPD was intentionally architected around the C10K concurrency problem and that Jordan selected a non-blocking, event-driven `kqueue` design as the most efficient approach for the problem.
* **Historical boundary**: Recorded the narrower, resume-safe context that Jordan was not aware of a publicly released event-driven web server solving the same need at the time, without claiming universal or industry-wide priority.
* **Evidence quality**: Classified PrimeHTTPD concurrency motivation, production scale, estimated infrastructure scale, and historical context; expanded open questions for dates and contemporaneous benchmark evidence.

## 2026-07-15

* **Creation**: Added Jordan Newman's professional-profile concept.
* **Confirmation**: Recorded `https://www.linkedin.com/in/jordan-newman-aa3b19b2/` as the canonical LinkedIn URL for future career artifacts.
* **Confirmation**: Recorded `https://github.com/phoem` as the canonical GitHub URL for future career artifacts.
* **Creation**: Added a confirmed career-timeline concept for employment dates and titles.
* **Correction**: Standardized Advantive to June 2022 - Present; DDI System to October 2021 - July 2022 as Senior Development Specialist; ISPRIME CEO to March 2018 - December 2019; DDI System (2017) to April 2017 - March 2018; and ISPRIME Owner and CIO to January 2001 - December 2014.
* **Synchronization**: Updated all three canonical generic resume sources to use the confirmed timeline.

## 2026-07-13

* **Creation**: Added a confirmed technology-experience concept for Kubernetes and container runtimes.
* **Clarification**: Recorded production Kubernetes workflow experience separately from experimental use of kubelet, containerd, and runc.
* **Boundary**: Recorded familiarity with NRI plugin development concepts without claiming that an NRI plugin has been written.
* **Resume update**: Updated the Netflix JR39731 resume with evidence-safe container runtime language.
* **Creation**: Added a confirmed Linux kernel experience concept.
* **Clarification**: Recorded strong Linux kernel familiarity while explicitly excluding Linux kernel-module authorship and upstream contribution claims.
* **Resume update**: Updated the Netflix JR39731 resume with accurate Linux-kernel positioning backed by production FreeBSD kernel development.

## 2026-07-12

* **Rename**: Renamed the repository from `MyResumes` to `CareerPortfolio`.
* **Migration**: Renamed the OKF bundle directory from `portfolio/` to `knowledge/`.
* **Documentation**: Updated workflow and repository references to use `phoem/CareerPortfolio` and `knowledge/`.

## 2026-07-11

* **Standardization**: Adopted Google Cloud Open Knowledge Format v0.1 for the project-knowledge bundle.
* **Documentation**: Added bundle navigation, local OKF conventions, and agent workflow requirements.
* **Update**: Converted existing project records to OKF concept documents with YAML frontmatter while preserving confirmed facts and open questions.
* **Creation**: Established project concepts for PrimeHTTPD, the CDN platform, VirtualDir, PrimeDump, PrimeDNSTop, KeepClean, StatCache, TAFOS, and the AVR smart smoke/CO2 detector.
