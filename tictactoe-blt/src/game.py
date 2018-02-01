# Game state
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from globals import *


class Game:
    def __init__(self, turn = 1, state = None):
        if state is None:
            state = [([None] * board_cols) for _ in range(board_rows)]
        self.turn = turn
        self.state = state

    def __repr__(self):
        s = f'Turn: {self.turn}\n'
        s += 'State:\n'
        for row in self.state:
            s += str(row) + '\n'
        return s

    def __str__(self):
        return self.__repr__()


def move(game, loc):
    row, col = loc
    if game.state[row][col]:
        pass
    else:
        game.state[row][col] = player(game)
        game.turn += 1


def player(game):
    if game.turn % 2 == 1:
        return player_x
    else:
        return player_o


def switch(player):
    if player == player_x:
        return player_o
    else:
        return player_x


def victory(game, loc):
    pass
