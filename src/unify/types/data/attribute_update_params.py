# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .u_reference_cardinality import UReferenceCardinality
from .u_related_reference_attribute_param import URelatedReferenceAttributeParam
from .u_attribute_option_update_item_param import UAttributeOptionUpdateItemParam

__all__ = [
    "AttributeUpdateParams",
    "Variant0",
    "Variant1",
    "Variant2",
    "Variant3",
    "Variant4",
    "Variant5",
    "Variant6",
    "Variant7",
    "Variant8",
    "UObjectsUMultiSelectAttributeUpdate",
    "Variant10",
    "UObjectsUReferenceAttributeUpdate",
    "UObjectsUSelectAttributeUpdate",
    "Variant13",
    "Variant14",
    "Variant15",
]


class Variant0(TypedDict, total=False):
    object_name: Required[str]

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


class Variant1(TypedDict, total=False):
    object_name: Required[str]

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


class Variant2(TypedDict, total=False):
    object_name: Required[str]

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


class Variant3(TypedDict, total=False):
    object_name: Required[str]

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


class Variant4(TypedDict, total=False):
    object_name: Required[str]

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


class Variant5(TypedDict, total=False):
    object_name: Required[str]

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


class Variant6(TypedDict, total=False):
    object_name: Required[str]

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


class Variant7(TypedDict, total=False):
    object_name: Required[str]

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


class Variant8(TypedDict, total=False):
    object_name: Required[str]

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


class UObjectsUMultiSelectAttributeUpdate(TypedDict, total=False):
    object_name: Required[str]

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

    options: Required[Iterable[UAttributeOptionUpdateItemParam]]
    """The list of options for the attribute."""


class Variant10(TypedDict, total=False):
    object_name: Required[str]

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


class UObjectsUReferenceAttributeUpdate(TypedDict, total=False):
    object_name: Required[str]

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

    related_attribute: Required[Optional[URelatedReferenceAttributeParam]]
    """The optional related attribute on the referenced object.

    When this exists, the relationship between the two objects is bidirectional.
    """

    related_object: Required[str]
    """The API name of the object that this attribute references."""


class UObjectsUSelectAttributeUpdate(TypedDict, total=False):
    object_name: Required[str]

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

    options: Required[Iterable[UAttributeOptionUpdateItemParam]]
    """The list of options for the attribute."""


class Variant13(TypedDict, total=False):
    object_name: Required[str]

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


class Variant14(TypedDict, total=False):
    object_name: Required[str]

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


class Variant15(TypedDict, total=False):
    object_name: Required[str]

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


AttributeUpdateParams: TypeAlias = Union[
    Variant0,
    Variant1,
    Variant2,
    Variant3,
    Variant4,
    Variant5,
    Variant6,
    Variant7,
    Variant8,
    UObjectsUMultiSelectAttributeUpdate,
    Variant10,
    UObjectsUReferenceAttributeUpdate,
    UObjectsUSelectAttributeUpdate,
    Variant13,
    Variant14,
    Variant15,
]
