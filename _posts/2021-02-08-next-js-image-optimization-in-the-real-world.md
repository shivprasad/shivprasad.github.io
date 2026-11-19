---
title: "Next.js Image Optimization in the Real World"
date: 2021-02-08 02:00:00 -0800
categories:
  - Blog
  - General
tags:
  - image
  - nextjs
  - performance
authors:
  - shiv
---

Next.js introduced a new `<Image />` component with built-in optimization.

We tested it on our product pages:
- WebP served automatically
- Lazy loading by default
- Resizing on demand

Caveats:
- Need a custom loader for non-Vercel hosting
- Dev builds can feel slower

Net result: faster loads, better Lighthouse scores.
