# Servicios Comunes

## Servicio FTP (Puerto 21)
FTP es un protocolo ampliamente utilizado para la transferencia de archivos a través de redes. La enumeración del servicio FTP implica recopilar información relevante como la versión del servidor FTP, configuraciones de permisos de archivos, usuarios y contraseñas (mediante ataques de fuerza bruta o adivinación), entre otros.

Para conectar:

```shell
ftp <IP>
```

### Usuario por defecto

```ruby
anonymous:<none>
```

### Enumeración de FTP

```ruby
nmap -p 21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 <IP>
```

## Servicio SSH (Puerto 22)

- SSH es un protocolo de administración remota que permite a los usuarios controlar y modificar sus servidores remotos a través de Internet mediante un mecanismo de autenticación seguro. Como una alternativa más segura al protocolo Telnet, que transmite información en texto plano, SSH utiliza técnicas criptográficas para garantizar que todas las comunicaciones hacia y desde el servidor remoto estén cifradas.

- SSH proporciona un mecanismo para autenticar a un usuario remoto, transferir entradas del cliente al host y retransmitir la salida de vuelta al cliente. Esto es particularmente útil para gestionar sistemas remotos de forma segura y eficiente sin necesidad de estar físicamente presente en el sitio.

- Es importante destacar que a través de la versión de SSH, también podemos identificar el nombre en clave de la distribución que se ejecuta en el sistema.

- Por ejemplo, si la versión del servidor SSH es "OpenSSH 8.2p1 Ubuntu 4ubuntu0.5", podemos determinar que el sistema está ejecutando una distribución de Ubuntu. El número de versión "4ubuntu0.5" se refiere a la revisión específica del paquete SSH en esa distribución de Ubuntu. A partir de esto, podemos identificar el nombre en clave de la distribución de Ubuntu, que en este caso sería "Focal" para Ubuntu 20.04.

Para conectar:

```shell
ssh usuario@ip -p puerto
```

### Enumeración de SSH

```ruby
nmap -p 22 --script=ssh2-enum-algos,ssh-hostkey,ssh-auth-methods <IP>
```

## Servicios HTTP y HTTPS (Puerto 80 / Puerto 443)

- HTTP (Protocolo de Transferencia de Hipertexto) es un protocolo de comunicación utilizado para la transferencia de datos en la World Wide Web. Se utiliza para transferir contenido de texto, imágenes, videos, hipervínculos, etc. El puerto predeterminado para HTTP es el puerto 80.

- HTTPS (Protocolo de Transferencia de Hipertexto Seguro) es una versión segura de HTTP que utiliza SSL/TLS para cifrar la comunicación entre el cliente y el servidor. Utiliza el puerto 443 por defecto. La principal diferencia entre HTTP y HTTPS es que HTTPS utiliza una capa de seguridad adicional para cifrar los datos, haciéndolos más seguros para la transferencia.

### Enumeración de HTTP/HTTPS

```ruby
nmap -p 80,443 --script=http-enum,http-headers,http-methods,http-webdav-scan <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Servicio SMB (Puerto 445)

SMB (Server Message Block) es un protocolo de intercambio de archivos en red que permite a las aplicaciones en una computadora leer y escribir archivos y solicitar servicios de programas de servidor en una red. Se utiliza comúnmente para proporcionar acceso compartido a archivos, impresoras y puertos serie entre nodos en una red.

Para listar recursos compartidos disponibles:

```ruby
smbclient -L 127.0.0.1 -N
```

Para conectar a un recurso compartido específico:

```ruby
smbclient //127.0.0.1/myshare -N
```

### Opciones avanzadas

- `-L`: Lista recursos activos
- `-N`: Habilita una sesión nula
- `-U`, `--user=USERNAME`: Especifica el nombre de usuario para la autenticación
```ruby
smbclient -L //192.168.1.100 -U test
```
- `-W`, --workgroup=WORKGROUP: Establece el nombre del grupo de trabajo
```ruby
smbclient -L //192.168.1.100 -W PENTESTDOMAIN
```
- `-p`, --port=PORT: Conecta a un puerto específico
```ruby
smbclient -L //192.168.1.100 -p 4455
```
- `-m`, --max-protocol=MAXPROTOCOL: Establece el nivel máximo de protocolo
```ruby
smbclient -L //192.168.1.100 -m SMB3
```
- `-c` 'COMMAND': Ejecuta un solo comando
```ruby
smbclient //192.168.1.100/share -c 'ls'
```
- Descargar un archivo
```ruby
smbclient //192.168.1.100/share -c 'get secret.txt'
```
- Subir un archivo
```ruby
smbclient //192.168.1.100/share -c 'put local_file.txt'
```

### Enumeración de SMB

```ruby
enum4linux -a <IP>
nmap -p 445 --script=smb-enum-shares,smb-enum-users <IP>
```

### Herramienta SMBMap

SMBMap es una herramienta poderosa diseñada para enumerar e interactuar con recursos compartidos SMB en redes. Permite listar unidades compartidas, examinar permisos de unidades, ver contenidos compartidos e incluso ejecutar comandos remotos en sistemas objetivo.

```ruby
smbmap -H 127.0.0.1
```

#### Opciones avanzadas

- `-H`: Especifica la dirección IP o el nombre del host del servidor SMB.
- `-P`: Especifica el puerto TCP para la conexión SMB.
- `-u`: Especifica el nombre de usuario para la conexión SMB.
- `-p`: Especifica la contraseña para la conexión SMB.
- `-d`: Especifica el dominio al que pertenece el usuario.
- `-s`: Especifica el recurso compartido específico que deseas enumerar.

---

## Servicio DNS (Puerto 53)

DNS (Domain Name System) traduce nombres de dominio legibles por humanos a direcciones IP. Es un servicio crítico para la navegación en Internet.

### Enumeración de DNS

```ruby
nmap -p 53 --script=dns-brute,dns-cache-snoop,dns-recursion <IP>
dig @<IP> <domain> ANY
```

---

## Servicio RDP (Puerto 3389)

RDP (Remote Desktop Protocol) permite el acceso remoto a escritorios de Windows.

### Enumeración de RDP

```ruby
nmap -p 3389 --script=rdp-enum-encryption <IP>
xfreerdp /u:usuario /p:contraseña /v:<IP>
```

---

## Servicio MySQL (Puerto 3306)

MySQL es un sistema de gestión de bases de datos relacional.

### Enumeración de MySQL

```ruby
nmap -p 3306 --script=mysql-enum,mysql-databases,mysql-users <IP>
mysql -h <IP> -u root -p
```