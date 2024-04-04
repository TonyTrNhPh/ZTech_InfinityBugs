import pygame
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
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.play = Play(self.screen, self.gameStateManager)
        self.score = Score(self.screen,self.gameStateManager)
        self.states = {'start': self.start,
                       'play': self.play,
                       'score':self.score}
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                # Click X on window to quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                # Separate the screen button
                if self.gameStateManager.get_state() == 'start':
                    # Click Quit button to quit the game
                    if self.start.quit_button.isClicked():
                        self.running = False
                        break
                    # Click Start button to play the game
                    if self.start.start_button.isClicked():
                        self.gameStateManager.set_state('play')
                elif self.gameStateManager.get_state() == 'play':
                    # Click Pause button to pause the game
                    if self.play.pause_button.isClicked():
                        self.play.toggle_pause()
                    if self.play.back_button.isClicked():
                        self.play.toggle_pause()
                    if self.play.quit_button.isClicked():
                        self.play.toggle_pause()
                        self.gameStateManager.set_state('score')
                    if event.type == pygame.KEYDOWN:
                        # Press ESC on the keyboard to pause or unpause the game
                        if event.key == pygame.K_ESCAPE and self.gameStateManager.get_state() == 'play':
                            self.play.toggle_pause()
                        elif event.key == pygame.K_ESCAPE:
                            self.play.toggle_pause()
                elif self.gameStateManager.get_state() == 'score':
                    if self.score.start_button.isClicked():
                        self.score.toggle_save()
                    if self.score.quit_button.isClicked():
                        self.gameStateManager.set_state('start')



            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()

            if self.gameStateManager.get_state() == 'start':
                self.play.pause_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)
                self.play.quit_button.undraw(self.screen)
            elif self.gameStateManager.get_state() == 'play':
                self.start.start_button.undraw(self.screen)
                self.start.quit_button.undraw(self.screen)
            elif self.gameStateManager.get_state() == 'score':
                self.play.pause_button.undraw(self.screen)
                self.play.back_button.undraw(self.screen)
                self.play.quit_button.undraw(self.screen)
                self.start.start_button.undraw(self.screen)
                self.start.quit_button.undraw(self.screen)

            self.clock.tick(FPS)


if __name__ == "__main__":  # Run only main function
    currentScreen = onScreen()
    currentScreen.run()
