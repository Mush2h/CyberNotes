# Ejemplos de Uso de ARP para Hacking Ético  

El protocolo ARP (Address Resolution Protocol) es una herramienta fundamental para el descubrimiento de equipos en redes locales. A continuación, se presentan algunos ejemplos prácticos de cómo utilizar ARP.  

## 1. Escaneo de Red con `arp-scan`  
`arp-scan` es una herramienta que permite descubrir dispositivos en una red local utilizando solicitudes ARP.  

### Ejemplo básico:  
```bash  
sudo arp-scan --interface=eth0 --localnet  
```  
Este comando escanea todos los dispositivos conectados a la red local a través de la interfaz `eth0`.  

## 2. Spoofing de ARP con `arpspoof`  
`arpspoof` es una herramienta que permite realizar ataques de suplantación ARP para interceptar tráfico en la red.  

### Ejemplo:  
```bash  
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1  
```  
Este comando engaña al dispositivo con IP `192.168.1.100` haciéndole creer que el atacante es el gateway (`192.168.1.1`).  

## 3. Visualización de la Tabla ARP  
El comando `arp` puede ser utilizado para inspeccionar la tabla ARP local y verificar las direcciones IP y MAC conocidas.  

### Ejemplo:  
```bash  
arp -a  
```  
Este comando muestra todas las entradas ARP almacenadas en la tabla del sistema.  

## 4. Descubrimiento de Dispositivos con `netdiscover`  
`netdiscover` utiliza ARP para identificar dispositivos en la red local.  

### Ejemplo:  
```bash  
sudo netdiscover -r 192.168.1.0/24  
```  
Este comando escanea el rango de IPs `192.168.1.0/24` para identificar dispositivos activos.  

