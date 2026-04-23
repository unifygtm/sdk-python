# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .u_uuid import UUuid
from ..._models import BaseModel

__all__ = ["UReferenceByID"]


class UReferenceByID(BaseModel):
    """Reference to another object record by ID.

    This will find an existing record by its ID, and an error will be returned if
    the record does not exist.
    """

    id: UUuid
    """String UUIDv4 value."""
