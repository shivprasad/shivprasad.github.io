---
title: "Converting Mailman/Pipermail text archive to mbox"
date: 2010-01-14 02:10:00 -0800
categories:
  - Tech
  - AI
tags:
  - mailman
  - mbox
---

I wanted to import mailing list archive in my Apple Mail.app which support "Files in mbox format". Found following python script byÂ [Paul](http://lists2.ssc.com/pipermail/linux-list/2006-February/026220.html) which converts text archive to mbox.

```
#!/usr/bin/env python
"""
to-mbox.py: Insert line feeds to create mbox format
Usage: ./to-mbox.py infile outfile
"""
import sys
if len(sys.argv) != 3:
print \_\_doc\_\_
sys.exit()
out = open(sys.argv[2],"w")
start = True
for line in open(sys.argv[1]):
if line.find("From ") == 0:
if start:
start = False
else:
out.write("\n")
line = line.replace(" at ", "@")
out.write(line)
out.close()

```
