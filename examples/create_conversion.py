import logging

import ewallet
from ewallet.models import Quote, Conversion

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
quote_response, _ = ewallet.create_quote(auth, Quote('EUR', 'USD'))
c = Conversion(quote_response, sell_amount=1)
data, code = ewallet.create_conversion(auth, c)

if code == 200:
    print(data)
else:
    logging.error('code: %s, data: %s' % (code, data))
