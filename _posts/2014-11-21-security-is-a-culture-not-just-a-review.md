---
title: "Security Is a Culture, Not Just a Review"
date: 2014-11-21 10:10:00 -0800
categories:
  - Blog
  - General
tags:
  - code-quality
  - review-process
  - security
  - shift-left
authors:
  - shiv
---

We recently caught a high-risk issue in review — something a tool would’ve missed. It reminded me that **security is a mindset**, not a checklist.

Here’s what we changed:
- Made security part of design discussions
- Added threat modeling to architecture reviews
- Built static analysis and secrets detection into CI

![Security Layers](https://owasp.org/www-project-top-ten/assets/images/OWASP-Top-10-2017.png)

Security Layers

If your security only starts at the end of the sprint, you’re already behind.
