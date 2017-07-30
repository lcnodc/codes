#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 28: Max Of Three

Implement a function that takes as input three variables, and returns
the largest of the three. Do this without using the Python max()
function!

The goal of this exercise is to think about some internals that Python
normally takes care of for us. All you need is some variables and if
statements!
"""

import random


def get_max(a, b, c):
    if a > b:
        if a > c:
            return a
        elif c > a:
            return c
        else:
            return a, c
    elif b > a:
        if b > c:
            return b
        elif c > b:
            return c
        else:
            return b, c
    else:
        if a > c:
            return a, b
        elif c > a:
            return c
        else:
            return a, b, c


def get_random_numbers(amount):

    for number in range(amount):
        yield random.randint(1, 100)


if __name__ == "__main__":

    for i in range(10):
        a, b, c = get_random_numbers(3)
        print(
            "The max of three (%i, %i, %i) is %s" %
            (a, b, c, get_max(a, b, c)))
