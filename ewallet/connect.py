import requests
import logging
import config


class Connect(object):
    def __init__(self, router, auth):
        self.url = config.get_config('default_host') + router
        self.headers = {'Authorization': auth.get_token(), 'Content-Type': 'application/json'}

    def get(self, path_param=None):
        try:
            if path_param:
                return requests.get(self.url + '/' + path_param, headers=self.headers)
            return requests.get(self.url, headers=self.headers)
        except Exception as e:
            logging.error(e)
            return None

    def post(self, data):
        try:
            response = requests.post(self.url, headers=self.headers, data=data)
            return response
        except Exception as e:
            logging.error(e)
            return None

    def delete(self, path_param):
        try:
            response = requests.delete(self.url + '/' + path_param, headers=self.headers)
            return response
        except Exception as e:
            logging.error(e)
            return None
