# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain

class TestLottoPick(unittest.TestCase):
    
    def test_lotto_pick_colorado(self, mock_input, choice, tickets):
        @unittest.skipIf(choice == "power ball or mega millions", re.IGNORECASE,
                         "Testing Colorado Input")
        @patch('builtins.input', return_value=['choice', 'tickets']):
        choice = mock_input('colorado')
        tickets = mock_input(1)
        result = LottoPickMain.main()
        self.assertEqual(result("colorado", re.IGNORECASE), True)

    def test_lotto_pick_power_ball(self, mock_input):
        @unittest.skipIf("colorado", "mega millions", re.IGNORECASE)
        @patch('builtins.input', return_value=['choice', 'tickets']):
        result = LottoPickMain.main()
        self.assertEqual(result("power ball", re.IGNORECASE), True)

    def test_lotto_pick_mega_millions(self, mock_input):
        @unittest.skipif("colorado", "power ball", re.IGNORECASE)
        @patch('builtins.input', return_value=['choice', 'tickets']):
        result = LottoPickMain.main()
        self.assertEqual(result("mega millions", re.IGNORECASE), True)