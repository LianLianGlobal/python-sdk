import ewallet
from ewallet import create_payee
from ewallet.models import Payee, BankInfo, Address, BaseInfoIndividual

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

p = Payee(BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
                             'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
          BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'USD', '123456789', 'Beijing Bank',
                   'BankAddress', '123456789'), '8636974357901546496')

data, code = create_payee(auth, p)
print(data)
