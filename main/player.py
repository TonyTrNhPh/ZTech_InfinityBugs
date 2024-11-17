import pygame
import threading
from sprite_sheet import Sprite
from time import sleep

# IMAGES PATH // do not erase
idle_sheet = Sprite('assets/character/Idle.png')
being_hit_sheet = Sprite('assets/character/Being_Hit.png')
block_sheet = Sprite('assets/character/Block.png')
up_sheet = Sprite('assets/character/Upper_Attack.png')
down_sheet = Sprite('assets/character/Down_Attack.png')
left_sheet = Sprite('assets/character/Left_Attack.png')
left_up_sheet = Sprite('assets/character/Upper_Left_Attack.png')
left_down_sheet = Sprite('assets/character/Down_Left_Attack.png')
right_sheet = Sprite('assets/character/Right_Attack.png')
right_up_sheet = Sprite('assets/character/Upper_Right_Attack.png')
right_down_sheet = Sprite('assets/character/Down_Right_Attack.png')
BG_GAMEPLAY_IMG = pygame.image.load('assets/background/reset.png')

# ANIMATION LIST // do not erase
idle_animation = [idle_sheet.parse_sprite('Idle_Sheet.png')]

being_hit_animation = [being_hit_sheet.parse_sprite('Being_Hit 0.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 1.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 2.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 3.ase'),
                       #    being_hit_sheet.parse_sprite('Being_Hit 4.ase')]
                       being_hit_sheet.parse_sprite('Being_Hit 3.ase')]

block_animation = [block_sheet.parse_sprite('Block 0.ase'),
                   block_sheet.parse_sprite('Block 1.ase'),
                   block_sheet.parse_sprite('Block 2.ase'),
                   block_sheet.parse_sprite('Block 3.ase'),
                   block_sheet.parse_sprite('Block 4.ase')]

up_attack_animation = [up_sheet.parse_sprite('Upper_Attack 0.ase'),
                       up_sheet.parse_sprite('Upper_Attack 1.ase'),
                       up_sheet.parse_sprite('Upper_Attack 2.ase'),
                       up_sheet.parse_sprite('Upper_Attack 3.ase'),
                       up_sheet.parse_sprite('Upper_Attack 4.ase')]

down_attack_animation = [down_sheet.parse_sprite('Down_Attack 0.ase'),
                         down_sheet.parse_sprite('Down_Attack 1.ase'),
                         down_sheet.parse_sprite('Down_Attack 2.ase'),
                         down_sheet.parse_sprite('Down_Attack 3.ase'),
                         down_sheet.parse_sprite('Down_Attack 4.ase')]

left_attack_animation = [left_sheet.parse_sprite('Left_Attack 0.ase'),
                         left_sheet.parse_sprite('Left_Attack 1.ase'),
                         left_sheet.parse_sprite('Left_Attack 2.ase'),
                         left_sheet.parse_sprite('Left_Attack 3.ase'),
                         left_sheet.parse_sprite('Left_Attack 4.ase')]

left_up_attack_animation = [left_up_sheet.parse_sprite('Upper_Left_Attack 0.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 1.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 2.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 3.ase'),
                            left_up_sheet.parse_sprite('Upper_Left_Attack 4.ase')]

left_down_attack_animation = [left_down_sheet.parse_sprite('Down_Left_Attack 0.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 1.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 2.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 3.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 4.ase')]

right_attack_animation = [right_sheet.parse_sprite('Right_Attack 0.ase'),
                          right_sheet.parse_sprite('Right_Attack 1.ase'),
                          right_sheet.parse_sprite('Right_Attack 2.ase'),
                          right_sheet.parse_sprite('Right_Attack 3.ase'),
                          right_sheet.parse_sprite('Right_Attack 4.ase')]

right_up_attack_animation = [right_up_sheet.parse_sprite('Upper_Right_Attack 0.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 1.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 2.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 3.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 4.ase')]

right_down_attack_animation = [right_down_sheet.parse_sprite('Down_Right_Attack 0.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 1.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 2.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 3.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 4.ase')]

time_per_frame = 0.08


class Player:
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y, 700, 700))
        self.display = display
        # Create a surface with an alpha channel
        self.mask = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.mask.set_alpha(0)
        self.font = pygame.font.Font('assets/font/Retro Gaming.ttf', 48)

    def draw(self):
        self.display.blit(idle_animation[0], (self.x, self.y))

    def update_each_frame(self):
        self.display.blit(BG_GAMEPLAY_IMG, self.rect.topleft)

    def being_hit(self):
        for index in range(0, len(being_hit_animation)):
            self.update_each_frame()
            self.is_hit()
            self.display.blit(being_hit_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def block_attack(self):
        for index in range(0, len(block_animation)):
            self.update_each_frame()
            self.is_block()
            self.display.blit(block_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def up_attack(self):
        for index in range(0, len(up_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(up_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def down_attack(self):
        for index in range(0, len(down_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(down_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_attack(self):
        for index in range(0, len(left_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(left_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_attack(self):
        for index in range(0, len(right_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(right_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_down_attack(self):
        for index in range(0, len(left_down_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(left_down_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_down_attack(self):
        for index in range(0, len(right_down_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(right_down_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_up_attack(self):
        for index in range(0, len(left_up_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit(left_up_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_up_attack(self):
        for index in range(0, len(right_up_attack_animation)):
            self.update_each_frame()
            self.is_parry()
            self.display.blit( right_up_attack_animation[index], (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def is_parry(self):
        self.text_display('PARRY', '#3574a4', 100, 150)

    def is_block(self):
        self.text_display('BLOCK', '#ffe361', 100, 150)

    def is_hit(self):
        self.text_display('HIT', 'red', 100, 150)

    def text_display(self, text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.display.blit(img, (x, y))
