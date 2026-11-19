---
title: "Introducing k6 for Load Testing APIs"
date: 2019-04-13 03:30:00 -0700
categories:
  - Blog
  - General
tags:
  - k6
  - load-testing
  - performance
authors:
  - shiv
---

We recently moved away from JMeter and Gatling for API load testing and tried out [k6](https://k6.io/).

Highlights:
- Scripted in JavaScript, very developer-friendly
- Integrated easily with CI
- Built-in support for thresholds and checks

A sample test:

```
import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  let res = http.get('https://my-api.com/health');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}

```

Highly recommend it for modern DevOps teams.
