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

#### Herramientas adicionales para enumerar SSH

1. **Hydra**: Para realizar ataques de fuerza bruta en el servicio SSH.
   ```shell
   hydra -l usuario -P lista_de_contraseñas ssh://<IP>
   ```

2. **Metasploit**: Framework para pruebas de penetración que incluye módulos para enumerar SSH.
   ```shell
   msfconsole
   use auxiliary/scanner/ssh/ssh_version
   set RHOSTS <IP>
   run
   ```

3. **ssh-audit**: Herramienta para auditar configuraciones y seguridad de un servidor SSH.
   ```shell
   ssh-audit <IP>
   ```

4. **CrackMapExec**: Para enumerar y probar credenciales en múltiples servicios, incluido SSH.
   ```shell
   crackmapexec ssh <IP> -u usuario -p contraseña
   ```

5. **Enum4linux-ng**: Aunque está más orientado a SMB, puede usarse para enumerar servicios SSH en ciertos casos.
   ```shell
   enum4linux-ng -M ssh <IP>
   ```
