from time import sleep

import pygame
import play_screen as pl
from play_screen import Play
from start_screen import Start
from score_screen import Score
from os.path import isfile, join
from os import listdir
from game_state_manager import GameStateManager
from button import Button

pygame.init()
pygame.display.set_caption("Infinity Bugs")

# Variables
FPS = 60
BG_COLOR = (240, 244, 251)
WIDTH, HEIGHT = 1280, 800


class onScreen:
    last_attack = 0
    time_now = 0
    cool_down = 600
    delay_tracking = 200

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.play = Play(self.screen, self.gameStateManager)
        self.score = Score(self.screen, self.gameStateManager)
        self.states = {'start': self.start,
                       'play': self.play,
                       'score': self.score}
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.time_now = pygame.time.get_ticks()
                # Click X on window to quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                # Separate the screen 
                if self.gameStateManager.get_state() == 'start':
                    # Click Quit button to quit the game
                    if self.start.quit_button.isClicked():
                        self.running = False
                        break
                    # Click Start button to play the game
                    if self.start.start_button.isClicked():
                        self.gameStateManager.set_state('play')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('Clicked')
                elif self.gameStateManager.get_state() == 'play':
                    # Click Pause button to pause the game
                    if self.play.pause_button.isClicked():
                        self.play.paused = True
                    if self.play.back_button.isClicked():
                        self.play.paused = False
                    if self.play.quit_button.isClicked():
                        self.play.paused = False
                        self.gameStateManager.set_state('score')
                    if event.type == pygame.KEYDOWN:
                        # Press ESC on the keyboard to pause or unpause the game
                        if event.key == pygame.K_ESCAPE:
                            self.play.toggle_pause()
                        elif event.key == pygame.K_ESCAPE:
                            self.play.toggle_pause()
                        elif self.time_now - self.last_attack >= self.cool_down:
                            self.last_attack = self.time_now
                            self.play.handle_event_key(event.key)
                            if self.play.health_bar.hp == 0:
                                self.play.run()
                                sleep(3)
                                self.gameStateManager.set_state('score')
                                self.play.health_bar.hp = self.play.health_bar.max_hp

                elif self.gameStateManager.get_state() == 'score':
                    if self.score.start_button.isClicked():
                        self.score.toggle_save()
                    if self.score.quit_button.isClicked():
                        self.gameStateManager.set_state('start')

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            # Overlapping check
            if self.gameStateManager.get_state() == 'start':
                self.play.pause_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)
                self.play.quit_button.undraw(self.screen)

            elif self.gameStateManager.get_state() == 'play' and self.play.paused is False:
                self.start.start_button.undraw(self.screen)
                self.start.quit_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)
                self.play.quit_button.undraw(self.screen)
                self.play.mode_button.undraw(self.screen)

            elif self.gameStateManager.get_state() == 'play' and self.play.paused is True:
                self.play.pause_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)

            elif self.gameStateManager.get_state() == 'score':
                self.play.pause_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)
                self.play.quit_button.undraw(self.screen)
                self.start.start_button.undraw(self.screen)
                self.start.quit_button.undraw(self.screen)

            self.clock.tick(FPS)

    def check_direction(self, prev_mouse_position, mouse_tracking, prev_time):
        if mouse_tracking:
            current_time = pygame.time.get_ticks()
            if current_time - prev_time >= self.delay_tracking:
                mouse_position = pygame.mouse.get_pos()
                dx = mouse_position[0] - prev_mouse_position[0]
                dy = mouse_position[1] - prev_mouse_position[1]
                direction = ""
                if dy > 0:
                    direction += "Down "
                elif dy < 0:
                    direction += "Up "
                if dx > 0:
                    direction += "Right "
                elif dx < 0:
                    direction += "Left "
                if direction:
                    print("Mouse direction:", direction)
                prev_mouse_position = mouse_position
                prev_time = current_time


if __name__ == "__main__":  # Run only main function
    currentScreen = onScreen()
    currentScreen.run()
