# Wfuzz

Wfuzz es una herramienta de fuerza bruta diseñada para encontrar recursos ocultos en aplicaciones web.  Permite realizar fuzzing en URLs, parámetros, cabeceras HTTP, cookies, entre otros, para descubrir directorios, archivos, vulnerabilidades y más.

## Instalación

Puedes instalar Wfuzz utilizando `pip`:

```bash
pip install wfuzz
```

## Uso Básico

### Descubrimiento de Directorios

Para buscar directorios ocultos en un servidor web:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt --hc 404 http://example.com/FUZZ
```

- `-c`: Colorea la salida.
- `-z file`: Especifica el diccionario a usar.
- `--hc 404`: Oculta las respuestas con código 404.
- `FUZZ`: Marcador que será reemplazado por las palabras del diccionario.

### Fuerza Bruta de Archivos

Para encontrar archivos específicos:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt --hc 404 http://example.com/FUZZ.html
```

## Uso Avanzado

### Fuzzing de Parámetros

Para buscar parámetros vulnerables en una URL:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt --hc 404 http://example.com/page.php?FUZZ=value
```

### Fuzzing de Valores de Parámetros

Para probar diferentes valores en un parámetro específico:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt --hc 404 http://example.com/page.php?param=FUZZ
```

### Fuzzing de Cabeceras HTTP

Para modificar cabeceras HTTP, como `User-Agent`:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt -H "User-Agent: FUZZ" http://example.com
```

### Fuzzing con Múltiples Marcadores

Puedes usar múltiples marcadores para realizar fuzzing en diferentes partes de la solicitud:

```bash
wfuzz -c -z file,/ruta/a/wordlist1.txt -z file,/ruta/a/wordlist2.txt --hc 404 http://example.com/FUZZ/FUZZ2
```

### Búsqueda de Archivos con Extensiones

Para probar múltiples extensiones de archivo:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt -z list,php-html-txt --hc 404 http://example.com/FUZZ.FUZ2Z
```

### Fuzzing Autenticado

Si necesitas autenticarte, puedes usar cookies:

```bash
wfuzz -c -z file,/ruta/a/wordlist.txt --hc 404 -b "session=abc123" http://example.com/FUZZ
```

