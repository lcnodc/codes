#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 34: Birthday Json

This exercise is Part 2 of 4 of the birthday data exercise series. The
other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’
birthdays. In this exercise, modify your program from Part 1 to load the
birthday dictionary from a JSON file on disk, rather than having the
dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to
the dictionary, and update the JSON file you have on disk with the
scientist’s name. If you run the program multiple times and keep adding
new names, your JSON file should keep getting bigger and bigger.
"""

import json, sys


# Global Variables.
person = dict()
persons = dict()


def write_to_file(filename, text):
    with open(filename, "w") as a_file:
        json.dump(text, a_file)
    # return filename


def read_from_file(filename):
    with open(filename, "r") as a_file:
        text = json.load(a_file)
    return text


def load_persons():
    global persons
    persons = read_from_file("birthday_persons.json")


def set_person(name, birthday):
    global person
    person[name] = birthday
    return person


def insert_person():
    name = input("\nWrite the name: ").title()
    birthday = input("Write the birthday [mm/dd/yyyy]: ")
    if input("Do you like insert this person to list[S/N]?").upper() == "S":
        persons.update(set_person(name, birthday))
        write_to_file("birthday_persons.json", persons)
        print("Person insert sucessfully!")
    else:
        print("Person not insert sucessfully!")


def get_persons():
    print()
    for name, birthday in persons.items():
        print("\t" + name)


def get_full_persons():
    print()
    for name, birthday in persons.items():
        print("\t" + name + "'s birthday is " + birthday)


def get_person():
    name = input("\nWho's birthday do you want to look up? ")
    person[name] = persons.get(name, None)
    if not person.get(name):
        print("\n\t" + "Sorry, person not found.")
    else:
        print("\n\t" + name + "'s birthday is " + person.get(name))


def exit():
    sys.exit()


def functions_switcher(option):
    switcher = {"S": get_person, "E": get_full_persons,
                "I": insert_person, "X": exit}
    function = switcher.get(option)
    return function()


if __name__ == "__main__":

    load_persons()

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    get_persons()

    while True:
        option = input(
            "\nWhat do you want: " +
            "\n\t(S)omeone's Birthday \n\t(E)veryone's birthday " +
            "\n\t(I)nsert a New Person \n\tE(x)it: ").upper()

        functions_switcher(option)
