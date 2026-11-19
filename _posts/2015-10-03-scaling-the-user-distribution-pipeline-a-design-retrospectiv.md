---
title: "Scaling the User Distribution Pipeline: A Design Retrospective"
date: 2015-10-03 03:15:00 -0700
categories:
  - Blog
  - General
tags:
  - pipeline
  - scalability
  - user-distribution
authors:
  - shiv
---

One of the big design shifts this quarter involved scaling a pipeline that distributes users across services based on data center location and available resources.

Key requirements:
- Resilient to retries
- Partition-aware routing
- Trackable from ingestion to delivery

Solution elements:
- Kafka for buffered ingestion
- Shard mapping based on consistent hashing
- Periodic audits with compensation workflows

This pattern borrows from event sourcing, but with just enough state to stay lightweight.
