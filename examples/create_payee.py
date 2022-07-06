import ewallet
from ewallet import create_payee
from ewallet.models import Payee, BankInfo, Address, BaseInfoIndividual, AdditionalInfo

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

additional_info = [
    AdditionalInfo('product_name', 'milk'),
    AdditionalInfo('quantity', '12')
]
p = Payee(BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
                             'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
          BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'USD', '12222444', 'Beijing Bank',
                   'BankAddress', '123456789'), '8636974357901546496', additional_info)
print(p)
data, code = create_payee(auth, p)
print(data)
