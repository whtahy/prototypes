# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import game
import gui
import ui
from config import *


#
# Public #######################################################################

def update(code, state):
    if code in k_exit \
            or (state.menu == ui.menu_main and code in k_esc) \
            or (blt.check(k_ctrl) and code == blt.TK_Q):
        ui.exit_game()

    if state.menu:
        if code in k_n:
            state.index = (state.index - 1) % len(state.menu.buttons)
        elif code in k_s:
            state.index = (state.index + 1) % len(state.menu.buttons)
        elif code in k_enter:
            state.menu.buttons[state.index].func(state)
        else:
            return False
    else:
        if code in k_esc:
            ui.pause(state)
        elif code in m_move:
            select_loc(state)
        elif code in k_center + k_enter + m_click:
            move(state)
        elif code in k_sw:
            select_add((1, -1), state)
        elif code in k_s:
            select_add((1, 0), state)
        elif code in k_se:
            select_add((1, 1), state)
        elif code in k_w:
            select_add((0, -1), state)
        elif code in k_e:
            select_add((0, 1), state)
        elif code in k_nw:
            select_add((-1, -1), state)
        elif code in k_n:
            select_add((-1, 0), state)
        elif code in k_ne:
            select_add((-1, 1), state)
        else:
            return False

    return True


#
# Helper #######################################################################

def game_coord(loc):
    x, y = loc
    row = (y - gui.offset(board_h, win_h)) // square_h
    col = (x - gui.offset(board_w, win_w)) // square_w
    return row, col


def move(state):
    if state.game.select in state.game.history \
            or game.winner(state.game) \
            or game.tie(state.game):
        return False
    elif state.game.select:
        select_loc(state)
        game.move(state.game)
    else:
        game.select(state.game)


def read_mouse():
    x = blt.state(blt.TK_MOUSE_X)
    y = blt.state(blt.TK_MOUSE_Y)
    return x, y


def select_add(p, state):
    if state.game.select:
        game.select(state.game, game.add(p, state.game.select))
    else:
        game.select(state.game)


def select_loc(state):
    r, c = game_coord(read_mouse())
    if 0 <= r < board_rows and 0 <= c < board_cols:
        game.select(state.game, (r, c))
