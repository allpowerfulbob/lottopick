# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import required modules
import unittest
import random
from unittest.mock import patch
import re
import LottoPickMain
import GenerateLottoNumbers

# Create the test class
class TestLottoPick(unittest.TestCase):

    # Create the rancom seed for the test
    def setUp(self):
        random.seed(42)
    
    # Test for the Colorado Lottery pick
    @patch('builtins.input', side_effect=('colorado', '1'))
    def test_lotto_pick_colorado(self, mock_input):
        random_numbers_colorado = random.random
        (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto)
        self.assertEqual("colorado", "GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto")
        for number in random_numbers_colorado:
            self.assertLess(5, 40)


    # Test for the Power Ball Lottery Pick
    @patch('builtins.input', side_effect=('power ball', '1'))
    def test_lotto_pick_power_ball(self, mock_input):
        random_numbers_power_ball = random.random
        (GenerateLottoNumbers.generate_lotto_numbers_power_ball)
        random_number_power_ball = random.random
        (GenerateLottoNumbers.generate_lotto_numbers_power_ball_powerball)
        self.assertEqual("power ball", "GenerateLottoNumbers.generate_lotto_numbers_power_ball",
                         "GenerateLottoNumbers.generate_lotto_numbers_power_ball_powerball")
        for number in random_numbers_power_ball:
            self.assertLess(5, 70)
        for number in random_number_power_ball:
            self.assertless(1, 26)

    # Test for the Mega Millions Lottery Pick
    @patch('builtins.input', side_effect=('mega millions', '1'))
    def test_lotto_pick_mega_millions(self, mock_input):
        random_numbers_mega_millions = random.random
        (GenerateLottoNumbers.generate_lotto_numbers_mega_millions)
        random_number_mega_millions = random.random
        (GenerateLottoNumbers.generate_lotto_numbers_mega_millions_megaball)
        self.assertEqual("mega millions", "GenerateLottoNumbers.generate_lotto_numbers_mega_millions",
                         "GenerateLottoNumbers.generate_lotto_numbers_mega_millions_megaball")
        for number in random_numbers_mega_millions:
            self.assertLess(5, 70)
        for number in random_number_mega_millions:
            self.assertLess(1, 24)

if __name__ == '__main__':
    unittest.main