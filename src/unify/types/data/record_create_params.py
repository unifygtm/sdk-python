# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .validation_mode import ValidationMode
from .u_record_attributes_param import URecordAttributesParam

__all__ = ["RecordCreateParams"]


class RecordCreateParams(TypedDict, total=False):
    data: Required[URecordAttributesParam]
    """Attribute key-value pairs associated with an object record."""

    validation_mode: ValidationMode
    """Validation mode to use when validating request data.

    `strict` validation will fail requests if any attribute fails validation,
    including unrecognized attributes.

    `ignore_invalid` validation will strip out unknown attributes and replace known,
    non-required attributes with `undefined` if they fail validation. The request
    will still fail if the request body does not contain the proper structure or if
    any required attributes fail validation.
    """
