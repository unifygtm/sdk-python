# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from .options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.data import (
    UReferenceCardinality,
    attribute_create_params,
    attribute_update_params,
)
from ...._base_client import make_request_options
from ....types.data.attribute_list_response import AttributeListResponse
from ....types.data.u_reference_cardinality import UReferenceCardinality
from ....types.data.attribute_create_response import AttributeCreateResponse
from ....types.data.attribute_delete_response import AttributeDeleteResponse
from ....types.data.attribute_update_response import AttributeUpdateResponse
from ....types.data.attribute_retrieve_response import AttributeRetrieveResponse
from ....types.data.attributes.u_attribute_option_param import UAttributeOptionParam
from ....types.data.u_related_reference_attribute_param import URelatedReferenceAttributeParam
from ....types.data.u_attribute_option_update_item_param import UAttributeOptionUpdateItemParam

__all__ = ["AttributesResource", "AsyncAttributesResource"]


class AttributesResource(SyncAPIResource):
    @cached_property
    def options(self) -> OptionsResource:
        return OptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AttributesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttributesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return AttributesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["ADDRESS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["BOOLEAN"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["COUNTRY"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["CURRENCY"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DATE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DATETIME"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DECIMAL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["EMAIL_ADDRESS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["INTEGER"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        options: Iterable[UAttributeOptionParam],
        type: Literal["MULTI_SELECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          options: The list of options for the attribute.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["PHONE_NUMBER"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        cardinality: UReferenceCardinality,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        related_attribute: Optional[URelatedReferenceAttributeParam],
        related_object: str,
        type: Literal["REFERENCE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          cardinality: The cardinality of the reference attribute.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          related_attribute: The optional related attribute on the referenced object. When this exists, the
              relationship between the two objects is bidirectional.

          related_object: The API name of the object that this attribute references.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        options: Iterable[UAttributeOptionParam],
        type: Literal["SELECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          options: The list of options for the attribute.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["TEXT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["URL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["UUID"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["api_name", "description", "display_name", "is_required", "is_unique", "type"],
        ["api_name", "description", "display_name", "is_required", "is_unique", "options", "type"],
        [
            "api_name",
            "cardinality",
            "description",
            "display_name",
            "is_required",
            "is_unique",
            "related_attribute",
            "related_object",
            "type",
        ],
    )
    def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["ADDRESS"]
        | Literal["BOOLEAN"]
        | Literal["COUNTRY"]
        | Literal["CURRENCY"]
        | Literal["DATE"]
        | Literal["DATETIME"]
        | Literal["DECIMAL"]
        | Literal["EMAIL_ADDRESS"]
        | Literal["INTEGER"]
        | Literal["MULTI_SELECT"]
        | Literal["PHONE_NUMBER"]
        | Literal["REFERENCE"]
        | Literal["SELECT"]
        | Literal["TEXT"]
        | Literal["URL"]
        | Literal["UUID"],
        options: Iterable[UAttributeOptionParam] | Omit = omit,
        cardinality: UReferenceCardinality | Omit = omit,
        related_attribute: Optional[URelatedReferenceAttributeParam] | Omit = omit,
        related_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._post(
            path_template("/data/v1/objects/{object_name}/attributes", object_name=object_name),
            body=maybe_transform(
                {
                    "api_name": api_name,
                    "description": description,
                    "display_name": display_name,
                    "is_required": is_required,
                    "is_unique": is_unique,
                    "type": type,
                    "options": options,
                    "cardinality": cardinality,
                    "related_attribute": related_attribute,
                    "related_object": related_object,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeCreateResponse,
        )

    def retrieve(
        self,
        attribute_name: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return self._get(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeRetrieveResponse,
        )

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          options: The list of options for the attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        cardinality: UReferenceCardinality,
        description: Optional[str],
        display_name: str,
        related_attribute: Optional[URelatedReferenceAttributeParam],
        related_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """
        Args:
          cardinality: The cardinality of the reference attribute.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          related_attribute: The optional related attribute on the referenced object. When this exists, the
              relationship between the two objects is bidirectional.

          related_object: The API name of the object that this attribute references.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          options: The list of options for the attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["object_name", "description", "display_name"],
        ["object_name", "description", "display_name", "options"],
        ["object_name", "cardinality", "description", "display_name", "related_attribute", "related_object"],
    )
    def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam] | Omit = omit,
        cardinality: UReferenceCardinality | Omit = omit,
        related_attribute: Optional[URelatedReferenceAttributeParam] | Omit = omit,
        related_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return self._patch(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "options": options,
                    "cardinality": cardinality,
                    "related_attribute": related_attribute,
                    "related_object": related_object,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeUpdateResponse,
        )

    def list(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._get(
            path_template("/data/v1/objects/{object_name}/attributes", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeListResponse,
        )

    def delete(
        self,
        attribute_name: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return self._delete(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeDeleteResponse,
        )


class AsyncAttributesResource(AsyncAPIResource):
    @cached_property
    def options(self) -> AsyncOptionsResource:
        return AsyncOptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttributesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttributesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return AsyncAttributesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["ADDRESS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["BOOLEAN"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["COUNTRY"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["CURRENCY"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DATE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DATETIME"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["DECIMAL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["EMAIL_ADDRESS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["INTEGER"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        options: Iterable[UAttributeOptionParam],
        type: Literal["MULTI_SELECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          options: The list of options for the attribute.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["PHONE_NUMBER"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        cardinality: UReferenceCardinality,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        related_attribute: Optional[URelatedReferenceAttributeParam],
        related_object: str,
        type: Literal["REFERENCE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          cardinality: The cardinality of the reference attribute.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          related_attribute: The optional related attribute on the referenced object. When this exists, the
              relationship between the two objects is bidirectional.

          related_object: The API name of the object that this attribute references.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        options: Iterable[UAttributeOptionParam],
        type: Literal["SELECT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          options: The list of options for the attribute.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["TEXT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["URL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["UUID"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute at the API level. It is unique
              within the object and cannot be changed.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          is_required: Whether the attribute is required.

          is_unique: Whether the attribute is unique.

          type: The type of value this attribute can hold.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["api_name", "description", "display_name", "is_required", "is_unique", "type"],
        ["api_name", "description", "display_name", "is_required", "is_unique", "options", "type"],
        [
            "api_name",
            "cardinality",
            "description",
            "display_name",
            "is_required",
            "is_unique",
            "related_attribute",
            "related_object",
            "type",
        ],
    )
    async def create(
        self,
        object_name: str,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        is_required: bool,
        is_unique: bool,
        type: Literal["ADDRESS"]
        | Literal["BOOLEAN"]
        | Literal["COUNTRY"]
        | Literal["CURRENCY"]
        | Literal["DATE"]
        | Literal["DATETIME"]
        | Literal["DECIMAL"]
        | Literal["EMAIL_ADDRESS"]
        | Literal["INTEGER"]
        | Literal["MULTI_SELECT"]
        | Literal["PHONE_NUMBER"]
        | Literal["REFERENCE"]
        | Literal["SELECT"]
        | Literal["TEXT"]
        | Literal["URL"]
        | Literal["UUID"],
        options: Iterable[UAttributeOptionParam] | Omit = omit,
        cardinality: UReferenceCardinality | Omit = omit,
        related_attribute: Optional[URelatedReferenceAttributeParam] | Omit = omit,
        related_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeCreateResponse:
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._post(
            path_template("/data/v1/objects/{object_name}/attributes", object_name=object_name),
            body=await async_maybe_transform(
                {
                    "api_name": api_name,
                    "description": description,
                    "display_name": display_name,
                    "is_required": is_required,
                    "is_unique": is_unique,
                    "type": type,
                    "options": options,
                    "cardinality": cardinality,
                    "related_attribute": related_attribute,
                    "related_object": related_object,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeCreateResponse,
        )

    async def retrieve(
        self,
        attribute_name: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return await self._get(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeRetrieveResponse,
        )

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          options: The list of options for the attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        cardinality: UReferenceCardinality,
        description: Optional[str],
        display_name: str,
        related_attribute: Optional[URelatedReferenceAttributeParam],
        related_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """
        Args:
          cardinality: The cardinality of the reference attribute.

          description: This is a description of the attribute. It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          related_attribute: The optional related attribute on the referenced object. When this exists, the
              relationship between the two objects is bidirectional.

          related_object: The API name of the object that this attribute references.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          options: The list of options for the attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        """Args:
          description: This is a description of the attribute.

        It is not required but will be shown in
              the UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the attribute.

          display_name: This is the user-facing attribute name that will be shown within Unify. It is
              unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["object_name", "description", "display_name"],
        ["object_name", "description", "display_name", "options"],
        ["object_name", "cardinality", "description", "display_name", "related_attribute", "related_object"],
    )
    async def update(
        self,
        attribute_name: str,
        *,
        object_name: str,
        description: Optional[str],
        display_name: str,
        options: Iterable[UAttributeOptionUpdateItemParam] | Omit = omit,
        cardinality: UReferenceCardinality | Omit = omit,
        related_attribute: Optional[URelatedReferenceAttributeParam] | Omit = omit,
        related_object: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeUpdateResponse:
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return await self._patch(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "options": options,
                    "cardinality": cardinality,
                    "related_attribute": related_attribute,
                    "related_object": related_object,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeUpdateResponse,
        )

    async def list(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._get(
            path_template("/data/v1/objects/{object_name}/attributes", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeListResponse,
        )

    async def delete(
        self,
        attribute_name: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttributeDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return await self._delete(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttributeDeleteResponse,
        )


class AttributesResourceWithRawResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_raw_response_wrapper(
            attributes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            attributes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            attributes.update,
        )
        self.list = to_raw_response_wrapper(
            attributes.list,
        )
        self.delete = to_raw_response_wrapper(
            attributes.delete,
        )

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        return OptionsResourceWithRawResponse(self._attributes.options)


class AsyncAttributesResourceWithRawResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_raw_response_wrapper(
            attributes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            attributes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            attributes.update,
        )
        self.list = async_to_raw_response_wrapper(
            attributes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            attributes.delete,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        return AsyncOptionsResourceWithRawResponse(self._attributes.options)


class AttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_streamed_response_wrapper(
            attributes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            attributes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            attributes.update,
        )
        self.list = to_streamed_response_wrapper(
            attributes.list,
        )
        self.delete = to_streamed_response_wrapper(
            attributes.delete,
        )

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        return OptionsResourceWithStreamingResponse(self._attributes.options)


class AsyncAttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_streamed_response_wrapper(
            attributes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            attributes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            attributes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            attributes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            attributes.delete,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        return AsyncOptionsResourceWithStreamingResponse(self._attributes.options)
