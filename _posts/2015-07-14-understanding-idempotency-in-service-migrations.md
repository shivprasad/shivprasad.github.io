---
title: "Understanding Idempotency in Service Migrations"
date: 2015-07-14 07:30:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - idempotency
  - microservices
authors:
  - shiv
---

During a migration effort, I had to re-execute failed steps safely — again and again. That’s when idempotency became a first-class citizen.

Concepts:
- Idempotency ensures operations can be retried without unintended effects
- It often requires designing stateless actions or storing operation logs
- `PUT` and `DELETE` in REST are idempotent by convention — but custom logic must also respect this

Tips:
- Use external request IDs for tracing
- Maintain an idempotency key per transactional unit
- Audit logs help verify safe replays

Building resilient migrations = building with retry in mind.
