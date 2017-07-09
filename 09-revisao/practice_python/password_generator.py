#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 16: Password Generator

Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
    - Ask the user how strong they want their password to be. For weak
    passwords, pick a word or two from a list.
"""

from random import choice
import string


def get_password(length: int):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    option = 0
    password = []

    [password.append("".join([choice(alphabet) for i in range(length)]))
        for p in range(2)]

    return password[int(input(
        "Choose between the two options:\n1 - %s\n2 -%s\n :" %
        (password[0], password[1]))) - 1] if length < 8 else password[option]


length = int(input("How big is the password you want? "))

print("Your password: %s" % get_password(length))
