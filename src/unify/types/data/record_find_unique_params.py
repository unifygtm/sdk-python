# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .u_record_attributes_param import URecordAttributesParam

__all__ = ["RecordFindUniqueParams"]


class RecordFindUniqueParams(TypedDict, total=False):
    match: Required[URecordAttributesParam]
    """Attribute key-value pairs associated with an object record."""
