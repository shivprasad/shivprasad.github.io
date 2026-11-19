---
title: "Kubernetes Networking Basics Explained"
date: 2019-04-04 02:00:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - k8s
  - networking
authors:
  - shiv
---

Networking in Kubernetes isn't as intuitive as people expect.

Here's what helped me understand it:
- Every Pod gets its own IP
- All Pods on a Node share the same network namespace
- Services act as virtual IPs backed by endpoints (Pods)
- `kube-proxy` sets up NAT rules for cluster traffic

Debug tip: use `kubectl exec` into busybox or alpine pod to test DNS/HTTP endpoints internally.

Bonus tool: [netshoot](https://github.com/nicolaka/netshoot) has been super helpful for debugging traffic.
