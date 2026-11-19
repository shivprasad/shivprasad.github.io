---
title: "Effective Zod Patterns for API Validation"
date: 2023-10-26 06:00:00 -0700
categories:
  - Blog
  - General
tags:
  - validation
  - zod
authors:
  - shiv
---

Using Zod for runtime validation?

My go-to patterns:
- `z.object({})` for schema-first mindset
- `.refine()` for custom rules
- Nesting with `.merge()` keeps things DRY

Bonus: reuse same schema for frontend + backend.
