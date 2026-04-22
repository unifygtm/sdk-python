# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .u_uuid import UUuid
from ..._models import BaseModel
from .u_record_attributes import URecordAttributes

__all__ = ["URecord"]


class URecord(BaseModel):
    """Object record with its associated metadata and attribute key-value pairs."""

    id: UUuid
    """String UUIDv4 value."""

    attributes: URecordAttributes
    """Attribute key-value pairs associated with an object record."""

    created_at: datetime
    """Date and time the record was created."""

    object: str
    """The API name of the object this record is an instance of."""

    updated_at: datetime
    """Date and time the record was last updated."""
