#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 26: Check Tic Tac Toe

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


def wins_positions():
    return (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))


def get_winner(players_positions):

    busy_position = 0

    for player in (1, 2):
        for positions in wins_positions():
            for position in positions:
                if position in players_positions.get(player):
                    busy_position += 1
                    if busy_position == 3:
                        return "Player %i wins." % player
            busy_position = 0
    else:
        return "This game hasn't winner."


def get_players_positions(game):
    positions = []
    players_positions = dict()

    for player in (1, 2):
        for num_row, row_value in enumerate(game):
            for num_col, col_value in enumerate(row_value):
                if col_value == player:
                    positions.append((num_row, num_col))
        players_positions[player] = positions[:]
        positions.clear()
    return players_positions


if __name__ == "__main__":

    games = [[[2, 2, 0],
              [2, 1, 0],
              [2, 1, 1]],
             [[1, 2, 0],
              [2, 1, 0],
              [2, 1, 1]],
             [[0, 1, 0],
              [2, 1, 0],
              [2, 1, 1]],
             [[1, 2, 0],
              [2, 1, 0],
              [2, 1, 2]]]

    for game in games:
        print(get_winner(get_players_positions(game)))

