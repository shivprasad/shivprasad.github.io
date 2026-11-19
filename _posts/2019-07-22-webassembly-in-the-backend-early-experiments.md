---
title: "WebAssembly in the Backend? Early Experiments"
date: 2019-07-22 07:15:00 -0700
categories:
  - Blog
  - General
tags:
  - wasm
  - webassembly
authors:
  - shiv
---

WebAssembly isn’t just for browsers. We ran some internal experiments with Wasm on the backend.

Use cases explored:
- Plugin systems for untrusted user logic
- Language-agnostic sandboxing
- Execution isolation in edge compute setups

We tried out:
- Wasmer for server-side execution
- Lucet for ahead-of-time compiled modules

Still early, but promising for multi-tenant scenarios and reducing cold starts.
