# Game state
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from globals import *


#
# Game state
#

class Game:
    def __init__(self, turn = 1, state = None):
        if state is None:
            state = [([None] * board_cols) for _ in range(board_rows)]

        self.state = state
        self.turn = turn
        self.winner = None
        self.history = ['Game start']


#
# Interact
#

def move(game, game_coord):
    r, c = game_coord
    if game.state[r][c] or game.winner:
        return
    elif tie(game):
        game.history += ['Tie']
    else:
        player = get_player(game)
        game.state[r][c] = player
        game.history += [(player, (r, c))]

        v = victory(game, player)
        if v:
            game.winner = player
            game.history += [(player, v)]
        elif tie(game):
            game.history += ['Tie']
        else:
            game.turn += 1


#
# Helpers
#

def get_player(game):
    if game.turn % 2 == 1:
        return player_x
    else:
        return player_o


def tie(game):
    return game.turn == board_rows * board_cols + 1


def victory(game, player):
    rows = [[(r, c) for c in range(board_cols)] for r in range(board_rows)]
    cols = [[(r, c) for r in range(board_rows)] for c in range(board_cols)]
    diag = [list(zip(range(board_rows), range(board_cols))),
            list(zip(range(board_rows), reversed(range(board_cols))))]

    for coord_set in rows + cols + diag:
        if victory_check(game, player, coord_set):
            return coord_set


def victory_check(game, player, coords):
    return all(game.state[r][c] == player for (r, c) in coords)
