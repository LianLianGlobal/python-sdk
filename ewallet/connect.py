# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import os

import requests
import logging

from ewallet import utils
from ewallet.config import get_config


class Connect(object):
    """Encapsulation of HTTP operations.

    Include get, post, delete, upload_file, download_file methods.

    Attributes:
        router: router of LianLianGlobal ewallet OpenAPI.
        auth: authentication token.
    """

    def __init__(self, router, auth):
        """Initialize Connect object.
        
        Args:
            router (str): Router of LianLianGlobal ewallet OpenAPI
            auth (TokenAuth): TokenAuth
        """
        self.router = router
        self.url = get_config('default_host') + router
        self.auth = auth
        self.headers = {'Content-Type': 'application/json'}
        self._session = requests.Session()

        # handler = logging.StreamHandler()
        # handler.setLevel(logging.WARNING)
        # formatter = logging.Formatter('%(asctime)s  %(filename)s  %(levelname)s  %(message)s')
        # handler.setFormatter(formatter)
        # logging.getLogger().addHandler(handler)

    def get(self, path_param=None, data=None):
        """Get method.
        
        Args:
            path_param (int or str): Path parameter
            data (str): Json data

        Returns:
            response (Response): Response object

        """
        if path_param is not None:
            self.url += '/' + str(path_param)
            self.router += '/' + str(path_param)
        self.headers['LLPAY-Signature'] = utils.generation_signature(get_config('private_key'),
                                                                     get_config('private_key_path'), 'GET',
                                                                     self.router, data or '')
        try:
            response = self._session.get(self.url, auth=self.auth, headers=self.headers, data=data,
                                         timeout=get_config('connection_timeout'))
            if response.status_code != requests.codes.ok:
                logging.warning('method: %s, url: %s, status_code: %s, data: %s' % (
                    'GET', self.url, response.status_code, response.text))
            return response
        except Exception as e:
            logging.error(e)
            return None

    def post(self, data=None):
        """ Post method.

        Args:
            data (str): Json data

        Returns:
            response (Response): Response object

        """
        self.headers['LLPAY-Signature'] = utils.generation_signature(get_config('private_key'),
                                                                     get_config('private_key_path'), 'POST',
                                                                     self.router, data or '')
        try:
            response = self._session.post(self.url, auth=self.auth, headers=self.headers, data=data,
                                          timeout=get_config('connection_timeout'))
            if response.status_code != requests.codes.ok:
                logging.warning('method: %s, url: %s, status_code: %s, data: %s' % (
                    'POST', self.url, response.status_code, response.text))
            return response
        except Exception as e:
            logging.error(e)
            return None

    def delete(self, path_param):
        """Delete method.
        
        Args:
            path_param (int or str): Path parameter

        Returns:
            response (Response): Response object

        """
        self.headers['LLPAY-Signature'] = utils.generation_signature(get_config('private_key'),
                                                                     get_config('private_key_path'), 'DELETE',
                                                                     self.router + '/' + str(path_param))
        try:
            response = self._session.delete(self.url + '/' + str(path_param), auth=self.auth, headers=self.headers,
                                            timeout=get_config('connection_timeout'))
            if response.status_code != requests.codes.ok:
                logging.warning('method: %s, url: %s, status_code: %s, data: %s' % (
                    'DELETE', self.url, response.status_code, response.text))
            return response
        except Exception as e:
            logging.error(e)
            return None

    def upload_file(self, files, data=None):
        """Upload file to LianLianGlobal File Server.

        Args:
            files (dict): File to upload
            data (str): Json data

        Returns:
            response (Response): Response object

        """
        try:
            response = self._session.post(self.url, auth=self.auth, files=files, data=data,
                                          timeout=get_config('file_connection_timeout'))
            if response.status_code != requests.codes.ok:
                logging.warning('method: %s, url: %s, status_code: %s, data: %s' % (
                    'upload_file', self.url, response.status_code, response.text))
            return response
        except Exception as e:
            logging.error(e)
            return None

    def download_file(self, file_id, dir_path):
        """Download file by file_id.
        
        Args:
            file_id (str or int): The file id on LianLianGlobal File Server, can be customized when you upload a file
            dir_path (str): Directory path to save downloaded file

        Returns:
            response (bool): Download is success or not.

        """
        try:
            response = self._session.get(self.url + '/' + str(file_id), auth=self.auth, stream=True,
                                         timeout=get_config('file_connection_timeout'))
            if response.status_code != requests.codes.ok:
                logging.warning('method: %s, url: %s, status_code: %s, data: %s' % (
                    'download_file', self.url, response.status_code, response.text))
                # response.raise_for_status()
            file_name = eval(response.headers['Content-Disposition'].split(';')[1].split('=')[1])
            print(os.path.join(dir_path, file_name))
            with open(os.path.join(dir_path, file_name), 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            return True
        except Exception as e:
            logging.error(e)
            return False
