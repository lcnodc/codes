#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise 12:List Ends
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For
practice, write this code inside a function.
"""

from random import randint, sample


def first_and_last(l: list) -> list:
	"""Return first and last elements takes list.
	::param l: list of integers
	::type l: list
	::rtype: list of integers
	"""
	return l[0::len(l) - 1 if len(l) > 1 else None]


"""Return a random list of random length."""
a = sample(range(100), randint(1, 100))

print("Random List: %s" % a)
print("First and Last Element: %s" % first_and_last(a))
