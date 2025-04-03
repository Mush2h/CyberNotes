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