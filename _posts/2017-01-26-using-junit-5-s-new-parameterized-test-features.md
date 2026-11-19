---
title: "Using JUnit 5’s New Parameterized Test Features"
date: 2017-01-26 02:45:00 -0800
categories:
  - Tech
  - Java
tags:
  - java
  - junit5
authors:
  - shiv
---

JUnit 5 finally makes parameterized tests a first-class citizen.

Sample usage:

```
@ParameterizedTest
@ValueSource(strings = {"hello", "world"})
void testWithStrings(String word) {
    assertNotNull(word);
}

```

Cleaner APIs, better IDE support — makes test coverage easier to reason about.
