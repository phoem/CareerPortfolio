---
type: Infrastructure Platform
title: CDN Platform
description: Production hosting and content-delivery platform spanning thousands of servers, multiple locations, and custom systems software.
tags: [cdn, distributed-systems, infrastructure, freebsd, networking, reliability]
timestamp: 2026-07-12T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
deployment: Approximately 3,000-4,000 servers, 10 CDN locations, multiple datacenters, and more than 65 Gbps peak traffic.
---

# CDN Platform

## Summary

Jordan Newman architected and operated a production hosting and content-delivery platform spanning approximately 3,000-4,000 servers, 10 CDN locations, multiple datacenters, and more than 65 Gbps of peak traffic.

## Personal Ownership

Jordan built the custom HTTP/CDN serving software and substantial supporting infrastructure software, and held architectural and operational responsibility for the platform.

## Confirmed Components

- [PrimeHTTPD](/PrimeHTTPD/README.md), a high-performance FreeBSD HTTP/CDN server;
- [VirtualDir](/VirtualDir/README.md), a FreeBSD kernel pathname-virtualization module;
- [PrimeDump](/PrimeDump/README.md), packet-analysis tooling;
- [PrimeDNSTop](/PrimeDNSTop/README.md), DNS-monitoring tooling;
- DDoS detection and mitigation software;
- monitoring, telemetry, authentication, security, deployment, and infrastructure-management systems.

## Production Context

- approximately 3,000-4,000 servers across the broader infrastructure;
- approximately 10 CDN locations;
- more than 65 Gbps peak traffic;
- approximately 200 PrimeHTTPD production servers;
- more than 150,000 concurrent PrimeHTTPD connections;
- 24/7 customer-facing production workloads.

## Open Questions

- exact CDN caching and content-placement architecture;
- content replication and invalidation workflow;
- traffic routing and load-balancing mechanisms;
- deployment and rollback design;
- per-location topology and capacity;
- exact PrimeHTTPD CDN features and request lifecycle.
