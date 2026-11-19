---
title: "Understanding Liveness vs Readiness in Kubernetes"
date: 2020-07-28 07:30:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - k8s
  - liveness
  - probes
  - readiness
authors:
  - shiv
---

Kubernetes probes are often misunderstood.

- **Readiness** tells when the pod is ready to serve traffic
- **Liveness** tells if the pod should be restarted

Common mistakes:
- Same probe endpoint for both → accidental restart loops
- Readiness not updated after DB disconnect

Best practice: Split endpoints and monitor probe logs during failures.
