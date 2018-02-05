# Game loop
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from bearlibterminal import terminal as blt

import draw
import state
import ui
from config import init_unicode, init_window


def start():
    blt.open()
    init_window()
    init_unicode()
    blt.refresh()


def game_loop(game):
    while True:
        if ui.update(game):
            draw.update(game)
        else:
            break


if __name__ == '__main__':
    start()
    game_loop(state.Game())
