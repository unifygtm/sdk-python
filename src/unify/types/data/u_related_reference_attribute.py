# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .u_reference_cardinality import UReferenceCardinality

__all__ = ["URelatedReferenceAttribute"]


class URelatedReferenceAttribute(BaseModel):
    api_name: str

    cardinality: UReferenceCardinality

    display_name: str
