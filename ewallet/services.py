import mimetypes

from ewallet import Connect


def get_balances(auth):
    connect = Connect('/gateway/v1/ew-balances', auth)
    response = connect.get()
    return response.json(), response.status_code


def create_quote(auth, quote):
    connect = Connect('/gateway/v1/ew-conversions/lockfx', auth)
    response = connect.post(quote.to_json())
    return response.json(), response.status_code


def create_conversion(auth, conversion):
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.post(conversion.to_json())
    return response.json(), response.status_code


def get_conversion(auth, conversion_request_id):
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.get(conversion_request_id)
    return response.json(), response.status_code


def create_payee(auth, payee):
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.post(payee.to_json())
    return response.json(), response.status_code


def delete_payee(auth, payee_id):
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.delete(payee_id)
    return response.text, response.status_code


def get_payee(auth, payee_id):
    connect = Connect('/gateway/v1/ew-payees', auth)
    response = connect.get(payee_id)
    return response.json(), response.status_code


def create_payout(auth, payout):
    connect = Connect('/gateway/v1/ew-payouts', auth)
    response = connect.post(payout.to_json())
    return response.json(), response.status_code


def get_payout(auth, payout_request_id):
    connect = Connect('/gateway/v1/ew-payouts', auth)
    response = connect.get(payout_request_id)
    return response.json(), response.status_code


def upload_file(auth, file_path, title=None, notes=None):
    mimetype = mimetypes.guess_type(file_path)
    if mimetype not in ['application/x-rar-compressed', 'application/zip', 'application/pdf', 'image/jpeg',
                        'image/png']:
        raise Exception('File type not supported')
    connect = Connect('/gateway/file/upload', auth)
    response = connect.post()
    return response.json(), response.status_code
