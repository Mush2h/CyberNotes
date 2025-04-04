# WHOIS

WHOIS es un protocolo y herramienta poderosa para buscar y recuperar información sobre nombres de dominio registrados, direcciones IP y recursos de red.

## Características Clave

- Búsqueda de propiedad de dominios
- Descubrimiento de detalles de registro
- Recuperación de información sobre recursos de red

## Información Típicamente Obtenida

### Detalles del Dominio
- Información del propietario del dominio
- Fechas de registro
- Fechas de expiración
- Detalles del servidor DNS
- Información del registrador
- Direcciones de correo electrónico de contacto
- Registros de servidores de nombres

## Uso Básico

### Sintaxis del Comando

```bash
kali@kali:~$ whois <dominio>
kali@kali:~$ whois cocacola.com
```

### Ejemplos Adicionales

#### Obtener Información de un Dominio Específico
```bash
kali@kali:~$ whois microsoft.com
```

#### Consultar Información de una Dirección IP
```bash
kali@kali:~$ whois 8.8.8.8
```


#### Buscar Información de Contacto del Propietario
```bash
kali@kali:~$ whois example.com | grep -i "email"
```

#### Analizar un Dominio con Whois y Filtrar Resultados
```bash
kali@kali:~$ whois targetsite.com | grep -E "Domain Name|Registrar|Creation Date|Expiration Date"
```

#### Automatizar Consultas con un Script
```bash
kali@kali:~$ for domain in $(cat domains.txt); do whois $domain; done
```

