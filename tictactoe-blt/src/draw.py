# Render man
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import bearlibterminal.terminal as blt

from globals import *
from utils import avatar, corners, u_code


def board():
    blt.layer(layer_board)
    for (x, y) in corners():
        blt.put(x, y, id_square)


def clear_layer(layer):
    blt.layer(layer)
    blt.clear_area(0, 0, window_cols, window_rows)


def game(game):
    if game.turn == 1:
        board()
    for (x, y) in corners():
        r = y // ratio_rows
        c = x // ratio_cols
        player = game.state[r][c]
        if player:
            move(player, x, y)
    if game.winner:
        victory()


def init():
    blt.open()
    init_unicode()
    init_window()


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


def move(player, x, y):
    blt.layer(layer_move)
    blt.put(x, y, avatar(player))


def select(x, y):
    clear_layer(layer_select)
    blt.layer(layer_select)
    blt.put(x, y, id_select)


def victory():
    blt.layer(layer_victory)
    print("WINNER")
