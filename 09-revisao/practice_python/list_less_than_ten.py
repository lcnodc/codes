#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 3: List less than ten.

Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that
are less than 5.

Extras:
    - Instead of printing the elements one by one, make a new list that
    has all the elements less than 5 from this list in it and print out
    this new list.
    - Write this in one line of Python.
    - Ask the user for a number and return a list that contains only
    elements from the original list a that are smaller than that number
    given by the user.
"""

# Lista inicial.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Lista original: %s" % a)

print("Menores que cinco (for): ", end="")
for i in a:
    if i < 5:
        print(i, end=" ")
print()

"""Extras 1
Lista de menores que 5.
"""
menor_que_cinco = []

for i in a:
    if i < 5:
        menor_que_cinco.append(i)

print("Menores que cinco: %s" % menor_que_cinco)

"""Extras 2
Escrevendo tudo em uma linha utilizando filter.
O Filter é uma função que data um condição, ele trabalha sobre uma lista
e filtra o elementa da lista toda vez que a condição for verdadeira.
"""
print(
    "Menores que cinco (filter, lambda): %s" %
    list(filter(lambda x: x < 5, a)))

"""Extras 3
Solicita ao usuário um valor limite.
"""
limite = int(input("Entre com um valor limite: "))
print(
    "Menores que cinco (filter, lambda, com limite): %s"
    % list(filter(lambda x: x < limite, a)))
