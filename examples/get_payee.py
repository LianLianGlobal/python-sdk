import ewallet
from ewallet import get_payout

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = get_payout(auth, 1656929029901)
print(data)
