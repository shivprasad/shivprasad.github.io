---
title: "Refinements in Spring Boot 2.0"
date: 2018-01-19 08:00:00 -0800
categories:
  - Tech
  - Java
tags:
  - java
  - spring-boot
authors:
  - shiv
---

Spring Boot 2.0 hit GA and came with subtle but powerful refinements:
- Embedded Netty support for WebFlux
- Actuator improvements (more endpoints + security config)
- Java 8+ baseline

I found the changes in actuator metrics and auto-config tweaks to be the most valuable. The new `/actuator/metrics` gave us visibility into thread pools and garbage collection patterns, right out of the box.

We also started experimenting with reactive patterns in WebFlux, though adoption was selective — not all workloads benefit from async.

Pro-tip: Don’t blindly migrate to WebFlux unless your use case fits high-concurrency, IO-bound scenarios.
