---
title: "My tryst with OSX86 on Dell Latitude D630"
date: 2009-08-05 03:19:00 -0700
categories:
  - Blog
  - General
tags:
  - d630
  - dell
  - osx86
---

hmm....
Tried to setup OS X on my Dell Latitude D630 and finally gave up. I don't think its possible to have a working OS X on D630.
I had tried all three DVD's which are available.

1. iDeneb v1.5.1 OSX10.5.7 (UPDATED VERSION) (Intel PC AMD PC) - This seemed most promising, being latest ... blah blah... Didn't worked.
2. Kalyway 10.5.2 DVD Intel_Amd (sse2/sse3) EFI V8 - All praised this one. Didn't worked.
3. IATKOS V7 10.5.7 - Didn't worked.

I always ended up with

> IOAPIC: Version 0x20 Vectors 0:23
> 

IÂ  tried to boot from external USB drives...same error. First restoring the iso's on the external drive didn't boot, partition type MBR tried using Disk Utility.
Had to use OSX86Tools_1.0.150 and Chameleon-1.0.11-installer to make those USB's bootable.
Burned iDeneb and Kalyway on DVD... didn't worked... booted without problem though unlike USB drive.
At the Darwin boot prompt entered options, -v -k -f cpus=2 etc etc still didn't worked.
Disables multi-core in bios... change to AHCI from ATA.... didn't worked.
Finally.... spending over two days.... my tryst with OSX86 on my Dell D630 is over.**Update**: [I was able to install Snow Leopard on my Dell D630](http://byteco.de/2009/12/06/successful-installation-of-snow-leopard-on-dell-d630/).
