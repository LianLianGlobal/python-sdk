import os

import requests
import logging
from ewallet.config import get_config


class Connect(object):
    """Encapsulation of HTTP operations.

    Include GET, POST, DELETE, upload_file, download_file methods.

    Attributes:
        router: router of LianLianPay ewallet OpenAPI.
        auth: authentication token.
    """
    def __init__(self, router, auth):
        """Initialize Connect object.

        :param router: Router of LianLianPay ewallet OpenAPI.
        :type router: str
        :param auth: Authentication token.
        :type auth: TokenAuth
        """
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
        if path_param is not None:
            self.url += '/' + str(path_param)
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

        Download file by file_id and save it to customized Directory path.

        :param file_id: The file id on LianLianPay's file server, can be customized when you upload a file.
        :type file_id: str or int
        :param dir_path: Directory path to save downloaded file.
        :type dir_path: str
        :return: Download is success or not.
        :rtype: bool
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
