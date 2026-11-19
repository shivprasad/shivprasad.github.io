---
title: "Design Patterns for Idempotency in Distributed Systems"
date: 2016-04-05 02:45:00 -0700
categories:
  - Tech
  - Distributed Systems
tags:
  - design-patterns
  - idempotency
authors:
  - shiv
---

In any retry-prone system — payment gateways, provisioning services, async job queues — idempotency is your safety net.

Patterns:
- Client-generated UUIDs
- Idempotency keys with deduplication storage
- Replay protection using Redis or database constraints

Example: Stripe’s use of Idempotency-Key header is a textbook implementation.

Make sure your side effects are idempotent or cancel-safe.
