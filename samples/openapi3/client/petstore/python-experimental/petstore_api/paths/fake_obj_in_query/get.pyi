# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

# query params


class MapBeanSchema(
    schemas.DictSchema
):


    class MetaOapg:
        class properties:
            keyword = schemas.StrSchema
            __annotations__ = {
                "keyword": keyword,
            }
        additional_properties = schemas.AnyTypeSchema
    
    keyword: typing.Union[MetaOapg.properties.keyword, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["keyword"]) -> typing.Union[MetaOapg.properties.keyword, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["keyword"], ]):
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        keyword: typing.Union[MetaOapg.properties.keyword, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'MapBeanSchema':
        return super().__new__(
            cls,
            *args,
            keyword=keyword,
            _configuration=_configuration,
            **kwargs,
        )