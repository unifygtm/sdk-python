# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OptionDeleteResponse"]


class OptionDeleteResponse(BaseModel):
    """Response for a successful delete operation."""

    status: Literal["success"]
