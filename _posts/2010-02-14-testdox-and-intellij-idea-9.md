---
title: "TestDox and IntelliJ IDEA 9"
date: 2010-02-14 14:01:00 -0800
categories:
  - Blog
  - General
tags:
  - idea
  - testdox
---

I really missed [TestDox](http://testdox.codehaus.org) plugin for IDEA. There is no official version as of now for IDEA 9.0
I tried to install latest available version but its not compatible. I played around with plugin.xml by removing *until-build="IU-93.94"*, it got enabled but then threw following exception,

```
Caused by: java.lang.NumberFormatException: For input string: "IU-93.94"
    at java.lang.NumberFormatException.forInputString(NumberFormatException.java:48)
    at java.lang.Integer.parseInt(Integer.java:449)
    at java.lang.Integer.parseInt(Integer.java:499)
    at org.codehaus.testdox.intellij.IntelliJApiFactory.<init>(IntelliJApiFactory.java:24)

```

I had patched the IntelliJApiFactory and updated .class file in the testdox-plugin-1.1.12-diana.jar. I am using it for some time and my usage is limited to navigate between class and its test. Not seeing any exceptions but overall IDEA 9.x plugin api are changed a lot and using a patched plugin might crash IDEA.
But for those who can't live without it, can download it [here](http://drop.io/testdox_idea_plugin/asset/testdox-plugin-zip). Extract it to your IDEA plugins directory.
