# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .u_date import UDate
from .u_boolean import UBoolean
from .u_decimal import UDecimal
from .u_address_param import UAddressParam
from .u_country_param import UCountryParam
from .validation_mode import ValidationMode
from .u_currency_param import UCurrencyParam
from .u_multiselect_param import UMultiselectParam
from .u_reference_by_id_param import UReferenceByIDParam
from .u_reference_by_match_param import UReferenceByMatchParam
from .u_reference_by_upsert_param import UReferenceByUpsertParam

__all__ = ["RecordUpdateParams", "Data"]


class RecordUpdateParams(TypedDict, total=False):
    object_name: Required[str]

    data: Required[Dict[str, Data]]
    """The attribute values to update in the record."""

    validation_mode: ValidationMode
    """Validation mode to use when validating request data.

    `strict` validation will fail requests if any attribute fails validation,
    including unrecognized attributes.

    `ignore_invalid` validation will strip out unknown attributes and replace known,
    non-required attributes with `undefined` if they fail validation. The request
    will still fail if the request body does not contain the proper structure or if
    any required attributes fail validation.
    """


Data: TypeAlias = Union[
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
