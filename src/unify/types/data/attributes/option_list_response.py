# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel
from .u_attribute_option import UAttributeOption

__all__ = ["OptionListResponse"]


class OptionListResponse(BaseModel):
    """Response for a successful list operation."""

    data: List[UAttributeOption]

    status: Literal["success"]
