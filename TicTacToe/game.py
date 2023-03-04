import player
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' +  ' | '.join(row) + ' | ')

    @staticmethod  # statyczna bo nie jest specyficzna dla obiektu, a jest dla calej klasy
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #another way below
        # moves = []
        # for(i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):  #function that chekcs if there is a winner after our last move
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #check rows
        row_index = square // 3  #returns always 0 or 1 or 2 which are rows
        row = self.board[row_index * 3 : (row_index + 1) *3]
        if all([spot == letter for spot in row]):
            return True

        #check columns
        if row_index == 0:
            column_index = square
        elif row_index == 1:
            column_index = square - 3
        else:
            column_index = square - 6
        # lub poprostu column_index = square % 3
        column = self.board[column_index:column_index+7:3]
        #lub column = [self.board[column_index + i *3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        if square in [0, 4, 8]:
            diagonal_1 = self.board[0:9:4]
            if all([spot == letter for spot in diagonal_1]):
                return True
        elif square in [2, 4, 6]:
            diagonal_2 = self.board[2:7:2]
            if all([spot == letter for spot in diagonal_2]):
                return True

        return False


def play(game, player_x, player_o, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #while game.available_moves(): #ZOBACZYMY CZY TO DOBRZE JEST
    while game.empty_squares():
        if letter == 'O':
            square = player_o.get_move(game)
        else:
            square = player_x.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                #print('\n')

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!!!')
                return letter #it returns the winner

            #now the opponent
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It is a tie!!!')


if __name__ == '__main__':
    x_player = player.HumanPlayer('X')
    #o_player = player.RandomComputerPlayer('O')
    o_player = player.GeniusComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)







