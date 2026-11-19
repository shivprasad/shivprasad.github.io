---
title: "Working with java.time.Temporal API"
date: 2018-02-05 06:30:00 -0800
categories:
  - Tech
  - Java
tags:
  - date-time
  - temporal
authors:
  - shiv
---

I used to fear date and time handling in Java — until the `java.time` API landed in Java 8.

This quarter, I finally explored the `TemporalAdjusters` and custom parsing capabilities. Here's a quick example:

```
LocalDate firstMonday = LocalDate.now()
    .with(TemporalAdjusters.firstInMonth(DayOfWeek.MONDAY));

```

It’s clean, immutable, and handles DST transitions better than JodaTime ever did.

If you're still using `Date` or `Calendar`, it’s time to switch. The type safety and predictability of `java.time` is a huge productivity booster.
