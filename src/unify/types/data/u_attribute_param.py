# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .u_reference_cardinality import UReferenceCardinality
from .attributes.u_attribute_option_param import UAttributeOptionParam
from .u_related_reference_attribute_param import URelatedReferenceAttributeParam

__all__ = [
    "UAttributeParam",
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


class UnionMember0(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["ADDRESS"]]
    """The type of value this attribute can hold."""


class UnionMember1(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["BOOLEAN"]]
    """The type of value this attribute can hold."""


class UnionMember2(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["COUNTRY"]]
    """The type of value this attribute can hold."""


class UnionMember3(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["CURRENCY"]]
    """The type of value this attribute can hold."""


class UnionMember4(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["DATE"]]
    """The type of value this attribute can hold."""


class UnionMember5(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["DATETIME"]]
    """The type of value this attribute can hold."""


class UnionMember6(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["DECIMAL"]]
    """The type of value this attribute can hold."""


class UnionMember7(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["EMAIL_ADDRESS"]]
    """The type of value this attribute can hold."""


class UnionMember8(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["INTEGER"]]
    """The type of value this attribute can hold."""


class UnionMember9(TypedDict, total=False):
    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    options: Required[Iterable[UAttributeOptionParam]]
    """The list of options for the attribute."""

    type: Required[Literal["MULTI_SELECT"]]
    """The type of value this attribute can hold."""


class UnionMember10(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["PHONE_NUMBER"]]
    """The type of value this attribute can hold."""


class UnionMember11(TypedDict, total=False):
    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    cardinality: Required[UReferenceCardinality]
    """The cardinality of the reference attribute."""

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    related_attribute: Required[Optional[URelatedReferenceAttributeParam]]
    """The optional related attribute on the referenced object.

    When this exists, the relationship between the two objects is bidirectional.
    """

    related_object: Required[str]
    """The API name of the object that this attribute references."""

    type: Required[Literal["REFERENCE"]]
    """The type of value this attribute can hold."""


class UnionMember12(TypedDict, total=False):
    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    options: Required[Iterable[UAttributeOptionParam]]
    """The list of options for the attribute."""

    type: Required[Literal["SELECT"]]
    """The type of value this attribute can hold."""


class UnionMember13(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["TEXT"]]
    """The type of value this attribute can hold."""


class UnionMember14(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["URL"]]
    """The type of value this attribute can hold."""


class UnionMember15(TypedDict, total=False):
    """Base properties that define an attribute on a Unify object."""

    api_name: Required[str]
    """This is the unique identifier for the attribute at the API level.

    It is unique within the object and cannot be changed.
    """

    description: Required[Optional[str]]
    """This is a description of the attribute.

    It is not required but will be shown in the UI to help understand the purpose of
    the object. Typically, this should be a short sentence or two explaining the
    attribute.
    """

    display_name: Required[str]
    """This is the user-facing attribute name that will be shown within Unify.

    It is unique within the object and can be changed at any time.
    """

    is_required: Required[bool]
    """Whether the attribute is required."""

    is_unique: Required[bool]
    """Whether the attribute is unique."""

    type: Required[Literal["UUID"]]
    """The type of value this attribute can hold."""


UAttributeParam: TypeAlias = Union[
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
