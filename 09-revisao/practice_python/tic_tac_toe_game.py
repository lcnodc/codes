#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 29: Tic Tac Toe Game

This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The
other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build a
Tic Tac Toe game in Python:

1. Draw the Tic Tac Toe game board
2. Checking whether a game board has a winner
3. Handle a player move from user input

The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to use
the functions from those previous exercises all together in the same
program to make a two-player game that you can play with a friend. There
are a lot of choices you will have to make when completing this
exercise, so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

    - You should keep track of who won - if there is a winner, show a
    congratulatory message on the screen.
    - If there are no more moves left, don’t ask for the next player’s
    move!

As a bonus, you can ask the players if they want to play again and keep
a running tally of who won more - Player 1 or Player 2.
"""

# TODO: Refactoring, please!

import random


# ::Define the winner:: #######################################################
def wins_positions():
    return (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))


def get_winner(players_positions):

    busy_position = 0

    for player in (" X ", " O "):
        for positions in wins_positions():
            for position in positions:
                if position in players_positions.get(player):
                    busy_position += 1
                    if busy_position == 3:
                        return "Player %s wins." % player
            busy_position = 0
    else:
        return "This game hasn't winner."
###############################################################################


# ::Draw the board:: ##########################################################
def draw_top(columns, row):
    print(" ---" * columns if row == 0 else "", end="")


def draw_middle(columns, row, pieces):

    print()
    for column in range(columns):
        piece = pieces.get((row + 1, column + 1), "   ")
        print("|" + piece, end="")
    print("|")


def draw_bottom(columns):
    print((" ---" * columns), end="")


def draw_board(rows, columns, pieces):

    for row in range(rows):
        draw_top(columns, row)
        draw_middle(columns, row, pieces)
        draw_bottom(columns)

    print()
###############################################################################


# :: Define Positions :: ######################################################
def convert_player_positions(players_positions):
    x, o = [], []

    for c, v in players_positions.items():
        if v == " X ":
            x.append(tuple(map(lambda x: x - 1, c)))
        if v == " O ":
            o.append(tuple(map(lambda x: x - 1, c)))
    return {" X ": x, " O ": o}


def get_position(piece):
    if piece == " X ":
        position = input("USER: Enter with a position in board: ")
        return tuple(map(int, position.split(",")))
    if piece == " O ":
        position = str(random.randint(1, 3)) + "," + str(random.randint(1, 3))
        print("CPU: Enter with a position in board:", position)
        return tuple(map(int, position.split(",")))
###############################################################################


# :: Main :: ##################################################################
if __name__ == "__main__":
    rows = 3
    columns = 3
    pieces = dict()
    busy_positions = 0
    piece = " X "

    while busy_positions < (rows * columns):
        position = get_position(piece)
        if position in pieces.keys():
            print("Position busy, choose other...")
        else:
            busy_positions += 1
            pieces[position] = piece
            piece = " O " if piece == " X " else " X "
        draw_board(rows, columns, pieces)
    print("The player winner: ", get_winner(convert_player_positions(pieces)))
###############################################################################
