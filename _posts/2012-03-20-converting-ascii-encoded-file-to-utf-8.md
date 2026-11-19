---
title: "Converting ASCII encoded file to UTF-8"
date: 2012-03-20 15:26:00 -0700
categories:
  - Blog
  - General
tags:
---

You get a file whose encoding you don't know and want to convert it to UTF-8 encoded file using java. How to do it?
Below should work -

```
import org.apache.commons.io.IOUtils;
import org.mozilla.universalchardet.UniversalDetector;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
public class Test {
public static void main(String[] args) throws IOException {
byte[] buf = new byte[4096];
String fileName = "Test.txt";
java.io.FileInputStream fis = new java.io.FileInputStream(fileName);
UniversalDetector detector = new UniversalDetector(null);
int nread;
while ((nread = fis.read(buf)) > 0 && !detector.isDone()) {
detector.handleData(buf, 0, nread);
}
detector.dataEnd();
String encoding = detector.getDetectedCharset();
detector.reset();
Reader reader = new InputStreamReader(new FileInputStream("Test.txt"), encoding);
byte[] bytes = IOUtils.toString(reader).getBytes("UTF-8");
System.out.println(new String(bytes, "UTF-8"));
}
}

```

This does rely on [another package](http://code.google.com/p/juniversalchardet/) which is used to detect encoding of file on the fly. This is optional if you already know the source encoding.
