---
title: "Eclipse Code Formatter - IntelliJ IDEA"
date: 2011-12-02 13:54:00 -0800
categories:
  - Tech
  - Java
tags:
  - eclipse
  - code-formatter
  - idea
  - intellij
  - java
---

When working with a team of developers spread across globe, one challenge is to maintain code formatting.
Most of teams using Eclipse as their primary IDE, rely on Eclipse code formatter that can be configured by enabling project specific setting and then adding **/.settings** directory to version control system. This directory contains **org.eclipse.jdt.core.prefs** which has formatting details.
Since these files are part of version control, all developers now has these settings file and formatting changes gets applied automatically on saving file.
But if you are an IDEA user, then there ~~is~~ was no way to use these Eclipse code formatting.
To make life somewhat easy, over the weekend I created a small plugin which basically let you use the Eclipse Code Formatter from IDEA. The main feature of this is that you can apply these on a Change List. Change List in IDEA is basically list of files that you have modified/created and are going to commit.
For more details visit project page - [eclipse-code-formatter-on-change-list](http://code.google.com/p/eclipse-code-formatter-on-change-list/)
The plugin is also available in [IDEA plugin repository](http://plugins.intellij.net/plugin/?idea&id=6566).
