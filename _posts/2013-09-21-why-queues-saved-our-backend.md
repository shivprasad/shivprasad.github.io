---
title: "Why Queues Saved Our Backend"
date: 2013-09-21 08:27:00 -0700
categories:
  - Tech
  - Backend
tags:
  - async-processing
  - backpressure
  - message-queues
  - scalability
authors:
  - shiv
---

We hit a wall once—literally. Our backend crashed during a peak event due to synchronous overloads. The fix wasn’t bigger servers; it was **better architecture**.

Message queues helped us:
- Decouple ingestion from processing
- Introduce graceful degradation
- Add retry mechanisms and dead-letter paths

Since then, queues became a default tool in my design toolbox. The key isn’t just adding a queue—it’s **designing for failure across the pipe**.
