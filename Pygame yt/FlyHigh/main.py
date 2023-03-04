import pygame
import random
import math
from pygame import mixer
import time

pygame.init()  # initialization
screen = pygame.display.set_mode((800, 600))  # screen creating

pygame.display.set_caption("Fly High")  # setting tittle
icon = pygame.image.load('planet.png')  # setting icon
pygame.display.set_icon(icon)

background = pygame.image.load('background.jpg')  # background

mixer.music.load('background.wav')
mixer.music.play(-1)

playerImage = pygame.image.load('space.png')  # Player
pX = 368  # 800 - 64 which is image size
pY = 450  # 600 - 64
pX_change = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 22)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 35)

def display_score(x, y):
    score = font.render("score: " + str(score_value), True, (212, 38, 113))
    screen.blit(score, (x, y))

def game_over():
    over_text = over_font.render("GAME OVER", True, (212, 38, 113))
    screen.blit(over_text, (300, 265))
    mixer.music.fadeout(1)
    time.sleep(1)

enemyImage_list, eX_list, eY_list, eX_change_list, eY_change_list = [], [], [], [], []   #Enemy
enemies_num = 6
for e in range(enemies_num):
    enemyImage_list.append(pygame.image.load('alien.png'))
    eX_list.append(random.randint(32, 768))
    eY_list.append(random.randint(32, 150))
    eX_change_list.append(0.35)
    eY_change_list.append(40)

bulletImage = pygame.image.load('bullet.png')  # Bullet
bX = 0
bY = 450
bY_change = 0.77
bullet_state = 'ready'


def fire_bullet(x, y):  # firing/drawing the bullet
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImage, (x + 16, y + 10))


def enemy(x, y, i):  # drawing enemy
    screen.blit(enemyImage_list[i], (x, y))


def player(x, y):  # drawing the player
    screen.blit(playerImage, (x, y))


def is_collision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if distance < 27:
        return True
    else:
        return False


running_game = True  # Game loop
while running_game:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

        if event.type == pygame.KEYDOWN:               #player movement
            if event.key == pygame.K_LEFT:
                pX_change = -0.3
            if event.key == pygame.K_RIGHT:
                pX_change = 0.3
            if event.key == pygame.K_SPACE:
                mixer.Sound('laser.wav').play()
                if bullet_state == 'ready':
                    bX = pX
                    fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0

    pX += pX_change
    if pX < 0:
        pX = 0
    elif pX > 736:
        pX = 736

    for i in range(enemies_num):                          #enemies movement
        if eY_list[i] > 435:
            for i in range(enemies_num):
                eY_list[i] = 2000
            game_over()
            break
        eX_list[i] += eX_change_list[i]
        if eX_list[i] < 0:
            eX_change_list[i] = 0.35
            eY_list[i] += eY_change_list[i]
        elif eX_list[i] > 768:
            eX_change_list[i] = -0.35
            eY_list[i] += eY_change_list[i]
        if is_collision(eX_list[i], eY_list[i], bX, bY):
            mixer.Sound('explosion.wav').play()
            bY = 480
            bullet_state = 'ready'
            score_value += 1
            eX_list[i] = random.randint(32, 768)
            eY_list[i] = random.randint(32, 150)
        enemy(eX_list[i], eY_list[i], i)

    if bY <= 0:                                #bulet movement
        bY = 450
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bX, bY)
        bY -= bY_change

    player(pX, pY)
    display_score(textX, textY)
    pygame.display.update()
