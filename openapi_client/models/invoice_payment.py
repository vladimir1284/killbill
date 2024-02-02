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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.audit_log import AuditLog
from openapi_client.models.payment_attempt import PaymentAttempt
from openapi_client.models.payment_transaction import PaymentTransaction
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InvoicePayment(BaseModel):
    """
    InvoicePayment
    """ # noqa: E501
    target_invoice_id: Optional[StrictStr] = Field(default=None, alias="targetInvoiceId")
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    payment_id: Optional[StrictStr] = Field(default=None, alias="paymentId")
    payment_number: Optional[StrictStr] = Field(default=None, alias="paymentNumber")
    payment_external_key: Optional[StrictStr] = Field(default=None, alias="paymentExternalKey")
    auth_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="authAmount")
    captured_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="capturedAmount")
    purchased_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="purchasedAmount")
    refunded_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="refundedAmount")
    credited_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="creditedAmount")
    currency: Optional[StrictStr] = None
    payment_method_id: Optional[StrictStr] = Field(default=None, alias="paymentMethodId")
    transactions: Optional[List[PaymentTransaction]] = None
    payment_attempts: Optional[List[PaymentAttempt]] = Field(default=None, alias="paymentAttempts")
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["targetInvoiceId", "accountId", "paymentId", "paymentNumber", "paymentExternalKey", "authAmount", "capturedAmount", "purchasedAmount", "refundedAmount", "creditedAmount", "currency", "paymentMethodId", "transactions", "paymentAttempts", "auditLogs"]

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
        """Create an instance of InvoicePayment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment_attempts (list)
        _items = []
        if self.payment_attempts:
            for _item in self.payment_attempts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paymentAttempts'] = _items
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
        """Create an instance of InvoicePayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targetInvoiceId": obj.get("targetInvoiceId"),
            "accountId": obj.get("accountId"),
            "paymentId": obj.get("paymentId"),
            "paymentNumber": obj.get("paymentNumber"),
            "paymentExternalKey": obj.get("paymentExternalKey"),
            "authAmount": obj.get("authAmount"),
            "capturedAmount": obj.get("capturedAmount"),
            "purchasedAmount": obj.get("purchasedAmount"),
            "refundedAmount": obj.get("refundedAmount"),
            "creditedAmount": obj.get("creditedAmount"),
            "currency": obj.get("currency"),
            "paymentMethodId": obj.get("paymentMethodId"),
            "transactions": [PaymentTransaction.from_dict(_item) for _item in obj.get("transactions")] if obj.get("transactions") is not None else None,
            "paymentAttempts": [PaymentAttempt.from_dict(_item) for _item in obj.get("paymentAttempts")] if obj.get("paymentAttempts") is not None else None,
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj


