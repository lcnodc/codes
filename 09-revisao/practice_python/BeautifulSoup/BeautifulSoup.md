# BeautifulSoup 4

Transforma um complexo documento HTML em uma complexa árvore de objetos Python.

_Este documento cobre uma pequena parte dos recursos da BeautifulSoup4, e foi
fortemente inspirado nas referências relacionadas abaixo_.

### Instalação 

Com o pip:

```bash
$ pip install bs4
```

Ou baixe e instale do fonte, o tarball em:

```
http://www.crummy.com/software/BeautifulSoup/download/4.x
```

Descompacte e execute:

```bash
$ python setup.py install
```

### Fazendo uma sopa

Para realizar o parser, importe a lib para seu código:

```python
from bs4 import BeautifulSoup
```

e passe para o construtor de BeautifulSoup o documento, que pode ser passado
de duas formas:

- Atráves do endereço de memória do documento:

```python
with open("index2.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")
```

- Através do endereço url do documento:

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

Uma string corresponde a um texto dentro de uma tag. BeautifulSoup usa a
classe NavigableString para representar esses textos:

```python
print("Imprimindo uma string de uma tag: ", soup.title.string)
```

**BeautifulSoup**

O objeto BeautifulSoup representa o documento como um todo, suporta a maioria
dos métodos descritos em _Navegando na árvore_ e _Procurando na árvore_.

```python
soup = BeautifulSoup(file, "html.parser")
```

### Navegando na árvore

**Para baixo**

Muitas tags podem conter string e outras tag. Estes elementos são filhos de
tags. Beautiful Soup provê vários atributos para navegar e iterar sobre os
filhos das tags.

- Navegando usando nomes de tags

A forma mais simples de navegar é informar o nome da tag. 

```python
print("Exibindo o head: ", soup.head)
print("Exibindo o head: ", soup.head.title)
```

- .contents and .children

Uma lista dos filhos de uma tag é retornada com o atributos .contents

```python
print("Exibindo o conteúdo de head com .contents:", soup.head.contents)
```

Com .children, assim como .contents é retornado o conteúdo de uma tag, 
representado por um objeto iterator, que poderá ser utilizado com um for.

```python
print("Recuperando o iterador com children de head:\n", soup.head.children)
print("
    Recuperando os elementos de head: ",
    [element for element in soup.head.children])
```

**Para cima**




**Para os lados**

**Para baixo e adiante**


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

### Referências

Crummy: The Site, [Beautiful Soup Documentation][1]
Read the Docs, [Beautiful Soup Documentation][2]

[1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[2]: https://media.readthedocs.org/pdf/beautiful-soup-4/latest/beautiful-soup-4.pdf
