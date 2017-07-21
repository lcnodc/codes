#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 17: Decode A Web Page

This is the first 4-chili exercise of this blog! We’ll see what people
think, and decide whether or not to continue with 4-chili exercises in
the future.

Use the BeautifulSoup and requests Python packages to print out a list
of all the article titles on the New York Times homepage.

I changed the statement from the previous exercise and instead of 
displaying the articles of NYT I will show the titles of the exercises
in the Practice Python website.

Finally, I record the program outputs in a text file called "output.txt"

"""

from bs4 import BeautifulSoup
import requests


def initial_parse(path):
    url = path
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    return soup


def parse_html2():
    s = initial_parse("http://www.practicepython.org/exercises/")
    return s.find_all("div")


with open("output.txt", "w") as arquivo:
    for div in parse_html2():
        if 'class' in div.attrs:
            if 'left' in div.get('class'):
                for li in div.find_all('li'):
                    print(20 * "-=", file=arquivo)
                    print(li.get_text().strip(), file=arquivo)
                print(20 * "-=", file=arquivo)
