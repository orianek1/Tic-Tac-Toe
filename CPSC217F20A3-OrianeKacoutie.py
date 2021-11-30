# Oriane Kacoutie
# Student Number 12347890
# Date: 2020-08-26
# Description: A Tic-Tac-Toe game.

# This program is a Tic Tac Toe game of various size from (3*3,3*4,4*3,4*4) board
# In this program, two players will be playing the game and the following codes will help the program to run

#
#  The location to insert your code is clearly marked with ###############################################################################
#

from SimpleGraphics import *
from math import factorial
from copy import deepcopy
import inspect
import sys
from pprint import pprint
import traceback
import inspect
from math import inf as infinity

# Contants for the board size
WIDTH = 600
HEIGHT = 600
# Constants for the game pieces
EMPTY = 0
X = 1
O = 2
# Constants to turn off tests for parts of assignment   
TESTPART1 = True
TESTPART2 = True
TESTPART3 = True
TESTPART4 = True
TESTPART5 = True
TESTPART6 = True
TESTPART7 = True
STOP1STFAIL = True


###############################################################################
#
#  Only modify the file below this point
#
###############################################################################

#
#  Insert your implementation of createBoard here (code and comments (in-line and above function))
#
#the codes from line 51 to line 54 are from a TA
#this code will enable us to create the board that will allow us to play the game
def createBoard(rows, cols):
    # to create the empty list board
    board=[]
    #to create the row in the 2d list
    for row in range (rows):
        temporaryBoard=[]
        #to create the columns in the 2d list
        for col in range (cols):
            temporaryBoard.append(EMPTY)
        board.append(temporaryBoard)
    return (board)

#
#  Insert your implementation of canPlay here (code and comments (in-line and above function))
#

#thia code is to check if there is an empty spot in the board so the player can play on that cell
def canPlay(board, rows, cols):
   return board[rows][cols] == EMPTY



#
#  Insert your implementation of play here (code and comments (in-line and above function))
#

#we define the function that will enable the code to work
#this code will put the player's piece at the position that was indicated
def play(board, rows, cols, piece):
    board[rows][cols] = piece


#
#  Returns True if there is no EMPTY location in the board
#
#  Parameters:
#    board: The board to examine
#
#  Returns: True if board has no EMPTY locations, False otherwise
#

#This function will enable us to check if the board game is full
#if the the board is empty it will keep playing the game
def full(board):
    #this is for each row to be checked
    for row in range( len(board)):
        #this is for each column to be checked
        for col in range(len(board[row])):
            #this is to check if the board is empty, it return False
            if board [row][col] == EMPTY:
                return False
    #it will return True if the board is full
    return True

#
#  Insert your implementations of winInRow, winInCol, winInDiag here (code and comments (in-line and above functions))
#

#This function enable the computer to check if one player has a win the game in a row
#we check if we have a row with the same markers
def winInRow(board, row, piece):
    #for each column to be checked and for the computer not to go over the set of ranges
    for col in range(len(board[row])-2):
        if board[row][col] == piece and board [row][col+1] == piece and board [row][col+2] == piece:
            return True
    #it return false if there is no same piece aline back to back on the same row
    return False


#This function enable the computer to check if one player has a win the game in a column
#we check if we have a column with the same markers
def winInCol(board, col, piece):
    # for each row to be checked and for the computer not to go over the set of ranges
    for row in range(len(board)-2):
        if board[row][col] == piece and board [row+1][col] == piece and board [row+2][col] == piece:
            return True
    # it return false if there is no same piece aline back to back on the same column
    return False


#This function enable the computer to check if one player has a win the game in a column
#we check if we have a column with the same markers
def winInDiag(board, piece):
    # the for loops check for each row and column in the board and makes sure that the computer does not checks over the set range
    for row in range(len(board)-2):
        for col in range(len(board[row])-2):
            #forward diagonal
            if board[row][col] == piece and board [row+1][col+1] == piece and board [row+2][col+2] == piece:
                return True

            #backward diagonal
            if board[row][col+2] == piece and board [row+1][col+1] == piece and board [row+2][col] == piece:
                return True
    # it return false if there is no same piece aline back to back on the same column
    else:
        return False



#
#  Returns True if player with indicated piece type has won game
#       Uses winInRow, winInCol, winInDiag
#
#  Parameters:
#    board: The board to examine
#    peice: The piece type to look for (will be X or O)
#
#  Returns: True if player with indicated piece has winning arrangement in board
#

#This function checks if a player has won the game
def won(board, piece):
# for each row to be checked and for the computer not to go over the set of ranges
    for row in range(len(board)):
        #if the player has a win in the rows, it will return True and stop the game
       if winInRow(board,row,piece):
            return True
# for each column to be checked and for the computer not to go over the set of ranges
    for col in range(len(board[0])):
        #if the player has a win in the column, it will return True and stop the game
        if winInCol(board,col,piece):
            return True
    #if the player has a win in the diagonal, it will return True and stop the game
    if winInDiag(board,piece):
        return True
#the program will return False if none of the conditions are met
    return False


#
#  Identify if a position will complete 3 in a row for a win
#
#  Parameters:
#    board: The game board to be checked, the piece type to be played
#
#  Returns: The row and column of the location the piece could be played to win.
#           If no winning play is possible then -1, -1 is returned.
#

#this function has the purpose to give an hint to the player when he enters 'a'.
#it will show the player a spot where he can play his piece so he can win the game or stop the other opponent
def hint(board, piece):
    # the for loops check for each row and column in the board and makes sure that the computer checks all the ranges for the columns and rows
    for row in range(len(board)):
        for col in range(len(board[row])):
            # cheching if the player can play a piece in a specific spot
            if canPlay(board,row, col) == True:
                # then the player piece will be position in the spot demanded
                play(board, row, col, piece)
                #checking if the player won the game
                if won(board, piece):
                    # the program goes back to the previous location , which means it leaves an empty spot
                    play(board, row, col, EMPTY)
                    #it returns the specific row and column
                    return row, col
                else:
                    # the program goes back to the previous location , which means it leaves an empty spot
                    play(board, row, col, EMPTY)
    #It return this to indicate there is no hint to show
    return -1,-1


