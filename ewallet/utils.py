# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import base64
import json
import time

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5


def timestamp():
    return str(round(time.time() * 1000))


def object_to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=False)


def _format_private_key(private_key):
    if not private_key.startswith('-----BEGIN PRIVATE KEY-----\n'):
        private_key = '-----BEGIN PRIVATE KEY-----\n' + private_key
    if not private_key.endswith('\n-----END PRIVATE KEY-----'):
        private_key = private_key + '\n-----END PRIVATE KEY-----'
    return private_key


def encode(private_key, private_key_path, payload):
    pkcs8_private_key = None
    if private_key != '':
        pkcs8_private_key = RSA.importKey(_format_private_key(private_key))
    elif private_key_path != '':
        pkcs8_private_key = RSA.importKey(open(private_key_path).read())
    h = SHA256.new(payload.encode())
    signer = PKCS1_v1_5.new(pkcs8_private_key)
    return base64.b64encode(signer.sign(h)).decode()


def generation_signature(private_key, private_key_path, http_method, uri, request_payload='', query_string='',
                         request_epoch=str(int(time.time()))):
    if private_key == '' and private_key_path == '':
        raise Exception('private_key or private_key_path must be set')
    if query_string != '':
        query_string = '&' + query_string
    payload = http_method + '&' + uri + '&' + request_epoch + '&' + request_payload + query_string
    signature = 't=' + request_epoch + ',v=' + encode(private_key, private_key_path, payload)
    return signature
