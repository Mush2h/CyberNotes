"""
Este script realiza un descubrimiento de puertos comunes en un servidor utilizando un proxy Squid.
Se conecta a una lista de puertos TCP comunes en la dirección configurada (main_url) y verifica si están abiertos.
El script utiliza una sesión de requests para realizar las solicitudes HTTP a través del proxy configurado.
Incluye manejo de excepciones para errores de conexión, tiempo de espera y otros problemas relacionados con las solicitudes.
"""

#!/usr/bin/python3

import sys
import signal
import requests

# Manejo de señal para Ctrl+C
def def_handler(sig, frame):
    print("\n\n [!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Configuración
main_url = "http://127.0.0.1"  # Editar si es necesario
squid_proxy = {'http': '<IP_SQUID_PROXY>', 'https': '<IP_SQUID_PROXY>'}  # Agregar proxy HTTPS

# Función para descubrir puertos
def portDiscovery():
    common_tcp_ports = {21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 5900, 8080, 8443}

    session = requests.Session()  # Usar una sesión para eficiencia

    for tcp_port in common_tcp_ports:
        url = f"{main_url}:{tcp_port}"
        try:
            response = session.get(url, proxies=squid_proxy, timeout=3)  # Timeout para evitar bloqueos
            print(f"[+] Puerto {tcp_port} abierto - Código HTTP: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"[-] Puerto {tcp_port} cerrado o no accesible")
        except requests.exceptions.Timeout:
            print(f"[!] Timeout en el puerto {tcp_port}")
        except requests.exceptions.RequestException as e:
            print(f"[X] Error en puerto {tcp_port}: {e}")

# Ejecutar si es el script principal
if __name__ == '__main__':
    portDiscovery()


