# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import sys

from pyscripts.scholar import pickle_obj, unpickle_file

from config import *
from game import Game


#
# State ########################################################################

class Menu:
    __slots__ = 'name', 'buttons'

    def __init__(self, name, buttons):
        self.name = name
        self.buttons = buttons

    def __eq__(self, other):
        return other and self.name == other.name


class Button:
    __slots__ = 'name', 'func'

    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __eq__(self, other):
        return self.func is other.func


#
# Action #######################################################################

def close_menu(app):
    app.index = 0
    app.menu = None


def exit_game(app = None):
    sys.exit()


def load(app):
    app.game = unpickle_file(save_path)
    close_menu(app)


def new_game(app):
    close_menu(app)
    app.game = Game()


def pause(app):
    app.menu = menu_pause


def resume(app):
    close_menu(app)


def save(app):
    pickle_obj(app.game, save_path)


#
# Button #######################################################################

b_exit_game = Button(s_exit_game, exit_game)
b_load = Button(s_load, load)
b_new_game = Button(s_new_game, new_game)
b_resume = Button(s_resume, resume)
b_save = Button(s_save, save)
b_start = Button(s_start, new_game)

#
# Menu #########################################################################

menu_main = Menu(
        s_menu_main,
        (
            b_start,
            b_load,
            b_exit_game,
        )
)

menu_pause = Menu(
        s_menu_pause,
        (
            b_resume,
            b_save,
            b_load,
            b_new_game,
            b_exit_game,
        )
)
