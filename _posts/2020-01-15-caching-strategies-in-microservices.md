---
title: "Caching Strategies in Microservices"
date: 2020-01-15 03:30:00 -0800
categories:
  - Tech
  - Microservices
tags:
  - cache
  - microservices
  - redis
authors:
  - shiv
---

Caching in a microservices setup isn't as simple as just dropping in Redis.

Here’s a quick matrix we used recently:

| Use Case | Cache Type | Notes |
| --- | --- | --- |
| Idempotent lookup | Read-through | Use TTL |
| Aggregated data | Write-behind | Async flush |
| Reference data | Local/Coherent | Watch staleness |

Mistakes we made:
- Cached 404s for too long
- Missed cache invalidation across services

Tools we used: Redis + Caffeine combo.
