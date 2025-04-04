# theHarvester

theHarvester es una herramienta gratuita basada en Linux para recopilar información sobre dominios, subdominios y direcciones de correo electrónico desde internet.

## Notas Importantes

- **Ya no funciona con Google ni LinkedIn**
- Diseñada para la recopilación de información y reconocimiento
- Código abierto y mantenida activamente

## Características Clave

- Enumeración de dominios
- Descubrimiento de subdominios
- Recolección de direcciones de correo electrónico
- Soporte para múltiples fuentes de datos
- Opciones de reporte flexibles

## Parámetros de Uso

### Opciones Principales

- `-d`: Especificar el dominio objetivo
  - Ejemplo: `-d ejemplo.com`

- `-b`: Seleccionar fuente de datos
  - Fuentes soportadas: 
    - `all`: Buscar en todas las fuentes disponibles
    - `bing`: Búsqueda en Microsoft Bing
    - `yahoo`: Búsqueda en Yahoo
    - `baidu`: Búsqueda en Baidu
    - `shodan`: Motor de búsqueda IoT de Shodan

- `-f`: Exportar resultados a un archivo
  - Formatos: HTML, XML
  - Ejemplo: `-f resultados.html`

- `-l`: Limitar el número de resultados
  - Ejemplo: `-l 100`

- `-s`: Realizar una consulta en Shodan

## Ejemplos Básicos

```console
kali@kali:~$ theHarvester
kali@kali:~$ theHarvester -d cocacola.es -b all
kali@kali:~$ theHarvester -d cocacola.es -b bing
```

## Ejemplos Avanzados 

### Buscar subdominios específicos en Bing y limitar resultados

```console
kali@kali:~$ theHarvester -d ejemplo.com -b bing -l 50
```

### Exportar resultados en formato HTML para análisis posterior

```console
kali@kali:~$ theHarvester -d ejemplo.com -b all -f reporte.html
```

### Usar Shodan para buscar dispositivos IoT relacionados con un dominio

```console
kali@kali:~$ theHarvester -d ejemplo.com -b shodan
```

### Combinación de múltiples fuentes para un análisis más completo

```console
kali@kali:~$ theHarvester -d ejemplo.com -b bing,yahoo,baidu
```

### Generar un reporte XML para integrarlo con otras herramientas

```console
kali@kali:~$ theHarvester -d ejemplo.com -b all -f reporte.xml
```

### Uso en un entorno corporativo para auditorías internas

```console
kali@kali:~$ theHarvester -d midominiointerno.com -b all -l 200 -f auditoria.html
```
