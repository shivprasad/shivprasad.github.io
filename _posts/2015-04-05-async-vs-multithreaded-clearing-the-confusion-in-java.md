---
title: "Async vs Multithreaded: Clearing the Confusion in Java"
date: 2015-04-05 03:20:00 -0700
categories:
  - Tech
  - Java
tags:
  - asynchronous
  - futures
  - threads
authors:
  - shiv
---

While reviewing a backend service, I noticed a pattern of overusing threads where async callbacks would've been sufficient. So I wrote this primer to clarify:

- Use threads for CPU-bound work
- Use async (e.g., CompletableFuture) for I/O-bound tasks
- Avoid spawning threads in loops — use executor services

Example:

```
CompletableFuture.supplyAsync(() -> fetchData())
                 .thenApply(this::process)
                 .thenAccept(this::persist);

```

Async = better resource utilization. Threads = power tools. Use wisely.
