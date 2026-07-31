---
type: Network Software Project
title: PrimeBGP
description: Passive BGP4 speaker for receiving route updates and maintaining learned prefixes for policy-based rerouting.
tags: [bgp, bgp4, routing, networking, red-black-tree, isprime]
timestamp: 2026-07-31
generated:
  at: 2026-07-31T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# PrimeBGP

## Summary

PrimeBGP is a passive BGP4 speaker designed and programmed by Jordan Newman at ISPRIME. It accepts BGP peering sessions, receives route `UPDATE` messages, and stores learned network prefixes in an in-memory red-black tree for policy-based rerouting.

## Personal Ownership

Jordan designed and programmed PrimeBGP.

## Confirmed Architecture

- passive BGP4 speaker;
- accepts BGP peering sessions;
- receives BGP route `UPDATE` messages;
- stores learned prefixes in an in-memory red-black tree;
- supports policy-based rerouting use cases.

## Evidence Quality

- The architecture and Jordan's design and implementation ownership were directly confirmed by Jordan on 2026-07-31.
- The implementation language, production deployment, peer count, route-table size, update rate, and operational outcomes are not yet documented.
- “Policy-based rerouting” must not be expanded into a claim that PrimeBGP directly changed router state until that behavior is clarified.

## Resume-Ready Description

Designed and programmed PrimeBGP, a passive BGP4 speaker that accepted peering sessions, processed route updates, and maintained learned prefixes in an in-memory red-black tree for policy-based rerouting.

## Related Concepts

- [CDN Platform](../CDN_Platform/README.md)
- [Network Infrastructure and Datacenter Operations](../Network_Infrastructure_Experience/README.md)
- [PrimeDump](../PrimeDump/README.md)
- [PrimeFlow](../PrimeFlow/README.md)

## Open Questions

- What programming language and libraries were used?
- Was PrimeBGP deployed in production, and across how many sites or peers?
- Approximately how many prefixes or route updates did it process?
- How was policy-based rerouting applied, and did PrimeBGP directly change router configuration or feed another system?
- Which BGP capabilities, message types, attributes, filtering policies, and failure-handling behaviors were implemented?
