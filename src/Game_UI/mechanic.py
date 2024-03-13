import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Scenario")

# Define enemy scenarios
scenario_number_generate = 3

# Function to generate a random list
def generate_random_list():
    numbers = [num for num in range(1, 10) if num != 5]
    random.shuffle(numbers)
    length = random.randint(2, 6)
    return numbers[:length]

def generate_counter_scenario(enemy_scenario):
    counter_scenario = []
    for sublist in enemy_scenario:
        counter_sublist = [10 - num for num in sublist]
        counter_scenario.append(counter_sublist)
    return counter_scenario

# Generate enemy_scenario
enemy_scenario = [generate_random_list() for _ in range(scenario_number_generate)]
enemy_counter_scenario = generate_counter_scenario(enemy_scenario)

# Print the generated enemy_scenario
print(enemy_scenario)
print(enemy_counter_scenario)

# Define regions for each move (example)
move_regions = {
    (0, SCREEN_HEIGHT // 3): 1,          # Top left
    (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3): 2,  # Top middle
    (2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3): 3,  # Top right
    (0, 2 * SCREEN_HEIGHT // 3): 4,          # Middle left
    (SCREEN_WIDTH // 3, 2 * SCREEN_HEIGHT // 3): 5,  # Middle middle
    (2 * SCREEN_WIDTH // 3, 2 * SCREEN_HEIGHT // 3): 6,  # Middle right
    (0, SCREEN_HEIGHT): 7,          # Bottom left
    (SCREEN_WIDTH // 3, SCREEN_HEIGHT): 8,  # Bottom middle
    (2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT): 9   # Bottom right
}

player_health = 10
enemy_health = 10

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw move regions (for visualization)
    for region, move in move_regions.items():
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(region[0], region[1], SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3), 2)

    # Update the display
    pygame.display.flip()

    # Capture mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Determine the move based on mouse position
    player_movement = None
    for region, move in move_regions.items():
        if region[0] < mouse_x < region[0] + SCREEN_WIDTH // 3 and region[1] < mouse_y < region[1] + SCREEN_HEIGHT // 3:
            player_movement = move
            break

    # Counter the enemy's attack based on player's move
    if player_movement is not None:
        print("Player move:", player_movement)
        for en_scn_idx, en_scn in enumerate(enemy_scenario):
            for en_move_idx, en_move in enumerate(en_scn):
                counter_move = enemy_counter_scenario[en_scn_idx][en_move_idx]
                if player_movement == counter_move:
                    print("Parry")
                    enemy_health -= 1
                    print("Enemy health:", enemy_health)
                    print("--------------------------")
                else:
                    print("Lost -1 HP")
                    player_health -= 1
                    print("Player health:", player_health)
                    print("--------------------------")

    # Check if either player or enemy health reaches zero
    if player_health <= 0:
        print("Player defeated! Game over.")
        break
    elif enemy_health <= 0:
        print("Enemy defeated! You win.")
        break

# Quit Pygame
pygame.quit()
