import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 300, 300)
        self.color = (255,255,255)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        # Calculate grid parameters relative to the player's rectangle
        grid_size = 300
        rows = 3
        thick = 3
        distance = grid_size // rows
        start_x = self.rect.left
        end_x = self.rect.right
        start_y = self.rect.top
        end_y = self.rect.bottom

        # Calculate outer rectangle coordinates for the border
        outer_rect = pygame.Rect(self.rect.left - thick,
                                 self.rect.top - thick,
                                 self.rect.width + 2 * thick,
                                 self.rect.height + 2 * thick)

        # Draw border rectangle
        pygame.draw.rect(surface, (0, 0, 0), outer_rect, thick)
        # Draw grid lines within the player's rectangle
        for x in range(start_x + distance, end_x, distance):
            pygame.draw.line(surface, (0, 0, 0), (x, start_y), (x, end_y), thick)
        for y in range(start_y + distance, end_y, distance):
            pygame.draw.line(surface, (0, 0, 0), (start_x, y), (end_x, y), thick)

        font = pygame.font.SysFont("arialblack", 36)
        numbers_list = [1,2,3,4,5,6,7,8,9]
        index = 0
        for y in range(end_y - distance, start_y - 1, -distance):
            for x in range(start_x, end_x, distance):
                text = font.render(str(numbers_list[index]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(x + distance // 2, y + distance // 2))
                surface.blit(text, text_rect)
                index += 1

    def move(self, key):
        key_pressed = {
            pygame.K_1: (255, 0, 0),
            pygame.K_2: (0, 255, 0),
            pygame.K_3: (0, 0, 255),
            pygame.K_4: (255, 0, 0),
            pygame.K_5: (0, 255, 0),
            pygame.K_6: (0, 0, 255),
            pygame.K_7: (255, 0, 0),
            pygame.K_8: (0, 255, 0),
            pygame.K_9: (0, 0, 255),
        }
        if key in key_pressed:
            self.color = key_pressed[key]


