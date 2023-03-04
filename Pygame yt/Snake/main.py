import pygame
import random
import tkinter as tk
from tkinter import messagebox

class cube:
    rows = 20
    width = 500

    def __init__(self, start, dx=1, dy=0, color=(0, 255, 0)):
        self.position = start
        self.dx = dx
        self.dy = dy
        self.color = color

    def draw(self, window, eyes=False):
        distance = self.width // self.rows
        i = self.position[0]
        j = self.position[1]
        pygame.draw.rect(window, self.color, (i*distance+1, j*distance+1, distance-2, distance-2))
        if eyes:
            centre = distance // 2
            radius = 3
            circleMiddle = (i * distance + centre - radius, j * distance + 8)
            circleMiddle2 = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(window, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(window, (0, 0, 0), circleMiddle2, radius)


    def move(self, dirX, dirY):
        self.dx = dirX
        self.dy = dirY
        self.position = (self.position[0] + self.dx, self.position[1] + self.dy)



class snake:
    def __init__(self, color, position):
        self.cubes = []   #list storing the cubes of snake
        self.turns = {}   #dictionary storing the position of turns
        self.color = color
        self.head = cube(position)
        self.cubes.append(self.head)
        self.direction_x = 0
        self.direction_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running_game
                running_game = False
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:      #everytime we hit the key the head turns, position of this turn needs to be stored so
                    self.direction_x = -1    #the rest of the cubes (cubes) turns at the same exact position
                    self.direction_y = 0
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y] #[:] kopiuje tablice
                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
                elif keys[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]
                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

        for i, cube in enumerate(self.cubes):
            p = cube.position[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if i == len(self.cubes) - 1:       #once last cube (tail) hits the turn we have to remove it from truns dict
                    self.turns.pop(p)
            else:                                  #the snake is moving constantly so if it hits the border it has to get out of the other part of the screen
                if cube.dx == -1 and cube.position[0] <= 0:
                    cube.position = (cube.rows - 1, cube.position[1])
                elif cube.dx == 1 and cube.position[0] >= cube.rows - 1:
                    cube.position = (0, cube.position[1])
                elif cube.dy == 1 and cube.position[1] >= cube.rows - 1:
                    cube.position = (cube.position[0], 0)
                elif cube.dy == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], cube.rows - 1)
                else:
                    cube.move(cube.dx, cube.dy)

    def reset(self, position):
        self.head = cube(position)
        self.cubes = []
        self.cubes.append(self.head)
        self.turns = {}
        self.direction_x = 0
        self.direction_y = 1

    def add_cube(self):
        tail = self.cubes[-1]
        dx, dy = tail.dx, tail.dy

        if dx == 1 and dy == 0:  #if we go right we have to add cube at the tail - 1 square and in the same row etc.
            self.cubes.append(cube((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.cubes.append(cube((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.cubes.append(cube((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.cubes.append(cube((tail.position[0], tail.position[1] + 1)))

        self.cubes[-1].dx = dx  #this tells in which direction the newly insterted cube (last one) has to go
        self.cubes[-1].dy = dy


    def draw(self, window):
        for i, cube in enumerate(self.cubes):
            if i == 0:
                cube.draw(window, True)
            else:
                cube.draw(window)



def DrawGrid(width, rows, window):
    between_lines = width // rows
    x, y = 0, 0
    for line in range(rows):
        x = x + between_lines
        y = y + between_lines                     #which means start at (25,0) end at (25, max(y))
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width)) #this draws in vertical manner
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y)) #this draws in horizontal manner



def redrawWindow(window, s, apple):
    global rows, witdh
    window.fill((0, 0, 0))
    apple.draw(window)
    s.draw(window)
    DrawGrid(width, rows, window)
    pygame.display.update()



def random_snak(rows, snake):
    positions = snake.cubes
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:  #it checks wether our random snak isnt spawned in the snakes boyd area
            continue
        else:
            break
    return(x, y)



def message(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass



def main():
    global rows, width, running_game
    rows = 20
    width = 500

    screen = pygame.display.set_mode((500, 500)) #creating the surface
    clock = pygame.time.Clock()                  #for time operating

    s = snake((0, 255, 0), (10, 10))
    snack = cube(random_snak(rows, s), color=(255, 0, 0))

    running_game = True
    while running_game:
        pygame.time.delay(60)
        clock.tick(10)
        s.move()
        if s.cubes[0].position == snack.position:
            s.add_cube()
            snack = cube(random_snak(rows, s), color=(255, 0, 0))
        for x in range(len(s.cubes)):
            if s.cubes[x].position in list(map(lambda z: z.position, s.cubes[x+1:])):  #checking the collision
                print(f"Score {len(s.cubes)}!")
                message('you lost', 'play again')
                s.reset((10, 10))
                break
        redrawWindow(screen, s, snack)                  #main fucntion drawing the surface/screen
    pass

main()