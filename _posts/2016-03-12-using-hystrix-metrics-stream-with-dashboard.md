---
title: "Using Hystrix Metrics Stream with Dashboard"
date: 2016-03-12 03:00:00 -0800
categories:
  - Tech
  - Microservices
tags:
  - hystrix
  - metrics
authors:
  - shiv
---

Hystrix provides a real-time metrics stream that feeds directly into dashboards.

Setup:
- Expose stream endpoint: `/hystrix.stream`
- Plug it into Hystrix Dashboard
- Watch circuit status, thread pool health, latency

![Hystrix Dashboard](https://netflix.github.io/Hystrix/images/hystrix-dashboard.png)

Hystrix Dashboard

Helps spot slowdowns before they escalate.
