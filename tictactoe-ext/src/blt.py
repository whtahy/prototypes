from bearlibterminal import terminal as blt


#
# Constants#####################################################################

cell_c = 8
cell_r = 16


#
# Main #########################################################################

def test():
    textbox(28, 12, 'Hello world!', 70, 11)

#
# Scratch ######################################################################

def noldor(font, col, row):
    s = 'The Noldor are known as the \'Deep Elves\', for they are the most ' \
        'learned and inventive of the elven kindreds. They saw the light of ' \
        'the Two Trees in Valinor and gained much in lore and skill.' \
        '\n\n' \
        'Str:  3\n' \
        'Dex:  1\n' \
        'Int:  1\n' \
        'Gra:  2\n'

    blt.puts(col, row, f'[font={font}]{s}', width = 67)

def grid():
    for c in range(1600//cell_c):
        for r in range(1000//cell_r):
            blt.put(c, r, 0xE000)

def square(n):
    return f'[font=square][{n}]'

def textbox(c, r, title, ncols, nrows):
    # blt.bkcolor('grey')
    # blt.clear_area(c, r, ncols+1, nrows)

    last_row = r + nrows - 1
    last_col = c + ncols - 1
    inner_width = ncols - 2
    inner_height = nrows - 2

    blt.print(c, r, square(0x250c))
    line_h(c + 1, r, inner_width)
    blt.print(last_col, r, square(0x2510))

    line_v(c, r + 1, inner_height)
    line_v(last_col, r + 1, inner_height)

    blt.print(c, last_row, square(0x2514))
    line_h(c + 1, last_row, inner_width)
    blt.print(last_col, last_row, square(0x2518))

    noldor('', c+2, r+1)


def line_h(c, r, length):
    for i in range(length):
        blt.print(c + i, r, square(0x2500))

def line_v(c, r, length):
    for i in range(length):
        blt.print(c, r + i, square(0x2502))

def box(c, r, w, h, color='blue'):
    blt.bkcolor(color)
    blt.clear_area(c, r, h, w)


#
# Boiler plate #################################################################

def start():
    blt.open()

    blt.composition(blt.TK_ON)
    blt.set(f'window.cellsize = {cell_c}x{cell_r}')
    blt.set(f'window.size = {1600//cell_c}x{1000//cell_r}')

    blt.set(f'font: FSEX300.ttf,' \
            f'size = 8x16,' \
            f'use-box-drawing = true,' \
            f'use-block-elements = true,' \
            f'font-hinting = none')

    blt.set(f'square font: FSEX300.ttf,' \
            f'size = 8x16,' \
            # f'codepage = 437,' \
            # f'resize = 16x16,' \
            # f'resize-filter = nearest,' \
            f'spacing = 2x1')

    blt.set('0xE000: outline.png')

    blt.refresh()


def wait():
    while True:
        if blt.has_input():
            code = blt.read()
            if code in (blt.TK_ESCAPE, blt.TK_CLOSE):
                break
        blt.delay(1)


if __name__ == '__main__':
    start()

    test()
    blt.refresh()

    wait()
