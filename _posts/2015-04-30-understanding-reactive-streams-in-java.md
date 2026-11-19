---
title: "Understanding Reactive Streams in Java"
date: 2015-04-30 11:40:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - backpressure
  - reactive
  - rxjava
authors:
  - shiv
---

With [Reactive Streams](https://www.reactive-streams.org/) picking up momentum, I explored RxJava in a pet project.

Highlights:
- `Observable` chains made transformation pipelines elegant
- Backpressure helps handle overload gracefully
- Debugging flow was hard — tooling needs to catch up

Sample:

```
Observable.just("a", "b", "c")
          .map(String::toUpperCase)
          .subscribe(System.out::println);

```

Promising model — but needs discipline.
