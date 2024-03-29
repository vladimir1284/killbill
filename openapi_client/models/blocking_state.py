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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.audit_log import AuditLog
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BlockingState(BaseModel):
    """
    BlockingState
    """ # noqa: E501
    blocked_id: Optional[StrictStr] = Field(default=None, alias="blockedId")
    state_name: Optional[StrictStr] = Field(default=None, alias="stateName")
    service: Optional[StrictStr] = None
    is_block_change: Optional[StrictBool] = Field(default=None, alias="isBlockChange")
    is_block_entitlement: Optional[StrictBool] = Field(default=None, alias="isBlockEntitlement")
    is_block_billing: Optional[StrictBool] = Field(default=None, alias="isBlockBilling")
    effective_date: Optional[datetime] = Field(default=None, alias="effectiveDate")
    type: Optional[StrictStr] = None
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["blockedId", "stateName", "service", "isBlockChange", "isBlockEntitlement", "isBlockBilling", "effectiveDate", "type", "auditLogs"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUBSCRIPTION', 'SUBSCRIPTION_BUNDLE', 'ACCOUNT'):
            raise ValueError("must be one of enum values ('SUBSCRIPTION', 'SUBSCRIPTION_BUNDLE', 'ACCOUNT')")
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
        """Create an instance of BlockingState from a JSON string"""
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
        """Create an instance of BlockingState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blockedId": obj.get("blockedId"),
            "stateName": obj.get("stateName"),
            "service": obj.get("service"),
            "isBlockChange": obj.get("isBlockChange"),
            "isBlockEntitlement": obj.get("isBlockEntitlement"),
            "isBlockBilling": obj.get("isBlockBilling"),
            "effectiveDate": obj.get("effectiveDate"),
            "type": obj.get("type"),
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj


