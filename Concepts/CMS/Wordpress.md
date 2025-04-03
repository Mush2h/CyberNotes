## Wordpress (WPScan)

- Para este sistema de gestión de contenidos, usamos WPScan. WPScan es una herramienta de código abierto utilizada para escanear sitios web en busca de vulnerabilidades de seguridad en WordPress.

- Con WPScan, podemos realizar una enumeración completa del sitio web y obtener información detallada sobre la instalación de WordPress, como la versión utilizada, plugins y temas instalados,  usuarios registrados en el sitio. También permite realizar pruebas de fuerza bruta para descubrir contraseñas débiles y vulnerabilidades conocidas en plugins y temas.

El uso de esta herramienta es bastante simple. La sintaxis básica es la siguiente:

```bash
wpscan --url https://example.com
```

Para enumerar usuarios o plugins vulnerables en WordPress utilizando WPScan, puedes añadir los siguientes parámetros:

```bash
wpscan --url https://example.com --enumerate u
```

Para enumerar plugins existentes que son vulnerables:

```bash
wpscan --url https://example.com --enumerate vp
```

### Enumeración avanzada

Además de los parámetros básicos, WPScan permite realizar enumeraciones más específicas:

- Para enumerar temas vulnerables:
```bash
wpscan --url https://example.com --enumerate vt
```

- Para enumerar configuraciones de WordPress:
```bash
wpscan --url https://example.com --enumerate c
```

### Ataques avanzados

```bash
wpscan --url https://example.com -e vp --api-token=token
```

Filtrar plugins
```bash
curl -s -X GET "https://example.com" | grep -oP 'plugins/\K[^/]+' | sort -u
```

Fuerza bruta con usuario y diccionario:

```bash
wpscan --url https://example.com -U <user> -P <dicc> --api-token= token
```

Enumeración con evasión 

```bash
wpscan --url https://example.com \                      
  --api-token token \
  --enumerate u \
  --random-user-agent \
  --throttle 10 \
  --request-timeout 15 \
  --max-threads 1 \
  --no-banner \
  --disable-tls-checks
```


### Ejemplo de escaneo completo

Para realizar un escaneo completo con WPScan, incluyendo enumeración de usuarios, plugins y temas, puedes usar el siguiente comando:

```bash
wpscan --url https://example.com --enumerate ap --api-token="token"
```

Además, otro recurso a tener en cuenta es el archivo `xmlrpc.php`. Este archivo es una funcionalidad de WordPress que permite la comunicación entre el sitio web y aplicaciones externas mediante el protocolo XML-RPC.

El archivo `xmlrpc.php` es utilizado por muchos plugins y aplicaciones móviles de WordPress para interactuar con el sitio y realizar varias tareas como publicar contenido, actualizar el sitio y obtener información.

Sin embargo, también puede ser abusado por atacantes para realizar ataques de fuerza bruta y descubrir credenciales válidas de usuarios del sitio, ya que permite realizar un número ilimitado de solicitudes de inicio de sesión sin ser bloqueado.


### Link xmlrpc.php

https://the-bilal-rizwan.medium.com/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32