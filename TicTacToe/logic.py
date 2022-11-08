# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],]

def print_board(values):
    print("\n")
    print("\t   0     1     2  - Rows")
    print("\t      |     |")
    print("\t0  {}  |  {}  |  {}".format(values[0][0], values[0][1], values[0][2]))
    print('\t _____|_____|_____')
    print("\t      |     |")
    print("\t1  {}  |  {}  |  {}".format(values[1][0], values[1][1], values[1][2]))
    print('\t _____|_____|_____')
    print("\t      |     |")
    print("\t2  {}  |  {}  |  {}".format(values[2][0], values[2][1], values[2][2]))
    print("\t      |     |")
    print("\n")


def get_winner(board,k):
    if board[0][0] == board[0][1] == board[0][2] == k:
        return k
    elif board[1][0] == board[1][1] == board[1][2] == k:
        return k
    elif board[2][0] == board[2][1] == board[2][2] == k:
        return k
    elif board[0][0] == board[1][0] == board[2][0] == k:
        return k
    elif board[0][1] == board[1][1] == board[2][1] == k:
        return k
    elif board[0][2] == board[1][2] == board[2][2] == k:
        return k
    elif board[1][1] == board[2][2] == board[0][0] == k:
        return k
    elif board[0][2] == board[1][1] == board[2][0] == k:
        return k
    else:
        return None