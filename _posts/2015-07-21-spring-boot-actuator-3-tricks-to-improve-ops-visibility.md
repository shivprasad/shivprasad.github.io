---
title: "Spring Boot Actuator: 3 Tricks to Improve Ops Visibility"
date: 2015-07-21 09:15:00 -0700
categories:
  - Tech
  - Java
tags:
  - observability
  - spring-boot
authors:
  - shiv
---

Spring Boot’s [Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html) endpoints made it easier to monitor our service internals.

3 tips:
- Enable `/env` and `/metrics` with access control
- Expose custom metrics via `MeterRegistry`
- Combine with Grafana dashboards for live alerts

Sample config:

```
management.endpoints.web.exposure.include: "*"

```

Ops teams love it when services are self-reporting.
