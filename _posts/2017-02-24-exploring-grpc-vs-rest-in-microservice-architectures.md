---
title: "Exploring gRPC vs REST in Microservice Architectures"
date: 2017-02-24 05:30:00 -0800
categories:
  - Blog
  - General
tags:
  - grpc
  - rest
authors:
  - shiv
---

gRPC is fast, but is it always better than REST?

Benefits:
- HTTP/2 multiplexing
- Protobuf = smaller payloads
- Codegen for clients

Caveats:
- Debugging not as straightforward
- Streaming and error handling need careful design

Verdict: Ideal for internal service-to-service calls, not always for public APIs.
