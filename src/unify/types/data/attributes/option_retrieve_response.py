# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel
from .u_attribute_option import UAttributeOption

__all__ = ["OptionRetrieveResponse"]


class OptionRetrieveResponse(BaseModel):
    """Response for a successful get operation."""

    data: UAttributeOption
    """Definition of an option for a `SELECT` or `MULTI_SELECT` attribute."""

    status: Literal["success"]
