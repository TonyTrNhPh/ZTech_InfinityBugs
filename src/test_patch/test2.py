import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (1280, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid Layout")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define grid parameters
grid_size = 300
cell_size = grid_size // 3
nums = [7, 8, 9, 4, 5, 6, 1, 2, 3]
cell_colors = [WHITE] * 9  # Initialize all cells as white
last_input_time = 0  # Time since the last key press
last_input_cells = []  # Indices of the cells to be turned red
current_cell_index = 0  # Index of the current cell being turned red
cell_timers = [0] * 9  # Timers for each cell

# Define a function to draw the grid
def draw_grid(Ox, Oy):
    for row in range(3):
        for col in range(3):
            # Draw the cell
            x = col * cell_size + Ox
            y = row * cell_size + Oy
            rect = pygame.Rect(x, y, cell_size, cell_size)
            cell_index = row * 3 + col
            if cell_timers[cell_index] > 0:
                cell_timers[cell_index] -= 1
                if cell_timers[cell_index] == 0:
                    cell_colors[cell_index] = WHITE
                else:
                    cell_colors[cell_index] = RED
            else:
                cell_colors[cell_index] = WHITE
            pygame.draw.rect(screen, cell_colors[cell_index], rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

            # Draw the number
            num = nums[row * 3 + col]
            font = pygame.font.Font(None, 36)
            text = font.render(str(num), True, BLACK)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            screen.blit(text, text_rect)

    pygame.display.update()

# Function to handle input
def handle_input(key):
    global last_input_time, last_input_cells, current_cell_index
    last_input_cells = []
    if key == pygame.K_KP1:
        last_input_cells = [6, 4, 2]
    elif key == pygame.K_KP2:
        last_input_cells = [7, 4, 1]
    elif key == pygame.K_KP3:
        last_input_cells = [8, 4, 0]
    elif key == pygame.K_KP4:
        last_input_cells = [3, 4, 5]
    elif key == pygame.K_KP5:
        last_input_cells = [4]
    elif key == pygame.K_KP6:
        last_input_cells = [5, 4, 3]
    elif key == pygame.K_KP7:
        last_input_cells = [0, 4, 8]
    elif key == pygame.K_KP8:
        last_input_cells = [1, 4, 7]
    elif key == pygame.K_KP9:
        last_input_cells = [2, 4, 6]
    last_input_time = pygame.time.get_ticks()
    current_cell_index = 0



# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_input(event.key)

    # Update cell colors
    current_time = pygame.time.get_ticks()
    if current_time - last_input_time >= current_cell_index * 100:
        if current_cell_index < len(last_input_cells):
            cell_timers[last_input_cells[current_cell_index]] = 50  # Set timer for 0.2 seconds (20 frames at 100 FPS)
            current_cell_index += 1

    draw_grid(800,100)
    clock.tick(200)  # Limit the frame rate to 100 FPS

# Quit Pygame
pygame.quit()