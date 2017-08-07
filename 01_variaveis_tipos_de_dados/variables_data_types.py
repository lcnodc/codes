#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Variáveis e Tipos de Dados: Notas de Estudo.

Variáveis são utilizadas para armazenar todos os dados manipulados
por um sistema. Uma linguagem de programação pode oferecer suporte a
inúmeros tipos de dados.

"""

"""Declarando uma variável do tipo string."""
my_var = " hello "

""" Um dado do tipo string oferece alguns métodos que permitem alterar
seu conteúdo, concatenar com outras string, formatá-lo para impressão,
etc.
"""

print(my_var)

"""title(): retorna a string com a primeira maiúscula."""
print(my_var.title())

"""Concatenando strings."""

my_var += "world "

print(my_var.title())

"""strip(): elimina espaços na string."""

print(my_var.title().strip())

""" Tipos númericos.

Inteiros e Floats, são tipos númericos que podem ser utilizados para
as mais diversas operações matemáticas.

"""
print("Soma: 1 + 1 = ", 1 + 1)
print("Subtração: 1 - 1 = ", 1 - 1)
print("Multiplicação: 2 * 2 = ", 2 * 2)
print("Divisão: 2.4 / 2 = ", 2.4 / 2)
print("Exponenciação: 2 ** 3 = ", 2 ** 3)

