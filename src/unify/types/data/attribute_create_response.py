# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .u_attribute import UAttribute

__all__ = ["AttributeCreateResponse"]


class AttributeCreateResponse(BaseModel):
    """Response for a successful create operation."""

    data: UAttribute
    """Definition of an attribute on a Unify object."""

    status: Literal["success"]
