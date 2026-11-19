---
title: "Failing Fast Saved Us From Failing Big"
date: 2014-09-18 13:45:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - circuit-breakers
  - design-patterns
  - failure-handling
  - timeouts
authors:
  - shiv
---

One of our internal services became unstable under load. We traced it to a slow downstream dependency with no timeout.

The solution:
- Add circuit breakers with sliding window metrics
- Monitor P99 latency, not averages
- Implement failover to cached fallback

![Circuit Breaker Flow](https://resilient-java.readthedocs.io/en/latest/_images/circuitbreaker.png)

Circuit Breaker Flow

**Fail fast, recover gracefully** — this mindset prevented cascading failures across our entire system.
