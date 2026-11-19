---
title: "Running LLM Agents in Production: Hard Lessons"
date: 2024-11-22 09:45:00 -0800
categories:
  - Blog
  - General
tags:
  - agents
  - llm
authors:
  - shiv
---

Real talk from deploying LLM agents:

- Token leakage through logs is real
- Rate limits hit harder than expected
- Retry logic must be circuit-breaker aware

This space is exciting, but high-maintenance.
