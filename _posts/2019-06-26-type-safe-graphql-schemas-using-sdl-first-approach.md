---
title: "Type-Safe GraphQL Schemas using SDL-first Approach"
date: 2019-06-26 02:45:00 -0700
categories:
  - Blog
  - General
tags:
  - graphql
  - schema
authors:
  - shiv
---

We started moving to a schema-first approach using GraphQL SDL + code generation.

Tools used:
- `graphql-tools` (JS)
- `graphql-codegen` for TypeScript typings
- `Apollo Federation` experiments (early days)

Advantages:
- Clear API contracts
- Faster onboarding
- IDE autocomplete and static checks

Watch out: schema drift is real — enforce schema registry and CI validation.
