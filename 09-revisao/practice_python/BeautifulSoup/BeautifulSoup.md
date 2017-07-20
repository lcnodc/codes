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

- .decendants

Retorna uma lista de todos os elementos descendentes, parecido com children, 
mas esse age de forma recursiva.

```python
print("Retorna tags com .descendants: ", [element for element in soup.head])
```

- .string

Retorna a string imediatamente abaixo da tag referenciada. Caso possua mais de
uma, None será retornado.

```python
print("Recupera a string de uma tag (title): ", soup.title.string)
print("Recupera a string de uma tag (body): ", soup.body.string)
```

.strings and stripped_strings

Se existir mais de uma string dentro de uma tag, use the .strings. Esse
generator proporcionará a iteração sobre os elementos retornados.

```python
[print(element) for element in soup.body.strings]
```

Porém, para cada string, uma quebra de linha será retornada, o que poderá ser resolvido com stripped_strings.

```python
[print(element) for element in soup.body.stripped_strings]
```

**Para cima**

- .parent

Retorna o elemento imediatamente superior (pai) da tag.

```python
print("Acessando parent de title:", soup.title.parent)
```

- .parents

Retorna todos os elementos acima da tag selecionada.

```python
[elements for element in soup.find(id="extra").parents]
```

**Para os lados**

- .next_sibling ou .previous_sibling

Retorna o elemento imediato de mesmo nível do documento.

```python
print(
    "div header-center: ", soup.find('div',
    'header center').next_sibling.next_sibling.next_sibling)
```

- .next_siblings ou .previous_siblings

Retorna todos os elementos de mesmo nível do documento.

**Para baixo e adiante**

- next_element ou .previous_element

Retorna o elemento, parseado imeadiatamente.

```python
print("Recuperando próximo elemento: ", soup.a.next_element)
```

- next_element ou .previous_element

### Procurando na árvore

**Tipos de filtros**

**find_all**

- string

Uma simples string passada como argumento representando uma tag, retorna todas
as tags iguais existentes no documento.

```python
soup.find_all("a")
```

- regular expression

Também é possível passar um expressão regular para o filtro.

```python
import re

soup.find_all(class_=re.compile("sister$"))
```

- list

É possível passar uma lista que irá retorna todos elementos correspondentes a
qualquer um dos argumentos passados.

```python
soup.find_all(["a", "div"])
```

- True

Passando True como argumento, todas as tags serão retornadas.

```python
soup.find_all(True)
```

- function

Também é possível passar uma function como argumento para find_all. As tags 
retornadas serão todas que a function retornar True.

```python
def has_class(tag):
    return tag.has_attr("class")


soup.find_all(has_class)
```

**find_all()**

Procura através das tag's descendentes e retorna todas os descendentes que 
coincidem com o argumento informados. Pode receber como argumento:

- name:

Retorna todas as tags com nome igual ao argumento informado, podendo ser o 
argumento uma string, uma expressão regular, uma lista, uma function ou um
valor True.

```python
print(soup.find_all("a"))
```

- Keywords arguments

Retorna todas as tags do valor passado como chave que possuem o atributo igual
ao valor passado.

```python
print(soup.find_all(id="extra"))
```

- Pesquisando pela classe CSS

Pode-se pesquisar pela classe css utilizando a palavra-chave css_ juntamente
com find_all().

```python
print(soup.find_all(class_="paragrafo_especial"))
```

- O argumento string

Utilizando a palavra chave string pode-se pesquisar por termos existentes nas
string ao invés das tags.

```python
print(soup.find_all(string=re.compile("nisi.$")))
```

- O argumento limit

limit é um argumento que define a quantidade de elementos retornados quando 
utilizado o método find_all.

```python
print(soup.find_all("p", limit=1))
```

- O argumento recursive

A pesquisa com find_all é recursiva por padrão. Ou seja, o retorno será uma 
análise de todos os descendentes da tag pesquisada, suas filhas, filhas das
filhas e assim por diante.


**find_parent e parents**

Realiza uma pesquisa no documento para cima, considerando a tag atual.

**find_next_sibling e siblings**

Itera sobre o resto de um elemento de next_sibling na árvore, retornando dos os
elementos em que o argumento passado coincidir.

**find_previous_sibling e siblings**

Itera sobre o resto de um elemento de previous_sibling na árvore, retornando
dos os elementos em que o argumento passado coincidir.

**find_next e all_next**

Itera sobre a próxima/todas a(s) tag(s) do documento, que coincidirem com o
valor passado como argumento.

**find_previous e all_previous**

Itera sobre as strings que anteriores à tag pesquisada no documento, sendo que
find_previous retorna somente a primeira que e all retorna todas que
coincidirem com o argumento.

**CSS Selectors**

BS4 suporta a maioria dos seletores CSS utilizados, basta passar uma string
dentro do método .select de um objeto Tag/BeautifulSoup.


### Referências

- Crummy: The Site, [Beautiful Soup Documentation][1]

[1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
