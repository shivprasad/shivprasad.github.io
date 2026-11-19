---
title: "Killing Java Process from Ant in Windows"
date: 2009-04-30 15:08:00 -0700
categories:
  - Tech
  - Java
tags:
  - ant
  - java
  - pskill
  - tomcat
---

I wanted to write a ant script for one of the environment, which would perform following tasks in order which will be repeated
1. Take Latest Code
2. Compile
3. Create WAR
4. Undeploy currently installed WAR from tomcat
5. Stop the tomcat
6. Copy the WAR to tomcat webapps folder
7. Start the tomcat
Starting the tomcat -

```

```

Stopping the tomcat -
I was facing some issues using the tomcat shutdown.bat as tomcat server was not stopping due to one of the application deployed was not getting stopped gracefully. And the next time tomcat tried to start it used to give "JVM_BIND Exception -Port already in use".
As Windows doesn't have a native kill command, I have used following which allowed me to kill any java process using ant.[PsKill](http://technet.microsoft.com/en-us/sysinternals/bb896683.aspx) - Running PsKill with a process ID directs it to kill the process of that ID on the local computer.[jps](http://java.sun.com/j2se/1.5.0/docs/tooldocs/share/jps.html) - The jps command will report the process ID of each JVM running on local computer.

```
Killing tomcat instance with PID - "${pid.out}"

```

The above way can be used to kill any java process using the ant.
