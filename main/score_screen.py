import pygame
from os.path import isfile, join
from os import listdir
from button import Button
import mysql.connector

# Variables
BG_SCOREMENU_IMG = pygame.image.load('assets/background/leaderboard.png')
BUTTON_START_IMG = pygame.image.load('assets/component/start_button.png')
BUTTON_QUIT_IMG = pygame.image.load('assets/component/quit_button.png')


class Score:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    def __init__(self, display, gameStateManager):
        self.start_button = Button(64 * 11, 64 * 11, BUTTON_START_IMG, 0.8)
        self.quit_button = Button(64 * 16, 64 * 11, BUTTON_QUIT_IMG, 0.8)
        self.display = display
        self.gameStateManager = gameStateManager
        self.save = False
        self.scoreboard = Scoreboard(x=750, y=150,column_width=200, row_height=40)  # Tạo một đối tượng Scoreboard

    def run(self):
        self.display.blit(BG_SCOREMENU_IMG, (0, 0))
        if self.save:
            self.save_overlay()
        else:
            self.start_button.draw(self.display)
            self.quit_button.draw(self.display)
            self.scoreboard.draw(self.display)
        pygame.display.flip()

    def toggle_save(self):
        self.save = not self.save

    def save_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))

class Scoreboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    def __init__(self, x, y,column_width, row_height, font_size=30):
        self.x = x
        self.y = y
        self.column_width = column_width
        self.row_height = row_height
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.scores = []  # Sử dụng danh sách các cặp (tên, điểm số)

        # Kết nối với cơ sở dữ liệu MySQL
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="12345",
            database="scoreboard_db"
        )
        self.load_scores()  # Tải dữ liệu từ cơ sở dữ liệu khi khởi tạo
        self.sort_scores_descending()  # Sắp xếp dữ liệu ngay sau khi tải

    def load_scores(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM scores")
        self.scores = mycursor.fetchall()

    def add_score(self, name, score):
        if score.isdigit():
            mycursor = self.mydb.cursor()
            sql = "INSERT INTO scores (name, score) VALUES (%s, %s)"
            val = (name, score)
            try:
                mycursor.execute(sql, val)
                self.mydb.commit()
                print("Score added successfully!")
                self.load_scores()  # Tải lại dữ liệu từ cơ sở dữ liệu
                self.sort_scores_descending()  # Sắp xếp dữ liệu sau khi thêm điểm mới
                pygame.display.flip()  # Cập nhật màn hình sau khi thêm điểm
            except mysql.connector.Error as err:
                print("Error:", err)
        else:
            print("Invalid score input. Please enter an integer.")

    def draw(self, surface):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM scores")
        self.scores = mycursor.fetchall()
        
        # Sắp xếp dữ liệu trước khi vẽ
        self.sort_scores_descending()

        # Nhãn cho các cột
        label_font = pygame.font.Font(None, 24)
        number_label = label_font.render("Num", True, self.BLACK)
        name_label = label_font.render("Name", True, self.BLACK)
        score_label = label_font.render("Score", True, self.BLACK)
        surface.blit(number_label, (self.x , self.y + 5))
        surface.blit(name_label, (self.x + self.column_width , self.y + 5))
        surface.blit(score_label, (self.x + 2 * self.column_width , self.y + 5))

        # Vẽ dữ liệu
        for i, (id, name, score) in enumerate(self.scores):
            text_surface = self.font.render(f"{i+1}.", True, self.BLACK)
            surface.blit(text_surface, (self.x , self.y + self.row_height * (i + 1) + 5))

            text_surface = self.font.render(name, True, self.BLACK)
            surface.blit(text_surface, (self.x + self.column_width , self.y + self.row_height * (i + 1) + 5))

            text_surface = self.font.render(str(score), True, self.BLACK)
            surface.blit(text_surface, (self.x + 2 * self.column_width , self.y + self.row_height * (i + 1) + 5))

            

    def sort_scores_descending(self):
        self.scores.sort(key=lambda x: x[2], reverse=True)