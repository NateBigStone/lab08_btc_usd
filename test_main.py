import unittest
from unittest import TestCase
from unittest.mock import patch

import main


class TestMain(TestCase):

    def setUp(self):
        """Future use for common test setup"""
        return None

    @patch('main.api_call')
    def test_main(self, mock_requests):
        """Test main func"""
        btc_price = 11463.3133
        resp = {'time': {'updated': 'Oct 20, 2020 03:05:00 UTC',
                                    'updatedISO': '2020-10-20T03:05:00+00:00',
                                    'updateduk': 'Oct 20, 2020 at 04:05 BST'},
                'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). \
                Non-USD currency data converted using hourly conversion rate from openexchangerates.org',
                'bpi': {'USD': {'code': 'USD', 'rate': '11,722.7883', 'description': 'United States Dollar',
                                'rate_float': btc_price}}}

        mock_requests.side_effect = [resp]
        total = main.convert(1)
        self.assertEqual('$11463.31', total)

    @patch('builtins.print')
    def test_main_user_input(self, mock_print):
        """Test various inputs that should fail and print a message for the user"""
        user_inputs = ['hey', 'hello', '-1', '1/4', '.1.1', 'nan']
        for user_input in user_inputs:
            main.convert(user_input)
            mock_print.assert_called_with(f'"{user_input}" is an invalid number, please try again\n')


if __name__ == '__main__':
    unittest.main()
