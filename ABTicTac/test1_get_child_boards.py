# test get_child_boards - separate test file
import numpy as np

def getChildren(board, char):
    ''' numpy version '''
    if not char in ['X', 'O']:
        raise ValueError("get_child_boards: expecting char='X' or 'O' ")

    newval = -1
    if char == 'X': newval = 1

    child_list = []

    # add your code here

    return child_list

def run_tests():
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    #TEST1 length of child list
    expect = b.size - np.count_nonzero(b)
    child_list = getChildren(b, 'X')

    if len(child_list) == expect:
        print (f"PASS Test 1")
    else: print (f"FAIL Test 1: \
        expect: {expect} actual: {len(child_list)}")

    #TEST2 - is expected board in list
    b2 = np.array([[1, 1, -1], [1, 0, 0], [-1, 0, 0]])
    found = False
    for board in child_list:
        if np.array_equal(board, b2):
            found = True
            break

    if found:
        print ("PASS Test 2")
    else: print (f"FAIL Test 2: Expected board not in child list")

    #TEST3 Test 4x4 array
    b3 = np.array([ [0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0] ])
    expect = b.size - np.count_nonzero(b)
    child_list = getChildren(b, 'X')

    if len(child_list) == expect:
        print(f"PASS Test 3  4x4 array")
    else:
        print(f"FAIL Test 3 4x4 array: \
            expect: {expect} actual: {len(child_list)}")

run_tests()
