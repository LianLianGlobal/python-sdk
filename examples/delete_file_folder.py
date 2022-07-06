import ewallet

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = ewallet.delete_file_folder(auth, 8637314184207917056)
print(code, data)
