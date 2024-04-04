import pygame
import sys
from pygame.locals import QUIT

class CharacterDisplay:
    def __init__(self, window_width, window_height, character_images):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.character_images = character_images
        self.current_image_index = 0
        self.frame_time = 0.1  # Thời gian mỗi frame
        self.clock = pygame.time.Clock()

        # Cài đặt cửa sổ và màn hình
        self.DISPLAYSURF = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Animating character')

    def draw_character(self):
        self.DISPLAYSURF.fill((255, 255, 255))  # Xóa màn hình
        current_character_image = self.character_images[self.current_image_index]
        self.DISPLAYSURF.blit(current_character_image, (100, 100))
        self.current_image_index = (self.current_image_index + 1) % len(self.character_images)
        pygame.display.update()

    def run(self):
        while True:
            print(pygame.time.get_ticks())
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_character()
            self.clock.tick(1 / self.frame_time)  # Đặt FPS để có thời gian mỗi frame là 0.8 giây

if __name__ == "__main__":
    # Load các hình ảnh của nhân vật
    character_images = []
    for i in range(1, 9):
        character_images.append(pygame.image.load(f'images/character{i}.jpg'))
    # Tạo đối tượng quản lý hiển thị nhân vật
    character_display = CharacterDisplay(800, 600, character_images)
    character_display.run()
