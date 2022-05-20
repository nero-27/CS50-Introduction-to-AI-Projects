
"""
Tic Tac Toe Player
"""

import math
import copy
import sys
import random


X = "X"
O = "O"
EMPTY = "EMPTY"


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): # working
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    Xcount = 0
    Ocount = 0
    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)
    if Xcount > Ocount:
        return O
    elif Xcount == Ocount:
        return X


def actions(board):     # working
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i,j))

    return moves


def result(board, action):  # working
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if board[action[0]][action[1]] == EMPTY:
        for act in actions(board):
            if act == action:
                new_board[action[0]][action[1]] = player(board)
                return new_board
    else:
        raise Exception ("slot is not available")


def isgameover(board):
    if winner(board) == X or winner(board) == O:
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # make columns
    cols = []
    for j in range(3):
        column = [row[j] for row in board]
        cols.append(column)

    # print("printing cols from winner : ", cols)
    
    # if terminal(board):
    # checking row conditions
    for row in board:
        Xcount = row.count(X)
        Ocount = row.count(O)
        if Xcount == 3:
            return X
        if Ocount == 3:
            return O

    # checking column condition
    for col in cols:
        Xc = col.count(X)
        Oc = col.count(O)
        if Xc == 3:
            return X
        if Oc == 3:
            return O

    # diagonal condition
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    
    # other diagonal condition
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None

    
        


def terminal(board):    # working
    """
    Returns True if game is over, False otherwise.
    """
    emptycount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                emptycount += 1

    if emptycount == 0:
        return True
    else:
        return False
    

def utility(board): # working
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif board == initial_state():
        move_index = max_value(board)[1]
        return actions(board)[move_index]
    else:
        if player(board) == X:
            move_index = max_value(board)[1]
            return actions(board)[move_index]
        if player(board) == O:
            move_index = min_value(board)[1]
            return actions(board)[move_index]
            
    
def min_value(board):
    # v = math.inf
    if terminal(board):
        return utility(board), None

    values = []
    for act in actions(board):
        v = max_value(result(board, act))[0]
        # print(f"this is v : {v} for action : {act}")
        values.append(v)

    # print(f"values from min value : {values}")
    min_v = min(values)
    min_v_index = values.index(min_v)
    # print(f"min value is : {min_v} with index {min_v_index}")

    return min_v, min_v_index

def max_value(board):
    v = -(math.inf)
    if terminal(board):
        return utility(board), None

    values = []
    for act in actions(board):
        v = min_value(result(board, act))[0]
        # print(f"this is v : {v} for action : {act}")
        values.append(v)

    # print(f"values from max value : {values}")

    max_v = max(values)
    max_v_index = values.index(max_v)
    # print(f"max value is : {max_v} with index {max_v_index}")

    return max_v, max_v_index


   


