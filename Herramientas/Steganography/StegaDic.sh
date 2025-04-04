#!/bin/bash

# Este script intenta extraer un archivo oculto en una imagen utilizando un diccionario de claves.
# Requiere como entrada una imagen y un archivo de texto con posibles contraseñas.
# Uso: ./StegaDic.sh <imagen> <diccionario> [archivo_salida]

color_rojo="\e[91m"
color_verde="\e[92m"
color_reset="\e[0m"

# Verifica la cantidad de argumentos
if [ $# -lt 2 ] || [ $# -gt 3 ]; then
    echo -e "${color_rojo}Uso: ./StegaDic.sh <imagen> <diccionario> [archivo_salida]${color_reset}"
    exit 1
fi

# Asigna los argumentos a variables
imagen="$1"
diccionario_claves="$2"
archivo_salida="${3:-extraido.dat}" # Archivo de salida por defecto

# Verifica la existencia de la imagen
if [ ! -f "$imagen" ]; then
    echo -e "${color_rojo}La imagen $imagen no existe.${color_reset}"
    exit 1
fi

# Verifica la existencia del diccionario
if [ ! -f "$diccionario_claves" ]; then
    echo -e "${color_rojo}El diccionario $diccionario_claves no existe.${color_reset}"
    exit 1
fi

# Inicializa variables
encontrado=false
intentos=0

# Recorre el diccionario de claves
while IFS= read -r clave; do
    intentos=$((intentos + 1))
    
    # Intenta extraer el archivo oculto utilizando la clave actual
    steghide extract -sf "$imagen" -p "$clave" -xf "$archivo_salida" >/dev/null 2>&1

    # Verifica el resultado de la extracción
    if [ $? -eq 0 ]; then
        echo -e "${color_verde}[+] Archivo extraído correctamente con la clave: $clave${color_reset}"
        echo -e "${color_verde}[+] Archivo guardado como: $archivo_salida${color_reset}"
        encontrado=true
        break
    fi
done < "$diccionario_claves"

# Mensaje final si no se encuentra la clave
if [ "$encontrado" = false ]; then
    echo -e "${color_rojo}[-] Contraseña no encontrada después de $intentos intentos.${color_reset}"
fi
