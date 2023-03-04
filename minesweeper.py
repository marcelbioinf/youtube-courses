import random
import re

class Board:
    def __init__(self, dimension, num_bombs):
        self.dim = dimension
        self.nb = num_bombs  # jednak musailem dodac te 2 ale nie chce mi sie zmieniac funkcji
        self.game_board = self.make_new_game_board(dimension, num_bombs)   #helper function
        self.dug = set()                                                   #initialize set to keep track pf which locations we've uncovered, we will use (row,cols) touples into the set
        self.assign_values_to_board(dimension)

    def make_new_game_board(self, dimension, num_bombs):
        board = [[None for x in range(dimension)] for y in range(dimension)]
        bombs_planted = 0
        while bombs_planted < num_bombs:
            #x, y = random.randint(0, dimension), random.randint(0, dimension)
            loc = random.randint(0, dimension**2 - 1)  # wersja z yt
            x, y = loc // dimension, loc % dimension
            if board[x][y] == '*':
                continue
            board[x][y] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self, dimension):
        for row in range(dimension):
            for column in range(dimension):
                if self.game_board[row][column] == '*':
                    continue
                num = 0
                for i in range(max(0, row - 1), min(dimension - 1, (row + 1) + 1)):
                    for j in range(max(0, column - 1), min(dimension - 1, (column + 1) + 1)):
                        if i == row and j == column:
                            continue
                        if self.game_board[i][j] == '*':
                            num += 1
                self.game_board[row][column] = num

    def dig(self, row, column):
        self.dug.add((row, column))
        if self.game_board[row][column] == '*':
            return False
        elif self.game_board[row][column] > 0:
            return True
        #self.board[row][column] == 0
        for i in range(max(0, row - 1), min(self.dim - 1, (row + 1) + 1)):
            for j in range(max(0, column - 1), min(self.dim - 1, (column + 1) + 1)):
                if (i, j) in self.dug:
                    continue # dont dig when you ve already been
                self.dig(i, j)
        return True

    def __str__(self):
        visible_board = [[None for x in range(self.dim)] for y in range(self.dim)]
        for i in range(self.dim):
            for j in range(self.dim):
                if (i, j) in self.dug:
                    visible_board[i][j] = str(self.game_board[i][j])
                else:
                    visible_board[i][j] = ' '

        #put this together into a string:
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep


def play(dimension=10, num_bombs=10):
    #s1: create board and plant the bombs
    board = Board(dimension, num_bombs)
    #s2: show the board to the user and ask where to dig
    #s3a: if location is a mobm show game over message
    #s3b: if loation is nota bomb, dig recoursively until each squre is at least next to bomb
    #s4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY
    safe = True
    while len(board.dug) < board.dim**2 - num_bombs:  #sa jeszcze miejsca ktore nie sa bombami wiec mozna kopac
        print(board)                                  #here we make a use of our magic function
        user_input = re.split(',(\\s)*', input("Where do you want to dig? Input as row,column: "))  # to akceptuje liczbe po ktorej jest przecinek i 0 lub nieskonczenie wiele spacji pomiedzy nim a druga liczba
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dimension or col < 0 or col >= dimension:
            print('ups wrong value, try again')
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    if safe:
        print("WOW YOU WON!")
    else:
        print("SORRY YOU LOST")
        board.dug = [(r,c) for r in range(dimension) for c in range(dimension)]
        print(board)


if __name__ == '__main__':
    play(10, 10)