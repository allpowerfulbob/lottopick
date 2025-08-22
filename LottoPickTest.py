# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain

class TestLottoPick(unittest.TestCase):
    
    def test_lotto_pick_colorado(self):
        self.skiptest("power ball", "mega millions")
        with patch('builtins.input', side_effect=['Colorado', 1]):
            result = LottoPickMain.main()
            self.assertEqual(result("colorado", re.IGNORECASE), True)

    def test_lotto_pick_power_ball(self):
        self.skiptest("colorado", "mega millions")
        with patch('builtins.input', side_effect=['Power Ball', 1]):
            result = LottoPickMain.main()
            self.assertEqual(result("power ball", re.IGNORECASE), True)

    def test_lotto_pick_mega_millions(self):
        self.skipTest("colorado", "power ball")
        with patch('builtins.input', side_effect=['Mega Millions', 1]):
            result = LottoPickMain.main()
            self.assertEqual(result("mega millions", re.IGNORECASE), True)