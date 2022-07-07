# -*- coding: utf-8 -*-
"""
@Project : python-sdk
@Author  : yangdm002
@Email   : yangdm002@lianlianpay.com
@Time    : 2022/7/6 16:00
"""
import json

from ewallet import utils


class Quote(object):
    """Quote object."""

    def __init__(self, sell_currency, buy_currency, validity='T_0'):
        """Initialize Quote object.

        Args:
            sell_currency (str): The currency that the client sells (in 3-letter ISO-4217 format)
            buy_currency (str): The currency that the client buys (in 3-letter ISO-4217 format)
            validity (str): When is the rate valid, default value: `T_0`
        """
        self.sell_currency = sell_currency
        self.buy_currency = buy_currency
        self.validity = validity

    def to_json(self):
        """Convert object to json string."""
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
    """Balance object."""

    def __init__(self, account_id, currency, available_amount):
        """Initialize Balance object.

        Args:
            account_id (str): Unique identifier of the LianLianGlobal account
            currency (str): Three-letter ISO 4217 currency code
            available_amount (str): The available amount
        """
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
    """BaseInfoIndividual object for individual in `create payee` operation."""

    def __init__(self, first_name, middle_name, last_name, id_type, id_number, email, country_code, phone_number,
                 phone_area_code, nickname):
        """Initialize BaseInfoIndividual object.

        Args:
            first_name (str): The first name
            middle_name (str): The middle name
            last_name (str): The last name
            id_type (str): The type of ID, one of `ID_TYPE_IDCARD`, `ID_TYPE_PASSPORT`, `ID_TYPE_HKID`, `ID_TYPE_TWID`
            id_number (str): The ID number
            email (str): The email address
            country_code (str): The country code
            phone_number (str): The phone number
            phone_area_code (str): The area code of the phone number
            nickname (str): The nickname
        """
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        # todo: check with developer of openapi
        self.id_type = id_type
        self.id_number = id_number
        self.email = email
        self.country_code = country_code
        self.phone_number = phone_number
        self.phone_area_code = phone_area_code
        self.nickname = nickname


class BaseInfoCorporate(object):
    """BaseInfoCorporate object for individual in `create payee` operation."""

    def __init__(self, country_code, corporate_name, corporate_phone_number,
                 corporate_phone_area_code, corporate_registration_number=None):
        """Initialize BaseInfoCorporate object.

        Args:
            country_code (str): The country code
            corporate_name (str): The corporate name
            corporate_phone_number (str): The corporate phone number
            corporate_phone_area_code (str): The corporate phone area code
            corporate_registration_number (str): The corporate registration number
        """
        self.country_code = country_code
        self.corporate_name = corporate_name
        self.corporate_phone_number = corporate_phone_number
        self.corporate_phone_area_code = corporate_phone_area_code
        if country_code == 'CN' and corporate_registration_number is None:
            raise ValueError('corporate_registration_number is required for China')
        self.corporate_registration_number = corporate_registration_number


class Address(object):
    """Address object for Payee"""

    def __init__(self, country_code, city, state, line1, postcode, line2=None):
        """Initialize Address object.

        Args:
            country_code (str): Two-letter ISO 3166-2 country code.
            city (str): City, district, suburb, town, or village.
            state (str): State, county, province, or region
            line1 (str): Address line1 (e.g. street, PO Box, or company name)
            line2 (str): Address line2 (e.g. apartment, suite, unit, or building)
            postcode (str): ZIP or postal code.
        """
        self.country_code = country_code
        self.city = city
        self.state = state
        self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        self.postcode = postcode


class RoutingInfo(object):
    """RoutingInfo object for Payee"""

    def __init__(self, bank_routing_type, bank_routing_number):
        """Initialize RoutingInfo object.

        Args:
            bank_routing_type (str): Routing number type. Allowed values: ABA, SORT, BSB, BANKCODE, BRANCHCODE
            bank_routing_number (str): The routing transit number for the bank account.
        """
        if bank_routing_type not in ['ABA', 'SORT', 'BSB', 'BANKCODE', 'BRANCHCODE']:
            raise ValueError('bank_routing_type must be ABA, SORT, BSB, BANKCODE or BRANCHCODE')
        self.bank_routing_type = bank_routing_type
        self.bank_routing_number = bank_routing_number


