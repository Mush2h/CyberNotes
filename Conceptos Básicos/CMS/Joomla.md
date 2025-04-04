## Joomla (Joomscan)

JoomScan es un escáner de vulnerabilidades de código abierto diseñado específicamente para el CMS Joomla. Aquí tienes una chuleta con sus parámetros más útiles:

```ruby
perl joomscan.pl -u <url>
```

### Parametros importantes

- `-u`, --url <URL>: Especifica la URL o dominio del sitio Joomla objetivo
- `-ec`, --enumerate-components: Enumera los componentes instalados
- `--cookie <String>`: Establece una cookie específica para la sesión de escaneo
- `-a, --user-agent <User-Agent>`: Usa un User-Agent personalizado
- `-r`, --random-agent: Usa un User-Agent aleatorio por cada petición
- `--timeout <Time-Out>`: Establece el tiempo máximo de espera por respuesta
- `--proxy <proxy>:` Usa un proxy (por ejemplo, http://127.0.0.1:8080)

### Funcionalidades avanzadas
- Enumeración de versión: Detecta la versión exacta de Joomla instalada.
- Escaneo de vulnerabilidades: Comprueba vulnerabilidades conocidas según la versión.
- Análisis de componentes: Detecta fallos en extensiones y módulos instalados.
- Detección de firewall: Identifica cortafuegos web comunes basados en Joomla.
- Descubrimiento de archivos: Localiza archivos sensibles como logs o backups.

### Output Options
- Genera reportes en formato texto plano y HTML.

### Ejemplos prácticos

1. **Escaneo básico de un sitio Joomla:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com
   ```
   Este comando realiza un escaneo básico para detectar vulnerabilidades en el sitio `https://www.ejemplo.com`.

2. **Enumerar componentes instalados:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com -ec
   ```
   Útil para identificar extensiones o módulos que puedan tener vulnerabilidades conocidas.

3. **Usar un proxy para el escaneo:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com --proxy http://127.0.0.1:8080
   ```
   Este comando redirige el tráfico del escaneo a través de un proxy, ideal para análisis en entornos controlados.

4. **Personalizar el User-Agent:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com -a "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
   ```
   Simula ser un bot de Google para evitar restricciones basadas en el User-Agent.

5. **Establecer un tiempo de espera personalizado:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com --timeout 10
   ```
   Configura un tiempo de espera de 10 segundos para cada solicitud, útil en sitios con respuestas lentas.

6. **Generar un reporte en HTML:**
   ```bash
   perl joomscan.pl -u https://www.ejemplo.com --output reporte.html
   ```
   Crea un reporte detallado en formato HTML para compartir con el equipo de seguridad.