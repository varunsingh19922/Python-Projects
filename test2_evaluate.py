import numpy as np

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
            return 1
        elif sum == -board.shape[0]:
            return -1

    for i in range(board.shape[0]):         # checking for winning condition in columns
        sum = 0
        for j in range(board.shape[1]):
            sum = sum + board[j][i]

        if sum == board.shape[0]:
            return 1
        elif sum == -board.shape[0]:
            return -1
    sum = 0

    for i in range(board.shape[0]):                 # checking win condition for forward diagonal   \
        sum = sum + board[i][i]

    if sum == board.shape[0]:
        return 1
    elif sum == -board.shape[0]:
        return -1

    sum = 0
    for i in range(board.shape[0]):                 # checking win condition for backward diagonal  /
        for j in range(board.shape[0]):
            if (i+j) == board.shape[0] - 1:
                sum = sum + board[i][j]


    if sum == board.shape[0]:
        return 1
    elif sum == -board.shape[0]:
        return -1

    return 0

#### TEST CODE ##########
def run_tests():
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    #TEST1 : No winner
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    score = evaluate(b)
    expect = 0

    if score == expect:
        print (f"PASS Test 1 No Win")
    else: print (f"FAIL Test 1 No Win: \
        expect: {expect} actual: {score}")

    #TEST 2: Win for X
    b = np.array([[1, 0, -1], [1, 0, 0], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 2  column win")
    else: print (f"FAIL Test 2: column win \
        expect: {expect} actual: {score}")

    #TEST3 Win for O
    b = np.array([[-1, -1, -1], [1, 0, 1], [1, 0, 1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 3  row win")
    else: print (f"FAIL Test 3: row win \
        expect: {expect} actual: {score}")


    #TEST4 Win for X on diagonal
    b = np.array([[-1, -1, 1], [1, 1, 1], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 4  diag win")
    else: print (f"FAIL Test 4: diag win \
        expect: {expect} actual: {score}")

    #TEST5 win for O on reverse diagonal
    b = np.array([[-1, 1, 1], [1, -1, -1], [1, 0, -1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 5  diag2 win")
    else: print (f"FAIL Test 5: diag2 win \
        expect: {expect} actual: {score}")

    #TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array([[-1, 1, 1, 0], [1, -1, -1, 0], \
                  [1, 0, -1, 0], [1,0,0,-1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 6  diag2 win 4x4")
    else: print (f"FAIL Test 6: diag2 win 4x4 \
        expect: {expect} actual: {score}")

    b = np.array([[1, 1, -1], [0, -1, 1], [-1, -1, 1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print(f"PASS Test 6  diag2 win 4x4")
    else:
        print(f"FAIL Test 6: diag2 win 4x4 \
            expect: {expect} actual: {score}")

run_tests()