# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .date import Date
from .boolean import Boolean
from .decimal import Decimal
from .address_param import AddressParam
from .country_param import CountryParam
from .currency_param import CurrencyParam
from .multiselect_param import MultiselectParam
from .reference_by_id_param import ReferenceByIDParam
from .reference_by_match_param import ReferenceByMatchParam
from .reference_by_upsert_param import ReferenceByUpsertParam

__all__ = ["ValueParam"]

ValueParam: TypeAlias = Union[
    AddressParam,
    Boolean,
    CountryParam,
    CurrencyParam,
    Date,
    Decimal,
    MultiselectParam,
    ReferenceByIDParam,
    ReferenceByMatchParam,
    ReferenceByUpsertParam,
]