##############################################################################
#
# Only modify code above this point in the file
#
##############################################################################

# Uses students full and won functions to decide if game has ended in current board
def gameover(board):
    if full(board) or won(board, X) or won(board, O):
        return True
    return False


##############################################################################
#
# Code below is for testing student functions (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################

# Determine whether or not a function exists in the namespace at the time
# this function is called
# Parameters:
#   name: The name of the function to check the existence of
# Returns: True if the function exists, False otherwise
def functionExists(name):
    members = inspect.getmembers(sys.modules[__name__])
    for (n, m) in members:
        if n == name and inspect.isfunction(m):
            return True
    return False


# Run a series of tests on the createBoard function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testCreateBoard():
    if not TESTPART1:
        return True

    print("Testing createBoard...")

    # Does the createBoard function exist?
    if functionExists("createBoard"):
        print("  The function seems to exist...")
    else:
        sys.stdout.write("  The createBoard function doesn't seem to exist...\n")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(createBoard).args) != 2:
        sys.stdout.write("  createBoard should have 2 arguments!\n")
        return False

    # Can I call function on expected sizes without crash
    for (rows, cols) in [(3, 3), (3, 4), (4, 3), (4, 4)]:

        # Try and call the function
        try:
            print("  Attempting to use createBoard(%d, %d)... " % (rows, cols))
            b = createBoard(rows, cols)
        except Exception as e:
            sys.stdout.write("An exception occurred during the attempt.\n")
            traceback.print_exc(file=sys.stderr)
            return False

        # Does it have the correct return type?
        if type(b) is not list:
            sys.stdout.write("    The value returned was a " + str(type(b)) + ", not a list.\n")
            return False

        # Does the list have the corret number of elements?
        if len(b) != rows:
            sys.stdout.write("    The board had " + str(len(b)) + " rows when " + str(rows) + " were expected.\n")
            return False

        # Is each row a list?  Does each row have the correct length?
        for i in range(len(b)):
            if type(b[i]) is not list:
                sys.stdout.write("    The row at index " + str(i) + " is a " + str(type(b[i])) + ", not a list.\n")
                return False
            if len(b[i]) != cols:
                sys.stdout.write(
                    "    The row at index" + str(i) + " had " + str(len(b[i])) + " elements when " + str(cols) + " were expected.\n")
                return False

        # Is each row unique
        for i in range(len(b)):
            for j in range(len(b)):
                if i != j:
                    if b[i] is b[j]:
                        sys.stdout.write("    The row at index " + str(
                            i) + " is pointing to the same row as the row at index " + str(j) + ".\n")
                        return False

        # Is every space on the board populated with an integer value between 
        # 0 and syms (not including syms)?
        for r in range(0, len(b)):
            for c in range(0, len(b[r])):
                if type(b[r][c]) is not int:
                    sys.stdout.write("    The value in row " + str(r) + " column " + str(c) + " is a " + str(
                        type(b[r][c])) + " , not an integer\n")
                    return False
                if b[r][c] != EMPTY:
                    sys.stdout.write("    The integer in row " + str(r) + " column " + str(c) + " is a " + str(
                        b[r][c]) + " which is not EMPTY=0\n")
                    return False

    print("Success.")
    print()
    return True


