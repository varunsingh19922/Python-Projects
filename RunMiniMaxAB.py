# MiniMax - Get score for board

import math
import numpy as np
import time
import random

from ExtraCredit2 import copy
import time
COUNT = 0    # use the COUNT variable to track number of boards explored
max_depth = 0  # adjust this for each board
possible_states_of_the_board = []
def showBoard(board):
    # displays rows of board
    strings = ["" for i in range(board.shape[0])]
    idx = 0
    for row in board:
        for cell in row:
            if cell == 1:
                s = 'X'
            elif cell == -1:
                s = 'O'
            else:
                s = '_'

            strings[idx] += s
        idx += 1

    # display final board
    for s in strings:
        print(s)

def get_board_one_line(board):
    # returns one line rep of a board
    import math
    npb_flat = board.ravel()
    stop = int(math.sqrt(len(npb_flat)))

    bstr = ''
    for idx in range(len(npb_flat)):
        bstr += (str(npb_flat[idx]) + ' ')
        if (idx + 1) % (stop) == 0:
            bstr += '|'
    return bstr

def evaluate(board):
    # replace with your code
    '''returns 1 for X win, -1 for O win, 0 for tie OR game in progress
        Using numpy functions to add values in rows and cols
        If we get a sum equal to size of row,col,diag (plus or minus)
         we have a winner
        '''
    # replace with your code
    for i in range(board.shape[0]):  # checking for winning condition in rows
        sum = 0
        for j in range(board.shape[1]):
            sum = sum + board[i][j]

        if sum == board.shape[0]:
            return 1
        elif sum == -board.shape[0]:
            return -1

    for i in range(board.shape[0]):  # checking for winning condition in columns
        sum = 0
        for j in range(board.shape[1]):
            sum = sum + board[j][i]

        if sum == board.shape[0]:
            return 1
        elif sum == -board.shape[0]:
            return -1
    sum = 0

    for i in range(board.shape[0]):  # checking win condition for forward diagonal   \
        sum = sum + board[i][i]

    if sum == board.shape[0]:
        return 1
    elif sum == -board.shape[0]:
        return -1

    sum = 0
    for i in range(board.shape[0]):  # checking win condition for backward diagonal  /
        for j in range(board.shape[0]):
            if (i + j) == board.shape[0] - 1:
                sum = sum + board[i][j]

    if sum == board.shape[0]:
        return 1
    elif sum == -board.shape[0]:
        return -1

    return 0

def is_terminal_node(board):
    # replace with your code
    global COUNT
    COUNT = COUNT+1

    if evaluate(board) != 0:
        return True
    flag = 0

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 0:
                flag = 1
                return False

    if flag == 0:  # flag value stays the same if the board is full
        return True


def get_child_boards(board, char):
    # replace with your code
    ''' numpy version '''
    if not char in ['X', 'O']:
        raise ValueError("get_child_boards: expecting char='X' or 'O' ")

    newval = -1
    if char == 'X': newval = 1

    child_list = []
    # add your code here

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            duplicate_Board = board.copy()
            if duplicate_Board[i][j] == 0:
                duplicate_Board[i][j] = newval
                child_list.append(duplicate_Board)
                continue

    return child_list


def minimax(board, depth, alpha, beta, maximizingPlayer):
    '''returns the value of the board
       0 (draw) 1 (win for X) -1 (win for O)
       Explores all child boards for this position and returns
       the best score given that all players play optimally
    '''

    if depth == 0 or is_terminal_node(board):
        return evaluate(board)

    if maximizingPlayer:  # max player plays X
        maxEva = -math.inf
        child_list = get_child_boards(board, 'X')
        for child_board in child_list:
            eva = minimax(child_board, depth-1, alpha, beta, False)
            maxEva = max(maxEva, eva)
            alpha = max(eva,alpha)
            if alpha>=beta:
                break
        return maxEva

    else:             # minimizing player
        minEva = math.inf
        child_list = get_child_boards(board, 'O')
        for child_board in child_list:
            eva = minimax(child_board, depth - 1, alpha, beta, True)
            minEva = min(minEva, eva)
            beta = min(eva, beta)
            if alpha >= beta:
                break
        return minEva

def run_minimax(board):
        # set max_depth to the number of blanks (zeros) in the board
    global max_depth
    max_depth = np.count_nonzero(board == 0)
    print(f"Running minimax w/ max depth {max_depth} for:")
    showBoard(board)
    number_of_X = 0
    number_of_O = 0

    for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i][j] == 1:
                    number_of_X += 1
                elif board[i][j] == -1:
                    number_of_O +=1

    if number_of_X-number_of_O == 0:
        return True
    else:
        return False


def run_code_tests():
    '''
    b1 : expect win for X (1)  < 200 boards explored
    b1 = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    In addtion to the board b1, run tests on the following
    boards:
       b2:  expect win for O (-1)  > 1000 boards explored
       b2 = np.array([[0, 0, 0], [1, -1, 1], [0, 0, 0]])

       b3: expect TIE (0)  > 500,000 boards explored; time around 20secs
       b3 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

       b4: expect TIE(0) > 7,000,000 boards;  time around 4-5 mins
       b4 = np.array(
        [[1, 0, 0, 0], [0, 1, 0, -1], [0, -1, 1, 0], [0, 0, 0, -1]])

    '''

    # Minimax for a board: evaluate the board
    #    expect win for X (1)  < 200 boards explored
    b1 = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    b2 = np.array([[0, 0, 0], [1, -1, 1], [0, 0, 0]])
    b3 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    b4 = np.array([[1, 0, 0, 0], [0, 1, 0, -1], [0, -1, 1, 0], [0, 0, 0, -1]])

    print(f"\n--------\nStart Board: \n{b1}")

    # set max_depth  to the number of blanks (zeros) in the board

    is_x_to_move = run_minimax(b2)
    start_time = time.time()
    # read time before and after call to minimax

    score = minimax(b2, max_depth, -math.inf, math.inf, is_x_to_move)
    end_time = time.time()


    time_taken = end_time - start_time
    print("Time taken to run function: {:.6f} seconds".format(time_taken))
    print(f"count : {COUNT}")
    print (f"score : {score}")








if __name__ == '__main__':
    run_code_tests()

