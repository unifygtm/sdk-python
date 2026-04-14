# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["UReferenceByMatchParam"]


class UReferenceByMatchParam(TypedDict, total=False):
    """Reference to another object record by match criteria.

    This will find an existing record using the provided match criteria, and
    `null` will be returned if no match is found.
    """

    match: Required[Dict[str, object]]
    """The attribute values to match against to find an existing record.

    At least one unique attribute must be included to ensure that at most one record
    is matched. Additional unique or non-unique attributes may also be included to
    refine the matching criteria.
    """
