# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .record import Record
from ..._models import BaseModel

__all__ = ["RecordRetrieveResponse"]


class RecordRetrieveResponse(BaseModel):
    """Response for a successful get operation."""

    data: Record
    """Object record with its associated metadata and attribute key-value pairs."""

    status: Literal["success"]
