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

from datetime import datetime

name = input("What's your name?: ")
age = int(input("How old is you?: "))

current_year = datetime.now().year
centenary = (100 - age) + current_year

quantity = int(input("How many times do your like show this message? "))

for i in range(quantity):
    print("%d - %s, your will be 100 years in %d." % (i + 1, name, centenary))
