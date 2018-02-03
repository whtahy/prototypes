# User input: keyboard + mouse
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import bearlibterminal.terminal as blt

import draw
import gameplay
from utils import corner, game_coord


def game_loop():
    game = gameplay.Game()
    draw.game(game)
    while True:
        if blt.has_input():
            code = blt.read()
            if code in (blt.TK_ESCAPE, blt.TK_CLOSE):
                break
            elif code == blt.TK_MOUSE_MOVE:
                select()
            elif code == blt.TK_MOUSE_LEFT:
                move(game)
                draw.game(game)


#
# Components
#

def move(game):
    gameplay.move(game, game_coord(read_mouse()))


def select():
    draw.select(corner(read_mouse()))


#
# Helpers
#

def read_mouse():
    x = blt.state(blt.TK_MOUSE_X)
    y = blt.state(blt.TK_MOUSE_Y)
    return x, y
