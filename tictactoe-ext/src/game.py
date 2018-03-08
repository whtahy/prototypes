# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from config import *


#
# Game state ###################################################################

class Game:
    def __init__(self):
        self.select = None
        self.history = []

    def __eq__(self, other):
        return self.history == other.history


#
# Mutate state #################################################################

def move(game):
    game.history.append(game.select)


def select(game, loc = (0, 0)):
    game.select = loc


#
# Derive state #################################################################

def player(n_moves):
    if n_moves % 2 == 0:
        return ch_x
    else:
        return ch_o


def player_str(n_moves):
    if player(n_moves) == ch_x:
        return 'X'
    else:
        return 'O'


def turn(game):
    return 1 + len(game.history) - (winner(game) or tie(game))


def tie(game):
    return len(game.history) == board_rows * board_cols


def winner(game):
    def check(coords):
        for x in coords:
            if x not in moves:
                return False
        return True

    n_moves = len(game.history)
    if n_moves >= 5:
        r, c = game.history[-1]
        first = n_moves % 2 == 0
        moves = game.history[first::2]

        row = [(r, x) for x in range(board_cols)]
        if check(row):
            return row

        col = [(x, c) for x in range(board_rows)]
        if check(col):
            return col

        diag_up = [(x, x) for x in range(board_rows)]
        if check(diag_up):
            return diag_up

        diag_dn = [(x, board_rows - 1 - x) for x in range(board_rows)]
        if check(diag_dn):
            return diag_dn

    return False


#
# Helper #######################################################################

def add(p, q):
    return (p[0] + q[0]) % board_rows, (p[1] + q[1]) % board_cols
