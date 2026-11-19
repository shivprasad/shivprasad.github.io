---
title: "Engineering Judgment: When Not to Scale"
date: 2014-07-08 03:30:00 -0700
categories:
  - Blog
  - General
tags:
  - design-maturity
  - eb1a
  - scalability
  - tradeoffs
authors:
  - shiv
---

Not every problem needs to be solved at scale.

In 2014, we had a service that was underperforming. Everyone reached for: sharding, async queues, auto-scaling groups.

But the actual fix? Rewrite a 40-line SQL query with proper indexing.

![Scaling Triangle](https://miro.medium.com/v2/resize:fit:720/format:webp/1*OaJ0U-KMRtVpz1z5YqLKHg.png)

Scaling Triangle

Scalability is sexy, but **judgment is leadership**. Knowing *when not to scale* is just as important.
