import os.path
import unittest

import ewallet
from ewallet import utils
from ewallet.models import Quote, Conversion, Payee, BaseInfoIndividual, BankInfo, Address, Payout, AdditionalInfo, \
    FileFolderInfo

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')


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
        data, code = ewallet.create_quote(auth, Quote('USD', 'EUR'))
        self.assertEqual(200, code)
        self.assertIn('base_currency', data)
        self.assertEqual('USD', data['sell_currency'])
        self.assertEqual('EUR', data['buy_currency'])
        self.assertIn('rate', data)
        self.assertIn('validity', data)

    def test_create_conversion(self):
        quote_response, _ = ewallet.create_quote(auth, Quote('USD', 'EUR'))
        data, code = ewallet.create_conversion(auth, Conversion(quote_response, sell_amount=1))
        self.assertEqual(200, code)
        self.assertIn('base_currency', data)
        self.assertEqual(quote_response['sell_currency'], data['sell_currency'])
        self.assertEqual(quote_response['buy_currency'], data['buy_currency'])
        self.assertEqual(quote_response['id'], data['rate_id'])

    def test_get_conversion(self):
        conversion_request_ids = ['1656905534392', '1656905578632']
        for conversion_request_id in conversion_request_ids:
            data, code = ewallet.get_conversion(auth, conversion_request_id)
            self.assertEqual(200, code)
            self.assertEqual(conversion_request_id, data['request_id'])


class PayoutTest(unittest.TestCase):
    def test_create_payee(self):
        p = Payee(
            BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
                               'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
            BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'USD', utils.timestamp(), 'Beijing Bank',
                     'BankAddress', '123456789'), '8636974357901546496')
        data, code = ewallet.create_payee(auth, p)
        self.assertEqual(200, code)
        self.assertIn('id', data)
        globals()['payee_id'] = data['id']

    def test_delete_payee(self):
        data, code = ewallet.delete_payee(auth, globals()['payee_id'])
        self.assertEqual(200, code)
        self.assertEqual('OK', data)
        data, code = ewallet.delete_payee(auth, globals()['payee_id'])
        self.assertEqual(400, code)
        self.assertIn('Payee not found.', data)

    def test_get_payee(self):
        payee_ids = ['910036999553002705920', '910037000230909973504', '910037272374441088000']
        for payee_id in payee_ids:
            data, code = ewallet.get_payee(auth, payee_id)
            self.assertEqual(200, code)
            self.assertEqual(payee_id, data['id'])

    def test_create_payout(self):
        timestamp = int(utils.timestamp())
        payout_request_ids = []
        for i in range(5):
            payout_request_ids.append(str(i + timestamp))
        globals()['payout_request_ids'] = payout_request_ids

        quote_response, _ = ewallet.create_quote(auth, Quote('USD', 'CNY'))
        for payout_request_id in payout_request_ids:
            additional_info = [
                {'name': 'product_name', 'value': 'milk'},
                {'name': 'quantity', 'value': '12'},
                {'name': 'unit_price', 'value': '1.00'},
                {'name': 'unit_price_currency', 'value': 'CNY'},
                {'name': 'purchase_date', 'value': '2020-01-01'}
            ]
            payout = Payout(910037181764652176384, quote_response, 5.2, 8636974357901546496, 'purpose', 'reference',
                            additional_info, payout_request_id)
            data, code = ewallet.create_payout(auth, payout)
            self.assertEqual(200, code)
            self.assertEqual(payout_request_id, data['request_id'])

    def test_get_payout(self):
        for payout_request_id in globals()['payout_request_ids']:
            data, code = ewallet.get_payout(auth, payout_request_id)
            self.assertEqual(200, code)
            self.assertEqual(payout_request_id, data['request_id'])


class SupportServiceTest(unittest.TestCase):
    def test_upload_file(self):
        filepaths = [
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.zip',
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.rar',
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.pdf',
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.png',
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpg',
            r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpeg'
        ]
        if not os.path.exists(filepaths[0]):
            self.skipTest("File not exist.")
        for filepath in filepaths:
            (_, filename) = os.path.split(filepath)
            data, code = ewallet.upload_file(auth, filepath, 'test title', 'test notes')
            self.assertEqual(200, code)
            self.assertIn('id', data)
            self.assertEqual(filename, data['name'])

    def test_download_file(self):
        dir_path = 'C:\\Users\\yangdm002\\Desktop\\OpenAPI test case\\files'
        if not os.path.exists(dir_path):
            self.skipTest("Directory not exist.")
        file_ids = [
            "8536706480177799168",
            "8536706480179634176",
            "8536706734738235392",
            "8536706734739808256"
        ]
        for file_id in file_ids:
            assert ewallet.download_file(auth, file_id, dir_path)

    def test_create_file_folder(self):
        file_ids = [
            "8536706480177799168",
            "8536706480179634176",
            "8536706734738235392",
            "8536706734739808256"
        ]
        additional_info = [
            AdditionalInfo('product_name', 'milk'),
            AdditionalInfo('quantity', '12')
        ]
        data, code = ewallet.create_file_folder(auth,
                                                FileFolderInfo(file_ids, 'just for test', 'PAYOUT', additional_info))
        self.assertEqual(200, code)
        self.assertIn('id', data)
        globals()['file_folder_id'] = data['id']

    def test_get_file_folder_info(self):
        data, code = ewallet.get_file_folder_info(auth, globals()['file_folder_id'])
        self.assertEqual(200, code)
        self.assertEqual(globals()['file_folder_id'], data['id'])

    def test_delete_file_folder(self):
        data, code = ewallet.delete_file_folder(auth, globals()['file_folder_id'])
        self.assertEqual(200, code)
        self.assertEqual('OK', data)
        data, code = ewallet.delete_file_folder(auth, globals()['file_folder_id'])
        self.assertEqual(400, code)
        self.assertIn('FileFolder not found.', data)
        file_ids = [
            "8536706480177799168",
            "8536706480179634176",
            "8536706734738235392",
            "8536706734739808256"
        ]
        data, code = ewallet.create_file_folder(auth, FileFolderInfo(file_ids, 'just for test', 'PAYOUT'))
        globals()['file_folder_id'] = data['id']


if __name__ == '__main__':
    unittest.main(verbosity=2)
