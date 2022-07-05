import mimetypes

filepaths = [
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.zip',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.rar',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_5MB.pdf',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.png',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpg',
    r'C:\Users\yangdm002\Desktop\OpenAPI test case\files\test_1MB.jpeg'
]

for filepath in filepaths:
    print(mimetypes.guess_type(filepath)[0])
