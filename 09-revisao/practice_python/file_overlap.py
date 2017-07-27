#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 23: File Overlap

Given two .txt files that have lists of numbers in them, find the
numbers that are overlapping. One .txt file has a list of all prime
numbers under 1000, and the other .txt file has a list of happy numbers
up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any
other number. And yes, happy numbers are a real thing in mathematics -
you can look it up on Wikipedia. The explanation is easier with an
example, which I will describe below.)
"""


import requests


def get_soup_web(path):
    """ Return the text of the url passed as argument."""
    return requests.get(path).text


def split_text(text):
    """Return a set of text's numbers passed as argument."""
    return set(map(int, text.split("\n")))


if __name__ == "__main__":

    prime_url = "http://www.practicepython.org/assets/primenumbers.txt"
    happy_url = "http://www.practicepython.org/assets/happynumbers.txt"

    prime_set = split_text(get_soup_web(prime_url))
    happy_set = split_text(get_soup_web(happy_url))

    print("Numbers that are overlaping:", sorted(prime_set & happy_set))
