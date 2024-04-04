# import pygame
# from os import listdir
# from os.path import join, isfile
#
#
# def get_sprite_sheets(dir1, dir2, width, height):
#     path = join("main","","assets", dir1, dir2)
#     images = [f for f in listdir(path) if isfile(join(path, f))]
#
#     all_sprites = {}
#     for img in images:
#         sprite_sheet = pygame.image.load(join(path, img))
#         sprites = []
#         for i in range(sprite_sheet.get_width() // width):
#             surface = pygame.Surface((width, height), pygame.SRCALPHA)
#             rect = pygame.Rect(i * width, 0, width, height)
#             surface.blit(sprite_sheet, (0, 0), rect)
#             sprites.append(surface)
#         all_sprites[img.replace(".png", "")] = sprites
#     return all_sprites
#
#
# class Player(pygame.sprite.Sprite):
#     # Example variable
#     COLOR = (0, 0, 0)
#     SPRITES= get_sprite_sheets("character","Left Up",700,700)
#     print(SPRITES)
#     def __init__(self, x, y, width, height):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.rect.topright = (x, y)
#
#     def draw(self, win):
#         # pygame.draw.rect(win, self.COLOR, self.rect)
#         self.sprite = self.SPRITES["Upper_Left_Attack"][0]
#         win.blit(self.sprite,(self.rect.x,self.rect.y))
#     @property
#     def upper_slash(self):
#         return 8
#
#     @property
#     def downward_slash(self):
#         return 2
#
#     @property
#     def right_slash(self):
#         return 4
#
#     @property
#     def left_slash(self):
#         return 6
#
#     @property
#     def upper_left_slash(self):
#         return 7
#
#     @property
#     def upper_right_slash(self):
#         return 9
#
#     @property
#     def downward_right_slash(self):
#         return 1
#
#     @property
#     def downward_left_slash(self):
#         return 3
#
#     @property
#     def blocking(self):
#         return 5
#
#     def death(self):
#         pass
#
#     def lose_health(self):
#         pass
