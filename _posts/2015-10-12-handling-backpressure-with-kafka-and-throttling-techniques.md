---
title: "Handling Backpressure with Kafka and Throttling Techniques"
date: 2015-10-12 05:30:00 -0700
categories:
  - Blog
  - General
tags:
  - backpressure
  - kafka
  - rate-limiting
authors:
  - shiv
---

Our message processing system needed to deal with backpressure gracefully — without dropping critical messages or overloading downstream systems.

Techniques used:
- Consumer rate limiting using pause/resume
- Monitoring `lag` and adjusting consumer thread pools
- Integrating circuit breakers for downstream APIs

Sample code:

```
if (tooMuchLag()) {
  consumer.pause(partitions);
}

```

Backpressure isn’t failure — it’s feedback. Design for it.
