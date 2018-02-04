# Render man
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from config import *


#
# public #######################################################################

def update(game):
    board()
    highlight(game)
    move(game)

    blt.refresh()


#
# private ######################################################################

def board():
    blt.layer(layer_board)
    clear_layer()

    for (x, y) in corners():
        blt.put(x, y, id_square)


def highlight(game):
    blt.layer(layer_select)
    clear_layer()

    x, y = cell_coord(game.select)

    blt.put(x, y, id_select)


def move(game):
    blt.layer(layer_move)
    clear_layer()
    for (r, c) in game_coords():
        player = game.state[r][c]
        if player:
            blt.put(*cell_coord((r, c)), player)


def tie(game):
    print(game.history[-1])


def victory(game):
    print(game.history[-1])


#
# init #########################################################################

def init():
    blt.open()
    init_unicode()
    init_window()
    board()
    blt.refresh()


def init_unicode():
    blt.set(f'{u_code(id_square)}: ../art/square.png')
    blt.set(f'{u_code(id_x)}: ../art/x.png')
    blt.set(f'{u_code(id_o)}: ../art/o.png')
    blt.set(f'{u_code(id_select)}: ../art/select.png')
    blt.set(f'{u_code(id_victory)}: ../art/victory.png')


def init_window():
    blt.composition(blt.TK_ON)
    blt.set(f'window.size = {window_cols}x{window_rows}')
    blt.set(f'window.cellsize = {px_cell_cols}x{px_cell_rows}')
    blt.set(f'input.filter = [keyboard, mouse]')


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
