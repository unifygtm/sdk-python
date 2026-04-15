# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.data import object_create_params, object_update_params
from ..._base_client import make_request_options
from ...types.data.object_list_response import ObjectListResponse
from ...types.data.object_create_response import ObjectCreateResponse
from ...types.data.object_delete_response import ObjectDeleteResponse
from ...types.data.object_update_response import ObjectUpdateResponse
from ...types.data.object_retrieve_response import ObjectRetrieveResponse

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectCreateResponse:
        """Args:
          api_name: This is the unique identifier for the object at the API level.

        It is unique
              within Unify and cannot be changed.

          description: This is a description of the object. It is not required but will be shown in the
              UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the object.

          display_name: This is the user-facing object name shown within Unify. It is not required to be
              unique within Unify and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/v1/objects",
            body=maybe_transform(
                {
                    "api_name": api_name,
                    "description": description,
                    "display_name": display_name,
                },
                object_create_params.ObjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreateResponse,
        )

    def retrieve(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectRetrieveResponse:
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
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectRetrieveResponse,
        )

    def update(
        self,
        object_name: str,
        *,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUpdateResponse:
        """Args:
          description: This is a description of the object.

        It is not required but will be shown in the
              UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the object.

          display_name: This is the user-facing object name shown within Unify. It is not required to be
              unique within Unify and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._patch(
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                },
                object_update_params.ObjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectListResponse:
        return self._get(
            "/data/v1/objects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListResponse,
        )

    def delete(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._delete(
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectDeleteResponse,
        )


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_name: str,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectCreateResponse:
        """Args:
          api_name: This is the unique identifier for the object at the API level.

        It is unique
              within Unify and cannot be changed.

          description: This is a description of the object. It is not required but will be shown in the
              UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the object.

          display_name: This is the user-facing object name shown within Unify. It is not required to be
              unique within Unify and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/v1/objects",
            body=await async_maybe_transform(
                {
                    "api_name": api_name,
                    "description": description,
                    "display_name": display_name,
                },
                object_create_params.ObjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreateResponse,
        )

    async def retrieve(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectRetrieveResponse:
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
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectRetrieveResponse,
        )

    async def update(
        self,
        object_name: str,
        *,
        description: Optional[str],
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUpdateResponse:
        """Args:
          description: This is a description of the object.

        It is not required but will be shown in the
              UI to help understand the purpose of the object. Typically, this should be a
              short sentence or two explaining the object.

          display_name: This is the user-facing object name shown within Unify. It is not required to be
              unique within Unify and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._patch(
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                },
                object_update_params.ObjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectListResponse:
        return await self._get(
            "/data/v1/objects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListResponse,
        )

    async def delete(
        self,
        object_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._delete(
            path_template("/data/v1/objects/{object_name}", object_name=object_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectDeleteResponse,
        )


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.create = to_raw_response_wrapper(
            objects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            objects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            objects.update,
        )
        self.list = to_raw_response_wrapper(
            objects.list,
        )
        self.delete = to_raw_response_wrapper(
            objects.delete,
        )


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.create = async_to_raw_response_wrapper(
            objects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            objects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            objects.update,
        )
        self.list = async_to_raw_response_wrapper(
            objects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            objects.delete,
        )


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.create = to_streamed_response_wrapper(
            objects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            objects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            objects.update,
        )
        self.list = to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = to_streamed_response_wrapper(
            objects.delete,
        )


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.create = async_to_streamed_response_wrapper(
            objects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            objects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            objects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            objects.delete,
        )
