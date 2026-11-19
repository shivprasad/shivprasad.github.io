---
title: "Speed Up SSH Connections"
date: 2009-12-09 10:10:00 -0800
categories:
  - Blog
  - General
tags:
  - os-x
  - ubuntu
  - controlmaster
  - openssh
  - ssh
---

If you are working with a remote server using SSH, which requires frequent connections you might have noticed how it takes a lot of time to establish a connection. You also have to enter password every time you connect.

You can speed up this processes by configuring ssh to reuse connection to the same server if its has a connection already established.

This is a feature of OpenSSH, which I have tested on Snow Leopard and Ubuntu.

As per manual,

> ControlMaster
Enables the sharing of multiple sessions over a single network connection. When set to `yes'', ssh(1) will listen for connections on a control socket specified using the ControlPath argument. Additional sessions can connect to this socket using the same ControlPath with ControlMaster set to`no'' (the default). These sessions will try to reuse the master instance's network connection rather than initiating new ones, but will fall back to connecting normally if the control socket does not exist, or is not listening.
> 

In order to configure, create or edit **~/.ssh/config** file and add following lines -

> Host *
 ControlMaster auto
 ControlPath /tmp/%r@%h:%p
> 

In order to test above, you can use **-v** while using ssh command. This will print debug information message while establishing a connection. While using ControlMaster you will notice that the there are lesser messages.

> debug1: auto-mux: Trying existing master
> 

If you don't want to reuse existing connection you can use ssh with  **-S none** which will create a new connection.
