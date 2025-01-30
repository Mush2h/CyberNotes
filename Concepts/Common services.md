# Common Services

## FTP Service
FTP es un protocolo ampliamente utilizado para la transferencia de archivos en redes. La enumeración del servicio FTP implica recopilar información relevante, como la versión del servidor FTP, la configuración de permisos de archivos, los usuarios y las contraseñas (mediante ataques de fuerza bruta o guessing), entre otros.



Para conectarte :
Port 21.
```shell 
 ftp <Ip>
```

### Usuarios por defecto 

```ruby
anonymous:<none>
```

## SSH Service

SSH es un protocolo de administración remota que permite a los usuarios controlar y modificar sus servidores remotos a través de Internet mediante un mecanismo de autenticación seguro. Como una alternativa más segura al protocolo Telnet, que transmite información sin cifrar, SSH utiliza técnicas criptográficas para garantizar que todas las comunicaciones hacia y desde el servidor remoto estén cifradas.

SSH proporciona un mecanismo para autenticar un usuario remoto, transferir entradas desde el cliente al host y retransmitir la salida de vuelta al cliente. Esto es especialmente útil para administrar sistemas remotos de manera segura y eficiente, sin tener que estar físicamente presentes en el sitio.

Cabe destacar que a través de la versión de SSH, también podemos identificar el codename de la distribución que se está ejecutando en el sistema.

Por ejemplo, si la versión del servidor SSH es “OpenSSH 8.2p1 Ubuntu 4ubuntu0.5“, podemos determinar que el sistema está ejecutando una distribución de Ubuntu. El número de versión “4ubuntu0.5” se refiere a la revisión específica del paquete de SSH en esa distribución de Ubuntu. A partir de esto, podemos identificar el codename de la distribución de Ubuntu, que en este caso sería “Focal” para Ubuntu 20.04.

Para conectarte:
Port 22
```shell 
 ssh <Ip>
```

## HTTP y HTTPS Service

HTTP (Hypertext Transfer Protocol) es un protocolo de comunicación utilizado para la transferencia de datos en la World Wide Web. Se utiliza para la transferencia de contenido de texto, imágenes, videos, hipervínculos, etc. El puerto predeterminado para HTTP es el puerto 80.

HTTPS (Hypertext Transfer Protocol Secure) es una versión segura de HTTP que utiliza SSL / TLS para cifrar la comunicación entre el cliente y el servidor. Utiliza el puerto 443 por defecto. La principal diferencia entre HTTP y HTTPS es que HTTPS utiliza una capa de seguridad adicional para cifrar los datos, lo que los hace más seguros para la transferencia.
