---
title: "Publishing Webservice on Multiple Network Interfaces"
date: 2011-04-06 09:13:00 -0700
categories:
  - Blog
  - General
tags:
---

Recently our IT support group decided to move one of component to a new VCS Cluster.
This component is a service component exposing various web services which are consumed by another .Net based UI component.
The initial attempt was not successful as the component was incompatible with multi-homed hosts (those with multiple IP addresses / network interfaces), because it listen to port 80 on the primary network interface only.
As currently the component was running on a single-homed host, thereâ€™s no problem, since thereâ€™s only one IP address, and no ambiguity.
But VCS clusters are multi-homed devices â€“ they have local IP, and cluster IP.
And in VCS world, nobody is connecting to host name / IP directly, connection should be established to cluster name / IP.
So to make the component publish web service on all interfaces, instead of using localhost or host address, use 0.0.0.0 as address. With 0.0.0.0 you tell it to 'listen' to incoming connections to any ip-address (associated with box).