class BankInfo(object):
    """BankInfo object for Payee"""

    def __init__(self, bank_country_code, holder_name, holder_type, account_currency, account_number, bank_name,
                 bank_address=None, swift_code=None, iban=None, routing_info=None):
        """Initialize BankInfo object.

        Args:
            bank_country_code (str): Bank country code, Two-letter ISO 3166-2 country code.
            holder_name (str): The name of the person or business that owns the bank account.
            holder_type (str): The type of entity that holds the account. This can be either INDIVIDUAL or CORPORATE.
            account_currency (str): Three-letter ISO 4217 currency code.
            account_number (str): Account number.
            bank_name (str): Name of the bank associated with the routing number (e.g., WELLS FARGO).
            bank_address (str): Bank detail address.
            swift_code (str): Bank SWIFT code.
            iban (str): Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
            routing_info (list): List of RoutingInfo object.
        """
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
        if type(routing_info) is list:
            self.routing_info = routing_info


class AdditionalInfo(object):
    """AdditionalInfo object"""

    def __init__(self, name, value):
        """Initialize AdditionalInfo object."""
        self.name = name
        self.value = value


class Payee(object):
    """Payee object for `create payee` operation."""
    def __init__(self, base_info, address, bank_info, file_folder_id, additional_info=None):
        """Initialize Payee object.

        Args:
            base_info (BankInfo): BaseInfo object
            address (Address): Address object
            bank_info (BankInfo): BankInfo object
            file_folder_id (int or str): The ID of File Folder.
            additional_info (AdditionalInfo): AdditionalInfo object
        """
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
    """Conversion object for `create conversion` operation."""
    def __init__(self, quote_response, sell_amount, buy_amount=None, request_id=None):
        """Initialize Conversion object.

        Args:
            quote_response (dict): Response from `create quote` operation. Can be constructed manually, contain keys of `sell_currency`, `buy_currency` and `id`
            sell_amount (int): Amount in sell_currency that the client sells. Must be specified if buy_amount is not specified.
            buy_amount (int): Amount in buy_currency that the client buys. Must be specified if sell_amount is not specified.
            request_id (int): The idempotent value generated by the client must be unique on each request. Conversion requests with the same request_id will be rejected. The parameter contains a maximum of 128 characters.
        """
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
    """Payout object for `create payout` operation."""
    def __init__(self, payee_id, quote_response, send_amount, file_folder_id, purpose, reference, additional_info=None,
                 request_id=None):
        """Initialize Payout object.

        Args:
            payee_id (int): Payee id from the response of `create payee` operation.
            quote_response (dict): Response from `create quote` operation. Can be constructed manually, contain keys of `sell_currency`, `buy_currency` and `id`
            send_amount (int): Amount paid to payee, main currency unit, rounded up to 2 decimal places.
            file_folder_id (int): The ID of File Folder.
            purpose (str): Purpose of send a payment
            reference (str): This is the postscript information visible to the payee.
            additional_info (AdditionalInfo): AdditionalInfo object
            request_id (str): The idempotent value generated by the client must be unique on each request. Conversion requests with the same request_id will be rejected. The parameter contains a maximum of 128 characters.
        """
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
    """FileInfo object for `get file infos` operation."""
    def __init__(self, file_id=None, name=None, title=None, page_size=20, page_number=1, start_time=None,
                 end_time=None):
        """Initialize FileInfo object.

        Args:
            file_id (int): The ID of File.
            name (str): A file name in the server, require exact match.
            title (str): User naming the file when uploading, require exact match.
            page_size (int): The default value is 20. A maximum of 100 data items can be displayed on a page.
            page_number (int): The query page number.
            start_time (int): File object creation period start time.
            end_time (int): File object creation period end time.
        """
        if file_id is not None:
            self.file_id = str(file_id)
        if name is not None:
            self.name = name
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
    """FileFolderInfo object for `create file folder` operation."""
    def __init__(self, file_ids, file_folder_name, purpose, additional_info=None):
        """Initialize FileFolderInfo object.
        
        Args:
            file_ids (list): List of file ids.
            file_folder_name (str): File folder name.
            purpose (str): The purpose of the upload file. Allowed values: PAYOUT, PAYEE
            additional_info (AdditionalInfo): AdditionalInfo object
        """
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
