# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from game import Game
from ui import menu_main


class State:
    __slots__ = 'game', 'index', 'menu'

    def __init__(self):
        self.game = Game()
        self.index = 0
        self.menu = menu_main
