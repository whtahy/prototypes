# Game loop
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import draw
import state
import ui


def gloop():
    game = state.Game()
    draw.init()
    while True:
        if ui.update(game):
            draw.update(game)
        else:
            break


if __name__ == '__main__':
    gloop()
