---
type: Technology Experience
title: Network Infrastructure and Datacenter Operations
description: Confirmed ISPRIME experience with BGP, transit providers, peering, private inter-PoP fiber, DNS traffic steering, monitoring, and datacenter operations.
tags: [networking, datacenter, pops, cisco, juniper, foundry, bgp, peering, dark-fiber, anycast, geodns, snmp, netflow]
timestamp: 2026-08-02
generated:
  at: 2026-07-31T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# Network Infrastructure and Datacenter Operations

## Summary

At ISPRIME, Jordan worked with production network infrastructure and helped design, set up, migrate, and operate the company's datacenters and points of presence.

## Confirmed Experience

- familiarity with Cisco, Juniper, and Foundry networking equipment from ISPRIME work;
- BGP4 experience, including the design and implementation of [PrimeBGP](../PrimeBGP/README.md);
- network-monitoring software using SNMP and NetFlow;
- design and implementation of [PrimeFlow](../PrimeFlow/README.md), a NetFlow v5 collection system;
- design and implementation of [PrimeDump](../PrimeDump/README.md) for packet-level network and DDoS visibility;
- participation in datacenter design and initial setup;
- participation in datacenter migrations;
- ongoing datacenter and network operations.

## Confirmed Production Network Architecture

- BGP routing across many network connections and routes;
- multiple upstream transit providers;
- direct peering connections and agreements;
- peering through internet exchanges;
- privately lit dark-fiber connectivity between points of presence;
- CDN traffic steering using anycast DNS and GeoDNS during different periods of the platform's operation.

## Production Context

This work supported the broader [CDN Platform](../CDN_Platform/README.md), which spanned approximately 3,000-4,000 servers, approximately 10 CDN locations, multiple datacenters, and more than 65 Gbps of peak traffic.

## Evidence Quality

- The vendor familiarity, protocol/tooling experience, and datacenter responsibilities were directly confirmed by Jordan on 2026-07-31.
- The broader platform scale is documented separately and must not be presented as the deployment scale of every individual network tool.
- The production network architecture and traffic-steering mechanisms were directly confirmed by Jordan on 2026-08-02.
- Jordan described these mechanisms as company/platform capabilities using “we.” His overall architecture and operations role is confirmed, but his personal ownership of individual BGP policies, peer configurations, DNS implementations, fiber engineering, and traffic-steering automation still requires clarification.
- Specific device models, configuration ownership, routing topology, migration count, automation interfaces, and availability outcomes are not yet documented.
- Current evidence does not support claims for NetBox, Nautobot, VRFs, VXLAN, EVPN, OSPF, IS-IS, gRPC, gNMI, EKS, or zero-touch deployment.

## Resume-Ready Description

Helped design, deploy, migrate, and operate multi-datacenter and PoP network infrastructure supporting approximately 3,000-4,000 servers across approximately 10 locations, using multi-provider BGP, direct and exchange peering, private inter-PoP fiber, anycast DNS, and GeoDNS; built BGP4, SNMP, NetFlow, packet-analysis, and DDoS-monitoring software.

## Related Concepts

- [CDN Platform](../CDN_Platform/README.md)
- [PrimeBGP](../PrimeBGP/README.md)
- [PrimeFlow](../PrimeFlow/README.md)
- [PrimeDump](../PrimeDump/README.md)
- [PrimeDNSTop](../PrimeDNSTop/README.md)

## Open Questions

- Which Cisco, Juniper, and Foundry platforms did Jordan configure directly?
- Which BGP policies, upstream and peering sessions, route announcements, anycast configurations, GeoDNS systems, and failover behaviors did Jordan personally design or configure?
- Did Jordan write or operate the anycast-DNS or GeoDNS software, or configure third-party systems?
- What role did PrimeBGP play in production traffic engineering, and did it feed or directly change router state?
- Which routing, switching, redundancy, and traffic-engineering protocols were used beyond BGP4?
- What portions of datacenter network design, deployment, migration, and operations did Jordan personally own?
- What configuration-generation, provisioning, inventory, source-of-truth, or change-management systems were used?
- How many datacenter migrations did Jordan help execute, and were any completed without customer-facing downtime?