# Run a series of tests on the canPlay and play functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testPlay():
    if not TESTPART2:
        return True

    print("Testing play, canPlay...")

    # Does the play, canPlay function exist?
    if functionExists("play"):
        print("  The function play seems to exist...")
    else:
        sys.stdout.write("  The play function doesn't seem to exist...\n")
        return False
    if functionExists("canPlay"):
        print("  The function canPlay seems to exist...")
    else:
        sys.stdout.write("  The canPlay function doesn't seem to exist...\n")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(canPlay).args) != 3:
        sys.stdout.write("  canPlay should have 3 arguments!\n")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(play).args) != 4:
        sys.stdout.write("  play should have 4 arguments!\n")
        return False

    for rows in [3, 4]:
        for cols in [3, 4]:
            b = createBoard(rows, cols)
            print("  The canPlay for all spots in empty board...")
            for row in range(rows):
                for col in range(cols):
                    r = canPlay(b, row, col)
                    # Check return type and value? Should be able to play everywhere.
                    if type(r) is not bool:
                        sys.stdout.write("    The value returned was a " + str(type(r)) + ", not a boolean.\n")
                        return False
                    if r is False:
                        message = "    The board " + str(b) + " is empty but canPlay(board, %d, %d) was False.\n"
                        sys.stdout.write(message % (row, col))
                        return False
                    b[row][col] = X
                    r = canPlay(b, row, col)
                    # Check return type and value? Should not be able to play here now.
                    if type(r) is not bool:
                        sys.stdout.write("    The value returned was a " + str(type(r)) + ", not a boolean.\n")
                        return False
                    if r is True:
                        message = "    The board " + str(
                            b) + " has piece at this spot but canPlay(board, %d, %d) was True.\n"
                        sys.stdout.write(message % (row, col))
                        return False
                    b[row][col] = EMPTY
            copy = deepcopy(b)
            # Change a copy of the board and check if result of play, canPlay matches changes expected
            print("  Test play/canPlay before and after playing at every location in", rows, "x", cols, " empty board")
            for row in range(rows):
                for col in range(cols):
                    r0 = canPlay(b, row, col)
                    if r0 is False:
                        message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False.\n"
                        sys.stdout.write(message % (row, col))
                        return False
                    # Play an X. Should not be able to play in this spot now.
                    r1 = play(b, row, col, X)
                    if type(r1) is not type(None):
                        message = "    The value returned by play(board, %d, %d, %d) was a " + str(
                            type(r1)) + ", not None.\n"
                        sys.stdout.write(message % (row, col, X))
                        return False
                    copy[row][col] = X
                    if copy != b:
                        message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(
                            copy) + "\n"
                        sys.stdout.write(message % (row, col, X))
                        return False
                    r2 = canPlay(b, row, col)
                    if r2 is True:
                        message = "   The board " + str(b) + " is occupied but canPlay(board, %d, %d) was True.\n"
                        sys.stdout.write(message % (row, col))
                        return True
                    # Play an EMPTY. Should be able to play in this spot now.
                    r3 = play(b, row, col, EMPTY)
                    if type(r3) is not type(None):
                        message = "    The value returned by play(board, %d, %d, %d) was a " + str(
                            type(r3)) + ", not None.\n"
                        sys.stdout.write(message % (row, col, EMPTY))
                        return False
                    copy[row][col] = EMPTY
                    if copy != b:
                        message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(
                            copy) + "\n"
                        sys.stdout.write(message % (row, col, EMPTY))
                        return False
                    r4 = canPlay(b, row, col)
                    if r4 is False:
                        message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False.\n"
                        sys.stdout.write(message % (row, col))
                        return False
                        # Play an O. Should not be able to play in this spot now.
                    r5 = play(b, row, col, O)
                    if type(r5) is not type(None):
                        message = "    The value returned by play(board, %d, %d, %d) was a " + str(
                            type(r5)) + ", not None.\n"
                        sys.stdout.write(message % (row, col, O))
                        return False
                    copy[row][col] = O
                    if copy != b:
                        message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(
                            copy) + "\m"
                        sys.stdout.write(message % (row, col, O))
                        return False
                    r6 = canPlay(b, row, col)
                    if r6 is True:
                        message = "   The board " + str(b) + " is occupied but canPlay(board, %d, %d) was True.\n"
                        sys.stdout.write(message % (row, col))
                        return True
                        # Play an EMPTY. Should be able to play in this spot now.
                    r7 = play(b, row, col, EMPTY)
                    if type(r7) is not type(None):
                        message = "    The value returned by play(board, %d, %d, %d) was a " + str(
                            type(r7)) + ", not None.\n"
                        sys.stdout.write(message % (row, col, EMPTY))
                        return False
                    copy[row][col] = EMPTY
                    if copy != b:
                        message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(
                            copy) + "\n"
                        sys.stdout.write(message % (row, col, EMPTY))
                        return False
                    r8 = canPlay(b, row, col)
                    if r8 is False:
                        message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False.\n"
                        sys.stdout.write(message % (row, col))
                        return False
    print("Success.")
    print()
    return True


# Run a series of tests on the full functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.   
def testFull():
    if not TESTPART3:
        return True

    print("Testing full...")

    # Does the full function exist?
    if functionExists("full"):
        print("  The function full seems to exist...")
    else:
        sys.stdout.write("  The full function doesn't seem to exist...\n")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(full).args) != 1:
        sys.stdout.write("  play should have 1 argument!\n")
        return False

    for rows in [3, 4]:
        for cols in [3, 4]:
            print("Testing full for a board of size", rows, "x", cols)
            b = createBoard(rows, cols)
            # Does full return right for empty board?
            print("  Testing call to full for empty board.")
            r = full(b)
            if type(r) is not bool:
                sys.stdout.write("    The value returned by full(board) was a " + str(type(r)) + ", not a boolean.\n")
                return False
            if r == True:
                sys.stdout.write("   The board " + str(b) + " is empty but full returned True.\n")
                return False
            for row in range(rows):
                for col in range(cols):
                    b[row][col] = X
            r = full(b)
            # Does full return right for full board?
            print("  Testing call to full for board full of Xs.")
            if type(r) is not bool:
                sys.stdout.write("    The value returned by full(board) was a " + str(type(r)) + ", not a boolean.\n")
                return False
            if r == False:
                sys.stdout.write("    The board " + str(b) + " is full but full returned False.\n")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Xs with one EMPTY spot")
            for row in range(rows):
                for col in range(cols):
                    b[row][col] = EMPTY
                    r = full(b)
                    if type(r) is not bool:
                        sys.stdout.write(
                            "    The value returned by full(board) was a " + str(type(r)) + ", not a boolean.\n")
                        return False
                    if r == True:
                        sys.stdout.write("    The board " + str(b) + " is not full returned True.\n")
                        return False
                    b[row][col] = X
            for row in range(rows):
                for col in range(cols):
                    b[row][col] = O
            r = full(b)
            # Does full return right for full board?
            print("  Testing call to full for board full of Os.")
            if type(r) is not bool:
                sys.stdout.write("    The value returned by full(board) was a " + str(type(r)) + ", not a boolean.\n")
                return False
            if r == False:
                sys.stdout.write("    The board " + str(b) + " is full but full returned False.")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Os with one EMPTY spot")
            for row in range(rows):
                for col in range(cols):
                    b[row][col] = EMPTY
                    r = full(b)
                    if type(r) is not bool:
                        sys.stdout.write(
                            "    The value returned by full(board) was a " + str(type(r)) + ", not a boolean.\n")
                        return False
                    if r == True:
                        sys.stdout.write("    The board " + str(b) + " is not full returned True.")
                        return False
                    b[row][col] = O
    print("Success.")
    print()
    return True


