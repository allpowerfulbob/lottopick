# Import the random module
import random

class LottoNumberGenerator:
        def __init__ (self, co_generator, pb_generator, mm_generator):
            co_generator = generate_lotto_numbers_colorado_lotto
            pb_generator = generate_lotto_numbers_power_ball
            mm_generator = generate_lotto_numbers_mega_millions

def generate_lotto_numbers_colorado_lotto(self):
    self.col_main_numbers = random.sample(range(1, 40), 5)
    return self.col_main_numbers

def generate_lotto_numbers_power_ball(self):
    pb_main_numbers = random.sample(range(1, 70), 5)
    power_ball = random.randint(1, 26)
    return pb_main_numbers, power_ball

def generate_lotto_numbers_mega_millions(self):
    mm_main_numbers = random.sample(range(1, 70), 5)
    mm_mega_ball = random.randint(1, 24)
    return mm_main_numbers, mm_mega_ball

