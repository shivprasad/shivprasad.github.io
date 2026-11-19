---
title: "Improving Observability in Multi-Region Deployments"
date: 2015-11-03 02:45:00 -0800
categories:
  - Tech
  - Observability
tags:
  - grafana
  - monitoring
  - multi-region
authors:
  - shiv
---

Deploying across multiple regions brings new visibility challenges.

Our solution:
- Push metrics to centralized Prometheus + Grafana
- Separate alerts by region
- Use consistent tags (`region`, `role`, `instance`) in all metrics

![Grafana Multi-Region](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Grafana_dashboard.png/800px-Grafana_dashboard.png)

Grafana Multi-Region

You can’t debug what you can’t see.
