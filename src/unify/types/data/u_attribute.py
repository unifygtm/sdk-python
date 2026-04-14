# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .u_reference_cardinality import UReferenceCardinality
from .attributes.u_attribute_option import UAttributeOption
from .u_related_reference_attribute import URelatedReferenceAttribute

__all__ = [
    "UAttribute",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
    "UnionMember7",
    "UnionMember8",
    "UnionMember9",
    "UnionMember10",
    "UnionMember11",
    "UnionMember12",
    "UnionMember13",
    "UnionMember14",
    "UnionMember15",
]


class UnionMember0(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["ADDRESS"]
    """The type of value this attribute can hold."""


class UnionMember1(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["BOOLEAN"]
    """The type of value this attribute can hold."""


class UnionMember2(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["COUNTRY"]
    """The type of value this attribute can hold."""


class UnionMember3(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["CURRENCY"]
    """The type of value this attribute can hold."""


class UnionMember4(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["DATE"]
    """The type of value this attribute can hold."""


class UnionMember5(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["DATETIME"]
    """The type of value this attribute can hold."""


class UnionMember6(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["DECIMAL"]
    """The type of value this attribute can hold."""


class UnionMember7(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["EMAIL_ADDRESS"]
    """The type of value this attribute can hold."""


class UnionMember8(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["INTEGER"]
    """The type of value this attribute can hold."""


class UnionMember9(BaseModel):
    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    options: List[UAttributeOption]
    """The list of options for the attribute."""

    type: Literal["MULTI_SELECT"]
    """The type of value this attribute can hold."""


class UnionMember10(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["PHONE_NUMBER"]
    """The type of value this attribute can hold."""


class UnionMember11(BaseModel):
    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    cardinality: UReferenceCardinality
    """The cardinality of the reference attribute."""

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    related_attribute: Optional[URelatedReferenceAttribute] = None
    """The optional related attribute on the referenced object.

    When this exists, the relationship between the two objects is bidirectional.
    """

    related_object: str
    """The API name of the object that this attribute references."""

    type: Literal["REFERENCE"]
    """The type of value this attribute can hold."""


class UnionMember12(BaseModel):
    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    options: List[UAttributeOption]
    """The list of options for the attribute."""

    type: Literal["SELECT"]
    """The type of value this attribute can hold."""


class UnionMember13(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["TEXT"]
    """The type of value this attribute can hold."""


class UnionMember14(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["URL"]
    """The type of value this attribute can hold."""


class UnionMember15(BaseModel):
    """Base properties that define an attribute on a Unify object."""

    api_name: str
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Optional[str] = None
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: str
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: bool
    """Whether the attribute is required."""

    is_unique: bool
    """Whether the attribute is unique."""

    type: Literal["UUID"]
    """The type of value this attribute can hold."""


UAttribute: TypeAlias = Union[
    UnionMember0,
    UnionMember1,
    UnionMember2,
    UnionMember3,
    UnionMember4,
    UnionMember5,
    UnionMember6,
    UnionMember7,
    UnionMember8,
    UnionMember9,
    UnionMember10,
    UnionMember11,
    UnionMember12,
    UnionMember13,
    UnionMember14,
    UnionMember15,
]
