# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .u_object import UObject
from ..._models import BaseModel

__all__ = ["ObjectCreateResponse"]


class ObjectCreateResponse(BaseModel):
    """Response for a successful create operation."""

    data: UObject

    status: Literal["success"]
