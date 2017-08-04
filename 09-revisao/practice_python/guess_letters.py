#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 31: Guess Letters

This exercise is Part 2 of 3 of the Hangman exercise series. The other
exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is
given by the program that the player has to guess, letter by letter. The
player guesses one letter at a time until the entire word has been
guessed. (In the actual game, the player can only guess 6 letters
incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this
exercise, write the logic that asks a player to guess a letter and
displays letters in the clue word that were guessed correctly. For now,
let the player guess an infinite number of times until they get the
entire word. As a bonus, keep track of the letters the player guessed
and display a different message if the player tries to guess that letter
again. Remember to stop the game when all the letters have been guessed
correctly! Don’t worry about choosing a word randomly or keeping track
of the number of guesses the player has remaining - we will deal with
those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
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


def check_game(hint):
    if "_" in hint:
        return False, False
    else:
        return False, True


if __name__ == "__main__":

    letters = []
    loose = False
    secret_word = choose_a_word(read_from_file("sowpods.txt"))
    win = False

    print("Welcome to Hangman!")

    while not loose and not win:
        print("\n" + get_hint(secret_word, letters))
        letters.append(input("\nType a letter: "))
        loose, win = check_game(get_hint(secret_word, letters))

    print("The word is: ", get_hint(secret_word, letters))
