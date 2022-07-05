import base64

from requests.auth import AuthBase


class Auth(object):
    def __init__(self, develop_id, master_access_token):
        self.__develop_id = develop_id
        self.__master_access_token = master_access_token
        self.__token = 'Basic ' + base64.urlsafe_b64encode(
            (develop_id + ':' + master_access_token).encode('utf-8')).decode('utf-8')

    def get_token(self):
        return self.__token


class TokenAuth(AuthBase):
    def __init__(self, develop_id, master_access_token):
        self.__token = 'Basic ' + base64.urlsafe_b64encode(
            (develop_id + ':' + master_access_token).encode('utf-8')).decode('utf-8')

    def __call__(self, r):
        r.headers['Authorization'] = self.__token
        return r


if __name__ == '__main__':
    auth = Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
    print(auth.get_token())
