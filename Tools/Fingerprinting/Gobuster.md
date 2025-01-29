# Gobuster

Gobuster is a tool used for brute-forcing:
- URIs (directories and files) on websites
- DNS subdomains

It has three main modes available:
- dir: Classic brute-force mode against DNS subdomains and "vhost"
- dns: DNS subdomain enumeration mode
- help: Displays Gobuster's top-level help
  - You can show specific help with `help dir`

## Interesting Options

- `-u`: Defines the URL to evaluate
- `-t`: Sets the number of concurrent threads
- `-w`: Specifies the file containing a wordlist
- `-x`: Defines the file extensions to search for

### Basic Examples

```shell
gobuster dir -u http://<ip>/<directorio> -t 20 -w /usr/

gobuster dir -w /usr/share/dirb/worlists/common.txt -u <ip>

gobuster dns -d example.com -w /usr/share/wordlists/dirbuster/directory-list-2.3 small.txt

gobuster dns -d google.com -w ~/wordlists/subdomains.txt
```

