---
title: "Debugging DNS Issues in Kubernetes"
date: 2018-04-04 02:30:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - dns
  - k8s
  - troubleshooting
authors:
  - shiv
---

DNS issues in Kubernetes are notoriously tricky to pin down. Around this time, we noticed intermittent failures in service resolution, affecting inter-pod communication across namespaces.

Common patterns included:
- Services resolving to outdated IPs
- CoreDNS pods getting OOMKilled
- `nxdomain` errors under high pod churn

Here's how we tackled it:
- Upgraded to CoreDNS and customized our `ConfigMap` to reduce aggressive caching
- Switched to headless services for StatefulSets to eliminate surprise DNS lookups
- Traced issues using `tcpdump` and `kubectl exec` with `dig`

Debug snippet:

```
kubectl exec busybox -- nslookup my-service.default.svc.cluster.local

```

This exercise reminded us of a simple truth: always include DNS behavior in your Kubernetes runbooks.
