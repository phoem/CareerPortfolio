---
type: Software Project
title: PrimeHTTPD
description: High-performance non-blocking event-driven HTTP and CDN server written in C for FreeBSD.
tags: [c, freebsd, http, cdn, networking, performance, kqueue, c10k]
generated:
  at: 2026-07-30T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
deployment: Approximately 200 production servers; more than 150,000 concurrent connections.
---

# PrimeHTTPD

## Summary

PrimeHTTPD is a high-performance, non-blocking, event-driven HTTP server written in C for FreeBSD. Jordan intentionally designed it around the C10K concurrency problem and selected a single-core, single-main-process `kqueue` architecture because he considered it the most efficient way to serve very large numbers of simultaneous connections without relying on a thread or process per connection. Only operations that could block were offloaded to a configurable pool of I/O worker processes. It was designed before publicly available event-driven web servers that solved C10K were available to him, then became a core component of a production content delivery network.

## Problem Solved

At the time PrimeHTTPD was conceived, Apache 1.3's process-oriented architecture imposed concurrency and efficiency limitations, Apache 2 was not yet a stable production alternative for Jordan's needs, and nginx had not yet been released. PrimeHTTPD was created to address the C10K problem directly through asynchronous event notification, non-blocking sockets, kernel-assisted file transfer, and careful avoidance of blocking operations in the networking path.

This historical context supports describing PrimeHTTPD as intentionally designed to solve C10K. It does not support claiming that it was the first web server to do so or that no unpublished or inaccessible implementation existed elsewhere.

## Personal Ownership

Jordan Newman architected and implemented PrimeHTTPD and the surrounding CDN software platform.

## Process and Event Architecture

- one main PrimeHTTPD process handled the core networking path;
- the main process used one primary `kqueue` event queue;
- only the main process called `accept()`;
- FreeBSD HTTP accept filtering caused `accept()` readiness to be surfaced only when a request-bearing connection was waiting;
- the main process handled client socket writes when `kqueue()` indicated that enough socket-buffer space was available for a large write;
- the write threshold or preferred write size was configurable;
- a configurable number of worker processes handled operations that could block;
- the architecture deliberately kept the common networking path single-process and event-driven while isolating blocking disk activity.

## Disk I/O Worker Architecture

PrimeHTTPD used Unix-domain descriptor passing with `sendmsg()` to transfer work and open descriptors between the main process and I/O workers.

### Opening files

- for an `open()` operation, the main process sent the path to an I/O worker;
- the worker performed the potentially blocking file open;
- the worker returned the opened file descriptor to the main process using `sendmsg()` ancillary-data descriptor passing.

### Offloading blocked `sendfile()` work

- the main process normally performed zero-copy transfers with `sendfile()` and `SF_NODISKIO`;
- when `sendfile()` indicated that disk I/O would be required, the main process avoided blocking;
- it passed the file descriptor, client socket descriptor, file offset, and requested byte count to an I/O worker using `sendmsg()`;
- the worker completed the blocking portion of the transfer;
- when finished, the worker returned the descriptors to the main process using `sendmsg()` so the main event loop could resume ownership.

### Worker selection and visibility

- the main process and workers shared an `mmap()`-backed memory region;
- the shared state recorded worker activity and workload information;
- the main process used that state to select the least-busy worker;
- the shared state also gave the main process visibility into what each worker was doing.

## Performance-Oriented Implementation

- non-blocking, event-driven networking selected specifically to address C10K-scale concurrency;
- `kqueue`-based event processing;
- persistent HTTP connections;
- `sendfile()`-based zero-copy file transfer;
- `SF_NODISKIO` to avoid blocking the event loop on disk reads;
- dedicated I/O workers for disk operations that would otherwise block;
- `sendmsg()` and descriptor passing for transferring files and sockets between processes;
- `mmap()`-based shared worker-status memory;
- least-busy-worker selection;
- `O_NONBLOCK` sockets;
- `TCP_NODELAY` and `TCP_NOPUSH` socket behavior and tuning;
- FreeBSD `accept_filter_http` support;
- design intended to minimize copies, blocking operations, unnecessary context switching, and per-connection overhead.

## HTTP and Application Features

Confirmed features include:

- persistent HTTP connections;
- gzip support;
- in-memory caching of generated gzip data alongside cached open file descriptors;
- file-descriptor caching;
- chunked transfer encoding;
- ETags;
- conditional GET handling;
- HTTP Basic authentication through Jordan's PrimeAuth system;
- cookie authentication through PrimeAuth;
- wildcard rewrite rules;
- PCRE2 regular-expression rewrite rules;
- configuration reload through the `SIGUSR1` signal.

## CDN Platform Context

PrimeHTTPD was not only a standalone web server. It served as the foundation of a production CDN and included CDN-oriented capabilities. Jordan also built the CDN infrastructure and supporting software around it.

Known production context:

- approximately 3,000-4,000 servers across the broader infrastructure;
- approximately 10 CDN locations;
- peak traffic exceeding 65 Gbps;
- PrimeHTTPD deployed across approximately 200 production servers;
- support for more than 150,000 concurrent connections;
- high-traffic customer production workloads.

