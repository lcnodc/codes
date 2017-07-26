#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 22: Read from File

Given a .txt file that has a list of a bunch of names, count how many of
each name there are in the file, and print out the results to the
screen. I have a .txt file for you, if you want to use it!

Extra:
    Instead of using the .txt file from above (or instead of, if you
    want the challenge), take this .txt file, and count how many of each
    “category” of each image there are. This text file is actually a
    list of files corresponding to the SUN database scene recognition
    database, and lists the file directory hierarchy for the images.
    Once you take a look at the first line or two of the file, it will
    be clear which part represents the scene category. To do this,
    you’re going to have to remember a bit about string parsing in
    Python 3. I talked a little bit about it in this post.
"""


from bs4 import BeautifulSoup
import requests


def get_soup_web(path):
    """ Return the soup object of the url passed as argument."""
    url = path
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    return soup


def write_to_file(filename, text):
    """Write to a file passed as argument filename the text passed as
    argument.
    """
    with open(filename, "w") as a_file:
        print(text, file=a_file)

    return filename


def read_from_file(filename):
    """Read from file passed as argument."""
    with open(filename, "r") as a_file:
        return a_file.read()


def count_words(text):
    """Count the words of text passed as argument."""
    total_words = 0
    for word in text.split("\n"):
        if word.strip():
            total_words += 1

    return total_words


if __name__ == "__main__":

    filename = "names.txt"
    print(
        "Number of words:",
        count_words(read_from_file(write_to_file(filename, get_soup_web(
            "http://www.practicepython.org/assets/nameslist.txt").get_text().
            strip()))))
