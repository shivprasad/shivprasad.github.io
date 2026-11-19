---
title: "Using Resilience4j for Circuit Breaker Pattern in Java"
date: 2018-07-03 03:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - circuit-breaker
  - java
  - resilience4j
authors:
  - shiv
---

Fault-tolerant design isn't optional anymore. As microservices expanded, I experimented with [Resilience4j](https://resilience4j.readme.io/) for circuit breaker implementations in Java.

Unlike Netflix’s Hystrix, Resilience4j is modular and lightweight, and integrates well with functional programming constructs.

Example:

```
CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("myService");
Supplier<String> decoratedSupplier = CircuitBreaker
    .decorateSupplier(circuitBreaker, () -> myRemoteCall());

Try<String> result = Try.ofSupplier(decoratedSupplier)
    .recover(throwable -> "fallback");

```

This gave us transparency into service degradation, prevented cascading failures, and allowed safe fallbacks.
