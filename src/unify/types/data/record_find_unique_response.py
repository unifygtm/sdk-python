# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .record import Record
from ..._models import BaseModel

__all__ = ["RecordFindUniqueResponse"]


class RecordFindUniqueResponse(BaseModel):
    """Response for a successful get operation."""

    data: Optional[Record] = None
    """Object record with its associated metadata and attribute key-value pairs."""

    status: Literal["success"]
