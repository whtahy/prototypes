# Game functions
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import os

from pyscripts.woodcut import print_arr
from pyscripts.zfc import npa, numpy_ncols, numpy_nrows


def board(n_rows = 3, n_cols = None):
    if n_cols is None:
        n_cols = n_rows
    return npa(['.'] * n_rows * n_cols).reshape(n_rows, n_cols)


def next_player(turn, players):
    return players[(turn - 1) % len(players)]


def play(pos, player, board_state):
    board_state[pos] = player


def print_board(board_state, turn, player):
    os.system('cls')
    print()
    print(f'Turn {turn}')
    print()
    print_arr(board_state)
    print(f'Player {player}')
    print()


def victory(pos, board_state, threshold = 3):
    args = (pos, board_state, threshold)
    deltas = [
        (1, 0),
        (0, 1),
        (1, 1),
        (-1, 1)
    ]

    for pair in deltas:
        if victory_crawl(*pair, *args):
            return True
    return False


def victory_crawl(delta_r, delta_c, pos, board_state, threshold):
    n_rows = numpy_nrows(board_state)
    n_cols = numpy_ncols(board_state)
    sym = board_state[pos]

    count = 1

    r, c = pos[0] + delta_r, pos[1] + delta_c
    while 0 <= r < n_rows and 0 <= c < n_cols:
        if sym == board_state[r, c]:
            count += 1
        else:
            break
        r += delta_r
        c += delta_c

    r, c = pos[0] - delta_r, pos[1] - delta_c
    while 0 <= r < n_rows and 0 <= c < n_cols:
        if sym == board_state[r, c]:
            count += 1
        else:
            break
        r -= delta_r
        c -= delta_c

    return count >= threshold
