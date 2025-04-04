# Esteganografía

## Introducción

La esteganografía es la práctica de ocultar información dentro de otro archivo, mensaje u objeto, de tal manera que su existencia pase desapercibida. Su nombre proviene de las palabras griegas "steganos" (cubierto) y "graphos" (escritura), y se diferencia de la criptografía en que no solo protege el contenido del mensaje, sino también su propia existencia.

### Tipos de Esteganografía:
- Esteganografía en Texto: Oculta mensajes en textos utilizando técnicas como el uso de espacios, letras específicas o patrones en palabras.
- Esteganografía en Imágenes: Utiliza imágenes digitales para incrustar datos manipulando píxeles o los bits menos significativos (LSB).
- Esteganografía en Audio y Video: Oculta información en archivos multimedia mediante modificaciones imperceptibles.
- Esteganografía en Protocolos: Incrusta datos en protocolos de comunicación como TCP/IP.

### Herramientas Útiles para Hacking Ético
- **Steghide**: Herramienta para incrustar y extraer datos en imágenes y archivos de audio.
- **zsteg**: Diseñada para detectar datos ocultos en imágenes PNG y BMP.
- **exiftool**: Permite analizar y modificar metadatos en archivos multimedia.
- **binwalk**: Ayuda a analizar y extraer datos ocultos en binarios y archivos comprimidos.
- **stegsolve**: Herramienta gráfica para analizar imágenes y detectar esteganografía.
- **Outguess**: Software para incrustar y extraer datos en imágenes JPEG.

### Ejemplos útiles

#### Steghide
- **Incrustar un mensaje en una imagen**:
  ```bash
  steghide embed -cf imagen.jpg -ef mensaje.txt -p contraseña
  ```
  Donde `imagen.jpg` es la imagen de portada, `mensaje.txt` es el archivo con el mensaje a ocultar, y `contraseña` es la clave para proteger los datos.

- **Extraer un mensaje oculto**:
  ```bash
  steghide extract -sf imagen.jpg -p contraseña
  ```

#### zsteg
- **Analizar una imagen PNG en busca de datos ocultos**:
  ```bash
  zsteg -a imagen.png
  ```

#### exiftool
- **Ver metadatos de un archivo**:
  ```bash
  exiftool archivo.jpg
  ```

- **Eliminar metadatos de una imagen**:
  ```bash
  exiftool -all= archivo.jpg
  ```

#### binwalk
- **Analizar un archivo binario en busca de datos ocultos**:
  ```bash
  binwalk archivo.bin
  ```

- **Extraer datos ocultos automáticamente**:
  ```bash
  binwalk -e archivo.bin
  ```

#### stegsolve
- **Abrir una imagen para analizar capas de color**:
  Ejecuta `stegsolve.jar`, carga la imagen y utiliza las herramientas de análisis visual para buscar patrones o datos ocultos.

#### Outguess
- **Incrustar un mensaje en una imagen JPEG**:
  ```bash
  outguess -k "clave" -d mensaje.txt imagen.jpg imagen_salida.jpg
  ```

- **Extraer un mensaje oculto**:
  ```bash
  outguess -k "clave" -r imagen_salida.jpg mensaje_extraido.txt
  ```