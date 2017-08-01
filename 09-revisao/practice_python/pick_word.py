#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 30: Pick Word

This exercise is Part 1 of 3 of the Hangman exercise series. The other
exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random
word from a list of words from the SOWPODS dictionary. Download this
file and save it in the same directory as your Python code. This file is
Peter Norvig’s compilation of the dictionary of words used in
professional Scrabble tournaments. Each line in the file contains a
single word.

Hint: use the Python random library for picking a random word.
"""

import random
import requests


def get_text_web(url):
    return requests.get(url).text


def write_to_file(filename, text):
    with open(filename, "w") as a_file:
        print(text, file=a_file)
    return filename


def read_from_file(filename):
    with open(filename, "r") as a_file:
        text = a_file.readlines()
    return text


def choose_a_word(a_list):
    return random.choice(a_list).strip()


if __name__ == "__main__":

    sowpods_url = "http://norvig.com/ngrams/sowpods.txt"

    print(choose_a_word(read_from_file("sowpods.txt")))

    # It can take almost 4 minutes
    # print(choose_a_word(
    #     read_from_file(
    #         write_to_file(
    #             "sowpods.txt", get_text_web(sowpods_url)))))
