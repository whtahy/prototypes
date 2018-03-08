# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from config import *
from render import render
from state import State
from update import update


def init():
    blt.open()

    blt.composition(blt.TK_ON)
    blt.set(f'window.size = {win_w}x{win_h}')
    blt.set(f'window.cellsize = {cell_x}x{cell_y}')
    blt.set(f'input.filter = [keyboard, mouse]')
    blt.set(f'input.precise-mouse = true')
    blt.set(f'input.alt-functions = false')

    init_assets()

    blt.refresh()


def init_assets():
    blt.set(f'{ch_square}: {dir_assets}square.png')
    blt.set(f'{ch_x}: {dir_assets}x.png')
    blt.set(f'{ch_o}: {dir_assets}o.png')
    blt.set(f'{ch_select}: {dir_assets}select.png')
    blt.set(f'{ch_victory}: {dir_assets}victory.png')


def user_input():
    while True:
        if blt.has_input():
            return blt.read()
        blt.delay(frame_delay)


def game_loop(state):
    render(state)
    while True:
        code = user_input()
        if update(code, state):
            render(state)


if __name__ == '__main__':
    init()
    game_loop(State())
