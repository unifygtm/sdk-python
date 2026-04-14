# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .u_object import UObject
from ..._models import BaseModel

__all__ = ["ObjectUpdateResponse"]


class ObjectUpdateResponse(BaseModel):
    """Response for a successful update operation."""

    data: UObject

    status: Literal["success"]
