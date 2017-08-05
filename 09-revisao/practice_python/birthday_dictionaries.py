#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 33: Birthday Dictionaries

This exercise is Part 1 of 4 of the birthday data exercise series. The
other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays
are, and be able to find that information based on their name. Create a
dictionary (in your file) of names and birthdays. When you run your
program it should ask the user to enter a name, and return the birthday
of that person back to them. The interaction should look something like
this:

    >>> Welcome to the birthday dictionary. We know the birthdays of:
    Albert Einstein
    Benjamin Franklin
    Ada Lovelace
    >>> Who's birthday do you want to look up?
    Benjamin Franklin
    >>> Benjamin Franklin's birthday is 01/17/1706.
"""


def get_persons():
    return {"Ada Lovelace": "12/10/1815",
            "Alan Turing": "06/23/1912",
            "Albert Einstein": "03/14/1879",
            "Benjamin Franklin": "01/17/1706",
            "Guido Van Rossum": "01/31/1956",
            "Isaac Newton": "01/04/1643",
            "Linux Torvalds": "12/28/1969"}


def get_person(name):

    return get_persons().get(name, "\n\t\t\t...Sorry, name not found.")


if __name__ == "__main__":

    print("Welcome to the birthday dictionary. We know the birthdays of:\n")
    [print("\t" + name) for name, birthday in get_persons().items()]

    name = input("\nWho's birthday do you want to look up? ")
    print("\n" + name + "'s birthday is", get_person(name))
