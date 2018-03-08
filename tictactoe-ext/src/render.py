# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import fmt
import game
import gui
from config import *


#
# Public #######################################################################

def render(state):
    blt.clear()

    if state.menu:
        blt.layer(layer_menu)
        menu(state)

    blt.layer(layer_board)
    blt.color('white')
    board()

    if game.winner(state.game):
        victory(state)
    elif game.tie(state.game):
        tie()

    select(state)
    moves(state)

    blt.refresh()


#
# Private ######################################################################

def menu(state):
    # textbox
    title = state.menu.name
    choices = fmt.menu([x.name for x in state.menu.buttons])
    x, y, w, h, padding = gui.textbox(choices, title = title)

    # select
    blt.color('dark orange')
    w_hl = fmt.text_w(choices) * 3
    y += padding + state.index * 2
    indent = gui.offset(w_hl * font_x, w * cell_x - font_x) - 1
    gui.highlight(x, y, w_hl, indent, 0)
    gui.highlight(x, y, w_hl, indent, 4)


def board():
    for (x, y) in corners():
        blt.put(x, y, ch_square)


def moves(state):
    for i, game_coord in enumerate(state.game.history):
        x, y = cell_coord(game_coord)
        blt.put(x, y, game.player(i))


def select(state):
    if state.game.select:
        x, y = cell_coord(state.game.select)
        blt.put(x, y, ch_select)


def tie():
    pass


def victory(state):
    for game_coord in game.winner(state.game):
        x, y = cell_coord(game_coord)
        blt.put(x, y, ch_victory)


#
# Helper #######################################################################

def cell_coord(game_coord):
    r, c = game_coord
    x = c * square_w
    y = r * square_h
    return x + gui.offset(board_w, win_w), y + gui.offset(board_h, win_h)


def corners():
    return [cell_coord(loc) for loc in game_coords()]


def game_coords():
    return [(r, c) for r in range(board_rows) for c in range(board_cols)]
