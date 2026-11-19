---
title: "Track Everything? Only If You Can Query Everything Too"
date: 2014-03-10 07:50:00 -0700
categories:
  - Tech
  - Observability
tags:
  - analytics
  - event-tracking
  - logging
  - metrics
authors:
  - shiv
---

In the [ThoughtWorks Radar (Mar 2014)](https://www.thoughtworks.com/radar/techniques/event-sourcing), the rise of **event-based tracking** was clear. Everyone wanted to log everything — page views, API hits, job states.

But I learned the hard way: **tracking without insight is tech debt**.

Tips that helped:
- Structure logs as events, not just text
- Define tracking goals before you emit data
- Invest in dashboards + drill-down tooling

![Track Everything Meme](https://i.imgur.com/Q3AvCxl.png)

Track Everything Meme

Track what matters. Delete what doesn’t. Store nothing you don’t intend to read.
