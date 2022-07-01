from ewallet import Auth
from ewallet import Connect

auth = Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
connect = Connect('/gateway/v1/ew-balances', auth)
print(connect.get().status_code)
