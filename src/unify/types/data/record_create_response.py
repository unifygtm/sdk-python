# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .u_date import UDate
from .u_uuid import UUuid
from ..._models import BaseModel
from .u_address import UAddress
from .u_boolean import UBoolean
from .u_country import UCountry
from .u_decimal import UDecimal
from .u_currency import UCurrency
from .u_multiselect import UMultiselect
from .u_reference_by_id import UReferenceByID
from .u_reference_by_match import UReferenceByMatch
from .u_reference_by_upsert import UReferenceByUpsert

__all__ = ["RecordCreateResponse", "Data", "DataAttributes"]

DataAttributes: TypeAlias = Union[
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
    None,
]


class Data(BaseModel):
    id: UUuid
    """String UUIDv4 value."""

    attributes: Dict[str, Optional[DataAttributes]]
    """Attribute values for the record.

    Each key is the API name of the attribute and each value is the corresponding
    attribute value for the record.
    """

    created_at: datetime
    """Date and time the record was created."""

    object: str
    """The API name of the object this record is an instance of."""

    updated_at: datetime
    """Date and time the record was last updated."""


class RecordCreateResponse(BaseModel):
    """Response for a successful create operation."""

    data: Data

    status: Literal["success"]
