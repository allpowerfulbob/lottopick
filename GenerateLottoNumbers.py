# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import the random module
import random

def generate_lotto_numbers_colorado_lotto():
     return sorted(random.sample(range(1, 40), 5))

def generate_lotto_numbers_power_ball():
    pb_main_numbers = random.sample(range(1, 70), 5)
    power_ball = random.randint(1, 26)
    return sorted(pb_main_numbers), power_ball

def generate_lotto_numbers_mega_millions():
    mm_main_numbers = random.sample(range(1, 70), 5)
    mm_mega_ball = random.randint(1, 24)
    return sorted(mm_main_numbers), mm_mega_ball

