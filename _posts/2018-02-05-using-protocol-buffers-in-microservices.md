---
title: "Using Protocol Buffers in Microservices"
date: 2018-02-05 02:00:00 -0800
categories:
  - Tech
  - Microservices
tags:
  - interservice-communication
  - protobuf
  - serialization
authors:
  - shiv
---

While JSON is human-readable and flexible, it's often not the best choice for internal service-to-service communication.

### Why Protobuf?

- Smaller payload sizes
- Faster (de)serialization
- Strongly typed schema
- Backward compatibility with versioning

I adopted Protobuf for communication between backend services on gRPC and REST. It required an initial tooling setup — codegen for Java and TypeScript clients, shared schemas in a Git repo — but the performance improvements were tangible.

Example schema:

```
syntax = "proto3";

message UserProfile {
  string id = 1;
  string name = 2;
  int32 age = 3;
}

```

JSON is still great for APIs consumed by humans (e.g., web/mobile clients), but for internal services, Protobuf is my new default.
