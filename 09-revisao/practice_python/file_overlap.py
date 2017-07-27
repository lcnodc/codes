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


def get_text_web(url):
    return requests.get(url).text


def write_to_file(filename, text):
    with open(filename, "w") as a_file:
        print(text, file=a_file)
    return filename


def read_from_file(filename):
    with open(filename, "r") as a_file:
        return a_file.read()


def split_text(text):
    return set(map(int, filter(
        lambda n: True if n else False, text.split("\n"))))


if __name__ == "__main__":

    prime_url = "http://www.practicepython.org/assets/primenumbers.txt"
    happy_url = "http://www.practicepython.org/assets/happynumbers.txt"

    prime_set = split_text(
        read_from_file(
            write_to_file(
                "prime.txt", get_text_web(prime_url))))

    happy_set = split_text(
        read_from_file(
            write_to_file(
                "happy.txt", get_text_web(happy_url))))

    print("Numbers that are overlaping:", sorted(prime_set & happy_set))
