---
type: Software Project
title: PrimeDump
description: Real-time libpcap-based packet analyzer for operational visibility, troubleshooting, and DDoS investigation.
tags: [networking, security, libpcap, packet-analysis, ddos, freebsd]
timestamp: 2026-07-11T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# PrimeDump

## Summary

PrimeDump is a custom libpcap-based traffic-analysis tool built for real-time visibility, troubleshooting, attack investigation, and mitigation support in production network infrastructure.

## Confirmed Implementation

- Ethernet, IP, TCP, UDP, and ICMPv6 header decoding;
- ncurses-based real-time views;
- integration with IPFW;
- use during traffic anomaly and DDoS investigation.

## Relationship to the Platform

PrimeDump complemented [PrimeHTTPD](/PrimeHTTPD/README.md), [PrimeDNSTop](/PrimeDNSTop/README.md), and the broader [CDN platform](/CDN_Platform/README.md) by providing packet-level operational visibility.

## Open Questions

- exact capture architecture and performance limits;
- filtering and aggregation features;
- automated mitigation actions;
- storage, export, or replay support;
- deployment footprint.
