## Servicio DNS (Puerto 53)

DNS (Domain Name System) traduce nombres de dominio legibles por humanos a direcciones IP. Es un servicio crítico para la navegación en Internet.

### Enumeración de DNS

```ruby
nmap -p 53 --script=dns-brute,dns-cache-snoop,dns-recursion <IP>
dig @<IP> <domain> ANY
```

#### Herramientas adicionales para la enumeración de DNS

1. **dnsenum**  
   Una herramienta para enumerar información DNS, como servidores de nombres, registros MX y subdominios.
   ```bash
   dnsenum <domain>
   ```

2. **fierce**  
   Una herramienta para encontrar subdominios y realizar consultas DNS.
   ```bash
   fierce --domain <domain>
   ```

3. **dnsrecon**  
   Permite realizar múltiples tipos de consultas DNS, como transferencias de zona y búsquedas inversas.
   ```bash
   dnsrecon -d <domain>
   ```

4. **host**  
   Una herramienta simple para realizar consultas DNS.
   ```bash
   host -t ns <domain>
   host -t mx <domain>
   ```

5. **sublist3r**  
   Una herramienta para enumerar subdominios utilizando motores de búsqueda y consultas DNS.
   ```bash
   sublist3r -d <domain>
   ```

#### Notas adicionales

- **Transferencia de zona (Zone Transfer):**  
  Si el servidor DNS está mal configurado, es posible realizar una transferencia de zona para obtener información sensible.  
  ```bash
  dig @<IP> <domain> axfr
  ```

- **Consulta inversa (Reverse Lookup):**  
  Permite obtener nombres de dominio asociados a una dirección IP.  
  ```bash
  dig -x <IP>
  ```

