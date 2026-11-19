---
title: "Event-Driven Architecture: Common Patterns and Pitfalls"
date: 2019-07-04 03:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - event-driven
  - kafka
  - microservices
authors:
  - shiv
---

Event-driven systems bring scalability and decoupling, but they also introduce challenges.

Common patterns we implemented:
- Event Sourcing: storing state changes as events
- CQRS: separating write and read models
- Outbox pattern: ensuring consistency between DB and event publishing

Pitfalls:
- Lack of traceability across async hops
- Event schema versioning issues
- Difficult debugging without a centralized log

Tip: Invest in an event registry and distributed tracing early.
