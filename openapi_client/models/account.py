# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform

    The version of the OpenAPI document: 0.24.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.audit_log import AuditLog
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Account(BaseModel):
    """
    Account
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    name: Optional[StrictStr] = None
    first_name_length: Optional[StrictInt] = Field(default=None, alias="firstNameLength")
    external_key: Optional[StrictStr] = Field(default=None, alias="externalKey")
    email: Optional[StrictStr] = None
    bill_cycle_day_local: Optional[StrictInt] = Field(default=None, alias="billCycleDayLocal")
    currency: Optional[StrictStr] = None
    parent_account_id: Optional[StrictStr] = Field(default=None, alias="parentAccountId")
    is_payment_delegated_to_parent: Optional[StrictBool] = Field(default=None, alias="isPaymentDelegatedToParent")
    payment_method_id: Optional[StrictStr] = Field(default=None, alias="paymentMethodId")
    reference_time: Optional[datetime] = Field(default=None, alias="referenceTime")
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    company: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    locale: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    is_migrated: Optional[StrictBool] = Field(default=None, alias="isMigrated")
    account_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="accountBalance")
    account_cba: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="accountCBA")
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["accountId", "name", "firstNameLength", "externalKey", "email", "billCycleDayLocal", "currency", "parentAccountId", "isPaymentDelegatedToParent", "paymentMethodId", "referenceTime", "timeZone", "address1", "address2", "postalCode", "company", "city", "state", "country", "locale", "phone", "notes", "isMigrated", "accountBalance", "accountCBA", "auditLogs"]

    @field_validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SPL', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWD', 'BTC'):
            raise ValueError("must be one of enum values ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SPL', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWD', 'BTC')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in audit_logs (list)
        _items = []
        if self.audit_logs:
            for _item in self.audit_logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['auditLogs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "name": obj.get("name"),
            "firstNameLength": obj.get("firstNameLength"),
            "externalKey": obj.get("externalKey"),
            "email": obj.get("email"),
            "billCycleDayLocal": obj.get("billCycleDayLocal"),
            "currency": obj.get("currency"),
            "parentAccountId": obj.get("parentAccountId"),
            "isPaymentDelegatedToParent": obj.get("isPaymentDelegatedToParent"),
            "paymentMethodId": obj.get("paymentMethodId"),
            "referenceTime": obj.get("referenceTime"),
            "timeZone": obj.get("timeZone"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "postalCode": obj.get("postalCode"),
            "company": obj.get("company"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "locale": obj.get("locale"),
            "phone": obj.get("phone"),
            "notes": obj.get("notes"),
            "isMigrated": obj.get("isMigrated"),
            "accountBalance": obj.get("accountBalance"),
            "accountCBA": obj.get("accountCBA"),
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj

