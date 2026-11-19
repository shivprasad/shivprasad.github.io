---
title: "Lessons from Taming Clock Skew in Distributed Jobs"
date: 2013-11-10 10:47:00 -0800
categories:
  - Tech
  - Distributed Systems
tags:
  - clock-skew
  - distributed-computing
  - retries
  - scheduling
authors:
  - shiv
---

We ran into a strange issue: scheduled jobs running "twice" or not at all across nodes. The culprit? **Clock skew**.

In distributed systems, time is an illusion—but you still need *some* notion of coordination. What helped:
- Using `ntpd` and tighter clock sync configurations
- Avoiding “run at exactly X” semantics
- Designing retries with **logical idempotency**

These bugs are rare, but they teach you humility. Distributed systems are always one leap second away from surprising you.
