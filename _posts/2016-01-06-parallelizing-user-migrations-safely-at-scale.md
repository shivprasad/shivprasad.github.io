---
title: "Parallelizing User Migrations Safely at Scale"
date: 2016-01-06 02:30:00 -0800
categories:
  - Blog
  - General
tags:
  - migrations
  - parallelism
  - scalability
authors:
  - shiv
---

At high volumes, user migrations need to be parallel — but safe.

Key issues:
- Avoiding race conditions and overloading partitions
- Coordinating steps across services
- Respecting dependencies and consistency

Techniques:
- Partition-level concurrency caps
- Leases with TTL to avoid duplicate execution
- Rate-limited task queues and failure queues

Diagrams helped explain coordination strategies to teams.
