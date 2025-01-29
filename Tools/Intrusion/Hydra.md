# Hydra

Hydra is a powerful tool for password cracking. Here's a comprehensive guide on its usage:

## Basic Syntax

```ruby
hydra -l/-L <user/list> -p/-P <password/dictionary> <IP address> <protocol>
```

## Key Parameters

- `-l`: Specify a single username
- `-L`: Use a list of usernames
- `-p`: Specify a single password
- `-P`: Use a password dictionary
- `-s`: Specify a port number
- `-o`: Save attack results to a file


## Advanced Options

- `-t`: Set number of parallel connections per target
- `-w`: Wait time between connections
- `-f`: Stop attack after first found login/password pair
- `-v`: Verbose mode, show login+pass for each attempt


## Examples

### FTP brute Force

```ruby
hydra -L users.txt -P passwords.txt 192.168.1.100 ftp
```

### SSH with Specific Port

```ruby
hydra -l root -P common_passwords.txt 10.0.0.1 ssh -s 2222
```

### HTTP PostForm

```ruby
hydra -l admin -P rockyou.txt 192.168.1.10 http-post-form "/login.php:username=^USER^&password=^PASS^:Login failed"
```
### SMTP with Result Output

```ruby
hydra -L users.txt -P passwords.txt smtp://10.0.0.1 -o smtp_results.txt
```