# Run a series of tests on the winInRow function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInRow():
    if not TESTPART4:
        return True

    print("Testing winInRow...")

    # Does the winInRow function exist?
    if functionExists("winInRow"):
        print("  The function winInRow seems to exist...")
    else:
        sys.stdout.write("  The winInRow function doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInRow).args) != 3:
        sys.stdout.write("  winInRow should have 3 arguments!\n")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (b, r, p, s) in [ \
            # Board sizes with wins
        ([[1, 1, 1], \
          [0, 0, 0], \
          [0, 0, 0]], 0, 1, True), \
            ([[1, 1, 1], \
              [0, 0, 0], \
              [0, 0, 0], \
              [0, 0, 0]], 0, 1, True), \
            ([[1, 1, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[1, 1, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            # Win in other rows
        ([[0, 0, 0, 0], \
          [1, 1, 1, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0]], 1, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 1, True), \
            ([[0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 0], \
              [0, 0, 0, 0]], 2, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 1, 1], \
              [0, 0, 0, 0]], 2, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0]], 2, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 0]], 3, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 1, 1]], 3, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1]], 3, 1, True), \
            # Win with other piece type
        ([[0, 0, 0, 0], \
          [2, 2, 2, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0]], 1, 2, True), \
            ([[0, 0, 0, 0], \
              [0, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, True), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, True), \
            # Win has other type around
        ([[1, 1, 1, 2], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0]], 0, 1, True), \
            ([[2, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            # Win isn't with asked about piece type
        ([[1, 1, 1, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0]], 0, 2, False), \
            ([[0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 2, False), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 2, False), \
            ([[2, 2, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            # Win broken by non empty
        ([[1, 1, 2, 1], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0], \
          [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 2, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for i in range(len(b)):
                attempt += 1
                result = winInRow(b, i, p)
                # Does it have the correct return type?
                if type(result) is not bool:
                    sys.stdout.write("  Attempting to use winInRow Test " + str(attempt))
                    sys.stdout.write("\nFAILED: The value returned was a " + str(type(result)) + ", not a Boolean.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue

                # Did it return the correct value
                if s and not result and r == i:
                    sys.stdout.write("  Attempting to use winInRow Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for row = " + str(i) + " piece = " + str(
                            p) + " when "+str(s)+" was expected.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif s and result and r != i:
                    sys.stdout.write("  Attempting to use winInRow Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for row = " + str(i) + " piece = " + str(
                            p) + " when False was expected. (There is a win in another row, but not the one the function was asked about.)\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                elif not s and result:
                    sys.stdout.write("  Attempting to use winInRow Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for row = " + str(i) + " piece = " + str(
                            p) + " when "+str(s)+" was expected.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception as e:
            sys.stdout.write("  Attempting to use winInRow Test " + str(attempt))
            sys.stdout.write("\nFAILED: An exception occurred during the attempt.\n")
            sys.stdout.write("The board was:\n")
            pprint(b)
            sys.stdout.write("\n")
            traceback.print_exc(file=sys.stderr)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        sys.stdout.write("Failed " + str(failed) + " test cases of " + str(attempt) + "\n")
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the winInCol function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInCol():
    if not TESTPART4:
        return True
    print("Testing winInCol...")

    # Does the winInCol function exist?
    if functionExists("winInCol"):
        print("  The function winInCol seems to exist...")
    else:
        sys.stdout.write("  The winInCol function doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInCol).args) != 3:
        sys.stdout.write("  winInCol should have 3 arguments!\n")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (b, c, p, s) in [ \
 \
            ([[1, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0]], 0, 1, True), \
            ([[1, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0], \
              [0, 0, 0]], 0, 1, True), \
            ([[0, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0]], 0, 1, True), \
            ([[1, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0], \
              [1, 0, 0]], 0, 1, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, True), \
            # Win in other rows
        ([[0, 1, 0, 0], \
          [0, 1, 0, 0], \
          [0, 1, 0, 0], \
          [0, 0, 0, 0]], 1, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 1, 0, 0], \
              [0, 1, 0, 0]], 1, 1, True), \
            ([[0, 1, 0, 0], \
              [0, 1, 0, 0], \
              [0, 1, 0, 0], \
              [0, 1, 0, 0]], 1, 1, True), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 2, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, 1, True), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, 1, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0]], 3, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 3, 1, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 3, 1, True), \
            # Win with other piece type
        ([[0, 2, 0, 0], \
          [0, 2, 0, 0], \
          [0, 2, 0, 0], \
          [0, 0, 0, 0]], 1, 2, True), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, 2, True), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, 2, True), \
            # Win has other type around
        ([[1, 0, 0, 0], \
          [1, 0, 0, 0], \
          [1, 0, 0, 0], \
          [2, 0, 0, 0]], 0, 1, True), \
            ([[2, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, True), \
            # Win isn't with asked about piece type
        ([[1, 0, 0, 0], \
          [1, 0, 0, 0], \
          [1, 0, 0, 0], \
          [0, 0, 0, 0]], 0, 2, False), \
            ([[0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 2, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 2, False), \
            ([[2, 0, 0, 0], \
              [2, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [2, 0, 0, 0], \
              [2, 0, 0, 0]], 0, 1, False), \
            ([[2, 0, 0, 0], \
              [2, 0, 0, 0], \
              [2, 0, 0, 0], \
              [2, 0, 0, 0]], 0, 1, False), \
            # Win broken by non empty
        ([[1, 0, 0, 0], \
          [1, 0, 0, 0], \
          [2, 0, 0, 0], \
          [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [2, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for i in range(len(b[0])):
                attempt += 1
                result = winInCol(b, i, p)
                # Does it have the correct return type?
                if type(result) is not bool:
                    sys.stdout.write("  Attempting to use winInCol Test " + str(attempt))
                    sys.stdout.write("\nFAILED: The value returned was a " + str(type(result)) + ", not a Boolean.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue

                # Did it return the correct value
                if s and not result and c == i:
                    sys.stdout.write("  Attempting to use winInCol Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for col = " + str(i) + " piece = " + str(
                            p) + " when "+str(s)+" was expected.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif s and result and c != i:
                    sys.stdout.write("  Attempting to use winInCol Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for col = " + str(i) + " piece = " + str(
                            p) + " when False was expected. (There is a win in another column, but not the one the function was asked about.)\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                elif not s and result:
                    sys.stdout.write("  Attempting to use winInCol Test " + str(attempt))
                    sys.stdout.write(
                        "\nFAILED: The value returned was " + str(result) + " for col = " + str(i) + " piece = " + str(
                            p) + " when "+str(s)+" was expected.\n")
                    sys.stdout.write("The board was:\n")
                    pprint(b)
                    sys.stdout.write("\n")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception as e:
            sys.stdout.write("  Attempting to use winInCol Test " + str(attempt))
            sys.stdout.write("\nFAILED: An exception occurred during the attempt.\n")
            sys.stdout.write("The board was:\n")
            pprint(b)
            sys.stdout.write("\n")
            traceback.print_exc(file=sys.stderr)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        sys.stdout.write("Failed " + str(failed) + " test cases of " + str(attempt) + "\n")
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the winInDiag function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInDiag():
    if not TESTPART5:
        return True
    print("Testing winInDiag...")

    # Does the winInDiag function exist?
    if functionExists("winInDiag"):
        print("  The function winInDiag seems to exist...")
    else:
        sys.stdout.write("  The winInDiag function doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInDiag).args) != 2:
        sys.stdout.write("  winInDiag should have 2 arguments!\n")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, s) in [ \
            # win in different board sizes
        ([[1, 0, 0], \
          [0, 1, 0], \
          [0, 0, 1]], 1, True), \
            ([[1, 0, 0], \
              [0, 1, 0], \
              [0, 0, 1], \
              [0, 0, 0]], 1, True), \
            ([[0, 0, 0], \
              [1, 0, 0], \
              [0, 1, 0], \
              [0, 0, 1]], 1, True), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0]], 1, True), \
            ([[0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[0, 0, 1], \
              [0, 1, 0], \
              [1, 0, 0]], 1, True), \
            ([[0, 0, 1], \
              [0, 1, 0], \
              [1, 0, 0], \
              [0, 0, 0]], 1, True), \
            ([[0, 0, 0], \
              [0, 0, 1], \
              [0, 1, 0], \
              [1, 0, 0]], 1, True), \
            ([[0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0]], 1, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            # Win with other piece type
        ([[0, 0, 0, 2], \
          [0, 0, 2, 0], \
          [0, 2, 0, 0], \
          [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0]], 2, True), \
            # Win has other type around
        ([[0, 0, 0, 2], \
          [0, 0, 2, 0], \
          [0, 2, 0, 0], \
          [1, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0]], 2, True), \
            # Win isn't with asked about piece type
        ([[1, 0, 0, 0], \
          [0, 1, 0, 0], \
          [0, 0, 1, 0], \
          [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 2, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 2, False), \
            ([[0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0]], 1, False), \
            # Win broken by non empty
        ([[1, 0, 0, 0], \
          [0, 2, 0, 0], \
          [0, 0, 1, 0], \
          [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 2, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 2, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
 \
            ([[1, 2, 0], \
              [2, 2, 1], \
              [1, 1, 2]], 1, False), \
            ([[1, 2, 0], \
              [2, 2, 1], \
              [1, 1, 2]], 2, False), \
            ([[1, 2, 1], \
              [1, 2, 2], \
              [2, 1, 0]], 1, False), \
            ([[1, 2, 1], \
              [1, 2, 2], \
              [2, 1, 0]], 2, False), \
            ([[2, 1, 1], \
              [1, 2, 2], \
              [0, 2, 1]], 1, False), \
            ([[2, 1, 1], \
              [1, 2, 2], \
              [0, 2, 1]], 2, False), \
            ([[0, 1, 2], \
              [2, 2, 1], \
              [1, 2, 1]], 1, False), \
            ([[0, 1, 2], \
              [2, 2, 1], \
              [1, 2, 1]], 2, False), \
 \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1]], 1, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1]], 2, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2]], 1, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2]], 2, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0]], 1, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0]], 2, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0]], 1, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0]], 2, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1], \
              [0, 0, 0]], 1, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1], \
              [0, 0, 0]], 2, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2], \
              [0, 0, 0]], 1, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2], \
              [0, 0, 0]], 2, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0], \
              [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            result = winInDiag(b, p)
            # Does it have the correct return type?
            if type(result) is not bool:
                sys.stdout.write("  Attempting to use winInDiag Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was a " + str(type(result)) + ", not a Boolean.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if s and not result:
                sys.stdout.write("  Attempting to use winInDiag Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was " + str(result) + " for piece = " + str(
                    p) + " when True was expected.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not s and result:
                sys.stdout.write("  Attempting to use winInDiag Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was " + str(result) + " for piece = " + str(
                    p) + " when False was expected.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            sys.stdout.write("  Attempting to use winInDiag Test " + str(attempt))
            sys.stdout.write("\nFAILED: An exception occurred during the attempt.\n")
            sys.stdout.write("The board was:\n")
            pprint(b)
            sys.stdout.write("\n")
            traceback.print_exc(file=sys.stderr)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        sys.stdout.write("Failed " + str(failed) + " test cases of " + str(attempt) + "\n")
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the won function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWon():
    if not TESTPART6:
        return True
    print("Testing won...")

    # Does the won function exist?
    if functionExists("won"):
        print("  The function won seems to exist...")
    else:
        sys.stdout.write("  The won won doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(won).args) != 2:
        sys.stdout.write("  won should have 2 arguments!\n")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, s) in [ \
            ([[1, 1, 1], \
              [0, 0, 0], \
              [0, 0, 0]], 1, True), \
            ([[0, 0, 0], \
              [1, 1, 1], \
              [0, 0, 0]], 1, True), \
            ([[0, 0, 0], \
              [0, 0, 0], \
              [1, 1, 1]], 1, True), \
            ([[2, 2, 2], \
              [0, 0, 0], \
              [0, 0, 0]], 2, True), \
            ([[0, 0, 0], \
              [2, 2, 2], \
              [0, 0, 0]], 2, True), \
            ([[0, 0, 0], \
              [0, 0, 0], \
              [2, 2, 2]], 2, True), \
            ([[1, 1, 1], \
              [0, 0, 0], \
              [0, 0, 0]], 2, False), \
            ([[0, 0, 0], \
              [1, 1, 1], \
              [0, 0, 0]], 2, False), \
            ([[0, 0, 0], \
              [0, 0, 0], \
              [1, 1, 1]], 2, False), \
            ([[2, 2, 2], \
              [0, 0, 0], \
              [0, 0, 0]], 1, False), \
            ([[0, 0, 0], \
              [2, 2, 2], \
              [0, 0, 0]], 1, False), \
            ([[0, 0, 0], \
              [0, 0, 0], \
              [2, 2, 2]], 1, False), \
            ([[1, 0, 0], \
              [0, 1, 0], \
              [0, 0, 1]], 1, True), \
            ([[0, 0, 1], \
              [0, 1, 0], \
              [1, 0, 0]], 1, True), \
            ([[2, 0, 0], \
              [0, 2, 0], \
              [0, 0, 2]], 2, True), \
            ([[0, 0, 2], \
              [0, 2, 0], \
              [2, 0, 0]], 2, True), \
            ([[1, 0, 0], \
              [0, 1, 0], \
              [0, 0, 1]], 2, False), \
            ([[0, 0, 1], \
              [0, 1, 0], \
              [1, 0, 0]], 2, False), \
            ([[2, 0, 0], \
              [0, 2, 0], \
              [0, 0, 2]], 1, False), \
            ([[0, 0, 2], \
              [0, 2, 0], \
              [2, 0, 0]], 1, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1]], 1, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1]], 2, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2]], 1, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2]], 2, False), \
 \
            ([[1, 2, 0], \
              [2, 2, 1], \
              [1, 1, 2]], 1, False), \
            ([[1, 2, 0], \
              [2, 2, 1], \
              [1, 1, 2]], 2, False), \
            ([[1, 2, 1], \
              [1, 2, 2], \
              [2, 1, 0]], 1, False), \
            ([[1, 2, 1], \
              [1, 2, 2], \
              [2, 1, 0]], 2, False), \
            ([[2, 1, 1], \
              [1, 2, 2], \
              [0, 2, 1]], 1, False), \
            ([[2, 1, 1], \
              [1, 2, 2], \
              [0, 2, 1]], 2, False), \
            ([[0, 1, 2], \
              [2, 2, 1], \
              [1, 2, 1]], 1, False), \
            ([[0, 1, 2], \
              [2, 2, 1], \
              [1, 2, 1]], 2, False), \
 \
            ([[1, 1, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 1, 1], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 2, 2]], 2, True), \
            ([[1, 1, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 1, 1], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 2, 2]], 1, False), \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 2, True), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 1, True), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 2, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 2, False), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, False), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, False), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 2, True), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 2, True), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 2, False), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 1, False), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, False), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0]], 1, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0]], 2, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0]], 1, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0]], 2, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1], \
              [0, 0, 0]], 1, False), \
            ([[1, 2, 1], \
              [2, 0, 2], \
              [1, 2, 1], \
              [0, 0, 0]], 2, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2], \
              [0, 0, 0]], 1, False), \
            ([[2, 1, 2], \
              [1, 0, 1], \
              [2, 1, 2], \
              [0, 0, 0]], 2, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 2, 1, 0], \
              [2, 0, 2, 0], \
              [1, 2, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[2, 1, 2, 0], \
              [1, 0, 1, 0], \
              [2, 1, 2, 0], \
              [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            result = won(b, p)
            # Does it have the correct return type?
            if type(result) is not bool:
                sys.stdout.write("  Attempting to use won Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was a " + str(type(result)) + ", not a Boolean.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if s and not result:
                sys.stdout.write("  Attempting to use won Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was " + str(result) + " for piece = " + str(
                    p) + " when True was expected.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not s and result:
                sys.stdout.write("  Attempting to use won Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was " + str(result) + " for piece = " + str(
                    p) + " when False was expected.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            sys.stdout.write("  Attempting to use won Test " + str(attempt))
            sys.stdout.write("\nFAILED: An exception occurred during the attempt.\n")
            sys.stdout.write("The board was:\n")
            pprint(b)
            sys.stdout.write("\n")
            traceback.print_exc(file=sys.stderr)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        sys.stdout.write("Failed " + str(failed) + " test cases of " + str(attempt) + "\n")
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the hint function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testHint():
    if not TESTPART7:
        return True
    print("Testing hint...")

    # Does the hint function exist?
    if functionExists("hint"):
        print("  The function hint seems to exist...")
    else:
        print("  The winInDiag hint doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(hint).args) != 2:
        sys.stdout.write("  hint should have 2 arguments!\n")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, r, c) in [ \
            ([[1, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 2), \
            ([[0, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 1), \
            ([[0, 0, 0, 0], \
              [2, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 1, 1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 1, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 0], \
              [0, 0, 0, 0]], 1, 2, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 1], \
              [0, 0, 0, 0]], 1, 2, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 0, 2, 0]], 2, 3, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 2]], 2, 3, 2), \
 \
            ([[1, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 1], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 0, 2, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 2]], 1, -1, -1), \
 \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 2), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 1, 3, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 1, 3, 1), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, 0), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 0), \
            ([[0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 2, 1, 1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0]], 2, 2, 1), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 1, 1, 2), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 2, 1, 3), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2]], 2, 2, 3), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0]], 1, -1, -1), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, -1, -1), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2]], 1, -1, -1), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 2, 0), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, -1, -1), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 0), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, 2, 3), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, -1, -1), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 1, 1, 3), \
 \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 2), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, 2, 2), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 2), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 2, 3), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 0, 2), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 2, 3, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 2, 1, 3), \
 \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 2, -1, -1), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 1, -1, -1)

    ]:

        # Attempt the function call
        try:
            attempt += 1
            row, col = hint(deepcopy(b), p)
            # Does it have the correct return type?
            if type(row) is not int:
                sys.stdout.write("  Attempting to use hint Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was a " + str(type(row)) + ", not a Integer.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            if type(col) is not int:
                sys.stdout.write("  Attempting to use hint Test " + str(attempt))
                sys.stdout.write("\nFAILED: The value returned was a " + str(type(col)) + ", not a Integer.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if r != row or c != col:
                sys.stdout.write("  Attempting to use hint Test " + str(attempt))
                sys.stdout.write(
                    "\nFAILED: The value returned was " + str(row) + " , " + str(col) + " for piece = " + str(
                        p) + " when " + str(r) + " , " + str(c) + " was expected.\n")
                sys.stdout.write("The board was:\n")
                pprint(b)
                sys.stdout.write("\n")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            sys.stdout.write("  Attempting to use hint Test " + str(attempt))
            sys.stdout.write("\nFAILED: An exception occurred during the attempt.\n")
            sys.stdout.write("The board was:\n")
            pprint(b)
            sys.stdout.write("\n")
            traceback.print_exc(file=sys.stderr)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        sys.stdout.write("Failed " + str(failed) + " test cases of " + str(attempt) + "\n")
    else:
        print("Passed all tests. <", attempt, ">")
    print()
    return


##############################################################################
##
##  Code for drawing (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

# Draw X with lines in box beginning at (x,y) with given square size and color
def drawX(x, y, sizex, sizey, color="black"):
    setColor(color)
    line(x + 15, y + 15, x + sizex - 15, y + sizey - 15)
    line(x + sizex - 15, y + 15, x + 15, y + sizey - 15)


# Draw O with lines in box beginning at (x,y) with given square size and color
def drawO(x, y, sizex, sizey, color="black"):
    setColor(color)
    setFill(None)
    ellipse(x + 15, y + 15, sizex - 30, sizey - 30)


# Draw hint information and X or O based on piece in given row, col of board
def drawHint(board, row, col, piece):
    setColor("orange")
    setFill(None)
    rows = len(board)
    cols = len(board[0])
    row_diff = int(HEIGHT / rows)
    col_diff = int(WIDTH / cols)
    rect(col * col_diff, row * row_diff, col_diff + 1, row_diff + 1)
    if piece == X:
        drawX(col * col_diff, row * row_diff, col_diff, row_diff, "orange")
    elif piece == O:
        drawO(col * col_diff, row * row_diff, col_diff, row_diff, "orange")


# Draw the board in given color
def drawBoard(board, color="black"):
    setColor("white")
    rect(0, 0, WIDTH, HEIGHT)
    setColor(color)
    rows = len(board)
    cols = len(board[0])
    row_diff = int(HEIGHT / rows)
    col_diff = int(WIDTH / cols)
    for y in range(row_diff, HEIGHT - 1, row_diff):
        line(0, y, WIDTH, y)
    for x in range(col_diff, WIDTH - 1, col_diff):
        line(x, 0, x, HEIGHT)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                drawX(col * col_diff, row * row_diff, col_diff, row_diff, color)
            elif board[row][col] == O:
                drawO(col * col_diff, row * row_diff, col_diff, row_diff, color)


# Setup window and draw initial white line to make it resize
def setupWindow():
    background("white")
    setColor("white")
    resize(WIDTH, HEIGHT)
    line(0, 0, 1, 1)


#############################################################################
##
##  Code for AI and hint for 3x3 tic-tac-toe (IF YOU ARE READING THIS YOU BETTER NOT BE CHANGING CODE DOWN HERE)
##
##############################################################################

# Get all open moves in the board (i.e. BLANK spots)
def openMoves(board):
    moves = []
    rows = list(range(0, len(board)))
    cols = list(range(0, len(board[0])))
    for row in rows:
        for col in cols:
            if canPlay(board, row, col):
                moves.append((row, col))
    return moves


# Evalaute the board
def evaluate(board, player1, player2):
    score = 0
    if won(board, player1):
        score = 1
    elif won(board, player2):
        score = -1
    else:
        score = 0
    return score


# Minimax suggest of what row, col to play in for player1 as initial call, and player as current tree call
def minimax(board, player1, player2, player, depth):
    # We will be either maximizing value if player1 called AI
    if player == player1:
        best = [None, None, -infinity]
    # Or minimizing if player2 did
    else:
        best = [None, None, +infinity]
    # If we run out of depth or game ends then get board state
    if depth == 0 or gameover(board):
        score = evaluate(board, player1, player2)
        return [None, None, score]
    # Get all open moves
    moves = openMoves(board)
    for move in moves:
        row, col = move[0], move[1]
        # Make play
        play(board, row, col, player)
        # Set next player to be other guy
        next_player = None
        if player == player1:
            next_player = player2
        else:
            next_player = player1
        # Get score by exploring down tree
        score = minimax(board, player1, player2, next_player, depth - 1)
        score[0], score[1] = row, col
        ##Undo the play
        play(board, row, col, EMPTY)
        # Depending on if we are currently on player1 or player 2 we update the best upwards, or downwards
        if player == player1:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best


# Calling AI, if level 4 we do full recursive minmax, if not we recurse only to certain depth
# If level=0 AI we just pick random open spot
def AI(board, player1, player2, level):
    if player1 != X and player1 != O:
        print("AI player1 should be X/O")
        exit(1)
    if player2 != X and player2 != O:
        print("AI player2 should be X/O")
        exit(1)
    if player1 == X and player2 != O:
        print("AI player1/player2 can't be X/X")
        exit(1)
    if player1 == O and player2 != X:
        print("AI player1/player2 can't be O/O")
        exit(1)
    if level < 0 or level > 4:
        print("AI level has to be 0 <= level <= 4")
        exit(1)
    # Do unlimited lookahead if level >= 4
    if level >= 4:
        result = minimax(board, player1, player2, player1, len(board) * len(board[0]) + 1)
        return result[0], result[1]
    # Otherwise multiply level by two (to get plays by each side for each level)
    elif level > 0:
        result = minimax(board, player1, player2, player1, level * 2)
        return result[0], result[1]
    # Otherwise random
    moves = openMoves(board)
    for move in moves:
        if canPlay(board, move[0], move[1]):
            return move
    # There is no move to be made
    return -1, -1


##############################################################################
##
##  Main function (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

def main():
    if not testCreateBoard():
        return
    if not testPlay():
        return
    testFull()
    testWinInRow()
    testWinInCol()
    testWinInDiag()
    testWon()
    testHint()
    setupWindow()
    rows = "?"
    while rows != "3" and rows != "4":
        rows = input("Pick a board row size (3 or 4): ")
    rows = int(rows)
    cols = "?"
    while cols != "3" and cols != "4":
        cols = input("Pick a board col size (3 or 4): ")
    cols = int(cols)
    board = createBoard(rows, cols)
    drawBoard(board)
    difficulty = "?"
    if rows == cols == 3:
        while difficulty != "0" and difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4":
            print("Pick a difficulty:")
            print("\t0\tAI plays randomly")
            print("\t1\tAI looks at its own and your next play")
            print("\t2\tAI looks two moves ahead for each player")
            print("\t3\tAI looks three moves ahead for each player")
            print("\t4\tAI looks ahead to end of game")
            print(
                "\t\t(Note a difficulty of 4 uses an AI algorithm that may slow down some computers and you will have to wait.")
            difficulty = input("Pick a difficulty:")
    else:
        while difficulty != "0" and difficulty != "1" and difficulty != "2" and difficulty != "3":
            print("Pick a difficulty:")
            print("\t0\tAI plays randomly")
            print("\t1\tAI looks at its own and your next play")
            print("\t2\tAI looks two moves ahead for each player")
            print("\t3\tAI looks three moves ahead for each player")
            difficulty = input("Pick a difficulty:")
    difficulty = int(difficulty)
    human = "?"
    while human != "X" and human != "O":
        human = input("Enter choice of X or O: ")
    if human == "X":
        print("Human is X.")
        print("Computer is O.")
        human = X
        computer = O
    else:
        print("Human is O.")
        print("Computer is X.")
        human = O
        computer = X
    player = X
    plays = 0
    while not gameover(board):
        value = (rows * cols) - plays
        if (value > 0):
            complexity = factorial(value)
            print("Estimated complexity of current game:", complexity)
        if human == player:
            print("Human player's turn.")
            h = input("Enter 'h' for a game winning hint; ")
            while h != "h" and h != "a" and h != "":
                h = input("Enter 'h' for a game winning hint or "" to move on; ").strip()
            if h == "h":
                row1, col1 = hint(board, human)
                row2, col2 = hint(board, computer)
                if row1 != -1:
                    print("Hint is row =", row1, "and col =", col1)
                    drawHint(board, row1, col1, human)
                elif row2 != -1:
                    print("Hint is row =", row2, "and col =", col2)
                    drawHint(board, row2, col2, human)
                else:
                    print("No hint")
            elif h == "a":
                row = -1
                col = -1
                row1, col1 = hint(board, human)
                if row1 != -1:
                    row, col = row1, col1
                elif rows == cols == 3:
                    row, col = AI(board, human, computer, 4)
                else:
                    row, col = AI(board, human, computer, 3)
                if row != -1:
                    print("Hint is row =", row, "and col =", col)
                    drawHint(board, row, col, human)
                else:
                    print("No hint")

            trying = True
            while trying:
                selection = list(range(0, rows))
                row = -1
                while row < 0 or row > rows - 1:
                    try:
                        row = int(input("Enter row " + str(selection) + ": "))
                    except Exception as e:
                        print("Invalid row entered!")
                selection = list(range(0, cols))
                col = -1
                while col < 0 or col > cols - 1:
                    try:
                        col = int(input("Enter col " + str(selection) + ": "))
                    except Exception as e:
                        print("Invalid row entered!")
                if canPlay(board, row, col):
                    play(board, row, col, human)
                    trying = False
                else:
                    print("Chosen location board[" + str(row) + "][" + str(col) + "] is full!")
                print("Human plays in row", row, "and column", str(col) + ".")
                player = computer
        else:
            row, col = AI(board, computer, human, difficulty)
            play(board, row, col, computer)
            print("AI plays in row", row, "and column", str(col) + ".")
            player = human
        drawBoard(board)
        plays += 1
    setFont("Times", "50", "bold")

    if won(board, X):
        if human == X:
            drawBoard(board, "green")
        else:
            drawBoard(board, "red")
        setColor("black")
        text(300, 300, "X won!")
    elif won(board, O):
        if human == O:
            drawBoard(board, "green")
        else:
            drawBoard(board, "red")
        setColor("black")
        text(300, 300, "O won!")
    else:
        drawBoard(board, "blue")
        setColor("black")
        text(300, 300, "Board full. Draw.")


main()
