import pygame
from button import  Button as bt
from player import Player as pl
from enemy_combat import enemy_scenario as es
from enemy_combat import enemy_counter_scenario as ecs
pygame.init()

#Define screen and caption
screen_size=(1280,900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Test Button")

#Define color
WHITE = (255,255,255)
BLACK = (0,0,0)
player_1 = pl(100,500,100)
player_2 = pl(800,100,100)

#Define buttons
buttons = []
for i in range(3):
    for j in range(3):
        buttons.append(bt(100 * j + 100, 100 * i + 100, BLACK, str(3 * i + j + 1)))



#Define game elements
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    player_1.draw(screen)
    player_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player_1.handle_event(event.key)
            if event.key == pygame.K_SPACE:
                player_2.array_handle(es)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
