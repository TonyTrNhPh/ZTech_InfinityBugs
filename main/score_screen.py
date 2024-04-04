import pygame
from os.path import isfile, join
from os import listdir
from button import Button

# Variables
BG_SCOREMENU_IMG = pygame.image.load(join("assets", "background", "score_screen.png"))
BUTTON_START_IMG = pygame.image.load(join("assets", "component", "start_button.png"))
BUTTON_QUIT_IMG = pygame.image.load(join("assets", "component", "quit_button.png"))


class Score:
    def __init__(self, display, gameStateManager):
        self.start_button = Button(64 * 11, 64 * 11, BUTTON_START_IMG, 0.8)
        self.quit_button = Button(64 * 16, 64 * 11, BUTTON_QUIT_IMG, 0.8)
        self.display = display
        self.gameStateManager = gameStateManager
        self.save = False

    def run(self):
        self.display.blit(BG_SCOREMENU_IMG, (0, 0))
        if self.save:
            self.save_overlay()
        else:
            self.start_button.draw(self.display)
            self.quit_button.draw(self.display)
        pygame.display.flip()

    def toggle_save(self):
        self.save = not self.save

    def save_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
