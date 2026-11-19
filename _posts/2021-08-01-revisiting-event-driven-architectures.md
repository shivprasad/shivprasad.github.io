---
title: "Revisiting Event-Driven Architectures"
date: 2021-08-01 02:00:00 -0700
categories:
  - Blog
  - General
tags:
  - event-driven
  - kafka
authors:
  - shiv
---

Took a step back this quarter to evaluate our event-driven setup.

Wins:
- Loose coupling helped with parallel development
- Data auditability improved

Challenges:
- Schema evolution is hard
- Tracing and monitoring is tricky

Tools like Kafka + Schema Registry + OpenTelemetry are helping. Event-driven isn't a silver bullet — but worth the investment when done right.
