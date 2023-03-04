from pprint import pprint


def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    return None, None


def is_valid(puzzle, guess, row, column):
    if guess in puzzle[row]:
        return False
    col_vals = []
    for r in range(9):
        col_vals.append(puzzle[r][column])      #lub one liner col_vals = [puzzle[r][column] for r in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3                  #zwraca wartosci tylko 0, 3 lub 6 - poczatki rzędu kazdego kwadratru
    col_start = (column // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solve_sudoku(puzzle):                                # sudoku solver with backtracking
    row, col = find_next_empty(puzzle)                   # choosse somewhere on the puzzle to make a guess
    if row is None:
        return True                                      #It means computer actually solved the sudoku
    for guess in range(1, 10):                           #1...9
        if is_valid(puzzle, guess, row, col):            #to check if the guess is valid in our puzzle at given row and column
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True                              #we will use reccurency
        puzzle[row][col] = -1                            #If we did not guessed right or the sollution we had so far turned out wrong we have backtack and try another number
    return False                                         #If we tried everything and it doesnt work out this puzzle is unsolvable


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
