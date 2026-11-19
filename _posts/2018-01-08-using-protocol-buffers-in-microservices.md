---
title: "Using Protocol Buffers in Microservices"
date: 2018-01-08 02:00:00 -0800
categories:
  - Tech
  - Microservices
tags:
  - protobuf
  - serialization
authors:
  - shiv
---

JSON is great for human readability, but once you’re exchanging high volumes of messages between internal services, its verbosity becomes a real issue.

That’s where Protocol Buffers (Protobuf) come in. Around this time, I started replacing JSON with Protobuf in our gRPC-based services. The results were significant — payload sizes dropped by over 60% and response times improved.

Sample `.proto` file:

```
syntax = "proto3";
message Product {
  string id = 1;
  string name = 2;
  float price = 3;
}

```

Using it in Java was simple with Maven plugins. One thing I learned early — versioning matters. Backward compatibility isn’t a given unless you respect field numbering rules.

Overall, Protobuf has been an excellent fit for internal communication, while we still serve JSON externally.
