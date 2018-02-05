# Read from state
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import state
from config import *


#
# public #######################################################################

def update(game):
    if game.select:
        select(game)
    else:
        board()
    if game.state != game.prev:
        move(game)
        if state.winner(game):
            victory(game)
    blt.refresh()


#
# private ######################################################################

def board():
    blt.layer(layer_board)
    clear_layer()

    for (x, y) in corners():
        blt.put(x, y, id_square)


def select(game):
    blt.layer(layer_select)
    clear_layer()

    x, y = cell_coord(game.select)
    blt.put(x, y, id_select)


def move(game):
    blt.layer(layer_move)

    x, y = cell_coord(game.select)
    blt.put(x, y, state.player(game))


def tie(game):
    print('It\'s a tie')


def victory(game):
    blt.layer(layer_gameover)
    clear_layer()

    _, victory_coords = state.winner(game)
    for loc in victory_coords:
        x, y = cell_coord(loc)
        blt.put(x, y, id_victory)


#
# aux ##########################################################################

def cell_coord(loc):
    r, c = loc
    x = c * square_cols
    y = r * square_rows
    return x, y


def clear_layer():
    blt.clear_area(0, 0, window_cols, window_rows)


def corners():
    return [cell_coord(loc) for loc in game_coords()]


def game_coords():
    return [(r, c) for r in range(board_rows) for c in range(board_cols)]


def u_code(n):
    return f'U+{hex(n)[2:]}'
