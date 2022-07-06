import ewallet
from ewallet import FileInfo

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = ewallet.get_file_infos(auth, FileInfo())
print(code, data)
