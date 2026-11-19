---
title: "Safari Testing Challenges in Frontend Projects"
date: 2018-01-29 08:45:00 -0800
categories:
  - Blog
  - General
tags:
  - safari
  - testing
authors:
  - shiv
---

Safari — the final boss of frontend compatibility.

We faced issues with:
- Date pickers not firing `onChange`
- CORS preflight caching behaving inconsistently
- Font rendering glitches with SVG

We introduced BrowserStack for CI coverage, especially targeting Safari 10 and 11. Still, nothing beats local repros.

Rule of thumb: if your UI works on Safari, it probably works everywhere else too.
