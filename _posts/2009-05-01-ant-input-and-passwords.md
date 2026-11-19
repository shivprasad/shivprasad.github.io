---
title: "Ant Input and Passwords"
date: 2009-05-01 06:43:00 -0700
categories:
  - Tech
  - Java
tags:
  - ant
  - console
  - input
  - java
  - password
---

Ant input task does not has a feature which will allow not to echo what user inputs, a necessity in case you are prompting for a password. As per the [ant input task documentation](http://ant.apache.org/manual/CoreTasks/input.html) -

> A regular complaint about this task is that it echoes characters to the console, this is a critical security defect, we must fix it immediately, etc, etc. We know it leaves something to be desired, but the problem is Java, not Ant. There is nothing we can do to stop the console echoing.
> 

But as of JDK 1.6, which allows you to [read password using console](http://java.sun.com/javase/6/docs/api/java/io/Console.html#readPassword%28%29), I have created following ant task which allows you to prompt a message to user and accept a password and it will be set as a ant property.
You can also use the same to accept normal input.

```
package com.shivprasad.anttask;
import java.io.Console;
import org.apache.tools.ant.BuildException;
import org.apache.tools.ant.Task;
public class YetAnotherInputTask extends Task {
private String outputproperty;
private String message;
private Boolean password;
public void setPassword(String password) {
this.password = Boolean.parseBoolean(password);
}
public void setMessage(String message) {
this.message = message;
}
public void setOutputproperty(String outputproperty) {
this.outputproperty = outputproperty;
}
@Override
public void execute() throws BuildException {
Console cons = System.console();
String text=null;
if (cons != null){
if(password.booleanValue()){
char[] passwd = cons.readPassword("[yainput] %s", message);
text = new String(passwd);
}else{
text = cons.readLine("[yainput] %s", message);
}
getProject().setProperty(outputproperty, text);
}
}
}

```

You can download above as a jar.
Download [ya-ant-input-task.jar](http://byteco.de/files/ya-ant-input-task.jar)
In order to use it in ant, you will have to have the above jar as part of classpath. Then define, ant task -

```

```

For actually using it -

```

```

The outputproperty is the property which will be available in ant after user enters the text.
Updated: Above code is licensed under : http://ant.apache.org/license.html
