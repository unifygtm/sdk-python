# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ObjectCreateParams"]


class ObjectCreateParams(TypedDict, total=False):
    api_name: Required[str]
    """This is the unique identifier for the object at the API level.

    It is unique within Unify and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the object.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    object.
    """

    display_name: Required[str]
    """This is the user-facing object name shown within Unify.

    It is not required to be unique within Unify and can be changed at any time.
    """
