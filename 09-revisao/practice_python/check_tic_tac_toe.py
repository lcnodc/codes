#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 25: Check Tic Tac Toe

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The
other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe
board. However, this is significantly more than half an hour of coding,
so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game
of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token
in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic
Tac Toe game board, tell me whether anyone has won, and tell me which
player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a
column, or a diagonal. Don’t worry about the case where TWO people have
won - assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

winner_schema = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]

"""


def get_winner(positions):

    player = 1

    if positions[0] == positions[1] == positions[2] == player:
        return "Player %i Wins!" % player
    elif positions[3] == positions[4] == positions[5] == player:
        return "Player %i Wins!" % player
    elif positions[6] == positions[7] == positions[8] == player:
        return "Player %i Wins!" % player
    elif positions[0] == positions[3] == positions[6] == player:
        return "Player %i Wins!" % player
    elif positions[1] == positions[4] == positions[7] == player:
        return "Player %i Wins!" % player
    elif positions[2] == positions[5] == positions[8] == player:
        return "Player %i Wins!" % player
    elif positions[0] == positions[4] == positions[8] == player:
        return "Player %i Wins!" % player
    elif positions[2] == positions[4] == positions[6] == player:
        return "Player %i Wins!" % player
    else:

        player = 2

        if positions[0] == positions[1] == positions[2] == player:
            return "Player %i Wins!" % player
        elif positions[3] == positions[4] == positions[5] == player:
            return "Player %i Wins!" % player
        elif positions[6] == positions[7] == positions[8] == player:
            return "Player %i Wins!" % player
        elif positions[0] == positions[3] == positions[6] == player:
            return "Player %i Wins!" % player
        elif positions[1] == positions[4] == positions[7] == player:
            return "Player %i Wins!" % player
        elif positions[2] == positions[5] == positions[8] == player:
            return "Player %i Wins!" % player
        elif positions[0] == positions[4] == positions[8] == player:
            return "Player %i Wins!" % player
        elif positions[2] == positions[4] == positions[6] == player:
            return "Player %i Wins!" % player
        else:
            return "This game hasn't winner."


def get_positions(board):
    positions = []

    for row_value in board:
        for col_value in row_value:
            positions.append(col_value)

    return positions


if __name__ == "__main__":

    board = [[2, 2, 0],
             [2, 1, 0],
             [2, 1, 1]]

    print(get_winner(get_positions(board)))
