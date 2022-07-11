# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import os

US_HOST = 'https://us-api.lianlianglobal.com'
TEST_HOST = 'http://192.168.132.148:8086'

_config = {
    'default_host': TEST_HOST,
    'connection_timeout': 20,  # 20 seconds
    'file_connection_timeout': 60,  # 60 seconds
    'default_upload_threshold': 1024 * 1024 * 10,  # 10MB
    'private_key': '',  # PKCS8 format
    'private_key_path': ''  # PKCS8 pem format
}


def get_config(key=None):
    """Get config value by key.

    If key is None, return all config.
    
    Args: key (str): config key, allowed keys: **default_host**, **connection_timeout**, 
    **file_connection_timeout**, **default_upload_threshold**. 

    Returns: 
        (str or int): config value

    """
    if key:
        return _config[key]
    return _config


def set_config(default_host=None, connection_timeout=None, file_connection_timeout=None, default_upload_threshold=None,
               private_key=None, private_key_path=None):
    """Set config value by key.

    Args:
        default_host (str): The current production environment is only **US_HOST**
        connection_timeout (int): HTTP connection timeout period
        file_connection_timeout (int): HTTP connection timeout period for file upload or download
        default_upload_threshold (int): File upload limit size, default is 10MB
        private_key (str): Private key for signature generation
        private_key_path (str): Path of private key file for signature generation

    Returns:

    """
    if default_host:
        _config['default_host'] = default_host
    if connection_timeout:
        _config['connection_timeout'] = connection_timeout
    if file_connection_timeout:
        _config['file_connection_timeout'] = file_connection_timeout
    if default_upload_threshold:
        _config['default_upload_threshold'] = default_upload_threshold
    if private_key:
        _config['private_key'] = private_key
    if private_key_path:
        if not os.path.exists(private_key_path):
            raise Exception('Private key file not exists')
        _config['private_key_path'] = private_key_path
