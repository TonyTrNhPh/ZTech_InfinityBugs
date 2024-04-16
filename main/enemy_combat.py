import random
from time import sleep

import pygame

scenario_number_generate = 2


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
