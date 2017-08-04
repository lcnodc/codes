#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 32: Hangman

This exercise is Part 3 of 3 of the Hangman exercise series. The other
exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise
you will have to have finished Parts 1 and 2 or use the solutions (Part
1 and Part 2).

In this exercise, we will finish building Hangman. In the game of
Hangman, the player only has 6 incorrect guesses (head, body, 2 legs,
and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In
Part 2, we wrote the logic for guessing the letter and displaying that
information to the user. In this exercise, we have to put it all
together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they
have left.
Keep track of the letters the user guessed. If the user guesses a letter
they already guessed, don’t penalize them - let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left",
display some picture art for the Hangman. This is challenging - do the
other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help
you!
"""

import random


def read_from_file(filename):
    with open(filename, "r") as a_file:
        text = a_file.readlines()
    return text


def choose_a_word(a_list):
    return random.choice(a_list).strip()


def get_hint(secret_word, letters):
    hint = []
    for letter_secret in secret_word:
        if letter_secret in letters:
            hint.append(letter_secret)
        else:
            hint.append("_")
    return " ".join(hint)


def check_game(secret_word, letters):

    fail = 0

    for index, letter in enumerate(letters):
        if letter in secret_word:
            secret_word = secret_word.replace(letter, "")
        elif letter in letters[:index]:
            letters.remove(letter)
            print("Letter already informed, please again...")
        else:
            fail += 1

    if not secret_word:
        return False, True
    elif fail == 6:
        return True, False
    else:
        print(
            "You have %i incorrect guesses left" %
            (6 - fail))
        return False, False


if __name__ == "__main__":

    letters = []
    loose = False
    secret_word = choose_a_word(read_from_file("sowpods.txt"))
    win = False

    print("Welcome to Hangman!")

    while not loose and not win:
        print("\n" + get_hint(secret_word, letters))
        letters.append(input("\nType a letter: "))
        print(get_hint(secret_word, letters))
        loose, win = check_game(secret_word[:], letters)

    print("%s" % "You win!" if win else "You loose")
