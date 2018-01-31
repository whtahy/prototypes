# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import bearlibterminal.terminal as blt

# TODO remove global state
# TODO external blt config
# TODO external keymap config

id_square = 0xE000
id_x = 0xE001
id_o = 0xE002
id_highlight = 0xE003

window_x = 24
window_y = 24
cell_x = 32
cell_y = 32
square_x = 256
square_y = 256

multi_x = square_x // cell_x
multi_y = square_y // cell_y


def init_art():
    blt.set('U+E000: ../art/square.png')
    blt.set('U+E001: ../art/x.png')
    blt.set('U+E002: ../art/o.png')
    blt.set('U+E003: ../art/select.png')


def start():
    blt.open()

    blt.composition(blt.TK_ON)
    blt.set(f'window.size = {window_x}x{window_y}')
    blt.set(f'window.cellsize = {cell_x}x{cell_y}')
    blt.set(f'input.filter = [keyboard, mouse]')

    init_art()
    draw_board()

    blt.refresh()


def stop():
    blt.close()


def corners():
    ls = []
    for i_x in range(3):
        for i_y in range(3):
            ls.append((i_x * multi_x, i_y * multi_y))
    return ls


def bounds():
    ls = []
    c = corners()
    for (x, y) in c:
        x_range = x, x + multi_x - 1
        y_range = y, y + multi_y - 1
        ls.append((x_range, y_range))
    return ls


def draw_board():
    for (x, y) in corners():
        blt.put(x, y, id_square)


def sh_exit(code):
    return code in (blt.TK_ESCAPE, blt.TK_CLOSE)


def in_range(x, tup):
    if tup[0] <= x <= tup[1]:
        return True
    else:
        return False


def highlight():
    x = blt.state(blt.TK_MOUSE_X)
    y = blt.state(blt.TK_MOUSE_Y)

    for (xr, yr) in bounds():
        if in_range(x, xr) and in_range(y, yr):
            draw_board()
            blt.put(xr[0], yr[0], id_highlight)
            blt.refresh()
            break


def process(code):
    if code == blt.TK_MOUSE_MOVE:
        highlight()


if __name__ == '__main__':
    start()

    while True:
        if blt.has_input():
            code = blt.read()
            if sh_exit(code):
                break
            else:
                process(code)

    stop()
