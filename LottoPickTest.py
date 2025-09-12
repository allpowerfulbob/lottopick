# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain
import GenerateLottoNumbers

class TestLottoPick(unittest.TestCase):
    
    @patch('builtins.input', side_effect=('colorado', '1'))
    def test_lotto_pick_colorado(self, mock_input):
        random_numbers_colorado = GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto
        self.assertEqual("colorado", "1")
        for number in random_numbers_colorado:
            self.assertLess(5, 40)


    @patch('builtins.input', side_effect=('power ball', '1'))
    def test_lotto_pick_power_ball(self, mock_input):
        random_numbers_power_ball = GenerateLottoNumbers.generate_lotto_numbers_power_ball
        self.assertEqual("power ball", "1")
        for number in random_numbers_power_ball:
            self.assertLess(5, 40)

    @patch('builtins.input', side_effect=('mega millions', '1'))
    def test_lotto_pick_mega_millions(self, mock_input):
        random_numbers_mega_millions = GenerateLottoNumbers.generate_lotto_numbers_mega_millions
        self.assertEqual("mega millions", "1")
        for number in random_numbers_mega_millions:
            self.assertLess(5, 40)

if __name__ == '__main__':
    unittest.main