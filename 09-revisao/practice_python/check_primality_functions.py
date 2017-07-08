#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 11: Check Primality Functions

Ask the user for a number and determine whether the number is prime or
not. (For those who have forgotten, a prime number is a number that has
no divisors.). You can (and should!) use your answer to Exercise 4 to
help you. Take this opportunity to practice using functions, described
below.

"""

__version__ = "3"


def is_prime(number):
    return False \
        if number < 2 or \
        [i for i in range(2, number) if number % i == 0] \
        else True


number = int(input("Enter with a number: "))

if is_prime(number):
    print("The number %i is prime." % number)
else:
    print("The number %i is not prime." % number)
