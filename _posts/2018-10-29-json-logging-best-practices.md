---
title: "JSON Logging Best Practices"
date: 2018-10-29 04:00:00 -0700
categories:
  - Tech
  - Observability
tags:
  - elk
  - json
  - log
authors:
  - shiv
---

Logging is boring — until it breaks. We migrated to structured JSON logs across services for better parsing and alerting.

Practices that helped:
- Standard keys: `timestamp`, `service`, `level`, `traceId`, `message`
- Avoid nested structures — simple flat JSONs parse faster
- Mask sensitive fields before logging

Toolchain: Logback encoder → Fluent Bit → Elasticsearch

Bonus: enabled JSON parsing in CloudWatch to reduce grep gymnastics.
