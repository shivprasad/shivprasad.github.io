---
title: "Benchmarking JSON vs Protobuf vs Avro for Internal APIs"
date: 2018-05-01 07:00:00 -0700
categories:
  - Blog
  - General
tags:
  - avro
  - protobuf
  - serialization
authors:
  - shiv
---

As internal microservices grew, so did our payload sizes. I benchmarked JSON, Protobuf, and Avro using realistic data models and the results were telling:

| Format | Size Reduction | Parse Speed Gain |
| --- | --- | --- |
| JSON | Baseline | Baseline |
| Protobuf | ~65% smaller | 3-4x faster |
| Avro | ~50% smaller | 2.5x faster |

TL;DR: JSON remains king for readability and clients, but Protobuf dominated internal APIs for performance.

Here’s a quick Java-based benchmark using JMH:

```
@Benchmark
public void parseWithProtobuf() {
    MyProto.parseFrom(byteArray);
}

```

Outcome: We standardized on Protobuf for service-to-service traffic and retained JSON for edge APIs.
