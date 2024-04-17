import pygame
from os.path import join


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def isClicked(self):
        action = False
        if self.visible:
            pos = pygame.mouse.get_pos()
            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            else:
                self.clicked = False
            return action
        else:
            return action

    def unClicked(self, surface):
        self.visible = not self.visible

    def toggle_visible(self):
        self.visible = not  self.visible
