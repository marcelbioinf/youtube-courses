import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + ' Your turn. Input move (0-8):')
            try:
                val = int(square) #srobuj przypisac int do square, jeśli square nie jest int to error!
                if val not in game.available_moves():
                    raise ValueError
                #if we pass both conditions:
                valid_square = val
                if val == 0:
                    valid_square = True #to pozwala na wykorzystanie 0
            except ValueError:
                print('Ups! Wrong input. Try again.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position'] #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #square = self.find_best_move(game)
        return square

    def is_winner(self, game):
        # check rows
        for row_index in range(3):
            row = game.board[row_index * 3: (row_index + 1) * 3]
            if all([spot == 'X' for spot in row]) or all([spot == 'O' for spot in row]):
                return True

        # check columns
        for column_index in range(3):
            column = game.board[column_index:column_index + 7:3]
            if all([spot == 'X' for spot in column]) or all([spot == 'O' for spot in column]):
               return True

        # check diagonals
        diagonal_1 = game.board[0:9:4]
        if all([spot == 'X' for spot in diagonal_1]) or all([spot == 'O' for spot in diagonal_1]):
            return True
        diagonal_2 = game.board[2:7:2]
        if all([spot == 'X' for spot in diagonal_2]) or all([spot == 'O' for spot in diagonal_2]):
            return True

        return False

    def find_best_move(self, game):
        best_move_p = -1000
        best_square = None
        for square in game.available_moves():
            game.board[square] = self.letter
            current_move_p = self.minimax(game, 'X' if self.letter == 'O' else 'X')
            if current_move_p > best_move_p:
                best_move_p = current_move_p
                best_square = square
            game.board[square] = ' '
        return best_square


    # def minimax(self, state, player):
    #     current_player = player
    #     max_player = self.letter
    #     min_player = 'O' if self.letter == 'X' else 'X'
    #
    #     if self.is_winner(state):                                  #tu na odwrót bo na koncu przesylam drugiego playera
    #         return 1 * (state.num_empty_squares() + 1) if player == min_player else -1 * (state.num_empty_squares() + 1) #tu byl jebany bug
    #     elif state.num_empty_squares() == 0:  #tie
    #         return 0
    #
    #     if current_player == max_player:
    #         best_value = -1000
    #         for square in state.available_moves():
    #             state.board[square] = max_player
    #             value = self.minimax(state, min_player)
    #             state.board[square] = ' '
    #             best_value = max(best_value, value)
    #         return best_value
    #
    #     else:
    #         best_value = 1000
    #         for square in state.available_moves():
    #             state.board[square] = min_player
    #             value = self.minimax(state, max_player)
    #             state.board[square] = ' '
    #             best_value = min(best_value, value)
    #         return best_value


    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:  #poslugujemy sie rekurencją czyli najpierw base case - czyli co w sytuacji gdy wszystko sie konczy
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for move in state.available_moves():
            #s1 try one move
            state.make_move(move, player)
            #s2 recurse to stimulate the game after that move
            sim_score = self.minimax(state, other_player)
            #s3 undo the move
            state.board[move] = ' '
            state.current_winner = None
            sim_score['position'] = move
            #s4 update the dicts
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best










