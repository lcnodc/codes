#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 21: Write To A File

Take the code from the How To Decode A Website exercise (if you didn’t
do it or just want to play with some different code, use the code from
the solution), and instead of printing the results to a screen, write
the results to a txt file. In your code, just make up a name for the
file you are saving to.

Extras:
    Ask the user to specify the name of the output file that will be
    saved.
"""

from bs4 import BeautifulSoup
import requests


def get_soup_web(path):
    """Return a object soup from a url passed."
    url = path
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    return soup


def write_to_file(filename, text):
    with open(filename, "a") as a_file:
        print(text, file=a_file)


if __name__ == "__main__":

    soup = get_soup_web("http://www.lipsum.com/feed/html")
    filename = input("Enter with a filename: ")
    
    [write_to_file(filename, element.text.strip())
        for element in soup.select("div > #lipsum")]
