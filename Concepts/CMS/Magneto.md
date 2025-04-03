## Magento (Magescan)
- MageScan es una herramienta muy útil para evaluar la seguridad y configuración de sitios Magento.

```ruby
magescan.phar scan <url>
```

### Parámetros clave
- `scan:` Escaneo completo del sitio Magento
- `--insecure, -k`: Permite conexiones SSL inseguras
- `<url>`: URL del sitio objetivo

### Specific Scan Types
- `scan:all`: Ejecuta todos los escaneos disponibles
- `scan:catalog`: Verifica exposición de catálogo, como productos visibles públicamente.
- `scan:modules`: Detecta módulos instalados y verifica si son vulnerables.
- `scan:patch`: Comprueba si los parches de seguridad están aplicados correctamente.
- `scan:sitemap`: Verifica la existencia y accesibilidad del archivo sitemap.
- `scan:unreachable`: Detecta rutas inaccesibles o páginas con errores.
- `scan:version`: Identifica la versión de Magento instalada, útil para detectar vulnerabilidades conocidas.

### Opciones de salida
- `--format=<format>`: Define el formato de salida. Opciones disponibles:
  - `text`: Salida legible para humanos.
  - `json`: Salida estructurada en JSON.
  - `xml`: Salida estructurada en XML.
- `--output=<file>`: Guarda el resultado en un archivo especificado.

### Comandos de ejemplo
- Escaneo completo:
    ```ruby
    magescan.phar scan http://example.com
    ```
- Detectar versión:
    ```ruby
    magescan.phar scan:version http://example.com
    ```
- Detectar módulos instalados:
    ```ruby
    magescan.phar scan:modules http://example.com
    ```
- Verificar exposición de catálogo:
    ```ruby
    magescan.phar scan:catalog http://example.com
    ```
- Comprobar parches de seguridad:
    ```ruby
    magescan.phar scan:patch http://example.com
    ```
- Guardar salida en JSON:
    ```ruby
    magescan.phar scan http://example.com --format=json --output=results.json
    ```
- Guardar salida en XML:
    ```ruby
    magescan.phar scan http://example.com --format=xml --output=results.xml
    ```
- Escaneo completo con conexión SSL insegura:
    ```ruby
    magescan.phar scan http://example.com --insecure
    ```

