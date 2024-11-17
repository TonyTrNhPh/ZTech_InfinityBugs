import tkinter
from time import sleep
import tkinter
import pygame
import play_screen as pl
from play_screen import Play
from start_screen import Start
from score_screen import Score
from os.path import isfile, join
from os import listdir
from game_state_manager import GameStateManager
from button import Button
from mouse_track import MouseTrackerApp

pygame.display.set_caption("Infinity Bugs")

# Variables
FPS = 60
BG_COLOR = (240, 244, 251)
WIDTH, HEIGHT = 1280, 800



class onScreen:
    intro = 3
    last_count = pygame.time.get_ticks()
    last_attack = 0
    time_now = 0
    cool_down = 1200
    delay_tracking = 200

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('start')
        # self.gameStateManager = GameStateManager('play')
        # self.gameStateManager = GameStateManager('score')
        self.start = Start(self.screen, self.gameStateManager)
        self.play = Play(self.screen, self.gameStateManager)
        # self.score = Score(self.screen, self.gameStateManager)
        self.states = {'start': self.start,
                       'play': self.play,
                       # 'score': self.score
                       }
        self.running = True
        self.mouse_tracker = MouseTrackerApp(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.time_now = pygame.time.get_ticks()
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if self.gameStateManager.get_state() == 'start':
                    # Click Quit button to quit the game
                    if self.start.quit_button.isClicked():
                        self.running = False
                        break
                    # Click Start button to play the game
                    if self.start.start_button.isClicked():
                        self.gameStateManager.set_state('play')
                elif self.gameStateManager.get_state() == 'play':
                    #
                    if self.play.pause_button.isClicked():
                        self.play.paused = True
                    if self.play.back_button.isClicked():
                        self.play.paused = False
                    if self.play.quit_button.isClicked():
                        self.play.paused = False
                        self.gameStateManager.set_state('score')
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos_x = pygame.mouse.get_pos()[0]
                        pos_y = pygame.mouse.get_pos()[1]
                        self.mouse_tracker.start_recording(pos_x, pos_y)
                    elif event.type == pygame.MOUSEMOTION:
                        pos_x = pygame.mouse.get_pos()[0]
                        pos_y = pygame.mouse.get_pos()[1]
                        self.mouse_tracker.track_mouse(pos_x, pos_y)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        direction = self.mouse_tracker.stop_recording()
                        print(direction)
                        if self.time_now - self.last_attack >= self.cool_down:
                            self.last_attack = self.time_now
                            self.play.handel_event_mouse(direction)

                    if event.type == pygame.KEYDOWN:
                        # Press ESC on the keyboard to pause or unpause the game
                        if event.key == pygame.K_ESCAPE:
                            self.play.toggle_pause()
                        if event.key == pygame.K_SPACE:
                            self.play.attack()
                        if self.play.player_health.hp <= 0 or self.play.enemy_health.hp <= 0:
                            if self.play.player_health.hp <= 0:
                                self.play.game_over_screen()
                            else:
                                self.play.game_win_screen()
                            sleep(3)
                            self.gameStateManager.set_state('score')
                            self.play.player_health.hp = self.play.player_health.max_hp
                            self.play.enemy_health.hp = self.play.enemy_health.max_hp
                elif self.gameStateManager.get_state() == 'score':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.score.text_field.isClicked:
                            self.score.text_field.active = True
                        else:
                            self.score.text_field.active = False
                    if event.type == pygame.KEYDOWN:
                        if self.score.text_field.active:
                            if event.key == pygame.K_RETURN:
                                # Lấy tên từ TextField
                                name = self.score.text_field.text
                                # Lấy điểm số từ TextField hoặc nơi khác
                                score =  self.play.score # Thay bằng phương thức hoặc giá trị thực tế
                                # Thêm bản ghi mới vào bảng điểm
                                self.score.scoreboard.update_or_add_score(name, score)
                                # Sắp xếp lại bảng điểm
                                self.score.scoreboard.sort_scores_descending()
                                # Xác định thứ hạng của bản ghi mới
                                rank = self.score.scoreboard.get_rank_for_name(name)
                                print(f"Name: {name}, Score: {score}, Rank: {rank}")
                                pygame.display.update()
                                self.score.text_field.text = ''
                                self.score.is_save = True
                                self.score.name = name
                                self.score.score = score
                                self.score.rank = rank

                            elif event.key == pygame.K_BACKSPACE:
                                self.score.text_field.text = self.score.text_field.text[:-1]
                            else:
                                # Chỉ chấp nhận các ký tự từ bàn phím
                                if event.unicode.isalnum() or event.unicode in [' ', '.']:
                                    self.score.text_field.text += event.unicode

                    if self.score.quit_button.isClicked():
                        self.gameStateManager.set_state('start')

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            # Overlapping check
            if self.gameStateManager.get_state() == 'start':
                self.play.pause_button.unClicked(self.screen)
                self.play.back_button.unClicked(self.screen)
                self.play.quit_button.unClicked(self.screen)

            elif self.gameStateManager.get_state() == 'play' and self.play.paused is False:
                self.start.start_button.unClicked(self.screen)
                self.start.quit_button.unClicked(self.screen)
                self.play.back_button.unClicked(self.screen)
                self.play.quit_button.unClicked(self.screen)
                self.play.mode_button.unClicked(self.screen)

            elif self.gameStateManager.get_state() == 'play' and self.play.paused is True:
                self.start.start_button.unClicked(self.screen)
                self.start.quit_button.unClicked(self.screen)
                self.play.pause_button.unClicked(self.screen)
                self.play.back_button.unClicked(self.screen)

            elif self.gameStateManager.get_state() == 'score':
                self.play.pause_button.unClicked(self.screen)
                self.play.back_button.unClicked(self.screen)
                self.play.quit_button.unClicked(self.screen)
                self.start.start_button.unClicked(self.screen)
                self.start.quit_button.unClicked(self.screen)


if __name__ == "__main__":  # Run only main function
    currentScreen = onScreen()
    currentScreen.run()
