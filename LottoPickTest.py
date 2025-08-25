# Import required modules
import unittest
from unittest.mock import patch
import re
import LottoPickMain

class TestLottoPick(unittest.TestCase):
    
    @patch('builtins.input', return_value=('choice', 'tickets'))
    def test_lotto_pick_colorado(self, mock_input):
        choice = (mock_input('colorado'))
        tickets = (mock_input('1'))
        result = LottoPickMain.main()
        self.assertEqual(result("colorado"), True)

    @patch('builtins.input', return_value=('choice', 'tickets'))
    def test_lotto_pick_power_ball(self, mock_input):
        choice = mock_input('power ball')
        tickets = mock_input('1')
        result = LottoPickMain.main()
        self.assertEqual(result("power ball"), True)

    @patch('builtins.input', return_value=('choice', 'tickets'))
    def test_lotto_pick_mega_millions(self, mock_input):
        choice = mock_input('mega millions')
        tickets = mock_input('1')
        result = LottoPickMain.main()
        self.assertEqual(result("mega millions"), True)