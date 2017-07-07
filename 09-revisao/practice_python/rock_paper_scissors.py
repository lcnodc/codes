#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 8: Rock Paper Scissors.

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to
the winner,and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    Discussion

Concepts for this week:
    While loops
    Infinite loops
    Break statements
"""

from random import randint

# https://gist.github.com/anonymous/a267b59db6206c03646a0196709764d7
results = {"r": "s", "p": "r", "s": "p"}
repeat = True

while repeat:
    user = input("User, (r)ock, (p)aper, (s)cissors: ").lower()
    bot = ["r", "p", "s"][randint(0, 2)]

    print("User: %s\nBot: %s" % (user, bot))

    print(
        "Draw" if user == bot else ("User" if results[user] == bot else "Bot"))

    repeat = True if input("Try again? (s/n): ").lower() == "s" else False
