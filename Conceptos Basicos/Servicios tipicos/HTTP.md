## Servicios HTTP y HTTPS (Puerto 80 / Puerto 443)

- HTTP (Protocolo de Transferencia de Hipertexto) es un protocolo de comunicación utilizado para la transferencia de datos en la World Wide Web. Se utiliza para transferir contenido de texto, imágenes, videos, hipervínculos, etc. El puerto predeterminado para HTTP es el puerto 80.

- HTTPS (Protocolo de Transferencia de Hipertexto Seguro) es una versión segura de HTTP que utiliza SSL/TLS para cifrar la comunicación entre el cliente y el servidor. Utiliza el puerto 443 por defecto. La principal diferencia entre HTTP y HTTPS es que HTTPS utiliza una capa de seguridad adicional para cifrar los datos, haciéndolos más seguros para la transferencia.

### Enumeración de HTTP/HTTPS

```ruby
nmap -p 80,443 --script=http-enum,http-headers,http-methods,http-webdav-scan <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
nikto -h http://<IP>
whatweb http://<IP>
curl -I http://<IP>
```

- **Nikto**: Escanea servidores web en busca de vulnerabilidades conocidas.
- **WhatWeb**: Identifica tecnologías y frameworks utilizados en el servidor web.
- **cURL**: Permite inspeccionar encabezados HTTP y realizar solicitudes personalizadas.