import json


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


q = Quote("USD", "EUR")
print(q)
