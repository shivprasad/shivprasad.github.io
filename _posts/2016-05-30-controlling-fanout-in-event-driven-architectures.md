---
title: "Controlling Fanout in Event-Driven Architectures"
date: 2016-05-30 09:15:00 -0700
categories:
  - Blog
  - General
tags:
  - event-driven
  - fanout
authors:
  - shiv
---

Event fanout is powerful, but unbounded fanout causes chaos.

Techniques:
- TTL + retry caps in queue handlers
- De-duplication with event IDs
- Throttling subscriptions via fanout controllers

Architecting for fanout control leads to better system predictability.
