# theHarvester

theHarvester is a free Linux-based tool for gathering information about domains, subdomains, and email addresses from the internet.

## Important Notes

- **No longer works with Google or LinkedIn**
- Designed for information gathering and reconnaissance
- Open-source and actively maintained

## Key Features

- Domain enumeration
- Subdomain discovery
- Email address collection
- Multiple data source support
- Flexible reporting options

## Usage Parameters

### Primary Options

- `-d`: Specify target domain
  - Example: `-d example.com`

- `-b`: Select data source
  - Supported sources: 
    - `all`: Search all available sources
    - `bing`: Microsoft Bing search
    - `yahoo`: Yahoo search
    - `baidu`: Baidu search
    - `shodan`: Shodan IoT search engine

- `-f`: Export results to file
  - Formats: HTML, XML
  - Example: `-f results.html`

- `-l`: Limit number of results
  - Example: `-l 100`

- `-s`: Perform Shodan query

## Basic Examples


```console
kali@kali:~$ theHarvester
kali@kali:~$ theHarvester -d cocacola.es -b all
kali@kali:~$ theHarvester -d cocacola.es -b bing

```
