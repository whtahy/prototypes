# Config
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from bearlibterminal import terminal as blt

id_square = 0xE000
id_x = 0xE001
id_o = 0xE002
id_select = 0xE003
id_victory = 0xE004

layer_board = 0
layer_select = 16
layer_gameover = 32
layer_move = 48

codes_close = [blt.TK_ESCAPE, blt.TK_CLOSE]
codes_move = [blt.TK_MOUSE_LEFT]
codes_select = [blt.TK_MOUSE_MOVE]

# game = 3 x 3 sq
board_rows = 3
board_cols = 3

# square = 256 x 256 px
px_square_rows = 256
px_square_cols = 256

# cell = 32 x 32 px
px_cell_rows = 32
px_cell_cols = 32

# square = 8 x 8 cell
square_rows = px_square_rows // px_cell_rows
square_cols = px_square_cols // px_cell_cols

# window = square * board = 24 x 24 cell
window_rows = board_rows * square_rows
window_cols = board_cols * square_cols

turn_start = 1


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


def u_code(n):
    return f'U+{hex(n)[2:]}'
