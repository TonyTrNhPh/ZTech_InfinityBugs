import pygame
import sys
import mysql.connector

# Khởi tạo Pygame
pygame.init()

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kích thước và margin của các cột trong lưới
COLUMN_WIDTH = 150
ROW_HEIGHT = 40


# Lớp TextField
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
        pygame.draw.rect(surface, WHITE, self.rect, 2)

        # Vẽ văn bản hướng dẫn
        instruction_surface = self.font.render(self.instruction_text, True, WHITE)
        surface.blit(instruction_surface, (self.rect.x + 5, self.rect.y - self.font_size - 5))

        # Vẽ nội dung của ô văn bản
        text_surface = self.font.render(self.text, True, WHITE)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

# Lớp Scoreboard
class Scoreboard:
    def __init__(self, x, y, font_size=30):
        self.x = x
        self.y = y
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
        number_label = label_font.render("Num", True, WHITE)
        name_label = label_font.render("Name", True, WHITE)
        score_label = label_font.render("Score", True, WHITE)
        surface.blit(number_label, (self.x , self.y + 5))
        surface.blit(name_label, (self.x + COLUMN_WIDTH , self.y + 5))
        surface.blit(score_label, (self.x + 2 * COLUMN_WIDTH , self.y + 5))

        # Vẽ dữ liệu
        for i, (id, name, score) in enumerate(self.scores):
            text_surface = self.font.render(f"{i+1}.", True, WHITE)
            surface.blit(text_surface, (self.x , self.y + ROW_HEIGHT * (i + 1) + 5))

            text_surface = self.font.render(name, True, WHITE)
            surface.blit(text_surface, (self.x + COLUMN_WIDTH , self.y + ROW_HEIGHT * (i + 1) + 5))

            text_surface = self.font.render(str(score), True, WHITE)
            surface.blit(text_surface, (self.x + 2 * COLUMN_WIDTH , self.y + ROW_HEIGHT * (i + 1) + 5))

    def sort_scores_descending(self):
        self.scores.sort(key=lambda x: x[2], reverse=True)

# Lớp Button
class Button:
    def __init__(self, x, y, width, height, text, font_size=25):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Thiết lập cửa sổ và màn hình
screen_width, screen_height = 1280, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scoreboard Example")

# Tạo một bảng điểm, ô văn bản và nút Lưu
scoreboard = Scoreboard(100, 100)
name_field = TextField(100, 450, 200, 40, instruction_text="Name")
score_field = TextField(350, 450, 200, 40, instruction_text="Score")
save_button = Button(600, 450, 100, 40, "Save")

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        name_field.handle_event(event)
        score_field.handle_event(event)
        if save_button.clicked(event):
            scoreboard.add_score(name_field.text, score_field.text)
            name_field.text = ''
            score_field.text = ''
            scoreboard.sort_scores_descending()
    screen.fill(BLACK)
    
    # Vẽ bảng điểm, các ô văn bản và nút Lưu lên màn hình
    scoreboard.draw(screen)
    name_field.draw(screen)
    score_field.draw(screen)
    save_button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
