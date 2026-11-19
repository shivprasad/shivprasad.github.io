---
title: "Pattern: Circuit Breaker in Microservices"
date: 2015-11-21 05:30:00 -0800
categories:
  - Tech
  - Microservices
tags:
  - circuit-breaker
  - microservices
authors:
  - shiv
---

One of the key patterns we applied was the Circuit Breaker — to protect critical downstream systems.

Tools explored: Hystrix, resilience4j

Example:

```
circuitBreaker.run(() -> callService());

```

Benefits:
- Prevent cascading failures
- Allow system to recover gracefully
- Monitor tripped circuits via dashboards

This pattern is a must-have in service meshes or mesh-like environments.
