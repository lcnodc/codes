#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Listas: Notas de Estudo.

Lista é uma estrutura que pode ser utilizada para armazenar coleções de
dados do mesmo tipo ou não.

"""


"""Formas de declarar e inicializar uma lista."""
my_list = list()
my_other_list = []

print("my_list: %s, my_other_list: %s " % (type(my_list), type(my_other_list)))

"""Cada elemento da lista possui um índice que será utilizado como chave
de acesso ao valor. Lembrando que o índice começa em 0, ou seja, o
primeiro elemento é o elemento de índice 0 e o no caso de uma lista de 5
elemento, o último terá índice 4, mas que pode ser representado por -1.

"""

my_int_list = [1, 2, 3, 4, 5, ]
print(my_int_list)
print(my_int_list[3])
print(my_int_list[0])
print(my_int_list[-1])


"""Listas podem armazenar todos os tipos suportados pelo Python..."""
my_string_list = ["red", "green", "blue", "black"]

print("Color: ", my_string_list[1].title())

""" ... simultâneamente."""
my_mixed_list = [1, "dois", 3.0, [4]]

print("List mixed: ", my_mixed_list)


"""Listas, assim como strings possuem métodos para manipular seus dados,
como por exemplo, adicinar e subtrair elementos.

"""
months = []
months.append("january"); print(months)
months.append("february"); print(months)
months.append("april"); print(months)

months[2] = "march"; print(months)
months.append("april"); print(months)
months.append("june"); print(months)
months.append("may"); print(months)


"""Inserindo itens na lista."""
months.insert(4, months[5]); print(months)


"""Removendo itens da lista."""
del months[6]; print(months)


"""Removendo itens da lista com pop().com

Esse método, remove e retorna o valor removido da lista.
Quando nenhum argumento for informado, o último elemento será removido.
"""
removed_items = []
removed_items.insert(0, months.pop())
print("Removed item: ", removed_items)
print("Months: ", months)

removed_items.append(months.pop(2))
print("Removed item: ", removed_items)
print("Months: ", months)


"""Removendo items pelo valor."""
months.remove("january")
print("Months: ", months)


"""Organizando uma lista.

Em resumo, quando um método da lista é chamado, utilizando o operador .,
o conteúdo da lista é alterado. Porém, quando a lista é passado como
argumento seu conteúdo não é alterado.

Assim, métodos como o .sort() não só retornam o conteúdo da lista de
forma ordenada como o altera permanentemente.

Já o sorted(list), retorna uma lista ordenada, mas conserva a original.

"""
list_of_ints = [43, 4, 12, 100, 67, 44, 6, 11]
print("Lista original: ", list_of_ints)

print("Lista ordenada com sorted: ", (list_of_ints))

list_of_ints.sort(); print("...ordenando a lista com list.sort()")
print("Lista ordenada com list.sort(): ", list_of_ints)


"""Manipulando itens da lista.

Várias operações podem ser realizadas com os itens de uma lista.
No caso de uma lista numérica, funções como max, min e sum podem ser
utilizadas para apurar informações sobre as listas.

len(): retorna a quantidade de itens da lista.
max(): retorna o maior valor da lista.
min(): retorna o menor valor da lista.
sum(): soma todos os itens da lista.

"""
print("Total de itens: ", len(list_integers))
print("Maior valor: ", max(list_integers))
print("Menor valor: ", min(list_integers))
print("Soma dos itens: ", sum(list_integers))


"""Iterando sobre uma lista.

Para iterar sobre uma lista, pode-se utilizar o for.
"""
list_integers = [1, 2, 3, 4, 5, 6]
for i in list_integers:
    print(i)


"""Listas numéricas.

Listas numéricas podem ser criadas utilizando o método range() para
gerar o iterator que ao ser passado para lsit() irá gerar uma lista.
"""
list_integers = list(range(10))
print(list_integers)

for i in list_integers:
    print(i)


"""Pode-se também passar range() diretamente para o for, já que ele só
precisa de um iterator para realizar o loop.

List Comprehensions

Como visto anteriormente, um for pode ser utilizado para percorrer uma
lista e geralmente para escreve um for utilizá-se no mínimo duas linhas.

List comprehensions é uma forma sintática que em uma lista é possível
escreve uma for para iterar sobre uma lista.

"""
list_of_integers = [i for i in range(20, 35)]
print("%s" % [i for i in list_of_integers])


"""Manipulando listas.

Para manipular e selecionar intervalos dentro de uma lista, basta
informar os indices desejados utilizando dois pontos.

lista[inicio : fim - 1]

"""
print(list_of_integers[0:3])
print(list_of_integers[4:-2])
print(list_of_integers[-2:])

print(list_of_integers[:]) 

""" Esta forma também pode ser usada para copiar uma lista."""

list_of_integers_copy = list_of_integers[:]

print("Removendo o %d da lista de inteiros." % list_of_integers.pop(3))
print("Lista de inteiros atualizada: ", list_of_integers[:])
print("Cópia da lista de inteiros: ", list_of_integers_copy[:])


"""Outros exemplos de listas.

Exibindo uma lista com os mais diversos tipos de dados.
"""

lista_variada = [True, [1, 2, 3, 4], 10, 4.3, "python", lambda x: x + 1]

print(lista_variada)
