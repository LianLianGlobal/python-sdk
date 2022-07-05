import ewallet
from ewallet import create_payee, utils, create_quote, create_payout
from ewallet.models import Payee, BankInfo, Address, BaseInfoIndividual, Payout, Quote

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

# p = Payee(BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
#                              'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
#           BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'CNY', utils.timestamp(), 'Beijing Bank',
#                    'BankAddress', '123456789'), '8636974357901546496')
#
# payee, code = create_payee(auth, p)
# print(payee, code)
# CNY 910037273922144769024
quote_response, _ = create_quote(auth, Quote('USD', 'CNY'))
# print(quote)
additional_info = [
    {'name': 'product_name', 'value': 'milk'},
    {'name': 'quantity', 'value': '12'},
    {'name': 'unit_price', 'value': '2.5'},
    {'name': 'unit_price_currency', 'value': 'CNY'},
    {'name': 'purchase_date', 'value': '2020-01-01'}
]
# print(type(additional_info) is list)
payout = Payout(910037181764652176384, quote_response, 5.2, 8636974357901546496, 'purpose', 'reference',
                additional_info, request_id='11112345')
# print(payout)
data, code = create_payout(auth, payout)

print(data)
