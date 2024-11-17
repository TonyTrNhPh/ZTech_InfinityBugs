import pygame
import threading
from sprite_sheet import Sprite
from time import sleep
import random
# IMAGES PATH // do not erase
idle_sheet = Sprite('main/assets/enemy/Idle_pose.png')
being_hit_sheet = Sprite('main/assets/enemy/Being_Hit.png')
being_stun_sheet = Sprite('main/assets/enemy/Stun_pose.png')
block_sheet = Sprite('main/assets/enemy/Block.png')
up_sheet = Sprite('main/assets/enemy/Upper_Attack.png')
down_sheet = Sprite('main/assets/enemy/Down_Attack.png')
left_sheet = Sprite('main/assets/enemy/Left_Attack.png')
left_up_sheet = Sprite('main/assets/enemy/Upper_Left_Attack.png')
left_down_sheet = Sprite('main/assets/enemy/Down_Left_Attack.png')
right_sheet = Sprite('main/assets/enemy/Right_Attack.png')
right_up_sheet = Sprite('main/assets/enemy/Upper_Right_Attack.png')
right_down_sheet = Sprite('main/assets/enemy/Down_Right_Attack.png')
BG_GAMEPLAY_IMG = pygame.image.load('main/assets/background/reset2.png')

# ANIMATION LIST // do not erase
idle_animation = [idle_sheet.parse_sprite('Idle_pose.ase')]

being_stun_animation = [being_stun_sheet.parse_sprite('stun_pose.ase')]

being_hit_animation = [being_hit_sheet.parse_sprite('Being_Hit 0.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 1.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 2.ase'),
                       being_hit_sheet.parse_sprite('Being_Hit 3.ase'),
                       #    being_hit_sheet.parse_sprite('Being_Hit 4.ase')]
                       being_hit_sheet.parse_sprite('Being_Hit 3.ase')]


block_animation = [block_sheet.parse_sprite('Block 1.ase'),
                   block_sheet.parse_sprite('Block 2.ase'),
                   block_sheet.parse_sprite('Block 3.ase'),
                   block_sheet.parse_sprite('Block 4.ase'),
                   block_sheet.parse_sprite('Block 0.ase')]

up_attack_animation = [up_sheet.parse_sprite('Upper_Attack 0.ase'),
                       up_sheet.parse_sprite('Upper_Attack 1.ase'), up_sheet.parse_sprite('Upper_Attack 1.ase'), up_sheet.parse_sprite(
                           'Upper_Attack 1.ase'), up_sheet.parse_sprite('Upper_Attack 1.ase'),
                       up_sheet.parse_sprite('Upper_Attack 2.ase'),
                       up_sheet.parse_sprite('Upper_Attack 3.ase'),
                       up_sheet.parse_sprite('Upper_Attack 4.ase'),
                       up_sheet.parse_sprite('Upper_Attack 0.ase')]

down_attack_animation = [down_sheet.parse_sprite('Down_Attack 0.ase'),
                         down_sheet.parse_sprite('Down_Attack 1.ase'), down_sheet.parse_sprite(
                             'Down_Attack 1.ase'), down_sheet.parse_sprite('Down_Attack 1.ase'), down_sheet.parse_sprite('Down_Attack 1.ase'),
                         down_sheet.parse_sprite('Down_Attack 2.ase'),
                         down_sheet.parse_sprite('Down_Attack 3.ase'),
                         down_sheet.parse_sprite('Down_Attack 4.ase'),
                         down_sheet.parse_sprite('Down_Attack 0.ase')]

left_attack_animation = [left_sheet.parse_sprite('Left_Attack 0.ase'),
                         left_sheet.parse_sprite('Left_Attack 1.ase'), left_sheet.parse_sprite(
                             'Left_Attack 1.ase'), left_sheet.parse_sprite('Left_Attack 1.ase'), left_sheet.parse_sprite('Left_Attack 1.ase'),
                         left_sheet.parse_sprite('Left_Attack 2.ase'),
                         left_sheet.parse_sprite('Left_Attack 3.ase'),
                         left_sheet.parse_sprite('Left_Attack 4.ase'),
                         left_sheet.parse_sprite('Left_Attack 0.ase')]

