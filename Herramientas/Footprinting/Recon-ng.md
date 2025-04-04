# Recon-ng

Recon-ng es un framework basado en Python que ofrece a los usuarios herramientas automatizadas para el reconocimiento de redes y la recopilación de información. Su interfaz es similar a Metasploit y se basa en varios módulos para su funcionalidad. Algunos módulos requieren una clave API, pero actualmente el sitio web para obtener estas claves no está disponible.

## Instalación

- Recon-ng viene preinstalado en Kali Linux. Para otras distribuciones de Linux, puedes instalarlo usando:

```bash
apt-get install recon-ng
```

## Uso Básico

- Para iniciar Recon-ng:

```bash
recon-ng 
```

## Características Principales

### Espacios de Trabajo:

Recon-ng permite trabajar con diferentes espacios de trabajo:
- Listar espacios de trabajo: `workspaces list`
- Crear un espacio de trabajo: `workspaces create [Nombre]`
- Cargar un espacio de trabajo: `workspaces load [Nombre]`
- Eliminar un espacio de trabajo: `workspaces remove [Nombre]`

### Gestión de Base de Datos:

- Ver el esquema de la base de datos: `db schema`
- Eliminar información: `db delete [información]`
- Insertar un dominio: `db insert domains`

### Visualización de Información Almacenada:

`show [tipo de información]`

- Ejemplos: `show hosts`, `show domains`, `show credentials`

### Instantáneas:
- Crear una instantánea: `snapshot take`
- Eliminar una instantánea: `snapshot remove [nombre]`
- Listar instantáneas: `snapshots list`
- Cargar una instantánea: `snapshot load [nombre]`

### Módulos:
- Listar herramientas del marketplace: `marketplace search`
- Búsqueda específica: `marketplace search [palabra clave]`
- Instalar un módulo: `marketplace install [ruta]`
- Instalar todos los módulos: `marketplace install all`
- Cargar un módulo: `modules load [módulo]`
- Listar opciones del módulo: `options list`
- Configurar una opción del módulo: `options set [campo] [valor]`
- Ejecutar un módulo: `run`
- Salir del módulo: `back`

### Claves API:
- Agregar una clave API: `keys add [nombre_api] [clave]`
- Listar claves: `keys list`
- Eliminar una clave: `keys remove [nombre_api]`

## Ejemplos Avanzados para Hacking Ético

### Escaneo de Subdominios
1. Cargar el módulo de subdominios:
   ```bash
   modules load recon/domains-hosts/subdomain_enum
   ```
2. Configurar el dominio objetivo:
   ```bash
   options set source [dominio.com]
   ```
3. Ejecutar el módulo:
   ```bash
   run
   ```

### Recolección de Direcciones de Correo Electrónico
1. Cargar el módulo de correos electrónicos:
   ```bash
   modules load recon/contacts-contacts/email_hunter
   ```
2. Configurar el dominio objetivo:
   ```bash
   options set domain [dominio.com]
   ```
3. Ejecutar el módulo:
   ```bash
   run
   ```

### Generación de Informes
1. Crear un informe en formato HTML:
   ```bash
   modules load reporting/html
   ```
2. Configurar el nombre del archivo de salida:
   ```bash
   options set filename [reporte.html]
   ```
3. Ejecutar el módulo:
   ```bash
   run
   ```

### Uso de Claves API para Módulos
1. Agregar una clave API para Shodan:
   ```bash
   keys add shodan [tu_clave_api]
   ```
2. Cargar el módulo de Shodan:
   ```bash
   modules load recon/hosts-hosts/shodan_hostname
   ```
3. Configurar el objetivo:
   ```bash
   options set host [ip_o_dominio]
   ```
4. Ejecutar el módulo:
   ```bash
   run
   ```
