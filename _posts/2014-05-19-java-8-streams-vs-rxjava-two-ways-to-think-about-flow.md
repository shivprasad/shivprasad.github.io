---
title: "Java 8 Streams vs RxJava: Two Ways to Think About Flow"
date: 2014-05-19 10:35:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - java-8
  - reactive
  - rxjava
  - streams
authors:
  - shiv
---

Java 8’s **Streams API** made pipelines readable. But as we explored async workloads, **RxJava** gave us even more control.

Differences I felt:
- Streams = pull-based, synchronous
- Rx = push-based, async-ready

We used both — Streams for in-memory transformations, Rx for UI + backend coordination.

![Rx vs Stream](https://res.cloudinary.com/practicaldev/image/fetch/s--THeYg5aA--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://i.imgur.com/j4iNwl2.png)

Rx vs Stream

This was my first real embrace of **reactive thinking** in production.
