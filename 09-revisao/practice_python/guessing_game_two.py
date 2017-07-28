#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 25: Guessing Game Two

In a previous exercise, we’ve written a program that “knows” a number
and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will
have in your head a number between 0 and 100. The program will guess a
number, and you, the user, will say whether it is too high, too low, or
your number.

At the end of this exchange, your program should print out how many
guesses it took to get your number.

As the writer of this program, you will have to choose how your program
will strategically guess. A naive strategy can be to simply start the
guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
But that’s not an optimal guessing strategy. An alternate strategy might
be to guess 50 (right in the middle of the range), and then increase /
decrease by 1 as needed. After you’ve written the program, try to find
the optimal strategy! (We’ll talk about what is the optimal one next
week with the solution.)
"""

import random


def get_secret_number(base, limit):
    print("Enter a number from %i to %i: " % (base, limit), end="")
    secret = random.randint(base, limit)
    print("%i" % secret)
    return secret


def get_suggested_number(base, limit):
    return base if base == limit else random.randint(base, limit)


def guessing_game(secret, base, limit, attempts):

    while True:

        attempts += 1
        suggested_number = get_suggested_number(base, limit)

        print("\nThe hunt number is %i" % suggested_number)

        if suggested_number == secret:
            return attempts
        else:
            base, limit, answer = (base, suggested_number - 1, "l") \
                if secret < suggested_number \
                else (suggested_number + 1, limit, "g")

            print("The secret number is (l)ower or (g)reater:", answer)


if __name__ == "__main__":
    base, limit = 1, 1000
    secret = get_secret_number(base, limit)
    print(
        "The number is %i and it guessed in %i attempts" %
        (secret, guessing_game(secret, base, limit, 0)))
