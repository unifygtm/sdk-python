# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .u_url import UURL
from .u_date import UDate
from .u_text import UText
from .u_uuid import UUuid
from .u_email import UEmail
from .u_select import USelect
from .u_address import UAddress
from .u_boolean import UBoolean
from .u_country import UCountry
from .u_decimal import UDecimal
from .u_integer import UInteger
from .u_currency import UCurrency
from .u_datetime import UDatetime
from .u_multiselect import UMultiselect
from .u_phone_number import UPhoneNumber
from .u_reference_by_id import UReferenceByID
from .u_reference_by_match import UReferenceByMatch
from .u_reference_by_upsert import UReferenceByUpsert

__all__ = ["UValue"]

UValue: TypeAlias = Union[
    UAddress,
    UBoolean,
    UCountry,
    UCurrency,
    UDate,
    UDatetime,
    UDecimal,
    UEmail,
    UInteger,
    UMultiselect,
    UPhoneNumber,
    UReferenceByID,
    UReferenceByMatch,
    UReferenceByUpsert,
    USelect,
    UText,
    UURL,
    UUuid,
]
