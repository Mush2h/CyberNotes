# CMS


## Wordpress (WPScan)

- En este sistema de gestión de contenidos, usamos WPScan. WPScan es una herramienta de código abierto utilizada para escanear sitios web en busca de vulnerabilidades de seguridad en WordPress.

- Con WPScan, podemos realizar una enumeración completa del sitio web y obtener información detallada sobre la instalación de WordPress, como la versión utilizada, plugins y temas instalados,  usuarios registrados en el sitio. También permite realizar pruebas de fuerza bruta para descubrir contraseñas débiles y vulnerabilidades conocidas en plugins y temas.

El uso de esta herramienta es bastante simple. La sintaxis básica es la siguiente:

```bash
wpscan --url https://example.com


```ruby
wpscan --url https://example.com
```

Para enumerar usuarios o plugins vulnerables en WordPress utilizando WPScan, puedes añadir los siguientes parámetros:

```ruby
wpscan --url https://example.com --enumerate u
```

Para enumerar plugins existentes que son vulnerables:

```ruby
wpscan --url https://example.com --enumerate vp
```

### Ataques avanzados

```ruby
wpscan --url https://example.com -e vp --api-token="token"

```

Filtrar plugins
```ruby
curl -s -X GET "https://example.com" | grep -oP 'plugins/\K[^/]+' | sort -u
```

Fuerza bruta con usuario y diccionario:

```ruby
wpscan --url https://example.com -U <user> -P <dicc> --api-token="token"
```

Además, otro recurso a tener en cuenta es el archivo `xmlrpc.php`. Este archivo es una funcionalidad de WordPress que permite la comunicación entre el sitio web y aplicaciones externas mediante el protocolo XML-RPC.

El archivo `xmlrpc.php` es utilizado por muchos plugins y aplicaciones móviles de WordPress para interactuar con el sitio y realizar varias tareas como publicar contenido, actualizar el sitio y obtener información.

Sin embargo, también puede ser abusado por atacantes para realizar ataques de fuerza bruta y descubrir credenciales válidas de usuarios del sitio, ya que permite realizar un número ilimitado de solicitudes de inicio de sesión sin ser bloqueado.

### Link xmlrpc.php

https://the-bilal-rizwan.medium.com/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32


## Joomla (Joomscan)

JoomScan es un escáner de vulnerabilidades de código abierto diseñado específicamente para el CMS Joomla. Aquí tienes una chuleta con sus parámetros más útiles:

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

## Drupal (Droopescan)

- Droopescan is a plugin-based scanner that helps identify security issues in various Content Management Systems, with a focus on Drupal.

```ruby
droopescan scan drupal -u <target_url>
```

## Key Parameters
`-u`, --url <URL>: Specify the target Drupal URL to scan
`-U`, --url-file <FILE>: Scan multiple URLs listed in a file
`-e`, --enumerate <OPTION>: Specify scan type (p: plugins, t: themes, v: versions, i: interesting URLs)
`--number <NUMBER>`: Set the number of requests to perform
`--threads <NUMBER>`: Set the number of threads for scanning (default: 4)

## Scan Types
- `p`: Plugin checks
- `t`: Theme checks
- `v`: Version checks
- `i`: Interesting URL checks

## Magento (Magescan)
- MageScan is a powerful tool designed to evaluate the quality and security of Magento sites. Here's a cheatsheet highlighting its most useful parameters and features:

```ruby
magescan.phar scan <url>
```

### Key Parameters
- `scan:` Perform a full scan of the target Magento site
- `--insecure, -k`: Allow insecure SSL connections
- `<url>`: Specify the target Magento URL to scan

### Specific Scan Types
- `scan:all`: Run all available scans
- `scan:catalog`: Check for catalog information exposure
- `scan:modules`: Detect installed modules
- `scan:patch`: Check for applied patches
- `scan:sitemap`: Check sitemap
- `scan:unreachable`: Check unreachable paths
- `scan:version`: Get the Magento version

### Output Options
- `--format=<format>`: Specify output format (text, json, xml)
- `--output=<file>`: Save output to a file

### Example Commands
- Full scan:
    ```ruby
    magescan.phar scan http://example.com
    ```
- Check Magento version:
    ```ruby
    magescan.phar scan:version http://example.com
    ```
- Detect installed modules:
    ```ruby
    magescan.phar scan:modules http://example.com
    ```

- Save scan results to a JSON file:
    ```ruby
    magescan.phar scan http://example.com --format=json --output=results.json
    ```
