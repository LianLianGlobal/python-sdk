import ewallet

auth = ewallet.Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

is_downloaded = ewallet.download_file(auth, '8537295444391354368',
                                      'C:\\Users\\yangdm002\\Desktop\\OpenAPI test case\\files\\aaa\\')
if is_downloaded:
    print('Downloaded successfully')
