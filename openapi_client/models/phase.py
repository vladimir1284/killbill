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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.duration import Duration
from openapi_client.models.price import Price
from openapi_client.models.usage import Usage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Phase(BaseModel):
    """
    Phase
    """ # noqa: E501
    type: Optional[StrictStr] = None
    prices: Optional[List[Price]] = None
    fixed_prices: Optional[List[Price]] = Field(default=None, alias="fixedPrices")
    duration: Optional[Duration] = None
    usages: Optional[List[Usage]] = None
    __properties: ClassVar[List[str]] = ["type", "prices", "fixedPrices", "duration", "usages"]

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
        """Create an instance of Phase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item in self.prices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fixed_prices (list)
        _items = []
        if self.fixed_prices:
            for _item in self.fixed_prices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fixedPrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in usages (list)
        _items = []
        if self.usages:
            for _item in self.usages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Phase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "prices": [Price.from_dict(_item) for _item in obj.get("prices")] if obj.get("prices") is not None else None,
            "fixedPrices": [Price.from_dict(_item) for _item in obj.get("fixedPrices")] if obj.get("fixedPrices") is not None else None,
            "duration": Duration.from_dict(obj.get("duration")) if obj.get("duration") is not None else None,
            "usages": [Usage.from_dict(_item) for _item in obj.get("usages")] if obj.get("usages") is not None else None
        })
        return _obj


