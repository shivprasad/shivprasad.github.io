---
title: "Observability with OpenMetrics and Prometheus"
date: 2019-05-19 07:00:00 -0700
categories:
  - Blog
  - General
tags:
  - metrics
  - prometheus
authors:
  - shiv
---

As OpenMetrics gained traction, we re-evaluated how we exposed metrics from our apps.

Prometheus already supported OpenMetrics format.

Best practices we followed:
- Use consistent labels across services (`env`, `region`, `instance`)
- Avoid high cardinality metrics (e.g., userId)
- Instrument business metrics alongside infra ones

We also added service metadata into `info` metrics to improve traceability.

Format clarity makes onboarding new team members much easier.
