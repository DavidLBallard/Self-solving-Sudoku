# #####test sudoku boards
# board = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
#          [9, 0, 0, 3, 0, 5, 0, 0, 1],
#          [0, 0, 1, 8, 0, 6, 4, 0, 0],
#          [0, 0, 8, 1, 0, 2, 9, 0, 0],
#          [7, 0, 0, 0, 0, 0, 0, 0, 8],
#          [0, 0, 6, 7, 0, 8, 2, 0, 0],
#          [0, 0, 2, 6, 0, 9, 5, 0, 0],
#          [8, 0, 0, 2, 0, 3, 0, 0, 9],
#          [0, 0, 5, 0, 1, 0, 3, 0, 0]
#          ]

# board = [[0, 6, 8, 0, 0, 2, 0, 0, 0],
#          [0, 5, 0, 4, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 9, 0, 6, 2],
#          [0, 0, 0, 1, 0, 8, 4, 9, 0],
#          [5, 0, 0, 0, 0, 0, 0, 0, 3],
#          [0, 9, 1, 6, 0, 4, 0, 0, 0],
#          [2, 1, 0, 7, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 3, 0, 5, 0],
#          [0, 0, 0, 9, 0, 0, 3, 4, 0],
#          ]
#  keeps track of the empy positions in the board as they are called
empty_Position = [0, 0]

# checks the row to see if the projected possible number is in the row


def check_Row(row, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    return True

# checks the column given to see if the projected possible number is in the Column


def check_Col(col, num):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True

#  checks the nearest 3x3 box based row and column submitted if the projected possible number
#  in the box


def check_Box(number, row, col):
    col_start = col - col % 3
    row_start = row - row % 3

    for r in range(3):
        for c in range(3):
            if board[r + row_start][c + col_start] == number:
                return False
    return True

#  function that checks all three possible area's to which the possible number could be in from the
#  functions above


def check_position(number, row, col):
    return check_Row(row, number) and check_Col(col, number) and check_Box(number, row, col)

# cycles through all the rows and columns to check for empositions based on "0" position
#  sets the global variable to the next empty spot


def check_empty_position():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                global empty_Position
                empty_Position = [row, col]
                return True
    return False


# solves the sudoku by calling the above functions
def solve_board():

    if not check_empty_position():
        return True

    row = empty_Position[0]
    col = empty_Position[1]

    for possible_number in range(1, 10):
        if check_position(possible_number, row, col):
            board[row][col] = possible_number
            if solve_board():
                return True

            board[row][col] = 0
    return False


# calls the solve board function based on which "Board" is not commented out in the global variables
solve_board()
#  loop that prints the board to a command line in a 9x9 version of the board
print("[*] Solution to the given Sudoku board submitted.[*]")
for row in board:
    print(str(row))
