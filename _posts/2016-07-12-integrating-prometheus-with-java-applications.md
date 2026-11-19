---
title: "Integrating Prometheus with Java Applications"
date: 2016-07-12 04:20:00 -0700
categories:
  - Tech
  - Java
tags:
  - java
  - metrics
  - prometheus
authors:
  - shiv
---

Prometheus is fast becoming the default choice for metrics.

Integration with Java:
- Use `micrometer` or `simpleclient` library
- Expose `/metrics` endpoint
- Set up alert rules in Prometheus server

![Prometheus Java Metrics](https://prometheus.io/assets/architecture.png)

Prometheus Java Metrics
