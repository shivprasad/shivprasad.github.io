---
title: "Migrating User Data with Zero Downtime: Lessons from the Field"
date: 2015-07-05 03:00:00 -0700
categories:
  - Blog
  - General
tags:
  - migration
  - user-data
  - zero-downtime
authors:
  - shiv
---

This quarter I began working on a large-scale user data migration system. The challenge? Move millions of users across partitions *without* impacting availability or data consistency.

Problem:
- Each user’s data spans multiple services
- Downtime wasn’t acceptable
- Some operations required cross-service consistency

Key strategies:
- Used a shadow copy + cutover approach
- Built a retry-safe orchestration layer with idempotent steps
- Eventual consistency was embraced, but with strong observability

Diagrams and rate-limited queues helped ensure smooth rollouts.

If you can’t pause the system, evolve it while running.
