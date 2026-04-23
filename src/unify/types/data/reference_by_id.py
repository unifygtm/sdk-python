# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .uuid import Uuid
from ..._models import BaseModel

__all__ = ["ReferenceByID"]


class ReferenceByID(BaseModel):
    """Reference to another object record by ID.

    This will find an existing record by its ID, and an error will be returned if
    the record does not exist.
    """

    id: Uuid
    """String UUIDv4 value."""
