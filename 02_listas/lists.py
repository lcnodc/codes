#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Listas: Notas de Estudo.

Lista é uma estrutura de de dado que pode ser utilizadas para armazenar
coleções de dados do mesmo tipo ou não.

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

"""Exibindo o tamanho da lista:"""
print("Quantidade de itens na lista:", len(list_of_ints))

