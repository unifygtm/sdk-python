# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UObject"]


class UObject(BaseModel):
    api_name: str
    """This is the unique identifier for the object at the API level.

    It is unique within Unify and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the object.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    object.
    """

    display_name: str
    """This is the user-facing object name shown within Unify.

    It is not required to be unique within Unify and can be changed at any time.
    """

    provider: Literal["UNIFY", "CUSTOMER"]
    """Represents who created and manages an object in Unify.

    In most ways, all objects within the Unify platform behave the same way
    regardless of whether they are defined by Unify or as custom objects by a plugin
    or user. This includes the ability to define custom attributes and access
    records via API.

    However, there are some subtle distinctions that require differentiating between
    these classifications of objects. This enumeration is used to represent these
    distinctions.
    """
