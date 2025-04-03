## Servicio RDP (Puerto 3389)

RDP (Remote Desktop Protocol) permite el acceso remoto a escritorios de Windows.

### Enumeración de RDP

```ruby
nmap -p 3389 --script=rdp-enum-encryption <IP>
xfreerdp /u:usuario /p:contraseña /v:<IP>
```

#### Herramientas adicionales

- **rdpscan**: Escanea rápidamente hosts para verificar si el servicio RDP está habilitado.
  ```bash
  rdpscan <IP>
  ```

- **Metasploit**: Usa módulos como `auxiliary/scanner/rdp/rdp_scanner` para enumerar RDP.
  ```bash
  msfconsole
  use auxiliary/scanner/rdp/rdp_scanner
  set RHOSTS <IP>
  run
  ```

- **Hydra**: Realiza ataques de fuerza bruta contra RDP.
  ```bash
  hydra -t 4 -l usuario -P lista_contraseñas rdp://<IP>
  ```

- **CrackMapExec**: Herramienta para enumerar y probar credenciales en servicios RDP.
  ```bash
  crackmapexec rdp <IP> -u usuario -p contraseña
  ```

