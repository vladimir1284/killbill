# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform

    The version of the OpenAPI document: 0.24.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from datetime import date

from pydantic import StrictStr, field_validator

from typing import List, Optional

from openapi_client.models.rolled_up_usage import RolledUpUsage
from openapi_client.models.subscription_usage_record import SubscriptionUsageRecord

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class UsageApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_all_usage(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RolledUpUsage:
        """Retrieve usage for a subscription

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_all_usage_serialize(
            subscription_id=subscription_id,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_all_usage_with_http_info(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RolledUpUsage]:
        """Retrieve usage for a subscription

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_all_usage_serialize(
            subscription_id=subscription_id,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_all_usage_without_preload_content(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve usage for a subscription

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_all_usage_serialize(
            subscription_id=subscription_id,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_usage_serialize(
        self,
        subscription_id,
        start_date,
        end_date,
        plugin_property,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
            'pluginProperty': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if subscription_id is not None:
            _path_params['subscriptionId'] = subscription_id
        # process the query parameters
        if start_date is not None:
            if isinstance(start_date, date):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, date):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        if plugin_property is not None:
            
            _query_params.append(('pluginProperty', plugin_property))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Killbill_Api_Key', 
            'basicAuth', 
            'Killbill_Api_Secret'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/1.0/kb/usages/{subscriptionId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_usage(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        unit_type: StrictStr,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RolledUpUsage:
        """Retrieve usage for a subscription and unit type

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param unit_type: (required)
        :type unit_type: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usage_serialize(
            subscription_id=subscription_id,
            unit_type=unit_type,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_usage_with_http_info(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        unit_type: StrictStr,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RolledUpUsage]:
        """Retrieve usage for a subscription and unit type

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param unit_type: (required)
        :type unit_type: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usage_serialize(
            subscription_id=subscription_id,
            unit_type=unit_type,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_usage_without_preload_content(
        self,
        subscription_id: Annotated[str, Field(strict=True)],
        unit_type: StrictStr,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        plugin_property: Optional[List[StrictStr]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve usage for a subscription and unit type

        

        :param subscription_id: (required)
        :type subscription_id: str
        :param unit_type: (required)
        :type unit_type: str
        :param start_date:
        :type start_date: date
        :param end_date:
        :type end_date: date
        :param plugin_property:
        :type plugin_property: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usage_serialize(
            subscription_id=subscription_id,
            unit_type=unit_type,
            start_date=start_date,
            end_date=end_date,
            plugin_property=plugin_property,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RolledUpUsage",
            '400': None
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_usage_serialize(
        self,
        subscription_id,
        unit_type,
        start_date,
        end_date,
        plugin_property,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
            'pluginProperty': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if subscription_id is not None:
            _path_params['subscriptionId'] = subscription_id
        if unit_type is not None:
            _path_params['unitType'] = unit_type
        # process the query parameters
        if start_date is not None:
            if isinstance(start_date, date):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, date):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        if plugin_property is not None:
            
            _query_params.append(('pluginProperty', plugin_property))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Killbill_Api_Key', 
            'basicAuth', 
            'Killbill_Api_Secret'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/1.0/kb/usages/{subscriptionId}/{unitType}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def record_usage(
        self,
        x_killbill_created_by: StrictStr,
        subscription_usage_record: SubscriptionUsageRecord,
        x_killbill_reason: Optional[StrictStr] = None,
        x_killbill_comment: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Record usage for a subscription

        

        :param x_killbill_created_by: (required)
        :type x_killbill_created_by: str
        :param subscription_usage_record: (required)
        :type subscription_usage_record: SubscriptionUsageRecord
        :param x_killbill_reason:
        :type x_killbill_reason: str
        :param x_killbill_comment:
        :type x_killbill_comment: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._record_usage_serialize(
            x_killbill_created_by=x_killbill_created_by,
            subscription_usage_record=subscription_usage_record,
            x_killbill_reason=x_killbill_reason,
            x_killbill_comment=x_killbill_comment,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def record_usage_with_http_info(
        self,
        x_killbill_created_by: StrictStr,
        subscription_usage_record: SubscriptionUsageRecord,
        x_killbill_reason: Optional[StrictStr] = None,
        x_killbill_comment: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Record usage for a subscription

        

        :param x_killbill_created_by: (required)
        :type x_killbill_created_by: str
        :param subscription_usage_record: (required)
        :type subscription_usage_record: SubscriptionUsageRecord
        :param x_killbill_reason:
        :type x_killbill_reason: str
        :param x_killbill_comment:
        :type x_killbill_comment: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._record_usage_serialize(
            x_killbill_created_by=x_killbill_created_by,
            subscription_usage_record=subscription_usage_record,
            x_killbill_reason=x_killbill_reason,
            x_killbill_comment=x_killbill_comment,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def record_usage_without_preload_content(
        self,
        x_killbill_created_by: StrictStr,
        subscription_usage_record: SubscriptionUsageRecord,
        x_killbill_reason: Optional[StrictStr] = None,
        x_killbill_comment: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Record usage for a subscription

        

        :param x_killbill_created_by: (required)
        :type x_killbill_created_by: str
        :param subscription_usage_record: (required)
        :type subscription_usage_record: SubscriptionUsageRecord
        :param x_killbill_reason:
        :type x_killbill_reason: str
        :param x_killbill_comment:
        :type x_killbill_comment: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._record_usage_serialize(
            x_killbill_created_by=x_killbill_created_by,
            subscription_usage_record=subscription_usage_record,
            x_killbill_reason=x_killbill_reason,
            x_killbill_comment=x_killbill_comment,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _record_usage_serialize(
        self,
        x_killbill_created_by,
        subscription_usage_record,
        x_killbill_reason,
        x_killbill_comment,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if x_killbill_created_by is not None:
            _header_params['X-Killbill-CreatedBy'] = x_killbill_created_by
        if x_killbill_reason is not None:
            _header_params['X-Killbill-Reason'] = x_killbill_reason
        if x_killbill_comment is not None:
            _header_params['X-Killbill-Comment'] = x_killbill_comment
        # process the form parameters
        # process the body parameter
        if subscription_usage_record is not None:
            _body_params = subscription_usage_record



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'Killbill_Api_Key', 
            'basicAuth', 
            'Killbill_Api_Secret'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/1.0/kb/usages',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


