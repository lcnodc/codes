#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ask the user for a number.

Depending on whether the number is even or odd, print out an appropriate
message to the user. Hint: how does an even / odd number react
differently when divided by 2?

Extras:

    - If the number is a multiple of 4, print out a different message.
    - Ask the user for two numbers: one number to check (call it num)
    and one number to divide by (check). If check divides evenly into
    num, tell that to the user. If not, print a different appropriate
    message.
"""

print("\nVerificando se é par/impar: ")
numero = int(input("Informe um número maior que 0: "))

if numero % 2 == 0:
    print("%d é um número par." % numero)

    if numero % 4 == 0:
        print("%d é multiplo de 4." % numero)
else:
    print("%d é um número impar." % numero)

# Extras
print("\nDivisão de dois números: ")
dividendo = int(input("Informe um número (Dividendo): "))
divisor = int(input("Informe um número (Divisor): "))

if dividendo > divisor:
    if dividendo % divisor == 0:
        print("%d é multiplo de %d." % (dividendo, divisor))
    else:
        print("%d não é multiplo de %d." % (dividendo, divisor))
else:
    print("%d (Dividendo) é menor que %d (Divisor)." % (dividendo, divisor))
