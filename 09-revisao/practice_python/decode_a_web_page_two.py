#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 19: Decode A Web Page 2

Using the requests and BeautifulSoup Python libraries, print to the
screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/
    monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to
print out the text to the screen so that you can read the full article
without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup
and requests libraries through the solution of the exercise posted here)

This will just print the full text of the article to the screen. It will
not make it easy to read, so next exercise we will learn how to write
this text to a .txt file.
"""

from bs4 import BeautifulSoup
import requests


def get_soup_file(path):
    with open(path, "r") as a_file:
        soup = BeautifulSoup(a_file, "html.parser")
    return soup


def get_soup_web(path):
    url = path
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")


if __name__ == "main":

    # soup = get_soup("https://goo.gl/csBVZj")
    soup = get_soup_file("vanity.html")

    with open("saida.txt", "w") as other_file:
        for element in soup.select("section p"):
            print(element.text + "\n", file=other_file)
