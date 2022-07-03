import logging

from ewallet import Connect


def get_balances(auth):
    connect = Connect('/gateway/v1/ew-balances', auth)
    response = connect.get()
    return response.json(), response.status_code


def create_quote(auth, quote):
    connect = Connect('/gateway/v1/ew-conversions/lockfx', auth)
    response = connect.post(quote.object_to_json())
    return response.json(), response.status_code


def create_conversion(auth, conversion):
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.post(conversion.object_to_json())
    return response.json(), response.status_code


def get_conversion(auth, conversion_request_id):
    connect = Connect('/gateway/v1/ew-conversions', auth)
    response = connect.get(conversion_request_id)
    return response.json(), response.status_code
