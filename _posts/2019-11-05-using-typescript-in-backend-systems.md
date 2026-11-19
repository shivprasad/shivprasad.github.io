---
title: "Using TypeScript in Backend Systems"
date: 2019-11-05 02:00:00 -0800
categories:
  - Tech
  - Frontend
tags:
  - node
  - type-safety
  - typescript
authors:
  - shiv
---

TypeScript isn't just for frontend anymore.

We started migrating our Node.js services to TypeScript.

Pros:
- Catch more issues at compile time
- Improved developer onboarding
- IDE support makes refactoring safer

We used `ts-node-dev` and strict typing mode. Took some effort, but dev confidence is way up.

Lesson: Define shared types via `.d.ts` and keep interfaces small and clean.
