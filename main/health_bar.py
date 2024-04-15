import pygame
from os.path import join


class HealthBar:
    def __init__(self, x, y, w, h, max_hp, img):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, '#3574a4', (self.x + 40, self.y + 16, self.w, self.h))
        pygame.draw.rect(surface, '#ffe361', (self.x + 40, self.y + 16, self.w * ratio, self.h))

    def draw_enemy(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, '#3574a4', (self.x, self.y + 16, self.w, self.h))
        pygame.draw.rect(surface, '#ffe361', (self.x, self.y + 16, self.w * ratio, self.h))
