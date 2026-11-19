---
title: "Designing Background Jobs for Safety and Efficiency"
date: 2016-11-10 04:00:00 -0800
categories:
  - Tech
  - Backend
tags:
  - background-jobs
  - task-queues
authors:
  - shiv
---

Background workers sound simple but can be risky.

Design considerations:
- At-least-once vs at-most-once
- Idempotency in job handlers
- Retry, visibility timeout, and dead-letter queues

Queue tools: Sidekiq, RabbitMQ, Amazon SQS.
