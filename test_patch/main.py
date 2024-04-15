import pygame
import threading
import time

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Thread Example")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont(None, 30)

# Circle position
circle_x = 100
circle_y = 100

# Function to draw a circle
def draw_circle(x, y, color):
    pygame.draw.circle(screen, color, (x, y), 50)

# Function to update the screen
def update_screen():
    while True:
        screen.fill(BLACK)
        draw_circle(circle_x, circle_y, RED)
        pygame.display.update()
        time.sleep(0.1)

# Function to move the circle
def move_circle():
    global circle_x, circle_y
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            circle_x += 10
            circle_y += 10
        time.sleep(0.1)

# Create threads for updating the screen and moving the circle
update_thread = threading.Thread(target=update_screen)
move_thread = threading.Thread(target=move_circle)

update_thread.start()
move_thread.start()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Display text to indicate the main loop is running
    text = font.render("Main Loop Running", True, WHITE)
    screen.blit(text, (150, 10))

    pygame.display.update()

# Wait for the update and move threads to finish
update_thread.join()
move_thread.join()

# Quit Pygame
pygame.quit()
