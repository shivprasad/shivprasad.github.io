---
title: "Rate Limiting User Operations to Prevent Abuse"
date: 2016-02-22 01:30:00 -0800
categories:
  - Blog
  - General
tags:
  - abuse-prevention
  - rate-limiting
authors:
  - shiv
---

We implemented rate-limiting logic to prevent abuse of APIs — especially account creation and login flows.

Strategy:
- Redis-based counters with expiration
- Hash keys per user/IP/action
- Dynamic throttling based on request behavior

Sample:

```
INCR login:user123
EXPIRE login:user123 60

```

Simple but powerful — especially when applied defensively.
