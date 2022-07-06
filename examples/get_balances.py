import logging

import ewallet

ewallet.set_config(default_host=ewallet.TEST_HOST)
auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
data, code = ewallet.get_balances(auth)
if code == 200:
    print(data)
else:
    logging.error(data)
