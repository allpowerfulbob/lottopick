# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain

class TestLottoPick(unittest.TestCase):
    
    @patch('builtins.input', return_value=('colorado', '1'))
    def test_lotto_pick_colorado(self, return_value):
        result = LottoPickMain.main()
        self.assertEqual(result("colorado"), True)

    @patch('builtins.input', return_value=('power ball', '1'))
    def test_lotto_pick_power_ball(self, return_value):
        result = LottoPickMain.main()
        self.assertEqual(result("power ball"), True)

    @patch('builtins.input', return_value=('mega millions', '1'))
    def test_lotto_pick_mega_millions(self, return_value):
        result = LottoPickMain.main()
        self.assertEqual(result("mega millions"), True)

if __name__ == '__main__':
    unittest.main()