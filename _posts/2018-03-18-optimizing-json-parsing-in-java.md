---
title: "Optimizing JSON Parsing in Java"
date: 2018-03-18 02:45:00 -0700
categories:
  - Tech
  - Java
tags:
  - jackson
  - json
  - performance
authors:
  - shiv
---

We had an API that slowed under large JSON payloads. After profiling, it turned out the bottleneck was in Jackson parsing.

Tweaks that helped:
- Used `@JsonProperty` annotations to reduce reflection
- Disabled `FAIL_ON_UNKNOWN_PROPERTIES`
- Enabled stream-based parsing where applicable

Bonus: We benchmarked Jackson vs Gson vs Moshi. Jackson won for speed, but Moshi impressed with predictability.

Java may not be a “fast” language for JSON, but with the right config, you can squeeze out solid performance.
