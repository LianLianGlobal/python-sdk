import logging

import ewallet
from ewallet.models import Quote

ewallet.set_config(default_host=ewallet.US_HOST)
auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
data, code = ewallet.create_quote(auth, Quote('USD', 'CNY'))

if code == 200:
    print(data)
else:
    logging.error('code: %s, data: %s' % (code, data))
