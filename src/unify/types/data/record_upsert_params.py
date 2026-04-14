# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
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

__all__ = [
    "RecordUpsertParams",
    "Match",
    "Create",
    "CreateOrUpdate",
    "CreateOrUpdateIfEmpty",
    "Update",
    "UpdateIfEmpty",
]


class RecordUpsertParams(TypedDict, total=False):
    match: Required[Dict[str, Optional[Match]]]
    """The attribute values to match against to find an existing record.

    At least one unique attribute must be included to ensure that at most one record
    is matched. Additional unique or non-unique attributes may also be included to
    refine the matching criteria.
    """

    validation_mode: ValidationMode
    """Validation mode to use when validating request data.

    `strict` validation will fail requests if any attribute fails validation,
    including unrecognized attributes.

    `ignore_invalid` validation will strip out unknown attributes and replace known,
    non-required attributes with `undefined` if they fail validation. The request
    will still fail if the request body does not contain the proper structure or if
    any required attributes fail validation.
    """

    create: Dict[str, Create]
    """The attribute values to use when creating a new record if no match is found."""

    create_or_update: Dict[str, CreateOrUpdate]
    """The attribute values to apply during both creation and update operations."""

    create_or_update_if_empty: Dict[str, CreateOrUpdateIfEmpty]
    """
    The attribute values to apply during both creation and update-if-empty
    operations.
    """

    update: Dict[str, Update]
    """
    The attribute values to use when updating an existing record if a match is
    found.
    """

    update_if_empty: Dict[str, UpdateIfEmpty]
    """
    The attribute values to update when a matching record is found and the existing
    attribute value on the record is `null`.
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

Create: TypeAlias = Union[
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

CreateOrUpdate: TypeAlias = Union[
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

CreateOrUpdateIfEmpty: TypeAlias = Union[
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

Update: TypeAlias = Union[
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

UpdateIfEmpty: TypeAlias = Union[
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
