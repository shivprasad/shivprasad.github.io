---
title: "Tracking State in Event-Sourced Systems"
date: 2016-12-04 05:30:00 -0800
categories:
  - Blog
  - General
tags:
  - cqrs
  - event-sourcing
authors:
  - shiv
---

In event sourcing, your current state is a replay away.

Key practices:
- Snapshotting to reduce read time
- Append-only logs and immutability
- Using projections for read-side optimization

State = sum of events, not a snapshot in time.
