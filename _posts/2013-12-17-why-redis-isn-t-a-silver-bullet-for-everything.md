---
title: "Why Redis Isn’t a Silver Bullet for Everything"
date: 2013-12-17 06:25:00 -0800
categories:
  - Blog
  - General
tags:
  - caching
  - design-tradeoffs
  - redis
  - scalability
authors:
  - shiv
---

Redis was (and is) amazing. In-memory speed, rich data types, pub-sub — a Swiss army knife for backend engineers.

But I learned in 2013 that **abusing Redis as a database** is a recipe for tears.

What went wrong:
- Used as a cache with no eviction policy — memory spiked fast
- Used for critical state without persistence — lost data during failover
- Used as a queue with no visibility — debugging became guesswork

We fixed it by:
- Using proper write-through patterns
- Adding backups and monitoring keys
- Treating Redis as **ephemeral, not durable**

![Redis Logo](https://upload.wikimedia.org/wikipedia/en/6/6b/Redis_Logo.svg)

Redis Logo

Every tool has a sharp edge. You just need to know where it cuts.
