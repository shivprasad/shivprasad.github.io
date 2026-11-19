---
title: "Building REST Clients with Retrofit 2"
date: 2018-08-26 07:30:00 -0700
categories:
  - Blog
  - General
tags:
  - client
  - rest
  - retrofit
authors:
  - shiv
---

On Android and JVM, [Retrofit 2](https://square.github.io/retrofit/) became my go-to HTTP client.

Setup was easy:

```
Retrofit retrofit = new Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build();

```

I especially liked:
- Interface-based declarative APIs
- Easy mocking with interceptors
- Integration with RxJava

A must-have when working with external APIs.
