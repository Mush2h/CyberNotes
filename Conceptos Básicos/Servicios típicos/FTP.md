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

#### Otras herramientas útiles

- **Hydra**: Para realizar ataques de fuerza bruta.
  ```shell
  hydra -l <usuario> -P <diccionario> ftp://<IP>
  ```

- **Metasploit**: Para explorar vulnerabilidades específicas.
  ```shell
  msfconsole
  use auxiliary/scanner/ftp/ftp_version
  set RHOSTS <IP>
  run
  ```

- **Netcat**: Para probar manualmente la conexión al puerto.
  ```shell
  nc <IP> 21
  ```

- **ftpmap**: Para escanear y enumerar directorios y archivos.
  ```shell
  ftpmap -h <IP>
  ```

- **Enum4linux**: Para enumerar usuarios y configuraciones si el servidor FTP está integrado con servicios SMB.
  ```shell
  enum4linux -u anonymous -p "" <IP>
  ```

