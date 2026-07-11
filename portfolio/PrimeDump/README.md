# PrimeDump

## Summary

PrimeDump is a custom libpcap-based traffic-analysis tool built for real-time visibility, troubleshooting, attack investigation, and mitigation support in production network infrastructure.

## Confirmed Implementation

- Ethernet, IP, TCP, UDP, and ICMPv6 header decoding;
- ncurses-based real-time views;
- integration with IPFW;
- use during traffic anomaly and DDoS investigation.

## Relationship to the Platform

PrimeDump complemented PrimeHTTPD, PrimeDNSTop, and the broader CDN and hosting infrastructure by providing packet-level operational visibility.

## Open Questions

- exact capture architecture and performance limits;
- filtering and aggregation features;
- automated mitigation actions;
- storage, export, or replay support;
- deployment footprint.
