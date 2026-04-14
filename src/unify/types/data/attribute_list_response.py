# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .u_attribute import UAttribute

__all__ = ["AttributeListResponse"]


class AttributeListResponse(BaseModel):
    """Response for a successful list operation."""

    data: List[UAttribute]

    status: Literal["success"]
