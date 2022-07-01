import json
from enum import Enum

from ewallet import utils


class Quote(object):
    def __init__(self, sell_currency, buy_currency, validity='T_0'):
        self.sell_currency = sell_currency
        self.buy_currency = buy_currency
        self.validity = validity

    def object_to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)

    def dict_to_object(self, d):
        self.sell_currency = d['sell_currency']
        self.buy_currency = d['buy_currency']
        self.validity = d['validity']
        return self

    def json_to_object(self, json_string):
        return json.loads(json_string, object_hook=self.dict_to_object)


class Balance(object):
    def __init__(self, account_id, currency, available_amount):
        self.account_id = account_id
        self.currency = currency
        self.available_amount = available_amount

    __hash__ = None

    def __eq__(self, other):
        return self.account_id == other.account_id and self.currency == other.currency and self.available_amount == other.available_amount

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)

    def __repr__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)


class EntityType(Enum):
    CORPORATE = 0
    INDIVIDUAL = 1


class Payee(object):
    def __init__(self, entity_type, base_info, address, bank_info, file_folder_id, additional_info):
        self.entity_type = entity_type
        self.base_info = base_info
        self.address = address
        self.bank_info = bank_info
        self.file_folder_id = file_folder_id
        self.additional_info = additional_info


class Conversion(object):
    def __init__(self, quote_response, sell_amount, buy_amount=None, request_id=None):
        if request_id is None:
            self.request_id = utils.timestamp()
        else:
            self.request_id = request_id
        self.sell_currency = quote_response['sell_currency']
        sell_amount = str(sell_amount)
        self.sell_amount = sell_amount
        self.buy_currency = quote_response['buy_currency']
        if buy_amount is not None:
            self.buy_amount = str(buy_amount)
        self.rate_id = quote_response['id']

    def object_to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


if __name__ == '__main__':
    q = Quote("USD", "EUR")
    print(q)

