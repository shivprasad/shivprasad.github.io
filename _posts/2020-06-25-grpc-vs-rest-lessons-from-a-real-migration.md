---
title: "gRPC vs REST: Lessons from a Real Migration"
date: 2020-06-25 03:00:00 -0700
categories:
  - Blog
  - General
tags:
  - grpc
  - rest
authors:
  - shiv
---

We replaced REST endpoints with gRPC in a latency-sensitive service.

Metrics:
- Median latency: 45ms → 20ms
- Payload size dropped by ~70%
- Auto-generated client libraries boosted DX

But:
- gRPC-web still lacks maturity
- Debugging gRPC isn’t as easy as curl-ing a REST endpoint

Tradeoffs, always. But the gains were measurable.
