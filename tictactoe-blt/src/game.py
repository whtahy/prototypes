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
        self.winner = None

    def __repr__(self):
        s = f'Turn: {self.turn}\n'
        if self.winner:
            s += f'Winner: {self.winner}\n'
        else:
            s += f'Player: {get_player(self)}\n'
        s += 'State:\n'
        for row in self.state:
            s += str(row) + '\n'
        return s

    def __str__(self):
        return self.__repr__()


def move(game, loc):
    row, col = loc
    if game.state[row][col] or game.winner:
        pass
    else:
        player = get_player(game)
        game.state[row][col] = player
        if victory(game, player):
            game.winner = player
        else:
            game.turn += 1
    return game


def get_player(game):
    if game.turn % 2 == 1:
        return player_x
    else:
        return player_o


def switch(player):
    if player == player_x:
        return player_o
    else:
        return player_x


def victory(game, player):
    a = [victory_row(game, player, row) for row in range(board_rows)]
    b = [victory_col(game, player, col) for col in range(board_cols)]
    c = victory_diag(game, player)

    return any(a) or any(b) or c


def victory_row(game, player, row):
    for col in range(board_cols):
        if game.state[row][col] != player:
            return False
    return True


def victory_col(game, player, col):
    for row in range(board_rows):
        if game.state[row][col] != player:
            return False
    return True


def victory_diag(game, player):
    for row in range(board_rows):
        col = row
        if game.state[row][col] != player:
            return False
    for row in range(board_rows):
        col = board_cols - 1 - row
        if game.state[row][col] != player:
            return False
    return True
