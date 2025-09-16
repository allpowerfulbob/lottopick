# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import the random module
import random

# Commented out seed, remove # to unittest
random.seed (42)

def generate_lotto_numbers_colorado_lotto():
     return sorted(random.sample(range(1, 40), 5))

def generate_lotto_numbers_power_ball():
    pb_main_numbers = random.sample(range(1, 70), 5)
    return sorted(pb_main_numbers)

def generate_lotto_numbers_power_ball_powerball():
    power_ball = random.randint(1, 26)
    return power_ball

def generate_lotto_numbers_mega_millions():
    mm_main_numbers = random.sample(range(1, 70), 5)
    return sorted(mm_main_numbers)

def generate_lotto_numbers_mega_millions_megaball():
    mm_mega_ball = random.randint(1, 24)
    return mm_mega_ball

