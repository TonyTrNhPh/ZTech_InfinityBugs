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
import threading
import time

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
    last_key_press_time = 0
    cooldown = 1.2  # 1.2 seconds
    intro = 3
    last_intro_count = pygame.time.get_ticks()

    def __init__(self, display, gameStateManager):
        self.font = pygame.font.Font('assets/font/Retro Gaming.ttf', 80)
        self.display = display
        self.score = 0
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
        self.game_over = False

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
                self.game_over = True
        pygame.display.flip()

    def game_over_screen(self):
        overlay = pygame.Surface(
            (self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
        self.player.text_display('GAME OVER', 'red', 512, 320)
        pygame.display.flip()

    def game_win_screen(self):
        overlay = pygame.Surface(
            (self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))
        self.player.text_display('YOU WIN', 'green', 512, 320)
        pygame.display.flip()

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_overlay(self):
        overlay = pygame.Surface(
            (self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))  # Semi-transparent white overlay
        self.display.blit(overlay, (0, 0))
        self.back_button.draw(self.display)
        self.mode_button.draw(self.display)
        self.quit_button.draw(self.display)

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

    def attack(self):
        is_stun_finsh = False

        def stun_thread():
            nonlocal is_stun_finsh
            self.enemy.update_each_frame()
            self.enemy.being_stun()
            pygame.display.flip()
            sleep(4)
            self.enemy.update_each_frame()
            self.enemy.draw()
            pygame.display.flip()
            is_stun_finsh = True

        scenarios = self.enemy.generate_random_scenario(100)
        for scenario in scenarios:
            for enemy_attack_key in scenario:
                is_enemy_stun = True
                sleep(0.5)
                if self.enemy_attack(enemy_attack_key):
                    is_enemy_stun = False
                if self.player_health.hp <= 0:
                    return
            if is_enemy_stun:
                is_stun_finsh = False
                enemy_thread = threading.Thread(target=stun_thread)
                enemy_thread.start()
                while not is_stun_finsh:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            current_time = time.time()
                            if current_time - self.last_key_press_time >= self.cooldown:
                                self.last_key_press_time = current_time
                                self.handle_event_key(event.key)
                                pygame.display.flip()
                                if event.key != pygame.K_KP5:
                                    self.score+=10
                                    self.enemy_being_hit()
                                    self.enemy.being_stun()
                                    self.enemy_health.hp -= 10
                                    self.enemy_health.draw_enemy(self.display)
                                    pygame.display.flip()
                                if self.enemy_health.hp <= 0:
                                    return
                enemy_thread.join()

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

    def enemy_attack(self, enemy_attack_key):
        enemy_attack_dict = {
            1: self.enemy_left_down_attack,
            2: self.enemy_down_attack,
            3: self.enemy_right_down_attack,
            4: self.enemy_left_attack,
            6: self.enemy_right_attack,
            7: self.enemy_left_up_attack,
            8: self.enemy_up_attack,
            9: self.enemy_right_up_attack,
        }
        parry_dict = {
            1: pygame.K_KP9,
            2: pygame.K_KP8,
            3: pygame.K_KP7,
            4: pygame.K_KP6,
            6: pygame.K_KP4,
            7: pygame.K_KP3,
            8: pygame.K_KP2,
            9: pygame.K_KP1,
        }

        is_enemy_attack_success = True
        is_enemy_attack_finish = False  # Initialize enemy_attack_flag
        is_press = False  # Initialize is_press

        def enemy_attack_thread():
            nonlocal is_enemy_attack_finish  # Use nonlocal to modify outer variable
            enemy_attack_dict[enemy_attack_key]()
            is_enemy_attack_finish = True  # Signal that the enemy attack has finished

        enemy_thread = threading.Thread(target=enemy_attack_thread)
        enemy_thread.start()
        key_parry = parry_dict[enemy_attack_key]
        while not is_enemy_attack_finish:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and not is_press:
                    is_press = True
                    if event.key == pygame.K_KP5 or event.key == key_parry:
                        is_enemy_attack_success = False
                        self.score+=5
                    self.handle_event_key(event.key)
                    self.player.update_each_frame()
                    self.player.draw()
                    pygame.display.flip()

        enemy_thread.join()
        if is_enemy_attack_success:
            self.player_health.hp -= 10
            self.player_health.draw(self.display)
            self.being_hit()
            self.player.draw()
            pygame.display.flip()

            return True
        return False

    def being_hit(self):
        self.player.being_hit()

    def block_attack(self):
        self.player.block_attack()

    def up_attack(self):
        self.player.up_attack()

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

    def text_display(self, text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.display.blit(img, (x, y))
        pygame.display.flip()
