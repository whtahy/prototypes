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
        self.victory_coords = None

    def __repr__(self):
        s = f'Turn: {self.turn}\n'

        if self.winner:
            s += f'Winner: {self.winner} @ {self.victory_coords}\n'
        else:
            s += f'Player: {get_player(self)}\n'

        s += 'State:\n'
        for row in self.state:
            s += str(row) + '\n'

        return s

    def __str__(self):
        return self.__repr__()


def move(game, game_coord):
    r, c = game_coord
    if game.state[r][c] or game.winner:
        pass
    else:
        player = get_player(game)
        game.state[r][c] = player

        v = victory(game, player)
        if v:
            game.winner = player
            game.victory_coords = v
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
    rows = [[(r, c) for c in range(board_cols)] for r in range(board_rows)]
    cols = [[(r, c) for r in range(board_rows)] for c in range(board_cols)]
    diag = [list(zip(range(board_rows), range(board_cols))),
            list(zip(range(board_rows), reversed(range(board_cols))))]

    for coord_set in rows + cols + diag:
        if victory_check(game, player, coord_set):
            return coord_set


def victory_check(game, player, coords):
    return all(game.state[r][c] == player for (r, c) in coords)
