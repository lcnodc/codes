#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 14: List Remove Duplicates

Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the
duplicates.

Extras:
    Write two different functions to do this - one using a loop and
    constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for
    that in a different function.

"""


def remove_duplicates(l: list) -> list:
    new_list = list()
    [new_list.append(i) for i in l if i not in new_list]
    return new_list


def remove_duplicates2(l: list) -> list:
    return list(set(l))


a = [1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 8, ]

print("Lista sem duplicados: %s" % remove_duplicates(a))
print("Lista sem duplicados 2: %s" % remove_duplicates2(a))
