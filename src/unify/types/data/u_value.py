# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .u_date import UDate
from .u_address import UAddress
from .u_boolean import UBoolean
from .u_country import UCountry
from .u_decimal import UDecimal
from .u_currency import UCurrency
from .u_multiselect import UMultiselect
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
    UDecimal,
    UMultiselect,
    UReferenceByID,
    UReferenceByMatch,
    UReferenceByUpsert,
]
