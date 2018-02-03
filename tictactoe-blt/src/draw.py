# Render man
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import bearlibterminal.terminal as blt

from globals import *
from utils import to_gamecoord


#
# Real time
#

def select(loc):
    x, y = loc
    clear_layer(layer_select)
    blt.layer(layer_select)
    blt.put(x, y, id_select)
    blt.refresh()


#
# Game state
#

def board():
    blt.layer(layer_board)
    for (x, y) in corners():
        blt.put(x, y, id_square)


def game(game):
    if game.turn == 1:
        init()
    for loc in corners():
        r, c = to_gamecoord(loc)
        player = game.state[r][c]
        if player:
            move(player, loc)
    if game.winner:
        victory()
    blt.refresh()


def init():
    blt.open()
    init_unicode()
    init_window()
    board()


def init_unicode():
    blt.set(f'{u_code(id_square)}: ../art/square.png')
    blt.set(f'{u_code(id_x)}: ../art/x.png')
    blt.set(f'{u_code(id_o)}: ../art/o.png')
    blt.set(f'{u_code(id_select)}: ../art/select.png')


def init_window():
    blt.composition(blt.TK_ON)
    blt.set(f'window.size = {window_cols}x{window_rows}')
    blt.set(f'window.cellsize = {cell_cols}x{cell_rows}')
    blt.set(f'input.filter = [keyboard, mouse]')


def move(player, loc):
    x, y = loc
    blt.layer(layer_move)
    blt.put(x, y, avatar(player))


def victory():
    blt.layer(layer_victory)
    print("WINNER")


#
# Helpers
#

def avatar(player):
    if player == player_x:
        return id_x
    elif player == player_o:
        return id_o
    else:
        return None


def bounds():
    ls = []
    c = corners()
    for (x, y) in c:
        x_range = x, x + ratio_cols - 1
        y_range = y, y + ratio_rows - 1
        ls.append((x_range, y_range))
    return ls


def clear_layer(layer):
    blt.layer(layer)
    blt.clear_area(0, 0, window_cols, window_rows)


def corners():
    ls = []
    for i_col in range(board_cols):
        for i_row in range(board_rows):
            ls.append((i_col * ratio_cols, i_row * ratio_rows))
    return ls


def in_range(x, tup):
    if tup[0] <= x <= tup[1]:
        return True
    else:
        return False


def u_code(n):
    return f'U+{hex(n)[2:]}'
