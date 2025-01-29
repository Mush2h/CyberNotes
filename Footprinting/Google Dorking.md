# Google Hacking (Google Dorking)

Google hacking, also known as **Google Dorking**, is a technique that leverages advanced Google search operators to uncover specific information on the internet. It is often used by attackers to identify security vulnerabilities, gather sensitive information, or locate misconfigured systems and applications.

---

## Summary Table of Operators

| Operator      | Description                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------|
| `OR`          | Searches for results where at least one of multiple terms appears.                              |
| `-`           | Excludes results containing the term following the symbol.                                      |
| `" "`         | Searches for an exact match of the text within the quotation marks.                             |
| `*`           | Acts as a wildcard to replace any word or phrase in a search query.                             |
| `site:`       | Limits the search to a specific domain or website.                                              |
| `related:`    | Finds websites similar to the specified domain.                                                 |
| `link:`       | Finds pages that link to the specified domain.                                                  |
| `cache:`      | Displays the cached version of a webpage as indexed by Google.                                  |
| `filetype:`   | Searches for files with a specific extension (e.g., PDF, DOC, SQL).                             |
| `inurl:`      | Searches for pages where the specified term appears in the URL.                                 |
| `intext:`     | Searches for pages where the specified term appears in the body text.                           |
| `intitle:`    | Searches for pages where the specified term appears in the title.                               |
| `inanchor:`   | Searches for pages where the specified term appears in hyperlink anchor text.                   |

---

## Examples

### Basic Examples

- **Search within a site and body text**:
`site:youtube.com intext:"Apple"`

- **Search for specific terms in URLs**:
`inurl:pepe.com`

- **Search for PDFs related to cybersecurity**:
`filetype:pdf ciberseguridad`

- **Search for Python files**:
`ext:py`

- **Wildcard search in titles**:
`intitle:ciber *`

### Advanced Example (Pro)

- **Search for PHP files containing sensitive information**:

`ext:php intext:"root:x:0:0:root:/root:/bin/bash"`