left_up_attack_animation = [left_up_sheet.parse_sprite('Upper_Left_Attack 0.ase'),
                            left_up_sheet.parse_sprite('Upper_Left_Attack 1.ase'), left_up_sheet.parse_sprite('Upper_Left_Attack 1.ase'), left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 1.ase'), left_up_sheet.parse_sprite('Upper_Left_Attack 1.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 2.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 3.ase'),
                            left_up_sheet.parse_sprite(
                                'Upper_Left_Attack 4.ase'),
                            idle_sheet.parse_sprite('Idle_pose.ase')]

left_down_attack_animation = [left_down_sheet.parse_sprite('Down_Left_Attack 0.ase'),
                              left_down_sheet.parse_sprite('Down_Left_Attack 1.ase'), left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 1.ase'), left_down_sheet.parse_sprite('Down_Left_Attack 1.ase'), left_down_sheet.parse_sprite('Down_Left_Attack 1.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 2.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 3.ase'),
                              left_down_sheet.parse_sprite(
                                  'Down_Left_Attack 4.ase'),
                              idle_sheet.parse_sprite('Idle_pose.ase')]

right_attack_animation = [right_sheet.parse_sprite('Right_Attack 0.ase'),
                          right_sheet.parse_sprite('Right_Attack 1.ase'), right_sheet.parse_sprite(
                              'Right_Attack 1.ase'), right_sheet.parse_sprite('Right_Attack 1.ase'), right_sheet.parse_sprite('Right_Attack 1.ase'),
                          right_sheet.parse_sprite('Right_Attack 2.ase'),
                          right_sheet.parse_sprite('Right_Attack 3.ase'),
                          right_sheet.parse_sprite('Right_Attack 4.ase'),
                          right_sheet.parse_sprite('Right_Attack 0.ase')]

right_up_attack_animation = [right_up_sheet.parse_sprite('Upper_Right_Attack 0.ase'),
                             right_up_sheet.parse_sprite('Upper_Right_Attack 1.ase'), right_up_sheet.parse_sprite('Upper_Right_Attack 1.ase'), right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 1.ase'), right_up_sheet.parse_sprite('Upper_Right_Attack 1.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 2.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 3.ase'),
                             right_up_sheet.parse_sprite(
                                 'Upper_Right_Attack 4.ase'),
                             idle_sheet.parse_sprite('Idle_pose.ase')]

right_down_attack_animation = [right_down_sheet.parse_sprite('Down_Right_Attack 0.ase'),
                               right_down_sheet.parse_sprite('Down_Right_Attack 1.ase'), right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 1.ase'), right_down_sheet.parse_sprite('Down_Right_Attack 1.ase'), right_down_sheet.parse_sprite('Down_Right_Attack 1.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 2.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 3.ase'),
                               right_down_sheet.parse_sprite(
                                   'Down_Right_Attack 4.ase'),
                               idle_sheet.parse_sprite('Idle_pose.ase')]

time_per_frame = 0.08


