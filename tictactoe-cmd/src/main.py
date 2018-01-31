# Game exec
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import os
import sys

from pyscripts.woodcut import printf

from tictactoe import board, next_player, play, print_board, victory


def user_input(msg = 'Enter move: '):
    s = input(msg)
    if s in ('exit', 'quit'):
        os.system('cls')
        sys.exit()
    elif s == '1':
        return 2, 0
    elif s == '2':
        return 2, 1
    elif s == '3':
        return 2, 2
    elif s == '4':
        return 1, 0
    elif s == '5':
        return 1, 1
    elif s == '6':
        return 1, 2
    elif s == '7':
        return 0, 0
    elif s == '8':
        return 0, 1
    elif s == '9':
        return 0, 2
    else:
        return None


def validate_input(players, game_state):
    pos = user_input()
    board_state = game_state[0]
    while pos is None or board_state[pos] in players:
        print_board(*game_state)
        if pos is None:
            printf('Invalid input! ')
        else:
            printf(f'{pos} is occupied! ')
        pos = user_input()
    return pos


def exit_game(msg):
    print(msg)
    print()
    s = input('Would you like another? (Y/N): ')
    if s in ('Y', 'y'):
        main()
    else:
        os.system('cls')
        sys.exit()


def main():
    n_rows = n_cols = threshold = 3
    n = n_rows * n_cols
    board_state = board(n_rows, n_cols)
    players = ('X', 'O')

    turn = 1
    player = next_player(turn, players)

    while True:
        game_state = (board_state, turn, player)
        print_board(*game_state)
        pos = validate_input(players, game_state)
        play(pos, player, board_state)

        if victory(pos, board_state, threshold = threshold):
            print_board(*game_state)
            exit_game('WINNER!')
        elif turn >= n:
            print_board(*game_state)
            exit_game('It\'s a tie!')
        else:
            turn += 1
            player = next_player(turn, players)


if __name__ == '__main__':
    main()
