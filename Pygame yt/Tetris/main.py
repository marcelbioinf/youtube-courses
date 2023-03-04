import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_positions):   #tworzenie grida - pola gry
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]  #10 kolumn x 20 wierszy wg mnie
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]   #locked_positions to słownik który przechowuje (pozycja j, pozycja i) = (c, c, c)
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]  #to zawsze zwraca 0 1 2 lub 3 gdy np jak dla T lista ma długosć 4

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)  #tutaj musze zachowac offset - sprawdz jakie bledy to wywoła!!  #to sprawia ze obiekty jakby spadają a nie pokazują się odrazu w całosci

    return positions


def valid_space(shape, grid):                  #dodaje do accepted_pos tylko czarne - puste miejsca. Nie moge już spadać w zajęte
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]          #spłaszczenie listy z listami z krotkami do listy krotek [[(0, 1)], [(1, 2)]]  --->  [(0, 1), (1,2)] - wygodniejszy format

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True   #to znaczy ze przegraismy gre
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    #surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/3 - (label.get_height()/2)))
    surface.blit(label, (400 - (label.get_width() / 2), 300 + (label.get_height() / 2)))

def draw_grid(surface, grid):  #rysowanie lini na pola gry
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):  #wiersze - 20       #poz poczatku             #poz końca
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i*block_size), (sx + play_width, sy + i*block_size))  #20 horyznotalnych linii
        for j in range(len(grid[i])):  #kolumny - 10
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy), (sx + j*block_size, sy + play_height))  #10 wertykalnych linii



def clear_rows(grid, locked):
    inc = 0                              #jeśli zapełnimy wiersz to trzeba go usunąć
    for i in range(len(grid)-1, -1, -1):  #to bedzie przusuwać się po wierszach od końca od dlugości gridu do -1(0) z krokiem -1
        row = grid[i]                     #to sie wykona 20 razy
        if (0, 0, 0) not in row:           #jeśli w row nie ma koloru czarego to znaczy ze jest pelny
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:                                              #musi być od końća sprawdzany grid
        for key in sorted(list(locked), key = lambda x: x[1])[::-1]:  #lambda sprawia ze sortujemy po wartosći y (wspolrzednej y) o indeksie 1 z klucza słownika który wyglada tak: (19,2) np.
            x, y = key
            if y < ind:   #Jeśli usune wiersz 17 (to jest 17 zapisane w ind - indeksie usunietego wiersza, to musze przesunąc wszystko  co jest powyzej tego 17 w dół)
                newKey = (x, y + inc)  #przesuwam wartość y w dół inc - increment zeby wiedzieć o ile w dół dany row ma być przesunięty
                locked[newKey] = locked.pop(key)  #dla nowego klucza wrzucam ten sam kolor co był w orygianlnym kluczu

    return inc    #czyli liczne usnuietych wierszy


def draw_next_shape(shape, surface):                #rysuje po prawej kolejny kształt jaki wypadnie
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width
    sy = top_left_y + play_height/2

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        for j, column in enumerate(list(line)):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*block_size+60, sy + i*block_size-25, block_size, block_size), 0)

    surface.blit(label, (sx + 50, sy - 70))

def update_score(nscore):
    score = max_score()
    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()
    return score

def draw_window(surface, grid, score=0, last_score = 0):  #rysowanie okna gry a w nim takze grida - pola gry
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
    #current score
    font = pygame.font.SysFont('comicsans', 25)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))
    sx = top_left_x + play_width
    sy = top_left_y + play_height / 2
    surface.blit(label, (sx + 75, sy + 100))
    #last score
    label = font.render('High Score: ' + str(last_score), 1, (255, 255, 255))
    sx = top_left_x - 300
    sy = top_left_y + 200
    surface.blit(label, (sx + 75, sy + 100))

    for i in range(len(grid)):  #20 wierszy
        for j in range(len(grid[i])):  #10 kolumn
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)  #powierzchnia, kolor z grida, (pozycja, pozycja, rozmiar, rozmiar)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)  #playing area
    draw_grid(surface, grid)
    #pygame.display.update()


def main(win):
    last_score = max_score()
    locked_positions = dict()
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)  #grid trzeba non stop updateowac w trakcie gry bo dochododzą nowe klocki
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:    #co 5 sekund bedzie zwiekszana szybkosc spadania
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time/1000 > fall_speed:  #jesli czas działania gry jest wiekszy od ustalonej szybkosci zpadania to wtedy przesun klocka w dół
            fall_time = 0
            current_piece.y += 1   #przesuń piece o 1 w dół
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:   #jesli i nie valid space i nie jestem też na szczycie ekranu
                current_piece.y -= 1   #ruszam sie w zła pozycję wiec spowrotem idz o 1 do góry  #czyli np udzeram o dno albo innego klocka wiec ustawiam change piece
                change_piece = True  #sygnal aby generowac nowy piece

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]   #ten zapis pwoduje 2 oddzielne wartosci x i y
            if y > -1:   #SPRAWDZ JAK BEZ TEGO WYGLADA
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])  #ten zapis pwoduje jedna krotke p
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, 'YOU LOST!', 80, (98, 185, 39))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            update_score(score)


def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle(win, 'Press any key to play', 30,  (122, 65, 199))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


window = pygame.display.set_mode((s_width, s_height))  #utworzenie okna gry
pygame.display.set_caption('Tetris')
main_menu(window)  # start game