---
title: "Scaling Decisions I Got Right (and Wrong) in 2013"
date: 2013-12-28 12:00:00 -0800
categories:
  - Blog
  - General
tags:
  - architecture
  - learning
  - postmortem
  - scalability
authors:
  - shiv
---

2013 was a growth year—not just in traffic, but in architecture maturity. Here’s a candid list of calls I made that aged well (and some that didn’t):

✅ Right:
- Decoupling ingestion and processing via queues
- Introducing retries + dead-letter queues
- Using schema-based events

❌ Wrong:
- Overengineering early microservices
- Delaying schema validation on input
- Underestimating operational toil in scale testing

![System Evolution](https://martinfowler.com/articles/microservices/images/microservice-obstacles.png)

System Evolution

Each decision taught me something about **resilience, observability, and developer velocity**. These are the lessons I carry forward.
