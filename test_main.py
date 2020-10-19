import unittest
from unittest import TestCase
from unittest.mock import patch

import main


class TestMain(TestCase):

    def setUp(self):
        return None

    @patch('builtins.input')
    @patch('main.api_call')
    def test_main(self, api_call, mock_input):
        mock_input.side_effect = ['1']
        api_call.return_value = 11463.3133
        total = main.convert()
        self.assertEqual('$11463.31', total)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_user_input(self, mock_print, mock_input):
        """Fun fact: 'inf' works, which I'm OK with"""
        user_inputs = ['hey', 'hello', '-1', '1/4', '.1.1', 'nan']
        for user_input in user_inputs:
            mock_input.side_effect = [user_input]
            main.convert()
            mock_print.assert_called_with(f'"{user_input}" is an invalid number, please try again\n')


if __name__ == '__main__':
    unittest.main()
