# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .u_url import UURL
from .u_date import UDate
from .u_text import UText
from .u_uuid import UUuid
from .u_email import UEmail
from .u_select import USelect
from .u_boolean import UBoolean
from .u_decimal import UDecimal
from .u_integer import UInteger
from .u_datetime import UDatetime
from .u_phone_number import UPhoneNumber
from .u_address_param import UAddressParam
from .u_country_param import UCountryParam
from .u_currency_param import UCurrencyParam
from .u_multiselect_param import UMultiselectParam
from .u_reference_by_id_param import UReferenceByIDParam
from .u_reference_by_match_param import UReferenceByMatchParam
from .u_reference_by_upsert_param import UReferenceByUpsertParam

__all__ = ["UValueParam"]

UValueParam: TypeAlias = Union[
    UAddressParam,
    UBoolean,
    UCountryParam,
    UCurrencyParam,
    UDate,
    UDatetime,
    UDecimal,
    UEmail,
    UInteger,
    UMultiselectParam,
    UPhoneNumber,
    UReferenceByIDParam,
    UReferenceByMatchParam,
    UReferenceByUpsertParam,
    USelect,
    UText,
    UURL,
    UUuid,
]
