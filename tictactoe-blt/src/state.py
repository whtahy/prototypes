# Data Management
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from config import board_cols, board_rows, history_tie, id_o, id_x


#
# Store state ##################################################################

class Game:
    def __init__(self):
        self.state = [([None] * board_cols) for _ in range(board_rows)]
        self.history = [('Game start', None)]
        self.select = (1, 1)


def select(game, loc):
    game.select = loc


#
# Modify state #################################################################

def move(game):
    r, c = game.select
    if game.state[r][c] or winner(game) or tie(game):
        pass
    else:
        p = player(game)
        game.state[r][c] = p
        game.history += [(p, (r, c))]

        w = winner(game)
        if winner(game):
            game.history += [w]
        elif tie(game):
            game.history += [history_tie]


#
# Derive state #################################################################

def player(game):
    t = turn(game)
    if t % 2 == 1:
        return id_x
    else:
        return id_o


def turn(game):
    turn = 1
    for row in game.state:
        for sq in row:
            if sq:
                turn += 1
    return turn


def winner(game):
    def diag():
        diag_up = [list(zip(range(board_rows), range(board_cols)))]
        diag_dn = [list(zip(range(board_rows), reversed(range(board_cols))))]
        if r == c == 2:
            return diag_up + diag_dn
        elif r == c:
            return diag_up
        elif r == board_cols - 1 - c:
            return diag_dn
        else:
            return []

    r, c = game.select
    player = game.state[r][c]
    if player:
        row = [[(r, x) for x in range(board_cols)]]
        col = [[(x, c) for x in range(board_rows)]]
        for coord_set in row + col + diag():
            if all(game.state[p][q] == player for (p, q) in coord_set):
                return player, coord_set


def tie(game):
    turn_max = 1 + board_rows * board_cols
    return turn(game) == turn_max
