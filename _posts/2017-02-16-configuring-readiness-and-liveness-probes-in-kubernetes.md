---
title: "Configuring Readiness and Liveness Probes in Kubernetes"
date: 2017-02-16 03:00:00 -0800
categories:
  - Tech
  - Kubernetes
tags:
  - kubernetes
  - liveness-probe
  - readiness-probe
authors:
  - shiv
---

Probes are critical for resilient services in Kubernetes.

- Readiness: Is the app ready to accept traffic?
- Liveness: Should the container be restarted?

YAML snippet:

```
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

```

Tune thresholds carefully — too strict and you’ll cause restarts.
