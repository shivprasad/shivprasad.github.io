---
title: "Micro-Frontend Lessons Learned from Real Projects"
date: 2019-06-02 08:30:00 -0700
categories:
  - Blog
  - General
tags:
  - microfrontend
  - web
authors:
  - shiv
---

Micro-frontends promise modularity, but they come at a cost.

Key takeaways:
- Use a shell app to orchestrate routing and shared state
- Prefer native Web Components or module federation over iframes
- Be strict about versioning and API contracts between teams

When done well, they allow teams to move fast — when done poorly, debugging becomes a nightmare.

Start with a monorepo and shared build tooling to minimize friction.
