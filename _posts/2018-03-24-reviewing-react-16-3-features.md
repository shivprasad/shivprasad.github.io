---
title: "Reviewing React 16.3 Features"
date: 2018-03-24 06:30:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - context-api
  - react
authors:
  - shiv
---

React 16.3 introduced a few important changes:

- **New Context API**: way cleaner and easier to use
- `getDerivedStateFromProps` replacing legacy lifecycles
- Forwarding Refs for HOCs

The new context API simplified theme handling in one of our internal dashboards. No more contextType gymnastics.

Also, the gradual deprecation of legacy lifecycles sent a strong message: modernize or be left behind.
