## Servicio MySQL (Puerto 3306)

MySQL es un sistema de gestión de bases de datos relacional.

### Enumeración de MySQL

```ruby
nmap -p 3306 --script=mysql-enum,mysql-databases,mysql-users <IP>
mysql -h <IP> -u root -p
```

#### Herramientas adicionales

- **Metasploit**: Framework para pruebas de penetración.
  ```bash
  use auxiliary/scanner/mysql/mysql_version
  set RHOSTS <IP>
  run
  ```

- **Hydra**: Ataques de fuerza bruta para credenciales.
  ```bash
  hydra -L users.txt -P passwords.txt <IP> mysql
  ```

- **MySQL Client**: Conexión directa para pruebas manuales.
  ```bash
  mysql -h <IP> -u <usuario> -p
  ```

- **sqlmap**: Automatización de pruebas de inyección SQL.
  ```bash
  sqlmap -u "mysql://<usuario>:<password>@<IP>:3306/<base_de_datos>"
  ```

#### Comandos útiles en MySQL

```sql
SHOW DATABASES;
USE <base_de_datos>;
SHOW TABLES;
SELECT * FROM <tabla>;
```