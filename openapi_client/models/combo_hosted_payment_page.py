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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.account import Account
from openapi_client.models.audit_log import AuditLog
from openapi_client.models.hosted_payment_page_fields import HostedPaymentPageFields
from openapi_client.models.payment_method import PaymentMethod
from openapi_client.models.plugin_property import PluginProperty
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ComboHostedPaymentPage(BaseModel):
    """
    ComboHostedPaymentPage
    """ # noqa: E501
    account: Optional[Account] = None
    payment_method: Optional[PaymentMethod] = Field(default=None, alias="paymentMethod")
    hosted_payment_page_fields: Optional[HostedPaymentPageFields] = Field(default=None, alias="hostedPaymentPageFields")
    payment_method_plugin_properties: Optional[List[PluginProperty]] = Field(default=None, alias="paymentMethodPluginProperties")
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["account", "paymentMethod", "hostedPaymentPageFields", "paymentMethodPluginProperties", "auditLogs"]

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
        """Create an instance of ComboHostedPaymentPage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hosted_payment_page_fields
        if self.hosted_payment_page_fields:
            _dict['hostedPaymentPageFields'] = self.hosted_payment_page_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payment_method_plugin_properties (list)
        _items = []
        if self.payment_method_plugin_properties:
            for _item in self.payment_method_plugin_properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paymentMethodPluginProperties'] = _items
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
        """Create an instance of ComboHostedPaymentPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": Account.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "paymentMethod": PaymentMethod.from_dict(obj.get("paymentMethod")) if obj.get("paymentMethod") is not None else None,
            "hostedPaymentPageFields": HostedPaymentPageFields.from_dict(obj.get("hostedPaymentPageFields")) if obj.get("hostedPaymentPageFields") is not None else None,
            "paymentMethodPluginProperties": [PluginProperty.from_dict(_item) for _item in obj.get("paymentMethodPluginProperties")] if obj.get("paymentMethodPluginProperties") is not None else None,
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj

