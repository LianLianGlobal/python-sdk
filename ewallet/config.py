# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
US_HOST = 'https://us-api.lianlianglobal.com'
TEST_HOST = 'http://192.168.132.148:8086'

_config = {
    'default_host': TEST_HOST,
    'connection_timeout': 10,  # 10 seconds
    'file_connection_timeout': 60,  # 60 seconds
    'default_upload_threshold': 1024 * 1024 * 10,  # 10MB
}


def get_config(key=None):
    if key:
        return _config[key]
    return _config


def set_config(default_host=None, connection_timeout=None, file_connection_timeout=None, default_upload_threshold=None):
    if default_host:
        _config['default_host'] = default_host
    if connection_timeout:
        _config['connection_timeout'] = connection_timeout
    if file_connection_timeout:
        _config['file_connection_timeout'] = file_connection_timeout
    if default_upload_threshold:
        _config['default_upload_threshold'] = default_upload_threshold