The platform also used [VirtualDir](/VirtualDir/README.md), [PrimeDump](/PrimeDump/README.md), [PrimeDNSTop](/PrimeDNSTop/README.md), PrimeAuth, and other custom operational software.

## Engineering Decisions and Tradeoffs

- **Single main event process:** kept connection state and event ownership centralized, reducing synchronization overhead in the hot path.
- **Worker processes only for blocking work:** preserved the simplicity and efficiency of a single event loop without allowing disk latency to stall network progress.
- **Descriptor passing instead of reopening state:** allowed ownership of open files and client sockets to move between processes without reconstructing connection state.
- **`SF_NODISKIO`:** treated cache misses or disk reads as exceptional work to offload rather than allowing the event loop to block.
- **Shared worker-state memory:** enabled low-overhead workload-aware dispatch and operational visibility.
- **Open descriptor and gzip caches:** reduced repeated filesystem opens and repeated compression work for frequently requested content.

## Evidence Quality

- **Exact qualitative fact:** PrimeHTTPD was intentionally architected to solve the C10K problem.
- **Exact qualitative fact:** Jordan selected an event-driven `kqueue` design because he judged it the most efficient concurrency model for that problem.
- **Exact architecture fact:** the hot networking path used one main process and one primary `kqueue`; only blocking work was delegated to configurable worker processes.
- **Exact architecture fact:** file and socket descriptors were transferred with `sendmsg()`, including offset and byte-count metadata for offloaded file transfers.
- **Exact architecture fact:** shared `mmap()` worker-state memory supported least-busy-worker selection and activity visibility.
- **Exact feature facts:** gzip caching, descriptor caching, chunked encoding, ETags, conditional GETs, PrimeAuth integration, wildcard rewrites, PCRE2 rewrites, and `SIGUSR1` reloads were supported.
- **Historical-context claim:** At the time of development, Jordan was not aware of a publicly released web server that already solved C10K using the architecture he needed. Resume wording must preserve this narrower scope and must not claim universal or industry-wide priority.
- **Estimated production scale:** approximately 3,000-4,000 servers across the broader infrastructure and approximately 10 CDN locations.
- **Confirmed production scale:** PrimeHTTPD deployed across approximately 200 production servers, supported more than 150,000 concurrent connections, and participated in infrastructure carrying peak traffic exceeding 65 Gbps.
- **Current evidence source:** direct technical recollection supplied by Jordan on 2026-07-30. Configuration and source-code review remain future verification opportunities.

## Resume-Ready Descriptions

### Detailed systems version

Architected and implemented PrimeHTTPD, a high-performance HTTP/CDN server in C for FreeBSD intentionally designed around the C10K concurrency problem. Built a single-process `kqueue` networking core and isolated blocking disk work in a configurable worker pool, using `sendmsg()` descriptor passing, `mmap()`-shared worker telemetry, least-busy-worker dispatch, and `sendfile()` with `SF_NODISKIO` to keep the event loop non-blocking.

Implemented persistent connections, descriptor and gzip caches, chunked encoding, ETags, conditional requests, signal-driven reloads, authentication integration, and wildcard/PCRE2 rewriting. Optimized around FreeBSD kernel capabilities to minimize copies, context switching, and per-connection overhead, supporting more than 150,000 concurrent connections across approximately 200 production servers.

### Recruiter-facing version

Designed and built a high-performance C web server specifically to overcome C10K-era concurrency limits, combining a single event-driven networking core with specialized worker processes for blocking disk activity. It became the serving foundation for a multi-location production CDN handling high-traffic customer workloads.

### Architect version

Architected the HTTP serving and CDN software platform for infrastructure spanning thousands of servers and multiple points of presence. Centralized the hot connection path in a single `kqueue` event process, delegated blocking work through descriptor-passing I/O workers, and combined kernel-aware transfer optimizations, caching, authentication, rewriting, and operational controls in a production runtime.

### OpenAI compute-infrastructure version

Designed a production event-driven runtime in C for FreeBSD that separated latency-sensitive network processing from blocking storage operations. Implemented Unix descriptor passing, shared-memory worker scheduling and telemetry, zero-copy transfer with non-blocking fallback, cached file and compressed-content state, and protocol-level features across approximately 200 servers supporting more than 150,000 concurrent connections.

## Open Questions

- exact development and first-production dates for PrimeHTTPD;
- contemporaneous benchmark records or documentation that can support careful historical comparison with Apache and later nginx releases;
- exact configuration syntax and full directive catalog;
- complete source-level process lifecycle, failure recovery, and descriptor-ownership rules;
- cache eviction, descriptor limits, gzip-cache sizing, and invalidation behavior;
- cache-control and byte-range implementation details;
- logging architecture and log-rotation behavior;
- exact multi-core deployment strategy across multiple PrimeHTTPD instances;
- benchmark methodology and comparative performance results;
- deployment automation and content-distribution workflow;
- exact request-time relationship between PrimeHTTPD, VirtualDir, PrimeAuth, and other CDN components;
- source-code and production-configuration review to verify and expand the architecture record.