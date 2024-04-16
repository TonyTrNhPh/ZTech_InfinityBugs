import pygame
import random
from health_bar import HealthBar
from os.path import isfile, join
from os import listdir
from button import Button
from sprite_sheet import Sprite
from time import sleep
from mouse_track import MouseTrackerApp
from player import Player
from enemy import Enemy


pygame.init()
pygame.display.set_caption("Infinity Bugs")

# Variables
BG_GAMEPLAY_IMG = pygame.image.load('assets/background/grid.png')
BUTTON_PAUSE_IMG = pygame.image.load('assets/component/pause_button.png')
BUTTON_BACK_IMG = pygame.image.load('assets/component/back_button.png')
BUTTON_QUIT_IMG = pygame.image.load('assets/component/quit_button.png')
BUTTON_MODE_IMG = pygame.image.load('assets/component/mode_button.png')
PLAYER_HEALTH_BAR_IMG = pygame.image.load("assets/component/health_bar.png")
ENEMY_HEALTH_BAR_IMG = pygame.image.load("assets/component/health_bar_2.png")

time_per_frame = 0.08
text_font = pygame.font.Font('assets/font/Retro Gaming.ttf', 48)


class Play:

    def __init__(self, display, gameStateManager):
        # self.index = 0
        self.display = display
        self.gameStateManager = gameStateManager
        self.paused = False
        self.pause_button = Button(64 * 18, 30, BUTTON_PAUSE_IMG, 1)
        self.back_button = Button(64 * 8.5, 64 * 4, BUTTON_BACK_IMG, 0.8)
        self.mode_button = Button(64 * 8.5, 64 * 6, BUTTON_MODE_IMG, 0.8)
        self.quit_button = Button(64 * 8.5, 64 * 8, BUTTON_QUIT_IMG, 0.8)
        self.player_health = HealthBar(40, 30, 560, 36, 100, None)
        self.enemy_health = HealthBar(700, 700, 560, 36, 100, None)
        self.player = Player(0, 100, self.display)
        self.enemy = Enemy(700, 100, self.display)

    def run(self):
        self.display.blit(BG_GAMEPLAY_IMG, (0, 0))
        if self.paused:
            self.pause_overlay()
        else:
            self.pause_button.draw(self.display)
            self.player.draw()
            self.enemy.draw()
            if self.enemy_health.hp != 0:
                self.enemy_health.draw_enemy(self.display)
            if self.player_health.hp != 0:
                self.player_health.draw(self.display)
            else:
                overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
                overlay.fill((255, 255, 255, 128))
                self.display.blit(overlay, (0, 0))
                self.text_display('GAME OVER', 'red', 512, 320)
        pygame.display.flip()

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
        # self.back_button.draw(self.display)
        # self.mode_button.draw(self.display)
        # self.quit_button.draw(self.display)

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

    def generate_random_number(self):
        rand_num = random.randint(1, 10)
        while rand_num == 5:
            rand_num = random.randint(1, 10)
        return rand_num

    def handel_scenario(self):
        movement = {
            1: self.enemy_left_down_attack,
            2: self.enemy_down_attack,
            3: self.enemy_right_down_attack,
            4: self.enemy_left_attack,
            6: self.enemy_right_attack,
            7: self.enemy_left_up_attack,
            8: self.enemy_up_attack,
            9: self.enemy_right_up_attack,
        }
        movement[self.generate_random_number()]()

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
        self.player.being_hit()

    def block_attack(self):
        self.player.block_attack()

    def up_attack(self):
        self.player.up_attack()
        self.enemy_health.hp -= 10
        self.enemy_being_hit()

    def down_attack(self):
        self.player.down_attack()

    def left_attack(self):
        self.player.left_attack()

    def right_attack(self):
        self.player.right_attack()

    def left_down_attack(self):
        self.player.left_down_attack()

    def right_down_attack(self):
        self.player.right_down_attack()

    def left_up_attack(self):
        self.player.left_up_attack()

    def right_up_attack(self):
        self.player.right_up_attack()

    def enemy_being_hit(self):
        self.enemy.being_hit()

    def enemy_block_attack(self):
        self.enemy.block_attack()

    def enemy_up_attack(self):
        self.enemy.up_attack()

    def enemy_down_attack(self):
        self.enemy.down_attack()

    def enemy_left_attack(self):
        self.enemy.left_attack()

    def enemy_right_attack(self):
        self.enemy.right_attack()

    def enemy_left_down_attack(self):
        self.enemy.left_down_attack()

    def enemy_right_down_attack(self):
        self.enemy.right_down_attack()

    def enemy_left_up_attack(self):
        self.enemy.left_up_attack()

    def enemy_right_up_attack(self):
        self.enemy.right_up_attack()


