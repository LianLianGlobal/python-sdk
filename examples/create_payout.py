import ewallet
from ewallet.models import Payout, Quote

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
private_key = 'MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAKlj9csqMDEPlXOmQEQA70E1KjhO1cNHGgkpIEUjI90JaxLzaphOs0D6a98mPApb7MR2dAKtPie7BXQX2WuZzcuh5CR5JZvtup7o5ShTmtcMQhBRdKTyKf0hNq86M51pptg5Gi6lNjup3S2QylaAxmZeux4+s6kKF5VNgtRwYA8bAgMBAAECgYBOfvYOOfSvJ4uYVjh9yvkUfLCd+1pv7ekQybAcmdYqvgyScZ66Ce5jdCi89hjorASiXkoQW3vsKWyzicHFbTbCHcDvAYzw/sNexEuOCnkIwKoX76uNjIVC5NRHeMNZmyLn2sg1ObEawc20FhBrD2bvetTL5cB4bBH8jMi1fb3/MQJBAPAx5b/dAOJOHkszfJUC7Ob8xa21J6IedA16ygtyzGq8HXjMeg6amaaP1LQ0V88pv0E2+L3fPwQkwNC57639oS8CQQC0iVstX5RarHfrcZ8mmlCqiCpF2V/PK4V8Q+AVHvgnjxxZXRBM+6gOun3VuFxC5o3YlBa2qBdPR9frjYxqa33VAkEAjF3skNo7eQUD6RiWlpJWFYrkjuYN2k0HrxTx3AzjbwCuDHkaX0xzvIXTXNg19IfGD/trE7LSJb7Au3ndmoVc2wJBAKn2DfJfYwkiCRuMsinjaUHCQxnTFRGyhU6Bj/oSV8jWP/gZVvlCieqjw0dq8uDAsJVOhTucb6Vhm3LUpXaij6kCQQDBotXgMLlmtKGkXYqs0q1EfeF9CxN/FA8d8oMMdg3ez/2Wz1gMZivJL0MRR7a2FwqRFUuNa6u2h5l6PZgtZk6x'
ewallet.set_config(private_key=private_key)

# p = Payee(BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
#                              'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
#           BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'CNY', utils.timestamp(), 'Beijing Bank',
#                    'BankAddress', '123456789'), '8636974357901546496')
#
# payee, code = create_payee(auth, p)
# print(payee, code)
# CNY 910037273922144769024
quote_response, _ = ewallet.create_quote(auth, Quote('USD', 'CNY'))
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
data, code = ewallet.create_payout(auth, payout)

print(data)
