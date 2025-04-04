# Nmap

- Inicialmente creado como una herramienta de código abierto para escaneo de puertos, funcionando en Linux.
- Es un potente escáner de redes disponible para múltiples sistemas operativos.

## Tareas Principales

- **Descubrimiento de hosts**: Identificar hosts activos en una red.
- **Detección de puertos abiertos**: Determinar qué puertos están abiertos en cada dispositivo.
- **Identificación de servicios**: Detectar los servicios que se ejecutan en cada máquina.
- **Detección del sistema operativo**: Identificar el sistema operativo y su versión.
- **Información de hardware**: Recopilar detalles sobre el hardware de red instalado.
- **Scripts NSE**: Incluye scripts desarrollados conocidos como Nmap Scripting Engine (NSE).

## Descubrimiento de Hosts

La función básica de descubrimiento de hosts se logra con el comando `nmap`:

```bash
nmap 192.168.1.130
nmap 192.168.1.1-254
nmap 192.168.1.0/24
nmap microsoft.com
```

### Parámetros Avanzados

- `-iL <archivo>`: Escanea los hosts listados en el archivo especificado.
- `--excludefile <archivo>`: Excluye los hosts listados en el archivo especificado.
- `-PS <puerto>`: Envía un **TCP SYN** al puerto especificado para descubrimiento de hosts.
- `-PA <puerto>`: Envía un **TCP ACK** al puerto especificado para descubrimiento de hosts.
- `-PU <puerto>`: Envía un **datagrama UDP** al puerto especificado para descubrimiento de hosts.
- `-n`: Desactiva la resolución DNS.
- `-R`: Resuelve DNS para todos los hosts descubiertos.
- `--traceroute`: Traza la ruta hacia los objetivos descubiertos.

## Escaneo de Puertos

Para identificar el estado de los 65,500 puertos en un objetivo:

```bash
nmap <ip> -p-
nmap 192.168.1.1 -p-
```

Para escanear solo los 100 puertos más comunes:

```bash
nmap <ip> -F
nmap 192.168.1.1 -F
```

### Parámetros Avanzados

- `-sS`: Escaneo TCP SYN.
- `-sT`: Escaneo TCP connect.
- `-sA`: Escaneo TCP ACK.
- `--sw`: Escaneo de ventana TCP.
- `--sM`: Escaneo TCP Maimon (un método sutil y sigiloso).

### Ejemplos Interesantes

- Escaneo de puertos específicos:

```bash
nmap -p 22,80,443 <ip>
```

- Escaneo de puertos comunes con velocidad mínima:

```bash
nmap -p 1-1024 --min-rate 1000 <ip>
```

- Escaneo de puertos UDP:

```bash
nmap -sU -p 53,161,162 <ip>
```

## Detección de Servicios y Sistemas Operativos

Basado en los puertos abiertos, Nmap puede detectar sistemas operativos y versiones de servicios:

### Parámetros

- `-sV`: Habilita la detección de versiones.
- `--allports`: No excluye ningún puerto durante la detección de versiones.
- `--version-intensity <nivel>`: Ajusta la intensidad de 0 (menos agresivo) a 9 (más agresivo).
- `--sR`: Escaneo RCP.
- `--O`: Detección del sistema operativo.
- `--v / -V`: Ajusta el nivel de verbosidad del análisis.

### Ejemplo Interesante

- Detección de servicios y sistema operativo con verbosidad:

```bash
nmap -sV -O -v <ip>
```

### Ejemplo Interesante

- Escaneo con señuelos para confundir sistemas de detección:

```bash
nmap -D RND:10 <ip>
```

## Control de Tiempo y Rendimiento

### Parámetros

- `--T <nivel>`: Ajusta la velocidad del escaneo (0 es el más lento pero sigiloso; 5 es el más rápido).
- `--min-parallelism <número> / --max-parallelism <número>`: Ajusta las sondas enviadas en paralelo.
- `--host-timeout <tiempo>`: Ignora objetivos lentos después de un tiempo de espera.

### Ejemplo Interesante

- Escaneo rápido con paralelismo ajustado:

```bash
nmap -T4 --min-parallelism 10 <ip>
```

## Exportación de Resultados

Nmap permite exportar resultados en formatos específicos:

### Opciones

- `--oX <archivo>`: Exporta resultados en formato XML (compatible con Metasploit).
- `--oG <archivo>`: Exporta resultados en formato grepable.
- `--oS <archivo>`: Exporta resultados en formato Script Kiddie.
- `--oA <archivo>`: Exporta resultados en todos los formatos.

