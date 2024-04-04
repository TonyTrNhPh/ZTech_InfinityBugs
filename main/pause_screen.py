import pygame
from os import listdir
from os.path import isfile, join
from button import Button

class Pause:
    def __init__(self,display,gameStateManager):
        self.display =display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill()