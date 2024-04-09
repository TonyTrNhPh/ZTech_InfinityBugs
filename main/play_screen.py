import pygame
from health_bar import HealthyBar
from os.path import isfile, join
from os import listdir
from button import Button
from sprite_sheet import Sprite
from time import sleep

pygame.init()
pygame.display.set_caption("Infinity Bugs")

# Variables
BG_GAMEPLAY_IMG = pygame.image.load(join("assets", "background", "grid.png"))
BUTTON_PAUSE_IMG = pygame.image.load(join("assets", "component", "pause_button.png"))
BUTTON_BACK_IMG = pygame.image.load(join("assets", "component", "back_button.png"))
BUTTON_QUIT_IMG = pygame.image.load(join("assets", "component", "quit_button.png"))
BUTTON_MODE_IMG = pygame.image.load(join("assets", "component", "mode_button.png"))

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

idle_animation = [idle_sheet.parse_sprite('Idle_Sheet.png')]

being_hit_animation = [being_hit_sheet.parse_sprite('Being_Hit 0.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 1.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 2.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 3.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 4.ase')]

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
                            left_up_sheet.parse_sprite('Upper_Left_Attack 1.ase'),
                            left_up_sheet.parse_sprite('Upper_Left_Attack 2.ase'),
                            left_up_sheet.parse_sprite('Upper_Left_Attack 3.ase'),
                            left_up_sheet.parse_sprite('Upper_Left_Attack 4.ase')]

left_down_attack_animation = [left_down_sheet.parse_sprite('Down_Left_Attack 0.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 1.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 2.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 3.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 4.ase')]

right_attack_animation = [right_sheet.parse_sprite('Right_Attack 0.ase'),
                          right_sheet.parse_sprite('Right_Attack 1.ase'),
                          right_sheet.parse_sprite('Right_Attack 2.ase'),
                          right_sheet.parse_sprite('Right_Attack 3.ase'),
                          right_sheet.parse_sprite('Right_Attack 4.ase')]

right_up_attack_animation = [right_up_sheet.parse_sprite('Upper_Right_Attack 0.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 1.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 2.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 3.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 4.ase')]

right_down_attack_animation = [right_down_sheet.parse_sprite('Down_Right_Attack 0.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 1.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 2.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 3.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 4.ase')]

time_per_frame = 0.08
text_font = pygame.font.Font('assets/font/Retro Gaming.ttf', 48)


class Play:

    def __init__(self, display, gameStateManager):
        # self.index = 0
        self.display = display
        self.gameStateManager = gameStateManager
        self.paused = False
        self.pause_button = Button(64 * 18, 40, BUTTON_PAUSE_IMG, 1)
        self.back_button = Button(64 * 8.5, 64 * 4, BUTTON_BACK_IMG, 0.8)
        self.mode_button = Button(64 * 8.5, 64 * 6, BUTTON_MODE_IMG, 0.8)
        self.quit_button = Button(64 * 8.5, 64 * 8, BUTTON_QUIT_IMG, 0.8)
        self.health_bar = HealthyBar(40, 48, 560, 36, 100)

    def handle_event_key(self, key):
        keys = {
            pygame.K_KP1: self.left_down_attack,
            pygame.K_KP2: self.down_attack,
            pygame.K_KP3: self.right_down_attack,
            pygame.K_KP4: self.left_attack,
            pygame.K_KP5: self.block_attack,
            pygame.K_KP6: self.right_attack,
            pygame.K_KP7: self.left_up_attack,
            pygame.K_KP8: self.up_attack,
            pygame.K_KP9: self.right_up_attack,
            pygame.K_SPACE: self.being_hit,
        }
        if key in keys:
            keys[key]()

    def handel_event_mouse(self, direction):
        directions = {
            'UP': self.up_attack,
            'DOWN': self.down_attack,
            'LEFT': self.left_attack,
            'RIGHT': self.right_attack,
            'BLOCK': self.block_attack,
            'LEFT_UP': self.left_up_attack,
            'RIGHT_UP': self.right_up_attack,
            'LEFT_DOWN': self.left_down_attack,
            'RIGHT_DOWN': self.right_down_attack,
        }
        if direction in directions:
            directions[direction]()

    def being_hit(self):
        for index in range(0, len(being_hit_animation)):
            self.blink()
            self.is_hit()
            self.health_bar.hp = self.health_bar.hp - 2
            self.display.blit(being_hit_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def block_attack(self):
        for index in range(0, len(block_animation)):
            self.blink()
            self.is_block()
            self.display.blit(block_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def up_attack(self):
        for index in range(0, len(up_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(up_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def down_attack(self):
        for index in range(0, len(down_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(down_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_attack(self):
        for index in range(0, len(left_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(left_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_attack(self):
        for index in range(0, len(right_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(right_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_down_attack(self):
        for index in range(0, len(left_down_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(left_down_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_down_attack(self):
        for index in range(0, len(right_down_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(right_down_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_up_attack(self):
        for index in range(0, len(left_up_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(left_up_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_up_attack(self):
        for index in range(0, len(right_up_attack_animation)):
            self.blink()
            self.is_parry()
            self.display.blit(right_up_attack_animation[index], (0, 0))
            pygame.display.flip()
            sleep(time_per_frame)

    def run(self):
        self.display.blit(BG_GAMEPLAY_IMG, (0, 0))
        if self.paused:
            self.pause_overlay()
        else:
            self.pause_button.draw(self.display)
            self.display.blit(idle_animation[0], (0, 0))
            if self.health_bar.hp != 0:
                self.health_bar.draw(self.display)
            else:
                overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
                overlay.fill((255, 255, 255, 128))
                self.display.blit(overlay, (0, 0))
                self.text_display('GAME OVER','red',512, 320)
        pygame.display.flip()

    def blink(self):
        self.display.blit(BG_GAMEPLAY_IMG, (0, 0))
        self.pause_button.draw(self.display)

    def is_parry(self):
        self.text_display('PARRY', '#3574a4', 100, 150)

    def is_block(self):
        self.text_display('BLOCK', '#ffe361', 100, 150)

    def is_hit(self):
        self.text_display('HIT', 'red', 100, 150)

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
        self.back_button.draw(self.display)
        self.mode_button.draw(self.display)
        self.quit_button.draw(self.display)

    def text_display(self, text, text_col, x, y):
        img = text_font.render(text, True, text_col)
        self.display.blit(img, (x, y))
