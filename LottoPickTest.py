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
    def test_lotto_pick_colorado_numbers(self, mock_input):
        random_numbers_colorado = random.random
        for number in range (1, 40):
            random_numbers_colorado
            self.assertEqual
            (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto, "2, 8, 15, 16, 18")


    # Test for the Power Ball Lottery Pick
    @patch('builtins.input', side_effect=('power ball', '1'))
    def test_lotto_pick_power_ball_numbers(self, mock_input):
        random_numbers_power_ball = random.random
        for number in range (1, 70):
            random_numbers_power_ball
            self.assertEqual
            (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto, "4, 15, 29, 32, 36")
    
    @patch('builtins.input', side_effect=('power ball', '1'))
    def test_lotto_pick_power_ball_power_ball(self, mock_input):
        random_numbers_power_ball_power_ball = random.random
        for number in range (1, 26):
            random_numbers_power_ball_power_ball
            self.assertEqual
            (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto, "5")

    # Test for the Mega Millions Lottery Pick
    
    @patch('builtins.input', side_effect=('mega millions', '1'))
    def test_lotto_pick_mega_millions_numbers(self, mock_input):
        random_numbers_mega_millions = random.random
        for number in range (1, 70):
            random_numbers_mega_millions
            self.assertEqual
            (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto, "4, 15, 29, 32, 36")
    
    @patch('builtins.input', side_effect=('mega millions', '1'))
    def test_lotto_pick_mega_millions_mega_ball(self, mock_input):
        random_numbers_mega_millions_mega_ball = random.random
        for number in range (1, 26):
            random_numbers_mega_millions_mega_ball
            self.assertEqual
            (GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto, "5")

if __name__ == '__main__':
    unittest.main()