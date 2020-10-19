import unittest
from unittest import TestCase
from unittest.mock import patch

import main


class TestMain(TestCase):

    @patch('builtins.input')
    @patch('main.api_call')
    def test_main(self, api_call, mock_input):
        mock_input.side_effect = ['1']
        api_call.return_value = 11463.3133
        total = main.convert()
        self.assertEqual('$11463.31', total)


if __name__ == '__main__':
    unittest.main()
