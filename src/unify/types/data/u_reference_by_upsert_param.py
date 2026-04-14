# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["UReferenceByUpsertParam"]


class UReferenceByUpsertParam(TypedDict, total=False):
    """Reference to another object record by performing a nested upsert.

    At least one of `create`, `create_or_update` or `create_or_update_if_empty`
    must be provided, and all required attributes on the object must be included
    in at least one of these properties.

    ## Precedence

    When the same attribute is specified in multiple properties, the values will
    be applied in a specific order of precedence. If a record is being created,
    the following order is used:

    1. `create`
    2. `create_or_update`
    3. `create_or_update_if_empty`

    If an existing record is being updated, the following order is used:

    1. `update`
    2. `create_or_update`
    3. `update_if_empty`
    4. `create_or_update_if_empty`
    """

    match: Required[Dict[str, object]]
    """The attribute values to match against to find an existing record.

    At least one unique attribute must be included to ensure that at most one record
    is matched. Additional unique or non-unique attributes may also be included to
    refine the matching criteria.
    """

    create: Dict[str, object]
    """The attribute values to use when creating a new record if no match is found."""

    create_or_update: Dict[str, object]
    """The attribute values to apply during both creation and update operations."""

    create_or_update_if_empty: Dict[str, object]
    """
    The attribute values to apply during both creation and update-if-empty
    operations.
    """

    update: Dict[str, object]
    """
    The attribute values to use when updating an existing record if a match is
    found.
    """

    update_if_empty: Dict[str, object]
    """
    The attribute values to update when a matching record is found and the existing
    attribute value on the record is `null`.
    """
