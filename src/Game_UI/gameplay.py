import pygame
import random

pygame.init()

#game screen window size and color
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
backround = "black"
#game title
pygame.display.set_caption("INFINITY BUGS")
#game font
font = pygame.font.SysFont("arialblack",40)
TEXT_COL = (255,255,255)

run = True
while run:
    #background color
    screen.fill(backround)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
