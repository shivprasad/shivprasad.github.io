---
title: "Spring Boot Actuator in Practice"
date: 2017-04-18 04:00:00 -0700
categories:
  - Tech
  - Java
tags:
  - actuator
  - metrics
authors:
  - shiv
---

Spring Boot Actuator exposes operational info for free.

Useful endpoints:
- `/health`
- `/metrics`
- `/env`
- `/loggers`

Add micrometer for Prometheus integration:

```
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>

```
