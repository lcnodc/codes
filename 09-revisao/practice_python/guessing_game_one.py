#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 9: Guess a number.

Generate a random number between 1 and 9 (including 1 and 9). Ask the
user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input
lessons from the very first exercise)

Extras:
    - Keep the game going until the user types “exit”
    - Keep track of how many guesses the user has taken, and when the
    game ends, print this out.
"""

from random import randint

attempts = 0
guessed = False
hits = 0
repeat = True

while repeat:
    random_number = randint(1, 9)
    while not guessed:
        user_number = int(input("Guess the number (1 - 9):"))
        message, guessed, attempts, hits = \
            ("Gotcha!", True, attempts + 1, hits + 1) if user_number == random_number else \
                ("Too low!", False, attempts + 1, hits + 0) if user_number < random_number else \
                    ("Too high!", False, attempts + 1, hits + 0)

        print(message)

    repeat, guessed = \
        (False, False) if input("Try again (Type 'exit' to exit)? ").lower() == "exit" else \
            (True, False)

print("Attempts: %d\nHits: %d" % (attempts, hits))
