---
type: Network Telemetry Project
title: PrimeFlow
description: NetFlow v5 collector daemon with a modular processing pipeline and companion packet-capture flow generator.
tags: [netflow, netflow-v5, pcap, telemetry, networking, monitoring, isprime]
timestamp: 2026-07-31
generated:
  at: 2026-07-31T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# PrimeFlow

## Summary

PrimeFlow is a NetFlow v5 collector daemon designed and programmed by Jordan Newman at ISPRIME. It used a modular processing pipeline and included a companion packet-capture-based flow generator.

## Personal Ownership

Jordan designed and programmed PrimeFlow and its companion flow generator.

## Confirmed Architecture

- NetFlow v5 collector daemon;
- modular flow-processing pipeline;
- companion `pcap`-based flow generator;
- built for network-monitoring use cases.

## Evidence Quality

- The architecture and Jordan's design and implementation ownership were directly confirmed by Jordan on 2026-07-31.
- The implementation language, production deployment, collector count, flow rate, retention model, downstream storage, and operational outcomes are not yet documented.
- No claim is currently supported for streaming-telemetry protocols such as gNMI or for event platforms such as Kafka.

## Resume-Ready Description

Designed and programmed PrimeFlow, a NetFlow v5 collector daemon with a modular processing pipeline and a companion `pcap`-based flow generator for network monitoring.

## Related Concepts

- [CDN Platform](../CDN_Platform/README.md)
- [Network Infrastructure and Datacenter Operations](../Network_Infrastructure_Experience/README.md)
- [PrimeBGP](../PrimeBGP/README.md)
- [PrimeDump](../PrimeDump/README.md)

## Open Questions

- What programming language and libraries were used?
- Was PrimeFlow deployed in production, and across how many collectors, routers, or locations?
- What flow rates or data volumes did it process?
- What modules existed in the processing pipeline?
- Where were processed flows stored, displayed, or exported?
- How was the companion flow generator deployed and used?
