---
title: "Writing Developer Notes with AsciiDoc"
date: 2015-04-22 04:15:00 -0700
categories:
  - Blog
  - General
tags:
  - asciidoc
  - developer-experience
authors:
  - shiv
---

Markdown is great, but [AsciiDoc](https://asciidoc.org/) won me over for internal tech notes.

- Rich formatting with minimal effort
- Native callouts, includes, and table support
- Integrates beautifully with Spring REST Docs

Here's a sample:

```
= My API Guide
Shiv Bade <shiv@byteco.de>

== Authentication

include::auth.adoc[]

```

It made documenting API behavior far more maintainable.
