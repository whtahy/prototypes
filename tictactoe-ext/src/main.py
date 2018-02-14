# Game loop
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from bearlibterminal import terminal as blt

import draw
import state
import ui
from config import codes_close, init_unicode, init_window


def start():
    blt.open()
    init_window()
    init_unicode()
    draw.board()
    blt.refresh()


def game_loop(game):
    while True:
        if blt.has_input():
            code = blt.read()
            if code in codes_close:
                break
            ui.update(game, code)
            draw.update(game)
        blt.delay(1)


if __name__ == '__main__':
    start()
    game_loop(state.Game())
