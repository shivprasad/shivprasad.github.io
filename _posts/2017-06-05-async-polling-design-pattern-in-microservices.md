---
title: "Async Polling Design Pattern in Microservices"
date: 2017-06-05 03:30:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - async
  - polling
authors:
  - shiv
---

Instead of blocking for results, async polling lets clients:
- Trigger request
- Poll status endpoint
- Get result once ready

Common in payment, analytics, export flows.

Always include status and retry-after hints in polling responses.
