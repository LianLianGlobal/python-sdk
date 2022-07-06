import ewallet
from ewallet.models import AdditionalInfo, FileFolderInfo

auth = ewallet.TokenAuth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')

data, code = ewallet.get_file_folder_info(auth, 8637314184207917056)
print(code, data)
