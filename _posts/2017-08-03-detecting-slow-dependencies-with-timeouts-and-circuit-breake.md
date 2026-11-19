---
title: "Detecting Slow Dependencies with Timeouts and Circuit Breakers"
date: 2017-08-03 06:45:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - circuit-breaker
  - timeouts
authors:
  - shiv
---

Slow responses often hurt more than failures.

How we improved UX:
- Timeouts for all network calls
- Circuit breakers for flapping endpoints
- Synthetic monitors to spot degradation early
