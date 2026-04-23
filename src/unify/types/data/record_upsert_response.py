# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .u_record import URecord
from ..._models import BaseModel

__all__ = ["RecordUpsertResponse"]


class RecordUpsertResponse(BaseModel):
    """Response for a successful update operation."""

    data: URecord
    """Object record with its associated metadata and attribute key-value pairs."""

    status: Literal["success"]
