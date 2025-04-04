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

## Evasión de Firewalls y Sistemas de Detección de Intrusos

Comandos para eludir sistemas de seguridad:

### Opciones Avanzadas

- `-f`: Fragmenta los paquetes enviados durante el escaneo.
- `--D <decoy1,decoy2>`: Usa señuelos para ocultar la fuente real del escaneo.
- `--S <ip>`: Suplanta la dirección IP de origen.
- `--g <puerto>`: Suplanta el puerto de origen.
- `--spoof-mac <mac_address>`: Suplanta la dirección MAC de origen.
- `--e <interfaz>`: Especifica la interfaz a usar para el escaneo.
- `--data-length <número>`: Agrega datos aleatorios a los paquetes.

```bash
nmap -f <ip>
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

Los scripts NSE permiten capacidades avanzadas de escaneo:

### Parámetros

- `--sC`: Ejecuta scripts predeterminados durante el escaneo.
- `--script <nombre_script>`: Ejecuta scripts específicos proporcionados por la biblioteca NSE de Nmap.
- `--script-trace`: Muestra los intercambios de entrada/salida durante la ejecución del script.

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