#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 6: String Lists.

Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)

Credits:
  http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""

__author__ = "lcnodc"

word = input("Digite uma palavra: ")
drow = word[::-1]

print("Palavra original: ", word)
print("Palavra invertida: ", drow)

# Utilizando a estrutura if...else.
if word == drow:
    print("A palavra %s é um palíndromo" % word)
else:
    print("A palavra %s não é um palíndromo" % word)

# Utilizando um operador ternário
print(
    "A palavra %s %s um palíndromo." %
    (word, ("é" if word == drow else "não é")))
