# SSL Certificate Inspection

We can inspect a web server's SSL certificate.

```ruby
openssl s_client -connect ejemplo.com:443
```
This command connects to the server on port 443 and displays detailed information about the SSL certificate, such as certificate validity, expiration date, encryption type, etc.

## Tools

Useful tools include 'sslyze' and 'sslscan'.

- Sslyze is an SSL security analysis tool used to evaluate a server's SSL configuration. It provides detailed information about the encryption used, supported protocols, and SSL certificates.

- SSLScan is another SSL security analysis tool used to evaluate a server's SSL configuration. It provides detailed information about supported SSL/TLS protocols, encryption used, and SSL certificates.

```ruby 
sslscan url.com
```

- The main difference between sslyze and sslscan is that sslyze focuses on evaluating the SSL/TLS security of a web server through comprehensive exploration of SSL/TLS protocols and configurations, while sslscan focuses on identifying SSL/TLS protocols supported by the server and the ciphers used.

Identifying the information provided by SSL/TLS analysis tools is of utmost importance, as it can allow us to detect vulnerabilities in a server's configuration and take measures to protect our confidential information.


## Heartbleed

For example, Heartbleed is a security vulnerability that affects the OpenSSL library and allows attackers to access the memory of a vulnerable server. If a web server is vulnerable to Heartbleed and we detect it through these tools, it means that an attacker could potentially access confidential information, such as private keys, usernames and passwords, etc.