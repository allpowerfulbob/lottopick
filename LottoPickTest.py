# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain
import GenerateLottoNumbers

class TestLottoPick(unittest.TestCase):
    
    @patch('builtins.input', side_effect=('colorado', '1'))
    def test_lotto_pick_colorado(self, mock_input):
        limit = 5
        random_numbers = GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto(40)
        self.assertEqual("colorado")
        self.assertEqual(len(random_numbers), 5)


    @patch('builtins.input', side_effect=('power ball', '1'))
    def test_lotto_pick_power_ball(self, mock_input):
        self.assertEqual("power ball", GenerateLottoNumbers.generate_lotto_numbers_power_ball)

    @patch('builtins.input', side_effect=('mega millions', '1'))
    def test_lotto_pick_mega_millions(self, mock_input):
        self.assertEqual("mega millions", GenerateLottoNumbers.generate_lotto_numbers_mega_millions)

if __name__ == '__main__':
    unittest.main