# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UAttributeOptionParam"]


class UAttributeOptionParam(TypedDict, total=False):
    """Definition of an option for a `SELECT` or `MULTI_SELECT` attribute."""

    api_name: Required[str]
    """This is the unique identifier for the attribute option at the API level.

    It is unique within the attribute and cannot be changed.
    """

    display_name: Required[str]
    """This is the user-facing attribute option name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """
