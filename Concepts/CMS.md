# CMS

## Wordpress (Wpscan)

- In this content management system, it's WPScan. WPScan is an open-source tool used to scan websites for security vulnerabilities in WordPress.

- With WPScan, we can perform a complete enumeration of the website and obtain detailed information about the WordPress installation, such as the version used, installed plugins and themes, and registered users on the site. It also allows us to perform brute force tests to discover weak passwords and known vulnerabilities in plugins and themes.

- WPScan is a very useful tool for website administrators who want to improve the security of their WordPress site, as it allows them to identify and correct vulnerabilities before they are exploited by malicious attackers. Additionally, it is an easy-to-use and highly effective tool for identifying potential security weaknesses on our website.

The use of this tool is quite simple. The basic syntax is as follows:

```ruby
wpscan --url https://example.com
```

If you want to enumerate users or vulnerable plugins in WordPress using the wpscan tool, you can add the following parameters to the command line:

```ruby
wpscan --url https://example.com --enumerate u
```

In case you want to enumerate existing plugins that are vulnerable, you can add the following parameter to the command line:

```ruby
wpscan --url https://example.com --enumerate vp
```

### Advance Attack

```ruby
wpscan --url https://example.com -e vp --api-token="token"

```

Filter plugins
```ruby
curl -s -X GET "https://example.com" | grep -oP 'plugins/\K[^/]+' | sort -u
```

```ruby
wpscan --url https://example.com -U <user> -P <dicc> --api-token="token"
```

- Additionally, another resource we consider is the xmlrpc.php file. This file is a WordPress feature that allows communication between the website and external applications using the XML-RPC protocol.

- The xmlrpc.php file is used by many WordPress plugins and mobile applications to interact with the website and perform various tasks, such as publishing content, updating the site, and obtaining information.

- However, this file can also be abused by malicious attackers to apply brute force and discover valid credentials of site users. This is because xmlrpc.php allows attackers to make an unlimited number of login requests without being blocked, making the execution of a brute force attack relatively simple.

### Link xmlrpc.php

https://the-bilal-rizwan.medium.com/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32


## Joomla (Joomscan)

JoomScan is an open-source vulnerability scanner designed specifically for Joomla CMS
. Here's a cheatsheet highlighting its most useful parameters:

```ruby
perl joomscan.pl -u <target_url>
```
### Key Parameters

`-u`, --url <URL>: Specify the target Joomla URL/domain to scan
`-ec`, --enumerate-components: Enumerate installed components
`--cookie <String>`: Set a specific cookie for the scan
`-a, --user-agent <User-Agent>`: Use a custom User-Agent
`-r`, --random-agent: Use a random User-Agent
`--timeout <Time-Out>`: Set the scan timeout
`--proxy <proxy>:` Set a proxy for the scan (e.g., http://127.0.0.1:8080)

### Advanced Features
- Version enumeration: Detects the exact Joomla version
- Vulnerability scanning: Checks for known vulnerabilities based on version
- Component analysis: Scans for vulnerabilities in installed components
- Firewall detection: Identifies common Joomla-based web application firewalls
- Common file discovery: Locates log and backup files

### Output Options
Generates reports in both text and HTML formats