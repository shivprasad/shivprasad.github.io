---
title: "Spring Boot: Writing Custom Health Indicators"
date: 2016-01-14 05:00:00 -0800
categories:
  - Tech
  - Java
tags:
  - health-checks
  - spring-boot
authors:
  - shiv
---

Spring Boot lets you expose custom health checks using `HealthIndicator`.

Sample:

```
@Component
public class QueueHealthIndicator implements HealthIndicator {
    public Health health() {
        if (queue.isAvailable()) {
            return Health.up().build();
        } else {
            return Health.down().withDetail("queue", "Unavailable").build();
        }
    }
}

```

Useful for circuit breakers, dashboards, and alerts.
