import json

from ewallet import utils


class Quote(object):
    def __init__(self, sell_currency, buy_currency, validity='T_0'):
        self.sell_currency = sell_currency
        self.buy_currency = buy_currency
        self.validity = validity

    def to_json(self):
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


class BaseInfoIndividual(object):
    def __init__(self, first_name, middle_name, last_name, id_type, id_number, email, country_code, phone_number,
                 phone_area_code, nickname):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.id_type = id_type
        self.id_number = id_number
        self.email = email
        self.country_code = country_code
        self.phone_number = phone_number
        self.phone_area_code = phone_area_code
        self.nickname = nickname


class BaseInfoCorporate(object):
    def __init__(self, country_code, corporate_name, corporate_phone_number,
                 corporate_phone_area_code, corporate_registration_number=None):
        self.country_code = country_code
        self.corporate_name = corporate_name
        self.corporate_phone_number = corporate_phone_number
        self.corporate_phone_area_code = corporate_phone_area_code
        if country_code == 'CN' and corporate_registration_number is None:
            raise ValueError('corporate_registration_number is required for China')
        self.corporate_registration_number = corporate_registration_number


class Address(object):
    def __init__(self, country_code, city, state, line1, line2, postcode):
        self.country_code = country_code
        self.city = city
        self.state = state
        self.line1 = line1
        self.line2 = line2
        self.postcode = postcode


class RoutingInfo(object):
    def __init__(self, bank_routing_type, bank_routing_number):
        if bank_routing_type not in ['ABA', 'SORT', 'BSB', 'BANKCODE', 'BRANCHCODE']:
            raise ValueError('bank_routing_type must be ABA, SORT, BSB, BANKCODE or BRANCHCODE')
        self.bank_routing_type = bank_routing_type
        self.bank_routing_number = bank_routing_number


class BankInfo(object):
    def __init__(self, bank_country_code, holder_name, holder_type, account_currency, account_number, bank_name,
                 bank_address=None, swift_code=None, iban=None, routing_info=None):
        self.bank_country_code = bank_country_code
        self.holder_name = holder_name
        self.holder_type = holder_type
        self.account_currency = account_currency
        self.account_number = account_number
        self.bank_name = bank_name
        if bank_address is not None:
            self.bank_address = bank_address
        if swift_code is not None:
            self.swift_code = swift_code
        if iban is not None:
            self.iban = iban
        if type(routing_info) is RoutingInfo:
            self.routing_info = routing_info.__dict__


class AdditionalInfo(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Payee(object):
    def __init__(self, base_info, address, bank_info, file_folder_id, additional_info=None):
        if type(base_info) is BaseInfoIndividual:
            self.entity_type = 'INDIVIDUAL'
        elif type(base_info) is BaseInfoCorporate:
            self.entity_type = 'CORPORATE'
        else:
            raise ValueError('base_info must be BaseInfoIndividual or BaseInfoCorporate')
        self.base_info = base_info.__dict__
        if type(address) is not Address:
            raise ValueError('address must be Address')
        self.address = address.__dict__
        if type(bank_info) is not BankInfo:
            raise ValueError('bank_info must be BankInfo')
        self.bank_info = bank_info.__dict__
        self.file_folder_id = file_folder_id
        # todo: check the format of additional_info
        if type(additional_info) is list:
            self.additional_info = additional_info

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


class Conversion(object):
    def __init__(self, quote_response, sell_amount, buy_amount=None, request_id=None):
        if request_id is None:
            self.request_id = utils.timestamp()
        else:
            self.request_id = str(request_id)
        self.sell_currency = quote_response['sell_currency']
        self.sell_amount = str(sell_amount)
        self.buy_currency = quote_response['buy_currency']
        if buy_amount is not None:
            self.buy_amount = str(buy_amount)
        self.rate_id = quote_response['id']

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


class Payout(object):
    def __init__(self, payee_id, quote_response, send_amount, file_folder_id, purpose, reference, additional_info=None,
                 request_id=None):
        self.payee_id = str(payee_id)
        self.rate_id = quote_response['id']
        self.pay_currency = quote_response['sell_currency']
        self.send_currency = quote_response['buy_currency']
        self.send_amount = str(send_amount)
        self.file_folder_id = str(file_folder_id)
        self.purpose = purpose
        self.reference = reference
        if request_id is None:
            self.request_id = utils.timestamp()
        else:
            self.request_id = str(request_id)
        # todo: verify additional_info
        if self.send_currency == 'CNY':
            if type(additional_info) is list:
                self.additional_info = additional_info
            elif additional_info is None:
                raise ValueError('additional_info is required for CNY')
            else:
                raise ValueError('additional_info must be list')

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


class FileInfo(object):
    def __init__(self, file_id=None, file_name=None, title=None, page_size=20, page_number=1, start_time=None,
                 end_time=None):
        if file_id is not None:
            self.file_id = str(file_id)
        if file_name is not None:
            self.file_name = file_name
        if title is not None:
            self.title = title
        self.page_size = int(page_size)
        self.page_number = int(page_number)
        if start_time is not None:
            self.start_time = int(start_time)
        if end_time is not None:
            self.end_time = int(end_time)

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


class FileFolderInfo(object):
    def __init__(self, file_ids, file_folder_name, purpose, additional_info=None):
        if purpose not in ['PAYOUT', 'PAYEE']:
            raise ValueError('purpose must be PAYOUT or PAYEE')
        self.purpose = str(purpose)
        if type(file_ids) is not list:
            raise ValueError('file_ids must be list')
        self.file_ids = [str(file_id) for file_id in file_ids]
        self.file_folder_name = str(file_folder_name)
        if type(additional_info) is list:
            self.additional_info = additional_info

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False)

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=False, indent=4)


if __name__ == '__main__':
    q = Quote("USD", "EUR")
    print(q)
    p = Payee(BaseInfoIndividual('John', '', 'Doe', 'PASSPORT', '123456789', 'xx@email.com', 'CN', '12345678', '123',
                                 'John'), Address('CN', 'Beijing', 'Beijing', 'StreeLine1', 'StreeLine2', '123456'),
              BankInfo('CN', 'John Doe', 'INDIVIDUAL', 'USD', '123456789', 'Beijing Bank',
                       'BankAddress', '123456789'), '8636974357901546496')
    print(p)
