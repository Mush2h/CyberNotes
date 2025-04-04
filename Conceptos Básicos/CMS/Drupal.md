## Drupal (Droopescan)

- Droopescan es un escáner modular que identifica problemas de seguridad en CMS, con enfoque principal en Drupal.

```ruby
droopescan scan drupal -u <target_url>
```

## Paremtros interesantes
- `-u`, --url <URL>: Especifica la URL del sitio Drupal a escanear
- `-U`, --url-file <FILE>: Escanea múltiples URLs desde un archivo
- `-e`, --enumerate <OPTION>: Define el tipo de escaneo (p: plugins, t: temas, v: versiones, i: URLs interesantes)
- `--number <NUMBER>`: Establece el número de peticiones a realizar
- `--threads <NUMBER>`: Número de hilos para el escaneo (por defecto: 4)

## Scan Types
- `p`: Plugin 
- `t`: Temas 
- `v`: Version 
- `i`: URLs interesantes

## Examples

### Escaneo básico de un sitio Drupal
Este comando realiza un escaneo básico en el sitio especificado:
```ruby
droopescan scan drupal -u http://example.com
```

### Escaneo de múltiples URLs desde un archivo
Para escanear varias URLs listadas en un archivo:
```ruby
droopescan scan drupal -U urls.txt
```
Donde `urls.txt` contiene una URL por línea.

### Enumeración de plugins
Para enumerar los plugins instalados en un sitio Drupal:
```ruby
droopescan scan drupal -u http://example.com -e p
```

### Escaneo con múltiples hilos
Para acelerar el escaneo utilizando 10 hilos:
```ruby
droopescan scan drupal -u http://example.com --threads 10
```

### Limitación del número de peticiones
Para limitar el número de peticiones realizadas durante el escaneo:
```ruby
droopescan scan drupal -u http://example.com --number 50
```
