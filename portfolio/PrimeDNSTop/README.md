# PrimeDNSTop

## Summary

PrimeDNSTop is a custom DNS traffic-monitoring tool built to identify abnormal DNS activity and recursion attacks in production infrastructure.

## Confirmed Implementation

- parses UDP port 53 traffic;
- parses RFC 1035 DNS queries;
- ranks source and domain activity;
- supports detection and investigation of DNS recursion attacks.

## Relationship to the Platform

PrimeDNSTop provided DNS-specific observability alongside PrimeDump and the broader DDoS detection and mitigation systems.

## Open Questions

- exact user interface and aggregation windows;
- support for response parsing and additional record types;
- automated alerting or mitigation behavior;
- deployment footprint and performance limits.
