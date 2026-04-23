# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .uuid import Uuid
from ..._models import BaseModel
from .record_attributes import RecordAttributes

__all__ = ["Record"]


class Record(BaseModel):
    """Object record with its associated metadata and attribute key-value pairs."""

    id: Uuid
    """String UUIDv4 value."""

    attributes: RecordAttributes
    """Attribute key-value pairs associated with an object record."""

    created_at: datetime
    """Date and time the record was created."""

    object: str
    """The API name of the object this record is an instance of."""

    updated_at: datetime
    """Date and time the record was last updated."""
