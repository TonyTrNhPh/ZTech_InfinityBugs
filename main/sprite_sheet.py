import pygame
import json

class Sprite:
    def __init__(self,filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename)
        self.meta_date = self.filename.replace('png','json')
        with open(self.meta_date) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x,y,w,h = sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image = self.get_sprite(x,y,w,h)
        return image