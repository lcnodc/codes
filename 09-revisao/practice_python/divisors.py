#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 4: Divisors.

Create a program that asks the user for a number and then prints out a
list of all the divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into another number. For
example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

numero = int(input("Entre com um número: "))

# Basic form.
print("Os divisores de %d são: " % numero, end="")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
print()

# Utilizando filter e lambda.
print(
    "Os divisores de %d são: %s: " %
    (numero,
        list(filter(lambda x: numero % x == 0, range(1, numero + 1)))))

# Utilizando List Comprehensions.
print("Os divisores de %d são: %s: " %
    (numero, [i for i in range(1, numero + 1) if numero % i == 0]))
