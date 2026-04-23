# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .record_attributes_param import RecordAttributesParam

__all__ = ["RecordFindUniqueParams"]


class RecordFindUniqueParams(TypedDict, total=False):
    match: Required[RecordAttributesParam]
    """Attribute key-value pairs associated with an object record."""
