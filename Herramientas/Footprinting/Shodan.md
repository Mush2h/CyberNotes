# Shodan

Shodan es un motor de búsqueda diseñado para descubrir dispositivos específicos, con un enfoque particular en dispositivos del Internet de las Cosas (IoT). Recopila información de varios servicios y protocolos, incluidos HTTP, SSH, FTP y SNMP.

- **Nota:** Es necesario registrarse para utilizar todas las funciones de Shodan.

## Sitio Web Oficial

* https://www.shodan.io/

## Filtros de Búsqueda

Shodan ofrece varios filtros para refinar las búsquedas:
- `city`: Especifica la ubicación física (ciudad) del dispositivo.

- `country`: Especifica el país donde se encuentra físicamente el dispositivo.

- `geo`: Permite especificar las coordenadas de longitud y latitud de la ubicación física del dispositivo. Un tercer parámetro opcional puede indicar el radio en kilómetros desde el punto especificado.

- `hostname`: Especifica el nombre de host del dispositivo.

- `net`: Especifica la dirección IP del host.

- `os`: Especifica el sistema operativo que ejecuta el host.

- `port`: Especifica un puerto particular de los soportados por el motor de búsqueda.

- `after/before`: Especifica un rango de fechas para acotar la búsqueda.

- `has_screenshot`: Indica si existe una captura de pantalla del dispositivo asociado.

Estos filtros pueden combinarse para crear búsquedas potentes y dirigidas a tipos específicos de dispositivos o servicios en internet.

## Ejemplos de Uso 


1. **Buscar cámaras IP en una ciudad específica:**
   ```
   city:"Madrid" port:554 has_screenshot:true
   ```
   Esto buscará cámaras IP en Madrid que tengan capturas de pantalla disponibles.

2. **Identificar servidores web con vulnerabilidades conocidas:**
   ```
   http.title:"Apache2 Ubuntu Default Page" country:"ES"
   ```
   Esto buscará servidores Apache2 en España que podrían estar mal configurados.

3. **Dispositivos IoT con puertos abiertos:**
   ```
   port:23 os:"Linux" country:"MX"
   ```
   Esto buscará dispositivos IoT con Telnet habilitado en México.

4. **Buscar routers con configuraciones predeterminadas:**
   ```
   net:"192.168.1.0/24" "Default password"
   ```
   Esto buscará routers en un rango de red específico que aún utilicen contraseñas predeterminadas.

5. **Identificar sistemas SCADA expuestos:**
   ```
   "SCADA" port:502 country:"US"
   ```
   Esto buscará sistemas SCADA accesibles en Estados Unidos.

6. **Buscar dispositivos con servicios FTP abiertos:**
   ```
   port:21 "220"
   ```
   Esto buscará dispositivos con servicios FTP habilitados.

