import pygame
import sys
from character_display import CharacterDisplay


if __name__ == "__main__":
    pygame.init()

    # Load các hình ảnh của nhân vật
    character_images = []
    for i in range(1, 9):
        character_images.append(pygame.image.load(f'images/character{i}.jpg'))

    # # Khởi tạo đối tượng nền
    # background = background(1000, 600)

    # Khởi tạo đối tượng quản lý hiển thị nhân vật
    character_display = CharacterDisplay(800, 600, character_images)

    # Bắt đầu vòng lặp chính
    running = True
    while running:
        # Vẽ hình ảnh nền
        #background.draw(character_display.DISPLAYSURF)

        # Bắt đầu hiển thị nhân vật
        character_display.run()

        # Kiểm tra và xử lý các sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Kết thúc Pygame khi kết thúc chương trình
    pygame.quit()
    sys.exit()
