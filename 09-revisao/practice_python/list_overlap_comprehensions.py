#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 10: List Overlap Comprehensions

This week’s exercise is going to be revisiting an old exercise (see
Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes. Write this in one line of
Python using at least one list comprehension. (Hint: Remember list
comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution
using one line of Python, but a few readers pointed out that this was
impossible to do without using sets that I had not yet discussed on the
blog, so you can either choose to use the original directive and read
about the set command in Python 3.3, or try to implement this on your
own and use at least one list comprehension in the solution.

Extra:
    - Randomly generate two lists to test this.

"""

from random import randint, sample

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # Deprecated
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Deprecated

a = sample(range(10), randint(1, 10))
b = sample(range(10), randint(1, 10))
c = []

# Using set, filter and lambda.
d = list(filter(lambda x: x in set(b), set(a)))

# Using list comprehensions.
[c.append(i) for i in a if i in b and i not in c]

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
