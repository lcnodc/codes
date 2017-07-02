#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 5: List Overlap.

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

Extras:
    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure
    this out at this point - we’ll get to it soon).

References:

    Python for Begginers:
    http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

"""

from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

"""Forma básica.
"""
for i in a:
    if i in b:
        if i not in c:
            c.append(i)

print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)

"""Converte em conjuntos
Ao converter em conjunto as duas listas, foi possível utilizar o
operador intersection, que retorna somente os itens existentes em ambos.
"""
print("Lista c (com conjuntos):", set(a) & set(b))

"""Utilizando List Comprehensions.
Para isso, foi necessário inserir os elementos em um conjunto e retornar
a representação de lista do conjunto.
"""
print(
    "Lista c (list comprehension):",
    list(set([i for i in a if i in b])))

"""Uma variação utilizando lambda.
"""
print(
    "Lista c (lambda):",
    list(set((lambda a, b: [n for n in a if n in b])(a, b))))

"""Com filter.
Retorna somente os elementos da lista em que a condição for True.

"""
print("Lista c (filter):", list(filter(lambda x: x in a, b)))

"""Extras 1 e 2.
Problema da repetição resolvido. Ao criar a lista, converte-a em um
conjunto.
"""
random_list_a = set([randint(1, 20) for i in range(10)])
random_list_b = set([randint(1, 20) for i in range(10)])

print(
    "Lista c (random):",
    list(filter(lambda x: x in random_list_a, random_list_b)))

print(
    "Lista c (list comprehension):",
    list(set([i for i in random_list_a if i in random_list_b])))

"""Forma básica.
O not in agora é desnecessário.
"""
random_list_c = []

for i in random_list_a:
    if i in random_list_b:
        if i not in random_list_c:
            random_list_c.append(i)

print("Lista a:", random_list_a)
print("Lista b:", random_list_b)
print("Lista c:", random_list_c)
