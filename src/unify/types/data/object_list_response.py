# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .u_object import UObject
from ..._models import BaseModel

__all__ = ["ObjectListResponse"]


class ObjectListResponse(BaseModel):
    """Response for a successful list operation."""

    data: List[UObject]

    status: Literal["success"]
