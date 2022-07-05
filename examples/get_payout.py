import ewallet
from ewallet import get_payee, get_payout

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = get_payout(auth, 910037181764652176384)
print(data)
