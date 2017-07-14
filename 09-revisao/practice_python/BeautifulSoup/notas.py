#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BEAUTIFUL SOUP: NOTAS

Lib que realizar parser em arquivos html e xml, utilizando seu parser
favorito.

Retorna uma estrutura de objetos Python que podem ser navegáveis e
modificáveis.

INSTALANDO BEAUTIFUL SOUP (bs4).
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Com o pip:
$ pip install bs4

Ou baixe e instale do fonte, o tarball em:
http://www.crummy.com/software/BeautifulSoup/download/4.x

Descompacte e execute:
$python setup.py install

"""

# Importando a lib do BeautifulSoup
from bs4 import BeautifulSoup
from random import randint

"""
Para parsear um documento passe a referência do arquivo aberto para o
bs4, informando o parser desejado.
TODO: cobrir url's posteriormente.
"""
with open("index2.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Exibindo o conteúdo de soup formatado.
# print(soup.prettify())

"""
TIPOS DE OBJETOS

TAG
A tag corresponde a exatamente a tag xml ou html do documento original.
Ela pode ser acessada utilizando o operador ponto (.) e o tipo da tag.

"""
print("Selecionando uma tag <a>: ", soup.a)
print(36 * "-=")
"""
NAME
Com o mesmo operador é possível acessar a o atributos name da tag.
"""
print("Recuperando o nome de uma tag: ", soup.a.name)
print(36 * "-=")
"""
É possível também alterar o nome da tag, utilizando o operador de igual.
"""
d = soup.a
d.name = "d"
print("Alterando o nome de uma tag: ", d)
print(36 * "-=")
"""
ATRIBUTOS
Acessando um atributo, utilizando a sintaxe de dicionários.
"""
print("Acessando um atributo de uma tag:", soup.a['target'])
print("Acessando um atributo de uma tag:", soup.img['src'])
print(36 * "-=")
"""
Ou acessar todos os atributos diretamente com attrs.
"""
print("Acessando todos os atributos de uma tag:", soup.a.attrs)

print(36 * "-=")
"""
Podemos iterar sobre esses atributos pois seu retorno é um dict:
"""
for key, value in soup.a.attrs.items():
    print("atributo: %s, \tvalor: %s" % (key, value))
print(36 * "-=")
"""
Assim, caso deseje alterar algum atributo recuperado com attrs, é só
recuperar o atributo desejado utilizando a sintaxe de um dict.

NAVIGABLESTRING
Uma string é uma pequeno texto presente dentro de uma tag. A classe
NavigableString contém esses textos.
"""
print("Imprimindo uma string de uma tag: ", soup.title.string)
print(36 * "-=")
"""
Para editar a string utilize o método replace_with.
"""
soup.title.string.replace_with("Pratique Python")
print("Substituindo uma string de uma tag: %s" % soup.title.string)
print(36 * "-=")
"""
BEAUTIFULSOUP
É a representação do documento como um todo.
Suporta a maioria dos métodos de navegação.
"""
print("Exibindo o nome de um objeto bs: ", soup.name)
print(36 * "-=")
"""
COMENTÁRIOS
Nesse exemplo, vou:
- fazer um loop em uma div que contém um comentário.
- Exibir o tipo de cada tag existente dentro da div

Entre os tipos existe um que é comentário.
"""
for i in soup.find("div", "header-left"):
    print("Tipo: ", type(i), i)
print(36 * "-=")
"""
NAVEGANDO NA ÁRVORE

Utilizar nomes é o método mais fácil de navegar na árvore de objetos.

Acessando o head e exibindo o title.
"""
print("Exibindo o head: ", soup.head.title)
print(36 * "-=")
"""
Para recuperar todas as tags utilize find_all

No exemplo abaixo, recuperamos todas as tags li que poderão ser
acessadas utilizando a sintaxe de uma lista.
"""
print("Quantidade de itens recuperados: ", len(soup.find_all("li")))
print("Acessando o elementos 50: ", soup.find_all("li")[50])
print(36 * "-=")
"""
CONTENTS AND CHILDREN

contents retorna o conteúdo de uma tag, excluindo a própria tag.string
"<title>Título</title>".contents == "Título"

"""
print("Exibindo head: ", soup.head)
print(36 * "-=")
print("Exibindo o conteúdo de head com .contents:", soup.head.contents)
print(36 * "-=")
print("Quantidade de itens dentro de head:", len(soup.head.contents))
print(36 * "-=")
"""
O primeiro elemento de head é uma nova linha, '\n'. Assim a expressão
abaixo irá exibir somente uma linha em branco.string
"""
print("Exibindo o conteúdo de head com .contents:", soup.head.contents[0])
print(36 * "-=")
"""
mas podemos selecionar qualquer elementos dentro da lista retornada.
Gerando um aleatório para selecionar qualquer conteúdo dentro de lista.
"""
elemento = randint(0, len(soup.head.contents) - 1)
print(elemento)
print(
    "Exibindo o conteúdo de head (anterior):",
    soup.head.contents[elemento - 1]
    if elemento - 1 >= 0 else None)
print(
    "Exibindo o conteúdo de head (selecionado):", soup.head.contents[elemento])
print(
    "Exibindo o conteúdo de head (posterior):",
    soup.head.contents[elemento + 1]
    if elemento + 1 < len(soup.head.contents) else None)

print(36 * "-=")
"""
Outra forma de iterar sobre o conteúdo de uma tag é utilizando o
children.
Recuperando o head
"""
print("Recuperando o head:\n", soup.head)
print("Recuperando o children de head:\n", soup.head.children)
print(36 * "-=")
"""
Considerando que children retorna um iterator, podemos iterar sobre ele.sobre
"""
print("Imprimindo os child's de head:")
for child in soup.head.children:
    print(child)
print(36 * "-=")
"""
Os childs de head são os contents em forma de string, inclusive os '\n'.

DESCENDANTS

Chamando simplesmente descendants, temos um generator.
"""
print(soup.head.descendants)
print(36 * "-=")
"""
Assim, podemos iterar sobre o generator e recuperar cada descendente da
tag pesquisada.
"""
print("Imprimindo os descendants:")
for descendant in soup.head.descendants:
    print(descendant)
print(36 * "-=")
"""
Diferença entre children e descendants:

O descendants é recursivo, ou seja, irá recuperar a tag e seu conteúdo,
e depois o seu conteúdo. Se o conteúdo for outra tag, o loop continuará
até o fim das tags.
"""
print("Tamanho da lista com children: ", len(list(soup.head.children)))
print("Tamanho da lista com descendants: ", len(list(soup.head.descendants)))
print(36 * "-=")
"""
STRINGS

Retorna uma string existente dentro de uma tag ou de uma tag filha.

"""
print("Recupera a string de uma tag (title): ", soup.title.string)
print(36 * "-=")
"""
Quando uma tag tiver mais que uma string, será retornado None.
"""
print("Recupera a string de uma tag (body): ", soup.body.string)
print(36 * "-=")
"""
Quando uma tag retorna mais que uma string, poderá ser utilizado strings
ao invésde string e string_stripped para retirar os espaços.
"""
print("Imprimindo todas as strings de uma tag:")
for string in soup.body.strings:
    print(string)
print(36 * "-=")

print("Imprimindo todas as strings de uma tag, sem espaços:")
for string in soup.body.stripped_strings:
    print(repr(string))
print(36 * "-=")
"""
PARENT

O atributo parent permite acessar elementos pais das tags.

"""
print("Acessando title:", soup.title)
print(36 * "-=")
print("Acessando parent de title:", soup.title.parent)
print(36 * "-=")
