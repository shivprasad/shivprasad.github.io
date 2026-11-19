---
title: "Why We’re Moving Node Backends to TypeScript"
date: 2020-04-20 07:00:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - node.js
  - typescript
authors:
  - shiv
---

The amount of time we've saved just catching bugs at compile time is ridiculous.

Benefits of TypeScript:
- Eliminates a whole class of undefined/null bugs
- Autocomplete with rich editor support (VSCode FTW)
- Better refactoring across a large codebase

Gotchas:
- Type definitions for third-party modules are sometimes stale
- CI/CD performance needs tuning with strict mode

Still: TypeScript is the default now. Vanilla JS is legacy.
