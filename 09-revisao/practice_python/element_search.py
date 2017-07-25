#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 20: Element Search

Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
"""


def in_list(a_list, number):
    return True if [True for i in a_list if i == number] else False


def in_list2(a_list, number):
    if len(a_list) == 1:
        return a_list[0] == number
    elif a_list[len(a_list) // 2] > number:
        return in_list2(a_list[:len(a_list) // 2], number)
    else:
        return in_list2(a_list[len(a_list) // 2:], number)


if __name__ == "__main__":

    a_list = [1, 3, 4, 5, 6, 7, 8, 12, 15, 20, 23, 33, 45, 64]
    number = int(input("Enter a number: "))

    print(
        "The number %i is in the list %s: %s" %
        (number, a_list, in_list(a_list, number)))

    print(
        "The number %i is in the list %s: %s" %
        (number, a_list, in_list2(a_list, number)))
