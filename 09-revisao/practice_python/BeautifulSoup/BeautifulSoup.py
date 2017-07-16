# BeautifulSoup

Transforma um complexo documento HTML em uma complexa árvore de objetos Python.


### Instalação 

Com o pip:

```python
$ pip install bs4
```

Ou baixe e instale do fonte, o tarball em:

```
http://www.crummy.com/software/BeautifulSoup/download/4.x
```

Descompacte e execute:

```python
$python setup.py install
```

### Fazendo uma sopa

Para realizar o parser, importe a lib para seu código:

```python
from bs4 import BeautifulSoup
```

e passe para o construtor de BeautifulSoup o documento, que pode ser passados
de duas formas:

- Atráves do endereço de memória do documento:

```python
with open("index2.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")
```

- Através do endereço url do documentos:

```python
url = "http://www.practicepython.com"
requested_url = requests.get(url)
html_text = requested_url.text
soup = BeautifulSoup(html_text, "html.parser")
```


### Tipos de Objetos

**Tag**

Um objeto Tab corresponde a uma tag do documento XML/HTML.

```python
print("Selecionando uma tag <a>: ", soup.a)
```

Uma tag tem:

- Nome

```python
print("Recuperando o nome de uma tag: ", soup.a.name)
```

- Atributos

```python
print("Acessando um atributo de uma tag:", soup.a['target'])
print("Acessando todos os atributos de uma tag:", soup.a.attrs)
```

- Atributos Multivalorados

```python
print("Acessando atributos multivalorados de uma tag:", soup.a.["class"]])
```

**NavigableString**

**BeautifulSoup**

**Comentários e Outros Especiais**


### Navegando na árvore

- Para baixo

- Para cima

- Para os lados

- Para baixo e adiante


### Procurando na árvore

**Tipos de filtros**

**find_all**

**find**

**find_parent e parents**

**find_next_sibling e siblings**

**find_previous_sibling e siblings**

**find_next e all_next**

**find_previous e all_previous**

**CSS Selectors**
