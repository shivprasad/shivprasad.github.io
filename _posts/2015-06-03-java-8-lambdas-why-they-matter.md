---
title: "Java 8 Lambdas: Why They Matter"
date: 2015-06-03 10:20:00 -0700
categories:
  - Tech
  - Java
tags:
  - java8
  - lambdas
authors:
  - shiv
---

I finally embraced Java 8 lambdas this quarter — they made my unit tests cleaner and data transformations tighter.

Before:

```
Collections.sort(list, new Comparator<>() {
  public int compare(String a, String b) { return a.compareTo(b); }
});

```

After:

```
list.sort((a, b) -> a.compareTo(b));

```

The difference is more than syntax — it's a mindset shift.
