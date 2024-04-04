import pygame
from os.path import isfile, join
from os import listdir
from button import Button

# Variables
BG_STARTMENU_IMG = pygame.image.load(join("assets", "background", "menu_screen.png"))
BUTTON_START_IMG = pygame.image.load(join("assets", "component", "start_button.png"))
BUTTON_QUIT_IMG = pygame.image.load(join("assets", "component", "quit_button.png"))


class Start:
    def __init__(self, display, gameStateManager):
        self.start_button = Button(64 * 8.5, 64 * 6, BUTTON_START_IMG, 0.8)
        self.quit_button = Button(64 * 8.5, 64 * 8, BUTTON_QUIT_IMG, 0.8)
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.blit(BG_STARTMENU_IMG, (0, 0))
        self.start_button.draw(self.display)
        self.quit_button.draw(self.display)
        pygame.display.flip()
