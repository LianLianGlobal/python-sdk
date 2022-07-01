import requests
import logging
from ewallet.config import get_config


class Connect(object):
    def __init__(self, router, auth):
        self.url = get_config('default_host') + router
        self.headers = {'Authorization': auth.get_token(), 'Content-Type': 'application/json'}
        self._session = requests.Session()

    def get(self, path_param=None):
        try:
            if path_param:
                return self._session.get(self.url + '/' + path_param, headers=self.headers)
            return self._session.get(self.url, headers=self.headers)
        except Exception as e:
            logging.error(e)
            return None

    def post(self, data):
        try:
            response = self._session.post(self.url, headers=self.headers, data=data)
            return response
        except Exception as e:
            logging.error(e)
            return None

    def delete(self, path_param):
        try:
            response = self._session.delete(self.url + '/' + path_param, headers=self.headers)
            return response
        except Exception as e:
            logging.error(e)
            return None
