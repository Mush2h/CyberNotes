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

#### Adicionales

- **CrackMapExec**: Herramienta para enumerar y explotar servicios SMB.
```ruby
crackmapexec smb <IP> -u <usuario> -p <contraseña>
```

- **Metasploit**: Framework para pruebas de penetración.
```ruby
use auxiliary/scanner/smb/smb_version
set RHOSTS <IP>
run
```

- **Impacket**: Conjunto de scripts para interactuar con SMB.
```ruby
python3 smbclient.py <usuario>:<contraseña>@<IP>
```

- **Nessus**: Escáner de vulnerabilidades que incluye módulos para SMB.

- **SMBMap**: Herramienta poderosa para enumerar recursos compartidos.
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

- **Responder**: Herramienta para capturar hashes NTLMv2.
```ruby
responder -I <interfaz>
```

- **rpcclient**: Cliente para interactuar con servicios RPC sobre SMB.
```ruby
rpcclient -U "" <IP>
```

- **smbclient**: Cliente SMB para interactuar con recursos compartidos.
```ruby
smbclient -L <IP> -N
```

- **Nmap Scripts Adicionales**:
```ruby
nmap -p 445 --script=smb-os-discovery,smb-vuln-* <IP>
```
