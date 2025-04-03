# Nmap

- Initially created as an open-source tool for port scanning, running on Linux.
- It is a powerful network scanner available for multiple operating systems.

## Main Tasks

- **Host discovery**: Identifying active hosts on a network.
- **Open port detection**: Determining which ports are open on each device.
- **Service identification**: Detecting the services running on each machine.
- **Operating system detection**: Identifying the OS and its version.
- **Hardware information**: Gathering details about installed network hardware.
- **NSE Scripts**: Includes developed scripts known as Nmap Scripting Engine (NSE).

## Host Discovery

The basic host discovery function is achieved using the `nmap` command:

```bash
nmap 192.168.1.130
nmap 192.168.1.1-254
nmap 192.168.1.0/24
nmap microsoft.com
```

### Advanced Parameters

- `-iL <file>`: Scans hosts listed in the specified file.
- `--excludefile <file>`: Excludes hosts listed in the specified file.
- `-PS <port>`: Sends a **TCP SYN** to the specified port for host discovery.
- `-PA <port>`: Sends a **TCP ACK** to the specified port for host discovery.
- `-PU <port>`: Sends a **UDP datagram** to the specified port for host discovery.
- `-n`: Disables DNS resolution.
- `-R`: Resolves DNS for all discovered hosts.
- `--traceroute`: Traces the route to discovered targets.

## Port Scanning

To identify the state of all 65,500 ports on a target:

```bash
nmap <ip> -p-
nmap 192.168.1.1 -p-
```


To scan only the top 100 most common ports:


```bash
nmap <ip> -F
nmap 192.168.1.1 -F
```

### Advanced Parameters

- `-sS`: TCP SYN scan.
- `-sT`: TCP connect scan.
- `-sA`: TCP ACK scan.
- `--sw`: TCP window scan.
- `--sM`: TCP Maimon scan (a subtle and stealthy method).

## Service and OS Detection

Based on open ports, Nmap can detect operating systems and service versions:

### Parameters

- `-sV`: Enables version detection.
- `--allports`: Does not exclude any ports during version detection.
- `--version-intensity <level>`: Sets intensity from 0 (least aggressive) to 9 (most aggressive).
- `--sR`: RCP scan.
- `--O`: OS detection.
- `--v / -V`: Adjusts verbosity level of the analysis.

## Firewall and Intrusion Detection Evasion

Commands to bypass security systems:

### Advanced Options

- `-f`: Fragments packets sent during scanning.
- `--D <decoy1,decoy2>`: Uses decoys to hide the real source of the scan.
- `--S <ip>`: Spoofs the source IP address.
- `--g <port>`: Spoofs the source port.
- `--spoof-mac <mac_address>`: Spoofs the source MAC address.
- `--e <interface>`: Specifies the interface to use for scanning.
- `--data-length <number>`: Adds random data to packets.

```bash
nmap -f <ip>
```

## Time and Performance Control Options

### Parameters

- `--T <level>`: Sets scan speed (0 is slowest but stealthiest; 5 is fastest).
- `--min-parallelism <number> / --max-parallelism <number>`: Adjusts probes sent in parallel.
- `--host-timeout <time>`: Ignores slow targets after a timeout.

## Exporting Results

Nmap allows exporting results in specific formats:

### Options

- `--oX <file>`: Exports results in XML format (compatible with Metasploit).
- `--oG <file>`: Exports results in grepable format.
- `--oS <file>`: Exports results in Script Kiddie format.
- `--oA <file>`: Exports results in all formats.

```bash
nmap -p- -sS 192.168.37.136 --min-rate 9000 -oG resultado_nmap.grep
nmap -p- -sS 192.168.37.136 --min-rate 9000 -oX resultado_nmap.xml
```

## Script Execution

NSE scripts allow advanced scanning capabilities:

### Parameters

- `--sC`: Runs default scripts during scanning.
- `--script <script_name>`: Runs specific scripts provided by Nmap NSE library.
- `--script-trace`: Displays input/output exchanges during script execution.


```bash
nmap -p 21 --script ftp-brute <ip>
```


## Scanning Levels (From Less Aggressive to More Aggressive)

```bash
nmap <ip>
nmap -sS -sU <ip>
nmap -sS -T4 -A -v <ip>
nmap -sS -sU -sV <ip>
nmap -sS -sU -sV -sC --script all <ip>

```


## Interesting Scans

### Vulnerability and Authentication Scripts

```bash
nmap --script=vuln --script=auth -v --min-rate 5000 192.168.37.136
```
### Firewall Bypass Script

```bash
nmap --script=firewall-bypass -v 192.168.1.1
```


## Silent but Long Scans

```shell 
nmap -T2 -Pn -n -sV <ip>
nmap -sS -T4 -Pn -p 1-65535 -n --min-rate 1000 --max-retries 0 <objetivo>

# udp
nmap -sU -T4 -Pn -p 1-65535 -n --min-rate 1000 --max-retries 0 <objetivo>
```