import pygame
from os.path import isfile, join
from os import listdir
from button import Button
import mysql.connector

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Variables
BG_SCOREMENU_IMG = pygame.image.load('main/assets/background/grid.png')
LEADERBOARD_IMG = pygame.image.load('main/assets/background/leaderboard.png')
BUTTON_START_IMG = pygame.image.load('main/assets/component/start_button.png')
BUTTON_QUIT_IMG = pygame.image.load('main/assets/component/quit_button.png')


class Score:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, display, gameStateManager):
        self.is_save = False
        self.name = ''
        self.score = ''
        self.rank = ''
        self.start_button = Button(64 * 11, 64 * 11, BUTTON_START_IMG, 0.8)
        self.quit_button = Button(800, 350, BUTTON_QUIT_IMG, 0.5)
        self.display = display
        self.gameStateManager = gameStateManager
        self.save = False
        self.scoreboard = Scoreboard(x=420, y=110, column_width=200, row_height=40)  # Tạo một đối tượng Scoreboard
        # Draws the score menu on
        self.text_field = TextField(x=500, y=350, width=200, height=30, font_size=25,
                                    instruction_text="Enter your name")
        self.font = pygame.font.Font('main/assets/font/Retro Gaming.ttf', 48)

    def run(self):
        self.display.blit(BG_SCOREMENU_IMG, (0, 0))
        self.display.blit(LEADERBOARD_IMG, (260, 0))
        self.scoreboard.draw(self.display)
        self.text_field.draw(self.display)
        self.quit_button.draw(self.display)
        if self.is_save:
            self.draw_text(self.name, self.score, self.rank, 420, 300)
        pygame.display.flip()

    def toggle_save(self):
        self.save = not self.save

    def save_overlay(self):
        overlay = pygame.Surface((self.display.get_width(), self.display.get_height()), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 128))
        self.display.blit(overlay, (0, 0))

    def handle_events(self, events):  # Thêm phương thức xử lý sự kiện
        for event in events:
            self.text_field.handle_event(event)  # Gọi phương thức xử lý sự kiện của TextField

    def draw_text(self, name, score, rank, x, y):
        font = pygame.font.Font('main/assets/font/Retro Gaming.ttf', 24)
        text = f"Rank: {rank}   Name:{name}    Score:{score}"
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(topleft=(x, y))
        self.display.blit(text_surface, text_rect)


class Scoreboard:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, x, y, column_width, row_height, font_size=30):
        self.x = x
        self.y = y
        self.column_width = column_width
        self.row_height = row_height
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.scores = []  # Sử dụng danh sách các cặp (tên, điểm số)
        self.font = pygame.font.Font('main/assets/font/Retro Gaming.ttf', 24)

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

    def update_or_add_score(self, name, score):
        # Tìm kiếm tên trong cơ sở dữ liệu
        for i, (id, n, s) in enumerate(self.scores):
            if n == name:
                current_score = int(s)
                new_score = int(score)
                # Nếu tên đã tồn tại:
                if new_score > current_score:
                    # Nếu điểm số mới lớn hơn điểm số hiện tại, cập nhật điểm số mới
                    self.update_score(id, score)
                return
        # Nếu tên chưa tồn tại, thêm một bản ghi mới vào cơ sở dữ liệu
        self.add_score(name, score)

    def update_score(self, id, score):
        mycursor = self.mydb.cursor()
        sql = "UPDATE scores SET score = %s WHERE id = %s"
        val = (score, id)
        try:
            mycursor.execute(sql, val)
            self.mydb.commit()
            print("Score updated successfully!")
            self.load_scores()  # Tải lại dữ liệu từ cơ sở dữ liệu
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_rank_for_name(self, name):
        for i, (id, n, s) in enumerate(self.scores):
            if n == name:
                return i + 1
        return None  # Trả về None nếu không tìm thấy tên trong bảng xếp hạng

    # def draw_text(self, surface, text, x,y):
    #     font = pygame.font.Font(None, 24)
    #     text_surface = font.render(text, True, self.BLACK)
    #     surface.blit(text_surface, text_rect)

    def text_display(self, text, text_col, x, y, surface):
        img = self.font.render(text, True, text_col)
        surface.blit(img, (x, y))

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
        surface.blit(number_label, (self.x, self.y + 5))
        surface.blit(name_label, (self.x + self.column_width, self.y + 5))
        surface.blit(score_label, (self.x + 2 * self.column_width, self.y + 5))

        # Vẽ dữ liệu
        for i, (id, name, score) in enumerate(self.scores[:3]):
            text_surface = self.font.render(str(i + 1) + ".", True, self.BLACK)
            surface.blit(text_surface, (self.x, self.y + self.row_height * (i + 1) + 5))

            text_surface = self.font.render(name, True, self.BLACK)
            surface.blit(text_surface, (self.x + self.column_width, self.y + self.row_height * (i + 1) + 5))

            text_surface = self.font.render(str(score), True, self.BLACK)
            surface.blit(text_surface, (self.x + 2 * self.column_width, self.y + self.row_height * (i + 1) + 5))

    def sort_scores_descending(self):
        self.scores.sort(key=lambda x: x[2], reverse=True)


class TextField:
    def __init__(self, x, y, width, height, font_size=25, instruction_text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.text = ''
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)
        self.instruction_text = instruction_text

    def isClicked(self):
        action = False
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.clicked = False
        return action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Khi nhấn Enter, không làm gì cả
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # Chỉ chấp nhận các ký tự từ bàn phím
                    if event.unicode.isalnum() or event.unicode in [' ', '.']:
                        self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect, 2)

        # Vẽ văn bản hướng dẫn
        instruction_surface = self.font.render(self.instruction_text, True, BLACK)
        surface.blit(instruction_surface, (self.rect.x - 150, self.rect.y + 5))

        # Vẽ nội dung của ô văn bản
        text_surface = self.font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))