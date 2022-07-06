# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import os.path

from ewallet import Connect, get_config
from ewallet.models import FileInfo, FileFolderInfo


def get_balances(auth):
    """Get all balances of the authed account.

    Args:
        auth (TokenAuth): The auth token

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-balances', auth)
    response = connect.get()
    return response.json(), response.status_code


def create_quote(auth, quote):
    """Create a LockFX quote.

    Args:
        auth (TokenAuth): The auth token
        quote (Quote): Quote object in models file

    Returns:
        data (dict): The response json of quote used for Exchange Service or Payout Service
        code (int): Http status code

    """
    connect = Connect('/gateway/v1/ew-conversions/lockfx', auth)
    response = connect.post(quote.to_json())
    return response.json(), response.status_code


def create_conversion(auth, conversion):
    """Create a conversion.

    Args:
        auth (TokenAuth): The auth token
        conversion (): Conversion object in models file

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.post(conversion.to_json())
    return response.json(), response.status_code


def get_conversion(auth, conversion_request_id):
    """"Get a conversion by conversion request id."""
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.get(conversion_request_id)
    return response.json(), response.status_code


def create_payee(auth, payee):
    """Create a payee.

    Args:
        auth (TokenAuth): The auth token
        payee (Payee): Payee object in models file

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.post(payee.to_json())
    return response.json(), response.status_code


def delete_payee(auth, payee_id):
    """Delete a payee by payee id."""
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.delete(payee_id)
    return response.text, response.status_code


def get_payee(auth, payee_id):
    """Get a payee by payee id."""
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.get(payee_id)
    return response.json(), response.status_code


def create_payout(auth, payout):
    """Create a payout.

    Args:
        auth (TokenAuth): The auth token
        payout (Payout): Payout object in models file

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-payouts', auth)
    response = connect.post(payout.to_json())
    return response.json(), response.status_code


def get_payout(auth, payout_request_id):
    """Get a payout by payout request id."""
    connect = Connect('/gateway/v1/ew-payouts', auth)
    response = connect.get(payout_request_id)
    return response.json(), response.status_code


def upload_file(auth, file_path, title=None, notes=None):
    """Upload a file to the LianLianGlobal's File Server.

    The file will be used for `PAYOUT` or `PAYEE` operation.

    Args:
        auth (TokenAuth): The auth token
        file_path (str): The local path of the file
        title (str): Additional information
        notes (str): Additional information

    Returns:
        (dict, int): The response json and status code

    """
    if not os.path.exists(file_path):
        raise Exception('File not exists: %s' % file_path)
    if file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.JPG') or file_path.endswith(
            '.JPEG'):
        mimetype = 'image/jpeg'
    elif file_path.endswith('.png') or file_path.endswith('.PNG'):
        mimetype = 'image/png'
    elif file_path.endswith('.pdf') or file_path.endswith('.PDF'):
        mimetype = 'application/pdf'
    elif file_path.endswith('.rar') or file_path.endswith('.RAR'):
        mimetype = 'application/x-rar-compressed'
    elif file_path.endswith('.zip') or file_path.endswith('.ZIP'):
        mimetype = 'application/zip'
    else:
        raise Exception('File type not supported')
    if os.path.getsize(file_path) > get_config('default_upload_threshold'):
        raise Exception('File size more than %s Bytes' % get_config('default_upload_threshold'))
    (_, filename) = os.path.split(file_path)
    files = {'file': (filename, open(file_path, 'rb'), mimetype)}
    data = None
    if title is not None and notes is not None:
        data = {'extension_info': '{\"title\": \"%s\", \"notes\": \"%s\"}' % (title, notes)}
    elif title is not None:
        data = {'extension_info': '{\"title\": \"%s\"}' % title}
    elif notes is not None:
        data = {'extension_info': '{\"notes\": \"%s\"}' % notes}
    connect = Connect('/gateway/file/upload', auth)
    response = connect.upload_file(files=files, data=data)
    return response.json(), response.status_code


def download_file(auth, file_id, dir_path):
    """Download a file from LianLianGlobal's File Server by file id.

    Args:
        auth (TokenAuth): The auth token
        file_id (int or str): The file id, can be obtained from the response of `upload_file` or `get_file_infos`
        dir_path (str): The local path of the directory to save the file

    Returns:
        (bool): Is the file downloaded successfully

    """
    if not os.path.isdir(dir_path):
        raise Exception('\"%s\" is not a directory' % dir_path)
    connect = Connect('/gateway/file', auth)
    return connect.download_file(file_id, dir_path)


def get_file_infos(auth, file_info):
    """Get file infos by file info.

    Args:
        auth (TokenAuth): The auth token
        file_info (FileInfo): FileInfo object in models file

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-files', auth)
    if type(file_info) is not FileInfo:
        raise Exception('FileInfo type error')
    response = connect.get(data=file_info.to_json())
    return response.json(), response.status_code


def create_file_folder(auth, file_folder_info):
    """Create a file folder on LianLianGlobal's Database.

    The file ids in file folder info is related with LianLianGlobal's File Server.

    Args:
        auth (TokenAuth): The auth token
        file_folder_info (FileFolderInfo): FileFolderInfo object in models file

    Returns:
        (dict, int): The response json and status code

    """
    connect = Connect('/gateway/v1/ew-folders', auth)
    if type(file_folder_info) is not FileFolderInfo:
        raise Exception('FileFolderInfo type error')
    response = connect.post(file_folder_info.to_json())
    return response.json(), response.status_code


def get_file_folder_info(auth, file_folder_id):
    """Get a file folder info by file folder id."""
    connect = Connect('/gateway/v1/ew-folders', auth)
    response = connect.get(file_folder_id)
    return response.json(), response.status_code


def delete_file_folder(auth, file_folder_id):
    """Delete a file folder by file folder id."""
    connect = Connect('/gateway/v1/ew-folders', auth)
    response = connect.delete(file_folder_id)
    return response.text, response.status_code
