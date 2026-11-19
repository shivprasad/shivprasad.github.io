---
title: "Your Systems Need a Health Check Too"
date: 2014-05-01 02:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - health-checks
  - liveness
  - readiness
  - resilience
authors:
  - shiv
---

You wouldn’t deploy code without tests. So why deploy services without **health checks**?

2014 was the year we got serious about:
- Liveness checks (is it running?)
- Readiness checks (can it handle traffic?)
- Dependency isolation (fail early if upstream is down)

![Health Check Pyramid](https://miro.medium.com/v2/resize:fit:720/format:webp/1*0FiM7Efu5VaHHRQ3ejRGGQ.png)

Health Check Pyramid

Health checks became the **first line of resilience**. They’re not optional anymore.
