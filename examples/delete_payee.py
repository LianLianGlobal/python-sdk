import logging

import ewallet
from ewallet import delete_payee

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = delete_payee(auth, 910037182273395037184)

if code == 200:
    print(data)
else:
    logging.error('code: %s, data: %s' % (code, data))
