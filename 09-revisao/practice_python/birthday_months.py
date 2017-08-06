#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 35: Birthday Months

This exercise is Part 3 of 4 of the birthday data exercise series. The
other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’
names and birthdays to disk. In this exercise, load that JSON file from
disk, extract the months of all the birthdays, and count how many
scientists have a birthday in each month.

Your program should output something like:

{
    "May": 3,
    "November": 2,
    "December": 1
}
"""

from collections import Counter
from datetime import date
import json
import requests
import sys


def get_text_web(url):
    return json.loads(requests.get(url).text)


def read_from_file(filename):
    with open(filename, "r") as a_file:
        text = json.load(a_file)
    return text


def get_month_name(text_date):
    year, month, day = text_date.split("-")
    obj_date = date(int(year), int(month), int(day))
    month_name = obj_date.strftime("%B")
    return month_name[:]


def count_months(persons, months: dict) -> dict:
    for name, birthday in persons.items():
        month_name = get_month_name(birthday)
        months[month_name] = months.get(month_name, 0) + 1
    return months


def count_months2(persons, months: list) -> Counter:
    for name, birthday in persons.items():
        months.append(get_month_name(birthday))
    return Counter(months)


def exit(message):
    sys.exit(message)


def functions_switcher(option):
    switcher = {"F": (read_from_file, "random_persons.json"),
                "W": (get_text_web, "https://goo.gl/EQZpaE"),
                "X": (exit, "\nBye bye!\n")}
    function = switcher.get(option)[0]
    return function(switcher.get(option)[1])


if __name__ == "__main__":

    while True:
        option = input(
            "Get your data from:\n\t[F]ile\n\t[W]eb:\n\tE[x]it: ").upper()
        print("\n", count_months(functions_switcher(option), dict()), "\n")
        # print("\n", count_months2(functions_switcher(option), list()), "\n")
