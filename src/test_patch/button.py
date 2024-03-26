import pygame


class Button:
    def __init__(self, x, y, color, text=''):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 95, 95)
        self.color = color
        self.text = text
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 48)
        self.clicked = False
        self.click_time = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        if self.clicked and pygame.time.get_ticks() - self.click_time >= 200:
            self.color = (0,0,0)
            self.text_color = (255, 255, 255)
            self.clicked = False

    def selected(self):
        self.color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.clicked = True
        self.click_time = pygame.time.get_ticks()  # Record the time button was clicked


