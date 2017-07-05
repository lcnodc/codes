#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 7: List Comprehensions

Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list
that has only the even elements of this list in it.

"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Utilizando list comprehensions.
b = [i for i in a if i % 2 == 0]

# Utilizando funções builtins do Python.
c = list(filter(lambda x: x % 2 == 0, a))

print("a: ", a)
print("b: ", b)
print("c: ", c)
