# Hacking con Google (Google Dorking)

El hacking con Google, también conocido como **Google Dorking**, es una técnica que utiliza operadores avanzados de búsqueda de Google para descubrir información específica en internet. A menudo es utilizado por profesionales de seguridad para identificar vulnerabilidades, recopilar información sensible o localizar sistemas y aplicaciones mal configurados.

---

## Tabla Resumen de Operadores

| Operador      | Descripción                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------|
| `OR`          | Busca resultados donde aparece al menos uno de varios términos.                                 |
| `-`           | Excluye resultados que contengan el término que sigue al símbolo.                               |
| `" "`         | Busca una coincidencia exacta del texto dentro de las comillas.                                 |
| `*`           | Actúa como un comodín para reemplazar cualquier palabra o frase en una consulta.                |
| `site:`       | Limita la búsqueda a un dominio o sitio web específico.                                         |
| `related:`    | Encuentra sitios web similares al dominio especificado.                                         |
| `link:`       | Encuentra páginas que enlazan al dominio especificado.                                          |
| `cache:`      | Muestra la versión en caché de una página web indexada por Google.                              |
| `filetype:`   | Busca archivos con una extensión específica (por ejemplo, PDF, DOC, SQL).                       |
| `inurl:`      | Busca páginas donde el término especificado aparece en la URL.                                  |
| `intext:`     | Busca páginas donde el término especificado aparece en el texto del cuerpo.                     |
| `intitle:`    | Busca páginas donde el término especificado aparece en el título.                               |
| `inanchor:`   | Busca páginas donde el término especificado aparece en el texto de anclaje de un hipervínculo.  |

---

## Ejemplos

### Ejemplos Básicos

- **Buscar dentro de un sitio y en el texto del cuerpo**:
`site:youtube.com intext:"Apple"`

- **Buscar términos específicos en URLs**:
`inurl:pepe.com`

- **Buscar PDFs relacionados con ciberseguridad**:
`filetype:pdf ciberseguridad`

- **Buscar archivos Python**:
`ext:py`

- **Búsqueda con comodines en títulos**:
`intitle:ciber *`

### Ejemplos Avanzados (Pro)

- **Buscar archivos PHP que contengan información sensible**:
`ext:php intext:"root:x:0:0:root:/root:/bin/bash"`

- **Buscar cámaras de seguridad expuestas**:
`inurl:"/view/index.shtml"`

- **Buscar archivos de configuración de bases de datos**:
`filetype:sql "password"`

- **Buscar páginas de inicio de sesión de administradores**:
`intitle:"admin login" inurl:admin`

- **Buscar documentos confidenciales en servidores públicos**:
`filetype:doc site:gov "confidencial"`

- **Buscar directorios abiertos en servidores web**:
`intitle:"index of" "parent directory"`

- **Buscar información de contacto en sitios web específicos**:
`site:example.com intext:"contacto"`

- **Buscar archivos de respaldo expuestos**:
`filetype:bak inurl:"backup"`




