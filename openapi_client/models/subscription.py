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

from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.audit_log import AuditLog
from openapi_client.models.event_subscription import EventSubscription
from openapi_client.models.phase_price import PhasePrice
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Subscription(BaseModel):
    """
    Subscription
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    bundle_id: Optional[StrictStr] = Field(default=None, alias="bundleId")
    bundle_external_key: Optional[StrictStr] = Field(default=None, alias="bundleExternalKey")
    subscription_id: Optional[StrictStr] = Field(default=None, alias="subscriptionId")
    external_key: Optional[StrictStr] = Field(default=None, alias="externalKey")
    start_date: Optional[datetime] = Field(default=None, alias="startDate")
    product_name: StrictStr = Field(alias="productName")
    product_category: Optional[StrictStr] = Field(default=None, alias="productCategory")
    billing_period: StrictStr = Field(alias="billingPeriod")
    phase_type: Optional[StrictStr] = Field(default=None, alias="phaseType")
    price_list: StrictStr = Field(alias="priceList")
    plan_name: Optional[StrictStr] = Field(alias="planName")
    state: Optional[StrictStr] = None
    source_type: Optional[StrictStr] = Field(default=None, alias="sourceType")
    cancelled_date: Optional[datetime] = Field(default=None, alias="cancelledDate")
    charged_through_date: Optional[date] = Field(default=None, alias="chargedThroughDate")
    billing_start_date: Optional[datetime] = Field(default=None, alias="billingStartDate")
    billing_end_date: Optional[datetime] = Field(default=None, alias="billingEndDate")
    bill_cycle_day_local: Optional[StrictInt] = Field(default=None, alias="billCycleDayLocal")
    quantity: Optional[StrictInt] = None
    events: Optional[List[EventSubscription]] = None
    price_overrides: Optional[List[PhasePrice]] = Field(default=None, alias="priceOverrides")
    prices: Optional[List[PhasePrice]] = None
    audit_logs: Optional[List[AuditLog]] = Field(default=None, alias="auditLogs")
    __properties: ClassVar[List[str]] = ["accountId", "bundleId", "bundleExternalKey", "subscriptionId", "externalKey", "startDate", "productName", "productCategory", "billingPeriod", "phaseType", "priceList", "planName", "state", "sourceType", "cancelledDate", "chargedThroughDate", "billingStartDate", "billingEndDate", "billCycleDayLocal", "quantity", "events", "priceOverrides", "prices", "auditLogs"]

    @field_validator('product_category')
    def product_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BASE', 'ADD_ON', 'STANDALONE'):
            raise ValueError("must be one of enum values ('BASE', 'ADD_ON', 'STANDALONE')")
        return value

    @field_validator('billing_period')
    def billing_period_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DAILY', 'WEEKLY', 'BIWEEKLY', 'THIRTY_DAYS', 'THIRTY_ONE_DAYS', 'SIXTY_DAYS', 'NINETY_DAYS', 'MONTHLY', 'BIMESTRIAL', 'QUARTERLY', 'TRIANNUAL', 'BIANNUAL', 'ANNUAL', 'SESQUIENNIAL', 'BIENNIAL', 'TRIENNIAL', 'NO_BILLING_PERIOD'):
            raise ValueError("must be one of enum values ('DAILY', 'WEEKLY', 'BIWEEKLY', 'THIRTY_DAYS', 'THIRTY_ONE_DAYS', 'SIXTY_DAYS', 'NINETY_DAYS', 'MONTHLY', 'BIMESTRIAL', 'QUARTERLY', 'TRIANNUAL', 'BIANNUAL', 'ANNUAL', 'SESQUIENNIAL', 'BIENNIAL', 'TRIENNIAL', 'NO_BILLING_PERIOD')")
        return value

    @field_validator('phase_type')
    def phase_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('TRIAL', 'DISCOUNT', 'FIXEDTERM', 'EVERGREEN'):
            raise ValueError("must be one of enum values ('TRIAL', 'DISCOUNT', 'FIXEDTERM', 'EVERGREEN')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PENDING', 'ACTIVE', 'BLOCKED', 'CANCELLED', 'EXPIRED'):
            raise ValueError("must be one of enum values ('PENDING', 'ACTIVE', 'BLOCKED', 'CANCELLED', 'EXPIRED')")
        return value

    @field_validator('source_type')
    def source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NATIVE', 'MIGRATED', 'TRANSFERRED'):
            raise ValueError("must be one of enum values ('NATIVE', 'MIGRATED', 'TRANSFERRED')")
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
        """Create an instance of Subscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in price_overrides (list)
        _items = []
        if self.price_overrides:
            for _item in self.price_overrides:
                if _item:
                    _items.append(_item.to_dict())
            _dict['priceOverrides'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item in self.prices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prices'] = _items
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
        """Create an instance of Subscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "bundleId": obj.get("bundleId"),
            "bundleExternalKey": obj.get("bundleExternalKey"),
            "subscriptionId": obj.get("subscriptionId"),
            "externalKey": obj.get("externalKey"),
            "startDate": obj.get("startDate"),
            "productName": obj.get("productName"),
            "productCategory": obj.get("productCategory"),
            "billingPeriod": obj.get("billingPeriod"),
            "phaseType": obj.get("phaseType"),
            "priceList": obj.get("priceList"),
            "planName": obj.get("planName"),
            "state": obj.get("state"),
            "sourceType": obj.get("sourceType"),
            "cancelledDate": obj.get("cancelledDate"),
            "chargedThroughDate": obj.get("chargedThroughDate"),
            "billingStartDate": obj.get("billingStartDate"),
            "billingEndDate": obj.get("billingEndDate"),
            "billCycleDayLocal": obj.get("billCycleDayLocal"),
            "quantity": obj.get("quantity"),
            "events": [EventSubscription.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "priceOverrides": [PhasePrice.from_dict(_item) for _item in obj.get("priceOverrides")] if obj.get("priceOverrides") is not None else None,
            "prices": [PhasePrice.from_dict(_item) for _item in obj.get("prices")] if obj.get("prices") is not None else None,
            "auditLogs": [AuditLog.from_dict(_item) for _item in obj.get("auditLogs")] if obj.get("auditLogs") is not None else None
        })
        return _obj

