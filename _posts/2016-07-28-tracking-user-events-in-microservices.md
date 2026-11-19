---
title: "Tracking User Events in Microservices"
date: 2016-07-28 02:30:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - event-tracking
  - microservices
authors:
  - shiv
---

Centralized logging is not enough — we needed user event trails across services.

Tools:
- Kafka with Avro schema
- Unique trace IDs
- Schema registry for evolution

This helped correlate issues, even weeks after they occurred.
