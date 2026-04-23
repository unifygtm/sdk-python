# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .u_uuid import UUuid

__all__ = ["UReferenceByIDParam"]


class UReferenceByIDParam(TypedDict, total=False):
    """Reference to another object record by ID.

    This will find an existing record by its ID, and an error will be returned if
    the record does not exist.
    """

    id: Required[UUuid]
    """String UUIDv4 value."""
