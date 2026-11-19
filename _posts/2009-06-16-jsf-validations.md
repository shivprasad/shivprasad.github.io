---
title: "JSF Validations"
date: 2009-06-16 08:00:00 -0700
categories:
  - Tech
  - Java
tags:
  - java
  - jsf
  - validations
---

**Using JSF Standard Built-in Validations**
JSF provides built-in support for validations of input component tags. You can supply it a attribute **required="true"** which will check if a value is supplied or not. There are built-in validators which you can nest in all JSF input tags.
Below are the built-in Validators -

1. f:validateDoubleRange
2. f:validateLongRange
3. f:validateLength

*One should be cautious as when the required attribute is not set and user supplies a blank input, then no validation are performed.*
Below is a example of using JSF Validator -

```
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h"%>
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f"%>
<%@ taglib uri="http://myfaces.apache.org/tomahawk" prefix="t"%>

JSF Validations Example Form

JSF Validations Example Form
----------------------------

```

![jsf14](http://byteco.de/wp-content/uploads/2009/06/jsf14.jpg)

jsf14

```
package com.test.validator;
import javax.faces.application.FacesMessage;
import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.validator.Validator;
import javax.faces.validator.ValidatorException;
public class EmailValidator implements Validator {
public void validate(FacesContext facesContext, UIComponent component, Object object)
throws ValidatorException {
org.apache.commons.validator.EmailValidator instance = org.apache.commons.validator.EmailValidator.getInstance();
if(!instance.isValid(object.toString())){
FacesMessage facesMessage = new FacesMessage("Invalid email address");
throw new ValidatorException(facesMessage);
}
}
}

```

**Step 2:**
Register above validator in faces-config.xml.

```
EmailValidator
EmailValidator
com.test.validator.EmailValidator

```

**Step 3:**
Use above registered validator in your page -

```
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h"%>
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f"%>
<%@ taglib uri="http://myfaces.apache.org/tomahawk" prefix="t"%>

JSF Validations Example Form

JSF Validations Example Form
----------------------------

```

![jsf2](http://byteco.de/wp-content/uploads/2009/06/jsf2.jpg)

jsf2

```
package com.test.validator;
import javax.faces.component.UIComponent;
import javax.faces.component.UIInput;
import javax.faces.context.FacesContext;
import javax.faces.validator.ValidatorException;
public class MarriedDateValidator extends DateValidator {
@Override
public void validate(FacesContext facesContext, UIComponent component,
Object object) throws ValidatorException {
UIInput input = (UIInput) component.findComponent("married");
if(input.isValid()){
if(input.getValue().toString().equals("true")){
super.validate(facesContext, component, object);
}
}
}
}

```

If you notice line where I get access to the input component *component.findComponent("married");* and then uses it for further decisions on validations.
Just for reference - below is the class DateValidator.

```
package com.test.validator;
import javax.faces.application.FacesMessage;
import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.validator.Validator;
import javax.faces.validator.ValidatorException;
public class DateValidator implements Validator {
public void validate(FacesContext facesContext, UIComponent component, Object object)
throws ValidatorException {
org.apache.commons.validator.DateValidator instance = org.apache.commons.validator.DateValidator.getInstance();
if(!instance.isValid(object.toString(), "dd/MM/yyyy", true)){
FacesMessage facesMessage = new FacesMessage("Invalid date");
throw new ValidatorException(facesMessage);
}
}
}

```

The next step is to define above in faces-config.xml.

```
MarriedDateValidator
MarriedDateValidator
com.test.validator.MarriedDateValidator

```

And then using it in your page -

```
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h"%>
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f"%>
<%@ taglib uri="http://myfaces.apache.org/tomahawk" prefix="t"%>

JSF Validations Example Form

JSF Validations Example Form
----------------------------

```

![jsf3](http://byteco.de/wp-content/uploads/2009/06/jsf3.jpg)

jsf3

```
package com.test.converter;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import javax.faces.application.FacesMessage;
import javax.faces.component.UIComponent;
import javax.faces.component.UIInput;
import javax.faces.context.FacesContext;
import javax.faces.convert.Converter;
import javax.faces.convert.ConverterException;
public class DateConverter implements Converter {
public Object getAsObject(FacesContext facesContext, UIComponent uiComponent, String val)
throws ConverterException {
String pattern = "dd/MM/yyyy";
boolean required = ((UIInput)uiComponent).isRequired();
if((val==null || val.trim().isEmpty()) && !required )
return null;
org.apache.commons.validator.DateValidator instance = org.apache.commons.validator.DateValidator.getInstance();
if(!instance.isValid(val.toString(), pattern, true)){
FacesMessage facesMessage = new FacesMessage("Using Converter - Invalid date");
throw new ConverterException(facesMessage);
}
try {
return new SimpleDateFormat(pattern).parse(val);
} catch (ParseException e) {
FacesMessage facesMessage = new FacesMessage("Using Converter - Invalid date");
throw new ConverterException(facesMessage);
}
}
public String getAsString(FacesContext facesContext, UIComponent uiComponent, Object val)
throws ConverterException {
return val.toString();
}
}

```

Please note following -*boolean required = ((UIInput)uiComponent).isRequired();* - Using this we can check if the field was required or not. Based on it we can either ignore the conversion or perform it.**Step 2:**
The next step is registering this convertor in faces-config.xml.

```
DateConverter
java.util.Date
com.test.converter.DateConverter

```

The JSF will call our converter when it finds the type of field in a bean as java.util.Date.
Below is our UserBean.java

```
package com.test.beans;
import java.util.Date;
import javax.faces.component.UIComponent;
import javax.faces.component.UIInput;
import javax.faces.context.FacesContext;
import javax.faces.validator.ValidatorException;
import com.test.validator.DateValidator;
public class UserBean {
private Date dateOfJoining;
public Date getDateOfJoining() {
return dateOfJoining;
}
public void setDateOfJoining(Date dateOfJoining) {
this.dateOfJoining = dateOfJoining;
}
public String sayHello() {
return "hello";
}
}

```

**Step 3:**
As you have mapped the converter for Date classes you don't need to specify anything in page -

```
<%@ taglib uri="http://java.sun.com/jsf/html" prefix="h"%>
<%@ taglib uri="http://java.sun.com/jsf/core" prefix="f"%>
<%@ taglib uri="http://myfaces.apache.org/tomahawk" prefix="t"%>

JSF Validations Example Form

JSF Validations Example Form
----------------------------

```

![jsf5](http://byteco.de/wp-content/uploads/2009/06/jsf5.jpg)

jsf5
