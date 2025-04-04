# Inspección de Certificados SSL

Podemos inspeccionar el certificado SSL de un servidor web.

```ruby
openssl s_client -connect ejemplo.com:443
```
Este comando se conecta al servidor en el puerto 443 y muestra información detallada sobre el certificado SSL, como la validez del certificado, la fecha de expiración, el tipo de cifrado, etc.

## Herramientas

Herramientas útiles incluyen 'sslyze', 'sslscan' y otras.

- **Sslyze** es una herramienta de análisis de seguridad SSL utilizada para evaluar la configuración SSL de un servidor. Proporciona información detallada sobre el cifrado utilizado, los protocolos soportados y los certificados SSL.

- **SSLScan** es otra herramienta de análisis de seguridad SSL utilizada para evaluar la configuración SSL de un servidor. Proporciona información detallada sobre los protocolos SSL/TLS soportados, el cifrado utilizado y los certificados SSL.

```ruby 
sslscan url.com
```

- La principal diferencia entre sslyze y sslscan es que sslyze se centra en evaluar la seguridad SSL/TLS de un servidor web mediante una exploración exhaustiva de los protocolos y configuraciones SSL/TLS, mientras que sslscan se enfoca en identificar los protocolos SSL/TLS soportados por el servidor y los cifrados utilizados.

Identificar la información proporcionada por las herramientas de análisis SSL/TLS es de suma importancia, ya que nos permite detectar vulnerabilidades en la configuración de un servidor y tomar medidas para proteger nuestra información confidencial.

### Ejemplo adicional: Verificar la compatibilidad con TLS 1.2 y 1.3

```ruby
openssl s_client -connect ejemplo.com:443 -tls1_2
openssl s_client -connect ejemplo.com:443 -tls1_3
```
Estos comandos verifican si el servidor soporta los protocolos TLS 1.2 y TLS 1.3 respectivamente.

### Ejemplo adicional: Obtener el certificado en formato PEM

```ruby
openssl s_client -connect ejemplo.com:443 -showcerts
```
Este comando muestra el certificado en formato PEM, que puede ser útil para análisis adicionales.

## Heartbleed

Por ejemplo, Heartbleed es una vulnerabilidad de seguridad que afecta la biblioteca OpenSSL y permite a los atacantes acceder a la memoria de un servidor vulnerable. Si un servidor web es vulnerable a Heartbleed y lo detectamos mediante estas herramientas, significa que un atacante podría potencialmente acceder a información confidencial, como claves privadas, nombres de usuario y contraseñas, etc.

### Ejemplo adicional: Detectar Heartbleed con Nmap

```bash
nmap --script ssl-heartbleed -p 443 ejemplo.com
```
Este comando utiliza Nmap para detectar si un servidor es vulnerable a Heartbleed.

### Ejemplo adicional: Comprobar la revocación del certificado

```ruby
openssl s_client -connect ejemplo.com:443 -status
```
Este comando verifica el estado de revocación del certificado utilizando OCSP (Online Certificate Status Protocol).

### Herramientas adicionales

- **TestSSL.sh**: Una herramienta de línea de comandos para probar la seguridad SSL/TLS de un servidor. Proporciona un análisis detallado de los protocolos soportados, cifrados, y configuraciones de seguridad.

```bash
./testssl.sh ejemplo.com
```

- **Nmap con scripts NSE**: Nmap incluye varios scripts NSE para analizar configuraciones SSL/TLS, como `ssl-enum-ciphers` para enumerar los cifrados soportados.

```bash
nmap --script ssl-enum-ciphers -p 443 ejemplo.com
```

Estas herramientas y comandos son esenciales para realizar pruebas de penetración y auditorías de seguridad en servidores web.