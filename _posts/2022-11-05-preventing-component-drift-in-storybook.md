---
title: "Preventing Component Drift in Storybook"
date: 2022-11-05 04:00:00 -0700
categories:
  - Blog
  - General
tags:
  - design-systems
  - storybook
authors:
  - shiv
---

Storybook is great for visual testing, but:

- Stories can drift from reality
- Snapshots ≠ real use

We use “golden states” linked to real props + mocks from staging data. Keeps things honest.
