import random

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

player_health = 10
enemy_health = 10




player_health = 10  # Example starting player health
enemy_health = 10  # Example starting enemy health

while player_health > 0 and enemy_health > 0:
    for en_scn_idx, en_scn in enumerate(enemy_scenario):
        for en_move_idx, en_move in enumerate(en_scn):
            print("Enemy attack:", en_move)
            # Determine the corresponding move in enemy_counter_scenario based on the current index
            counter_move = enemy_counter_scenario[en_scn_idx][en_move_idx]
            player_movement = int(input("Player move: "))
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

        # Check if either player or enemy health reaches zero after each enemy move
        if player_health <= 0 or enemy_health <= 0:
            break

    # Check if either player or enemy health reaches zero after each enemy scenario
    if player_health <= 0 or enemy_health <= 0:
        break
