import ewallet
from ewallet.models import AdditionalInfo, FileFolderInfo

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

file_ids = [
    "8536706480177799168",
    "8536706480179634176",
    "8536706734738235392",
    "8536706734739808256"
]

additional_info = [
    AdditionalInfo('product_name', 'milk'),
    AdditionalInfo('quantity', '12')
]

data, code = ewallet.create_file_folder(auth, FileFolderInfo(file_ids, 'file folder name', 'PAYEE', additional_info))
print(data)
