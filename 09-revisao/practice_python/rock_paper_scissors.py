#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 8: Rock Paper Scissors

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)

Remember the rules:
    - Rock beats scissors
    - Scissors beats paper
    - Paper beats rock
"""

from random import randint

results = {
    ("Rock", "Paper"): "Paper",
    ("Paper", "Rock"): "Paper",
    ("Rock", "Scissor"): "Rock",
    ("Scissor", "Rock"): "Rock",
    ("Scissor", "Paper"): "Scissor",
    ("Paper", "Scissor"): "Scissor", }

players = dict()
shape_list = ["Rock", "Paper", "Scissor"]
repeat = True

while repeat:
    try:
        players["player_1"] = shape_list[int(input(
            "Entry with a shape (1 - Rock, 2 - Paper, 3 - Scissor): ")) - 1]

        players["bot"] = shape_list[randint(0, 2)]

        print("Player 1:", players.get("player_1"))
        print("Bot:", players.get("bot"))

        if players.get("player_1") == players.get("bot"):
            print("Draw")
        else:
            print(
                "Winner: %s"
                % results.get(players["player_1"], players["bot"]))

    except (IndexError, ValueError):
        print("Invalid: Entry with value between 1 and 3.")
    else:
        repeat = (
            True if input("Try again (s/n)?").lower() == "s" else False)
