import ewallet

filepaths = [
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.zip',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.rar',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_5MB.pdf',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.png',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpg',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpeg',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_76MB.pdf',
]

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
data, code = ewallet.upload_file(auth, filepaths[6])
print(data)
