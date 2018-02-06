# Data
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from config import board_cols, board_rows, id_o, id_x, turn_start


#
# Store state ##################################################################

class Game:
    def __init__(self):
        self.history = []
        self.move = None
        self.select = None
        self.state = [([None] * board_cols) for _ in range(board_rows)]


#
# Modify state #################################################################

def move(game):
    r, c = game.select
    if game.state[r][c] or winner(game) or tie(game):
        game.move = None
    else:
        game.move = game.select
        game.state[r][c] = player(game)
        game.history += [game.move]
        print(game.history)


def select(game, loc):
    game.move = None
    game.select = loc


#
# Derive state #################################################################

def player(game):
    t = turn(game)
    if t % 2 == turn_start:
        return id_x
    else:
        return id_o


def turn(game):
    turn = turn_start + sum(1 for row in game.state for sq in row if sq)
    return turn


def winner(game):
    def diags():
        diag_up = [list(zip(range(board_rows), range(board_cols)))]
        diag_dn = [list(zip(range(board_rows), reversed(range(board_cols))))]
        return diag_up + diag_dn

    rows = [[(r, c) for c in range(board_cols)] for r in range(board_rows)]
    cols = [[(r, c) for r in range(board_rows)] for c in range(board_cols)]

    for coord_set in rows + cols + diags():
        p, q = coord_set[0]
        player = game.state[p][q]
        if player and all(game.state[r][c] == player
                          for (r, c) in coord_set[1:]):
            return player, coord_set


def tie(game):
    turn_max = turn_start + board_rows * board_cols
    return turn(game) == turn_max and not winner(game)
