# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .date import Date
from .address import Address
from .boolean import Boolean
from .country import Country
from .decimal import Decimal
from .currency import Currency
from .multiselect import Multiselect
from .reference_by_id import ReferenceByID
from .reference_by_match import ReferenceByMatch
from .reference_by_upsert import ReferenceByUpsert

__all__ = ["Value"]

Value: TypeAlias = Union[
    Address, Boolean, Country, Currency, Date, Decimal, Multiselect, ReferenceByID, ReferenceByMatch, ReferenceByUpsert
]
