# Common Services

## FTP Service (Port 21)
FTP is a widely used protocol for file transfer over networks. FTP service enumeration involves gathering relevant information such as FTP server version, file permission configurations, users, and passwords (through brute force attacks or guessing), among others.

To connect:

```shell 
 ftp <Ip>
```

### Default User

```ruby
anonymous:<none>
```

### FTP Enumeration 

```ruby
nmap -p 21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 <IP>
```



## SSH Service(Port 22)

- SSH is a remote administration protocol that allows users to control and modify their remote servers over the Internet through a secure authentication mechanism. As a more secure alternative to the Telnet protocol, which transmits information in plain text, SSH uses cryptographic techniques to ensure that all communications to and from the remote server are encrypted.

- SSH provides a mechanism to authenticate a remote user, transfer inputs from the client to the host, and relay the output back to the client. This is particularly useful for securely and efficiently managing remote systems without having to be physically present at the site.
It's worth noting that through the SSH version, we can also identify the codename of the distribution running on the system.

- For example, if the SSH server version is "OpenSSH 8.2p1 Ubuntu 4ubuntu0.5", we can determine that the system is running an Ubuntu distribution. The version number "4ubuntu0.5" refers to the specific revision of the SSH package in that Ubuntu distribution. From this, we can identify the codename of the Ubuntu distribution, which in this case would be "Focal" for Ubuntu 20.04.

To connect:

```shell 
 ssh <Ip>
```

### SSH Enumeration 

```ruby
nmap -p 22 --script=ssh2-enum-algos,ssh-hostkey,ssh-auth-methods <IP>
```

## HTTP y HTTPS Service ( Port 80 / Port 443)

- HTTP (Hypertext Transfer Protocol) is a communication protocol used for data transfer on the World Wide Web. It is used for transferring text content, images, videos, hyperlinks, etc. The default port for HTTP is port 80.

- HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP that uses SSL/TLS to encrypt communication between the client and server. It uses port 443 by default. The main difference between HTTP and HTTPS is that HTTPS uses an additional security layer to encrypt data, making it more secure for transfer.


### HTTP/HTTPS Enumeration

```ruby
nmap -p 80,443 --script=http-enum,http-headers,http-methods,http-webdav-scan <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

```


## SMB Service ( Port 445)
`
SMB (Server Message Block) is a network file sharing protocol that allows applications on a computer to read and write to files and to request services from server programs in a computer network. It's commonly used for providing shared access to files, printers, and serial ports between nodes on a network.

To list available shares:
```ruby
smbclient -L 127.0.0.1 -N 
```

To connect to a specific share:

```ruby
smbclient //127.0.0.1/myshare -N
```

### Advanced Options
- `-L`: List active resources
- `-N`: Enable a null session
- `-U`, `--user=USERNAME`: Specify the username for authentication
```ruby
smbclient -L //192.168.1.100 -U test
```
- `-W`, --workgroup=WORKGROUP: Set the workgroup name
```ruby
smbclient -L //192.168.1.100 -W PENTESTDOMAIN
```
- `-p`, --port=PORT: Connect to a specific port
```ruby
smbclient -L //192.168.1.100 -p 4455
```
- `-m`, --max-protocol=MAXPROTOCOL: Set max protocol level
```ruby
smbclient -L //192.168.1.100 -m SMB3
```
- `-c` 'COMMAND': Execute a single command
```ruby
smbclient //192.168.1.100/share -c 'ls'
```
- get FILENAME: Download a file
```ruby
smbclient //192.168.1.100/share -c 'get secret.txt'
```
- put FILENAME: Upload a file
```ruby
smbclient //192.168.1.100/share -c 'put local_file.txt'
```

### SMB Enumeration 

```ruby
enum4linux -a <IP>
nmap -p 445 --script=smb-enum-shares,smb-enum-users <IP>
```

### Tool Smabmap 

SMBMap is a powerful tool designed for enumerating and interacting with SMB (Server Message Block) shares across networks. It allows users to list share drives, examine drive permissions, view share contents, and even execute remote commands on target systems

```ruby
smbmap -H 127.0.0.1
```

This tool is quite useful as it shows permissions and comments.
