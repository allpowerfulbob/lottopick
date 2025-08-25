# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain

class TestLottoPick(unittest.TestCase):
    
    @unittest.skipIf("power ball or mega millions", "Testing Colorado Input")
    @patch('builtins.input', return_value=['choice', 'tickets'])
    def test_lotto_pick_colorado(self, mock_input, choice, tickets):
        
        choice = mock_input('colorado')
        tickets = mock_input(1)
        result = LottoPickMain.main()
        self.assertEqual(result("colorado", re.IGNORECASE), True)

    @unittest.skipIf("colorado or mega millions", "Testing Power Ball")
    @patch('builtins.input', return_value=['choice', 'tickets'])
    def test_lotto_pick_power_ball(self, mock_input, choice, tickets):
        
        result = LottoPickMain.main()
        self.assertEqual(result("power ball", re.IGNORECASE), True)

    @unittest.skipIf("colorado or power ball", "Testing Mega Millions")
    @patch('builtins.input', return_value=['choice', 'tickets'])
    def test_lotto_pick_mega_millions(self, mock_input, choice, ticktets):
        
        result = LottoPickMain.main()
        self.assertEqual(result("mega millions", re.IGNORECASE), True)