#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 15: Reverse Word Order

Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the
string:

    My name is Michele
    Then I would see the string:

    Michele is name My
    shown back to me.
"""


def reverse_word_order(word: str):
    return " ".join(word.split(" ")[::-1])


long_string = input("Write a long string: ")
print("The string in backwards order: %s" % reverse_word_order(long_string))
