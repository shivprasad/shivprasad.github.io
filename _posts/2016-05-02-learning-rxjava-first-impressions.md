---
title: "Learning RxJava: First Impressions"
date: 2016-05-02 06:20:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - reactive
  - rxjava
authors:
  - shiv
---

Spent time diving into RxJava.

Insights:
- `Observable` pipelines feel clean and concise
- Great for streaming data and async workflows
- Debugging can be tricky — use `.doOnNext` and `Schedulers.trampoline()` in tests

![RxJava Stream](https://raw.githubusercontent.com/wiki/ReactiveX/RxJava/images/rx-operators/merge.png)

RxJava Stream

It’s functional programming meets async.
