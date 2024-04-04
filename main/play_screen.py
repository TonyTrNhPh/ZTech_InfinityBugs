import pygame
from os.path import isfile, join
from os import listdir
from button import Button

pygame.init()
pygame.display.set_caption("Infinity Bugs")

# Variables
BG_GAMEPLAY_IMG = pygame.image.load(join("assets", "background", "grid.png"))
BUTTON_PAUSE_IMG = pygame.image.load(join("assets", "component", "pause_button.png"))
BUTTON_BACK_IMG = pygame.image.load(join("assets", "component", "back_button.png"))
BUTTON_QUIT_IMG = pygame.image.load(join("assets", "component", "quit_button.png"))
BUTTON_MODE_IMG = pygame.image.load(join("assets", "component", "mode_button.png"))




class Play:
    def __init__(self,display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.paused = False
        self.pause_button = Button(64 * 18, 40, BUTTON_PAUSE_IMG, 1)
        self.back_button = Button(64 * 8.5, 64 * 4, BUTTON_BACK_IMG, 0.8)
        self.mode_button = Button(64 * 8.5, 64 * 6, BUTTON_MODE_IMG, 0.8)
        self.quit_button = Button(64 * 8.5, 64 * 8, BUTTON_QUIT_IMG, 0.8)

    def run(self):
        self.display.blit(BG_GAMEPLAY_IMG, (0, 0))
        if self.paused:
            self.pause_overlay()
        else:
            self.pause_button.draw(self.display)
        pygame.display.flip()

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
        self.back_button.draw(self.display)
        self.mode_button.draw(self.display)
        self.quit_button.draw(self.display)












