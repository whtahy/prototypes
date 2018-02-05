# Write to state
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from bearlibterminal import terminal as blt

import state
from config import (
    codes_close, codes_move, codes_select, square_cols, square_rows
)


#
# public #######################################################################

def update(game):
    if blt.has_input():
        code = blt.read()
        if code in codes_close:
            return False
        elif code in codes_move:
            move(game)
        elif code in codes_select:
            select(game)
    return True


#
# private ######################################################################

def select(game):
    loc = game_coord(read_mouse())
    state.select(game, loc)


def move(game):
    state.move(game)


#
# aux ##########################################################################

def game_coord(loc):
    x, y = loc
    row = y // square_rows
    col = x // square_cols
    return row, col


def read_mouse():
    x = blt.state(blt.TK_MOUSE_X)
    y = blt.state(blt.TK_MOUSE_Y)
    return x, y