```bash
nmap -p- -sS 192.168.37.136 --min-rate 9000 -oG resultado_nmap.grep
nmap -p- -sS 192.168.37.136 --min-rate 9000 -oX resultado_nmap.xml
```

## Ejecución de Scripts

He revisado el archivo y he identificado que la información sobre los scripts y categorías de Nmap encaja perfectamente en la sección **"Ejecución de Scripts"**. He añadido la información proporcionada directamente en esa sección. Aquí está el contenido actualizado:


## Ejecución de Scripts

Los scripts NSE permiten capacidades avanzadas de escaneo. Nmap incluye una amplia variedad de scripts que automatizan tareas de reconocimiento y descubrimiento en la red, además de obtener información valiosa sobre los sistemas y servicios que se están ejecutando en ellos.

### Parámetros

- `--sC`: Ejecuta scripts predeterminados durante el escaneo.
- `--script <nombre_script>`: Ejecuta scripts específicos proporcionados por la biblioteca NSE de Nmap.
- `--script-trace`: Muestra los intercambios de entrada/salida durante la ejecución del script.

```bash
nmap -p 21 --script ftp-brute <ip>
```

### Categorías de Scripts

Nmap organiza sus scripts en diferentes categorías, cada una diseñada para realizar tareas específicas. Algunas de las categorías más comunes incluyen:

- **default**: Esta es la categoría predeterminada en Nmap, que incluye una gran cantidad de scripts de reconocimiento básicos y útiles para la mayoría de los escaneos.
- **discovery**: Se enfoca en descubrir información sobre la red, como la detección de hosts y dispositivos activos, y la resolución de nombres de dominio.
- **safe**: Incluye scripts considerados seguros que no realizan actividades invasivas que puedan desencadenar una alerta de seguridad en la red.
- **intrusive**: Contiene scripts más invasivos que pueden ser detectados fácilmente por sistemas de detección de intrusos o Firewalls, pero que proporcionan información valiosa sobre vulnerabilidades.
- **vuln**: Se enfoca específicamente en la detección de vulnerabilidades y debilidades en los sistemas y servicios que se están ejecutando en la red.

### Ejemplo Interesante

- Escaneo de vulnerabilidades utilizando la categoría `vuln`:

```bash
nmap --script vuln <ip>
```

```bash
nmap -p 21 --script ftp-brute <ip>
```

### Ejemplo Interesante

- Escaneo de vulnerabilidades:

```bash
nmap --script vuln <ip>
```

## Escaneos Silenciosos pero Largos

```bash
nmap -T2 -Pn -n -sV <ip>
nmap -sS -T4 -Pn -p 1-65535 -n --min-rate 1000 --max-retries 0 <objetivo>

# UDP
nmap -sU -T4 -Pn -p 1-65535 -n --min-rate 1000 --max-retries 0 <objetivo>
```


## Evasión de Firewalls

### Técnicas de Evasión

- **MTU (`--mtu`)**: Ajusta el tamaño máximo de los paquetes enviados para que sean lo suficientemente pequeños y pasen desapercibidos por el Firewall.

  ```bash
  nmap --mtu 16 <ip>
  ```

- **Data Length (`--data-length`)**: Agrega datos aleatorios a los paquetes enviados para evitar patrones detectables.
  ```bash
  nmap --data-length 50 <ip>
  ```

- **Source Port (`--source-port`)**: Configura manualmente el puerto de origen de los paquetes enviados.
  ```bash
  nmap --source-port 53 <ip>
  ```

- **Decoy (`-D`)**: Envía paquetes falsos junto con los reales para confundir sistemas de detección.
  ```bash
  nmap -D RND:10 <ip>
  ```

- **Fragmented (`-f`)**: Fragmenta los paquetes enviados para que el Firewall no pueda reconocer el tráfico como un escaneo.
  ```bash
  nmap -f <ip>
  ```

- **Spoof-MAC (`--spoof-mac`)**: Cambia la dirección MAC del paquete para evitar la detección.
  ```bash
  nmap --spoof-mac 00:11:22:33:44:55 <ip>
  ```

- **Stealth Scan (`-sS`)**: Realiza un escaneo SYN sin establecer una conexión completa, lo que lo hace más sigiloso.
  ```bash
  nmap -sS <ip>
  ```

- **Min Rate (`--min-rate`)**: Controla la velocidad de los paquetes enviados para evitar la detección.
  ```bash
  nmap --min-rate 100 <ip>
  ```

### Ejemplo Interesante

- Escaneo con múltiples técnicas de evasión combinadas:
  ```bash
  nmap -sS -f -D RND:5 --spoof-mac 00:11:22:33:44:55 --min-rate 100 <ip>
  ```