---
title: "Introducing Throttling to Downstream APIs"
date: 2015-02-28 08:00:00 -0800
categories:
  - Blog
  - General
tags:
  - api-gateway
  - load-shedding
  - throttling
authors:
  - shiv
---

After a sudden traffic surge brought down a partner API, we built in throttling using Spring Cloud Gateway and a basic token bucket algorithm.

Sample config:

```
spring:
  cloud:
    gateway:
      routes:
        - id: throttled_route
          uri: http://backend/
          predicates:
            - Path=/partner/**
          filters:
            - name: RequestRateLimiter
              args:
                redis-rate-limiter.replenishRate: 10
                redis-rate-limiter.burstCapacity: 20

```

With Redis-backed rate limiting, we shed load predictably and protected upstream services.

If your system fails under unexpected load, it's not reliable — it's fragile.
