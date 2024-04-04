import pygame
from os import listdir
from os.path import join, isfile


class Bot(pygame.sprite.Sprite):
    # Example variable
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topright = (x, y)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

    @property
    def upper_slash(self):
        return 8

    @property
    def downward_slash(self):
        return 2

    @property
    def right_slash(self):
        return 4

    @property
    def left_slash(self):
        return 6

    @property
    def upper_left_slash(self):
        return 7

    @property
    def upper_right_slash(self):
        return 9

    @property
    def downward_right_slash(self):
        return 1

    @property
    def downward_left_slash(self):
        return 3

    @property
    def blocking(self):
        return 5

    def death(self):
        pass

    def lose_health(self):
        pass
