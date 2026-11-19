---
title: "Observability vs Monitoring: A Practitioner’s View"
date: 2019-03-12 04:00:00 -0700
categories:
  - Blog
  - General
tags:
  - logs
  - metrics
  - tracing
authors:
  - shiv
---

Buzzwords aside, here’s how I see the difference:

- **Monitoring** tells you when something’s wrong
- **Observability** helps you understand why

We matured from just dashboards to:
- Structured logging (JSON + traceIds)
- Distributed tracing with Jaeger
- SLO-driven alerts

Combined with proactive alert tuning, this let us detect anomalies *before* user reports came in.
