---
title: "Eventual Consistency Patterns in Microservices"
date: 2016-07-04 03:00:00 -0700
categories:
  - Tech
  - Distributed Systems
tags:
  - eventual-consistency
  - microservices
authors:
  - shiv
---

In microservices, strong consistency is often too costly — eventual consistency is the norm.

Patterns that help:
- Outbox pattern with change data capture (CDC)
- Retry queues with exponential backoff
- Tombstone records for deletes

Testing for eventual consistency takes effort — simulate time and retries.
