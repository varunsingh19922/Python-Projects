import numpy as np

# test is_terminal_node
# tip: use your tested evaluate() to help with this

def evaluate(board):
    '''returns 1 for X win, -1 for O win, 0 for tie OR game in progress
    Using numpy functions to add values in rows and cols
    If we get a sum equal to size of row,col,diag (plus or minus)
     we have a winner
    '''
      # replace with your code
    for i in range(board.shape[0]):         # checking for winning condition in rows
        sum = 0
        for j in range(board.shape[1]):
            sum = sum + board[i][j]

        if sum == board.shape[0]:
            return True
        elif sum == -board.shape[0]:
            return True

    for i in range(board.shape[0]):         # checking for winning condition in columns
        sum = 0
        for j in range(board.shape[1]):
            sum = sum + board[j][i]

        if sum == board.shape[0]:
            return True
        elif sum == -board.shape[0]:
            return True
    sum = 0

    for i in range(board.shape[0]):  # checking win condition for forward diagonal   \
        sum = sum + board[i][i]

    if sum == board.shape[0]:
        return True
    elif sum == -board.shape[0]:
        return True

    sum = 0
    for i in range(board.shape[0]):  # checking win condition for backward diagonal  /
        for j in range(board.shape[0]):
            if (i + j) == board.shape[0] - 1:
                sum = sum + board[i][j]

    if sum == board.shape[0]:
        return True
    elif sum == -board.shape[0]:
        return True

    return False

def is_terminal_node(board):

    if evaluate(board) == True:
        return True
    flag = 0

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 0:
                flag = 1
                return False

    if flag == 0:        # flag value stays the same if the board is full
        return True

#### TEST CODE ##########
def run_tests():

    #TEST1 : Not terminal
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = False

    if is_terminal == expected:
        print (f"PASS Test 1 Non Terminal Board")
    else: print (f"FAIL Test 1 Non Terminal Board: \
        expect: {expected} actual: {is_terminal}")

    #TEST 2: Terminal
    b = np.array([[1, 1, 1], [1, -1, -1], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 2  Terminal Board")
    else:
        print(f"FAIL Test 2  Terminal Board: \
            expect: {expected} actual: {is_terminal}")


    #TEST3
    b = np.array([[1, -1, 1], [1, 1, -1], [-1, 1, -1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 3  Terminal Board")
    else:
        print(f"FAIL Test 3  Terminal Board: \
            expect: {expected} actual: {is_terminal}")

    #TEST4 Win for X on diagonal
    b = np.array([[1, 0, 0], [0, 1, -1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 4  Terminal Board")
    else:
        print(f"FAIL Test 4  Terminal Board: \
            expect: {expected} actual: {is_terminal}")

    #TEST5 win for O on reverse diagonal
    b = np.array([[1, 1, -1], [0, -1, 1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 5  Terminal Board")
    else:
        print(f"FAIL Test 5  Terminal Board: \
            expect: {expected} actual: {is_terminal}")


    #TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array([[1, 1, 0, -1], [0, 0, -1, 1],
                  [0, -1, 1, 0], [-1,0,0,0]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 6  Terminal Board")
    else:
        print(f"FAIL Test 6  Terminal Board: \
                expect: {expected} actual: {is_terminal}")




run_tests()