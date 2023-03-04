import pygame
from network import Network
import time
#uzywając modułu pickle jest o wiele latwiej - mogę wysyłac do serwera i z serwera cale obikety


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.vel = 3  #movement value

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(stri):    #funckja obslugujaca przesylanie pozycji itd
    stri = stri.split(",")
    return int(stri[0]), int(stri[1]) #przyjmuje stringa zwracam krotke

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])  #zwracam stringa

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network() #stworzenie tego obiektu łączy nas z serwerem
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0, 0, 255))
    while run:

        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y)))) #wysyłam do serwera pozycje playera x i serwer mi odsyla jakas pozycje
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)

main()