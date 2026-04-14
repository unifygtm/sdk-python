# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .u_reference_cardinality import UReferenceCardinality

__all__ = ["URelatedReferenceAttributeParam"]


class URelatedReferenceAttributeParam(TypedDict, total=False):
    api_name: Required[str]

    cardinality: Required[UReferenceCardinality]

    display_name: Required[str]
