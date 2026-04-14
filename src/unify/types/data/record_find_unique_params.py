# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .u_date import UDate
from .u_boolean import UBoolean
from .u_decimal import UDecimal
from .u_address_param import UAddressParam
from .u_country_param import UCountryParam
from .u_currency_param import UCurrencyParam
from .u_multiselect_param import UMultiselectParam
from .u_reference_by_id_param import UReferenceByIDParam
from .u_reference_by_match_param import UReferenceByMatchParam
from .u_reference_by_upsert_param import UReferenceByUpsertParam

__all__ = ["RecordFindUniqueParams", "Match"]


class RecordFindUniqueParams(TypedDict, total=False):
    match: Required[Dict[str, Optional[Match]]]
    """The attribute values to match against to find an existing record.

    At least one unique attribute must be included to ensure that at most one record
    is matched. Additional unique or non-unique attributes may also be included to
    refine the matching criteria.
    """


Match: TypeAlias = Union[
    UAddressParam,
    UBoolean,
    UCountryParam,
    UCurrencyParam,
    UDate,
    UDecimal,
    UMultiselectParam,
    UReferenceByIDParam,
    UReferenceByMatchParam,
    UReferenceByUpsertParam,
]
