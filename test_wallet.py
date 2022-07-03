from unittest import skipIf

import ewallet
import unittest
from ewallet.models import Quote, Conversion

ewallet.set_config(default_host=ewallet.US_HOST)
auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')


class BalanceTest(unittest.TestCase):
    def test_get_balances(self):
        data, code = ewallet.get_balances(auth)
        self.assertEqual(code, 200)
        for balance in data:
            self.assertIn('account_id', balance)
            self.assertIn('currency', balance)
            self.assertIn('available_amount', balance)


class ExchangeTest(unittest.TestCase):
    def test_create_quote(self):
        data, code = ewallet.create_quote(auth, Quote('EUR', 'GBP'))
        self.assertEqual(200, code)
        self.assertIn('base_currency', data)
        self.assertEqual('EUR', data['sell_currency'])
        self.assertEqual('GBP', data['buy_currency'])
        self.assertIn('rate', data)
        self.assertIn('validity', data)

    def test_create_conversion(self):
        quote_response, _ = ewallet.create_quote(auth, Quote('GBP', 'EUR'))
        data, code = ewallet.create_conversion(auth, Conversion(quote_response, sell_amount=1))
        self.assertEqual(200, code)
        self.assertIn('base_currency', data)
        self.assertEqual(quote_response['sell_currency'], data['sell_currency'])
        self.assertEqual(quote_response['buy_currency'], data['buy_currency'])
        self.assertEqual(quote_response['id'], data['rate_id'])

    def test_get_conversion(self):
        conversion_request_ids = ['1656843338124']
        for conversion_request_id in conversion_request_ids:
            data, code = ewallet.get_conversion(auth, conversion_request_id)
            self.assertEqual(200, code)
            self.assertEqual(conversion_request_id, data['request_id'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
