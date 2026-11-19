---
title: "Why I Stopped Using XML for Configuration"
date: 2013-07-30 13:11:00 -0700
categories:
  - Blog
  - General
tags:
  - xml
  - yaml
  - code-readability
  - configuration
authors:
  - shiv
---

Once upon a time, I had entire deployment scripts, server configs, and Spring beans defined in XML. It worked—until it didn’t. Debugging deeply nested structures and understanding overrides across environments became painful.

Around this time, I started migrating to **YAML and annotation-based configuration**, and the experience felt refreshing. The code became self-documenting, and the delta between dev and prod setups became easier to reason about.

This post isn’t an anti-XML rant. It’s a recognition that **readability and maintainability** should be first-class goals, not afterthoughts.

What I learned:
- Prefer formats that support diffs well (and are human-friendly).
- Layered configs are fine, but keep them discoverable.
- Declarative is good—until you need control flow. Know where to draw the line.
