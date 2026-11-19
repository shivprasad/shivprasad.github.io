---
title: "Jaeger vs Zipkin: What We Chose for Tracing"
date: 2019-08-15 06:00:00 -0700
categories:
  - Blog
  - General
tags:
  - jaeger
  - tracing
  - zipkin
authors:
  - shiv
---

We evaluated both Jaeger and Zipkin for distributed tracing.

Zipkin:
- Lightweight
- Simpler UI
- Easier to get started

Jaeger:
- Native support for OpenTelemetry
- Richer UI with dependency graph
- Better scalability in larger setups

We chose Jaeger, especially with OpenTracing/OpenTelemetry convergence.

Tip: Start small with a single service and build out from there.
