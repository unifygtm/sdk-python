# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .uuid import Uuid

__all__ = ["ReferenceByIDParam"]


class ReferenceByIDParam(TypedDict, total=False):
    """Reference to another object record by ID.

    This will find an existing record by its ID, and an error will be returned if
    the record does not exist.
    """

    id: Required[Uuid]
    """String UUIDv4 value."""
