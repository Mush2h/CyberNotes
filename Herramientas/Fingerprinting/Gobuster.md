# Gobuster

Gobuster es una herramienta utilizada para realizar ataques de fuerza bruta en:
- URIs (directorios y archivos) en sitios web
- Subdominios DNS

Tiene tres modos principales disponibles:
- dir: Modo clásico de fuerza bruta contra subdominios DNS y "vhost"
- dns: Modo de enumeración de subdominios DNS
- help: Muestra la ayuda general de Gobuster
  - Puedes mostrar ayuda específica con `help dir`

## Opciones Interesantes

- `-u`: Define la URL a evaluar
- `-t`: Establece el número de hilos concurrentes
- `-w`: Especifica el archivo que contiene una lista de palabras
- `-x`: Define las extensiones de archivo a buscar

### Ejemplos Básicos

```shell
gobuster dir -u http://<ip>/<directorio> -t 20 -w /usr/

gobuster dir -w /usr/share/dirb/wordlists/common.txt -u <ip>

gobuster dns -d example.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt

gobuster dns -d google.com -w ~/wordlists/subdomains.txt
```

### Ejemplos Avanzados 

- Enumerar directorios con extensiones específicas:
```shell
gobuster dir -u http://<ip> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
```

- Buscar subdominios DNS con un tiempo de espera personalizado:
```shell
gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt -t 50
```

- Fuerza bruta en un servidor con autenticación básica:
```shell
gobuster dir -u http://<ip> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -U admin -P password123
```

- Enumerar directorios en un servidor HTTPS ignorando errores de certificado:
```shell
gobuster dir -u https://<ip> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k
```

- Buscar subdominios con un rango de IP específico:
```shell
gobuster dns -d example.com -w /usr/share/wordlists/subdomains.txt --wildcard
```

