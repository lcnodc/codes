#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 01: Character input.

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:
    Add on to the previous program by asking the user for another number
    and printing out that many copies of the previous message. (Hint:
    order of operations exists in Python)
    Print out that many copies of the previous message on separate
    lines.
    (Hint: the string "\n is the same as pressing the ENTER button)
    
Credits:
    Michele Pratusevich
    http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

"""

# importa datetime do módulo datetime.
from datetime import datetime

nome = input("Qual o seu nome: ")
# Perunta sobre a idade e converte para inteiro.
idade = int(input("Qual a sua idade: "))

# Recupera o ano utilizando datetime.
ano_atual = datetime.now().year
# Calcula o centésinmo aniversário.
centenario = (100 - idade) + ano_atual

# Extras
quantidade = int(input("Quantas vezes deseja exibir a mensagem? "))

for i in range(quantidade):
    print("%d - %s, você fará 100 anos em %d." % (i + 1, nome, centenario))
