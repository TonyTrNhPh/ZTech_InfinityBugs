import pygame
import random
import player as p

pygame.init()

#game screen window size and color
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
backround = "white"
size = 300
rows = 3

#game title
pygame.display.set_caption("INFINITY BUGS")
#game font
font = pygame.font.SysFont("arialblack",40)
TEXT_COL = (255,255,255)

#game element
player_1 = p.Player(200, 500);
player_2 = p.Player(800, 100);
run = True

while run:
    # background color
    screen.fill(backround)
    # player
    player_1.draw(screen)
    player_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            player_1.move(event.key)

    pygame.display.update()
pygame.quit()
