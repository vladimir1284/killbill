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
from openapi_client.models.limit import Limit
from openapi_client.models.price import Price
from openapi_client.models.tiered_block import TieredBlock
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Tier(BaseModel):
    """
    Tier
    """ # noqa: E501
    limits: Optional[List[Limit]] = None
    fixed_price: Optional[List[Price]] = Field(default=None, alias="fixedPrice")
    recurring_price: Optional[List[Price]] = Field(default=None, alias="recurringPrice")
    blocks: Optional[List[TieredBlock]] = None
    __properties: ClassVar[List[str]] = ["limits", "fixedPrice", "recurringPrice", "blocks"]

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
        """Create an instance of Tier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in limits (list)
        _items = []
        if self.limits:
            for _item in self.limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['limits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fixed_price (list)
        _items = []
        if self.fixed_price:
            for _item in self.fixed_price:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fixedPrice'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_price (list)
        _items = []
        if self.recurring_price:
            for _item in self.recurring_price:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recurringPrice'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in blocks (list)
        _items = []
        if self.blocks:
            for _item in self.blocks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['blocks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Tier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limits": [Limit.from_dict(_item) for _item in obj.get("limits")] if obj.get("limits") is not None else None,
            "fixedPrice": [Price.from_dict(_item) for _item in obj.get("fixedPrice")] if obj.get("fixedPrice") is not None else None,
            "recurringPrice": [Price.from_dict(_item) for _item in obj.get("recurringPrice")] if obj.get("recurringPrice") is not None else None,
            "blocks": [TieredBlock.from_dict(_item) for _item in obj.get("blocks")] if obj.get("blocks") is not None else None
        })
        return _obj


