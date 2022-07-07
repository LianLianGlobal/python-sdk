# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import base64

from requests.auth import AuthBase


class Auth(object):
    """Get the auth token. """
    def __init__(self, develop_id, master_access_token):
        """Initialize Auth object."""
        self.__develop_id = develop_id
        self.__master_access_token = master_access_token
        self.__token = 'Basic ' + base64.urlsafe_b64encode(
            (develop_id + ':' + master_access_token).encode('utf-8')).decode('utf-8')

    def get_token(self):
        """Get the token of auth. """
        return self.__token


class TokenAuth(AuthBase):
    """One of auth methods for requests.auth.AuthBase

    Attributes:
        develop_id (str): develop_id from LianLianGlobal website ->Settings -> Developers
        master_access_token (str): master_access_token from LianLianGlobal website -> Settings -> Developers
    """
    def __init__(self, develop_id, master_access_token):
        """Initialize TokenAuth object."""
        self.__token = 'Basic ' + base64.urlsafe_b64encode(
            (develop_id + ':' + master_access_token).encode('utf-8')).decode('utf-8')

    def __call__(self, r):
        """Call TokenAuth object."""
        r.headers['Authorization'] = self.__token
        return r


if __name__ == '__main__':
    auth = Auth('8ZCZo2rqOb2swvSzTlc7v472G', 'czCAB1FftSbNfLnP1jTOYkmg1RtDfecR')
    print(auth.get_token())