class Enemy:
    def __init__(self, x, y, display, scale=0.7):
        self.x = x
        self.y = y
        self.scale = scale
        self.rect = pygame.Rect((x, y, 600, 600))
        self.display = display
        # Create a surface with an alpha channel
        self.mask = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.mask.set_alpha(0)
        self.font = pygame.font.Font('main/assets/font/Retro Gaming.ttf', 48)

    def draw(self):
        self.update_each_frame()
        scaled_animation = pygame.transform.scale(idle_animation[0], (int(idle_animation[0].get_width() * self.scale),
                                                                      int(idle_animation[0].get_height() * self.scale)))
        self.display.blit(scaled_animation, (self.x, self.y))

    def draw_block(self):
        scaled_animation = pygame.transform.scale(block_animation[3], (int(block_animation[3].get_width() * self.scale),
                                                                       int(block_animation[3].get_height() * self.scale)))
        self.display.blit(scaled_animation, (self.x, self.y))

    def update_each_frame(self):
        self.display.blit(BG_GAMEPLAY_IMG, self.rect.topleft)

    def being_stun(self):
        self.update_each_frame()
        scaled_animation = pygame.transform.scale(being_stun_animation[0], (int(being_stun_animation[0].get_width() * self.scale),
                                                                       int(being_stun_animation[0].get_height() * self.scale)))
        self.display.blit(scaled_animation, (self.x, self.y))

    def being_hit(self):
        for index in range(0, len(being_hit_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(being_hit_animation[index],
                                                      (int(being_hit_animation[index].get_width() * self.scale),
                                                       int(being_hit_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

        def animate_hit():
            for index in range(len(being_hit_animation)):
                self.update_each_frame()
                scaled_animation = pygame.transform.scale(being_hit_animation[index],
                                                          (int(being_hit_animation[index].get_width() * self.scale),
                                                           int(being_hit_animation[
                                                               index].get_height() * self.scale)))
                self.display.blit(scaled_animation, (self.x, self.y))
                pygame.display.flip()
                sleep(time_per_frame)  # Use time.sleep() instead of sleep()

        # Create a thread and start it
        # hit_thread = threading.Thread(target=animate_hit)
        # hit_thread.start()

    def block_attack(self):
        for index in range(0, len(block_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(block_animation[index],
                                                      (int(block_animation[index].get_width() * self.scale),
                                                       int(block_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def up_attack(self):
        for index in range(0, len(up_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(up_attack_animation[index],
                                                      (int(up_attack_animation[index].get_width() * self.scale),
                                                       int(up_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def down_attack(self):
        for index in range(0, len(down_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(down_attack_animation[index],
                                                      (int(down_attack_animation[index].get_width() * self.scale),
                                                       int(down_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_attack(self):
        for index in range(0, len(left_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(left_attack_animation[index],
                                                      (int(left_attack_animation[index].get_width() * self.scale),
                                                       int(left_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_attack(self):
        for index in range(0, len(right_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(right_attack_animation[index],
                                                      (int(right_attack_animation[index].get_width() * self.scale),
                                                       int(right_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_down_attack(self):
        for index in range(0, len(left_down_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(left_down_attack_animation[index],
                                                      (int(left_down_attack_animation[index].get_width() * self.scale),
                                                       int(left_down_attack_animation[
                                                           index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_down_attack(self):
        for index in range(0, len(right_down_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(right_down_attack_animation[index],
                                                      (int(right_down_attack_animation[index].get_width() * self.scale),
                                                       int(right_down_attack_animation[
                                                           index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def left_up_attack(self):
        for index in range(0, len(left_up_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(left_up_attack_animation[index],
                                                      (int(left_up_attack_animation[index].get_width() * self.scale),
                                                       int(left_up_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
            pygame.display.flip()
            sleep(time_per_frame)

    def right_up_attack(self):
        for index in range(0, len(right_up_attack_animation)):
            self.update_each_frame()
            scaled_animation = pygame.transform.scale(right_up_attack_animation[index],
                                                      (int(right_up_attack_animation[index].get_width() * self.scale),
                                                       int(right_up_attack_animation[index].get_height() * self.scale)))
            self.display.blit(scaled_animation, (self.x, self.y))
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

    def generate_random_list(self):
        numbers = [num for num in range(1, 10) if num != 5]
        random.shuffle(numbers)
        length = random.randint(2, 6)
        return numbers[:length]

    def generate_random_scenario(self, scenario_number_generate):
        return [self.generate_random_list() for _ in range(scenario_number_generate)]
