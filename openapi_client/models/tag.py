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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.audit_log import AuditLog
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Tag(BaseModel):
    """
    Tag
    """ # noqa: E501
    tag_id: Optional[StrictStr] = Field(default=None, alias="tagId")
    object_type: Optional[StrictStr] = Field(default=None, alias="objectType")
    object_id: Optional[StrictStr] = Field(default=None, alias="objectId")
    tag_definition_id: Optional[StrictStr] = Field(default=None, alias="tagDefinitionId")
    tag_definition_name: Optional[StrictStr] = Field(default=None, alias="tagDefinitionName")
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["tagId", "objectType", "objectId", "tagDefinitionId", "tagDefinitionName", "auditLogs"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACCOUNT', 'ACCOUNT_EMAIL', 'BLOCKING_STATES', 'BUNDLE', 'CUSTOM_FIELD', 'INVOICE', 'PAYMENT', 'TRANSACTION', 'INVOICE_ITEM', 'INVOICE_PAYMENT', 'SUBSCRIPTION', 'SUBSCRIPTION_EVENT', 'SERVICE_BROADCAST', 'PAYMENT_ATTEMPT', 'PAYMENT_METHOD', 'TAG', 'TAG_DEFINITION', 'TENANT', 'TENANT_KVS'):
            raise ValueError("must be one of enum values ('ACCOUNT', 'ACCOUNT_EMAIL', 'BLOCKING_STATES', 'BUNDLE', 'CUSTOM_FIELD', 'INVOICE', 'PAYMENT', 'TRANSACTION', 'INVOICE_ITEM', 'INVOICE_PAYMENT', 'SUBSCRIPTION', 'SUBSCRIPTION_EVENT', 'SERVICE_BROADCAST', 'PAYMENT_ATTEMPT', 'PAYMENT_METHOD', 'TAG', 'TAG_DEFINITION', 'TENANT', 'TENANT_KVS')")
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
        """Create an instance of Tag from a JSON string"""
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
        """Create an instance of Tag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tagId": obj.get("tagId"),
            "objectType": obj.get("objectType"),
            "objectId": obj.get("objectId"),
            "tagDefinitionId": obj.get("tagDefinitionId"),
            "tagDefinitionName": obj.get("tagDefinitionName"),
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj


