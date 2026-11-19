---
title: "Building Resilient Systems: Circuit Breakers with Hystrix"
date: 2015-04-15 06:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - fallback
  - hystrix
  - resilience
authors:
  - shiv
---

A recent production issue reminded us: never trust remote systems to behave.

We integrated [Netflix Hystrix](https://github.com/Netflix/Hystrix) to wrap remote calls with:
- Circuit breaker
- Timeout
- Fallback

Sample snippet:

```
@HystrixCommand(fallbackMethod = "defaultResponse")
public String getProfile(String id) {
    return profileService.call(id);
}

public String defaultResponse(String id) {
    return "unavailable";
}

```

One timeout shouldn’t bring down your system. Hystrix made sure of that.
