# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.data.attributes import option_create_params, option_update_params
from ....types.data.attributes.option_list_response import OptionListResponse
from ....types.data.attributes.option_create_response import OptionCreateResponse
from ....types.data.attributes.option_delete_response import OptionDeleteResponse
from ....types.data.attributes.option_update_response import OptionUpdateResponse
from ....types.data.attributes.option_retrieve_response import OptionRetrieveResponse

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)

    def create(
        self,
        attribute_name: str,
        *,
        object_name: str,
        api_name: str,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute option at the API level. It is
              unique within the attribute and cannot be changed.

          display_name: This is the user-facing attribute option name that will be shown within Unify.
              It is unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return self._post(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            body=maybe_transform(
                {
                    "api_name": api_name,
                    "display_name": display_name,
                },
                option_create_params.OptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionCreateResponse,
        )

    def retrieve(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionRetrieveResponse:
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
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return self._get(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionRetrieveResponse,
        )

    def update(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionUpdateResponse:
        """
        Args:
          display_name: This is the user-facing attribute option name that will be shown within Unify.
              It is unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return self._patch(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            body=maybe_transform({"display_name": display_name}, option_update_params.OptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionUpdateResponse,
        )

    def list(
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
    ) -> OptionListResponse:
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
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionListResponse,
        )

    def delete(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionDeleteResponse:
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
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return self._delete(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionDeleteResponse,
        )


class AsyncOptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        attribute_name: str,
        *,
        object_name: str,
        api_name: str,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionCreateResponse:
        """
        Args:
          api_name: This is the unique identifier for the attribute option at the API level. It is
              unique within the attribute and cannot be changed.

          display_name: This is the user-facing attribute option name that will be shown within Unify.
              It is unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        return await self._post(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            body=await async_maybe_transform(
                {
                    "api_name": api_name,
                    "display_name": display_name,
                },
                option_create_params.OptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionCreateResponse,
        )

    async def retrieve(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionRetrieveResponse:
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
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return await self._get(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionRetrieveResponse,
        )

    async def update(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionUpdateResponse:
        """
        Args:
          display_name: This is the user-facing attribute option name that will be shown within Unify.
              It is unique within the object and can be changed at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not attribute_name:
            raise ValueError(f"Expected a non-empty value for `attribute_name` but received {attribute_name!r}")
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return await self._patch(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            body=await async_maybe_transform({"display_name": display_name}, option_update_params.OptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionUpdateResponse,
        )

    async def list(
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
    ) -> OptionListResponse:
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
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options",
                object_name=object_name,
                attribute_name=attribute_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionListResponse,
        )

    async def delete(
        self,
        option_name: str,
        *,
        object_name: str,
        attribute_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionDeleteResponse:
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
        if not option_name:
            raise ValueError(f"Expected a non-empty value for `option_name` but received {option_name!r}")
        return await self._delete(
            path_template(
                "/data/v1/objects/{object_name}/attributes/{attribute_name}/options/{option_name}",
                object_name=object_name,
                attribute_name=attribute_name,
                option_name=option_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptionDeleteResponse,
        )


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.create = to_raw_response_wrapper(
            options.create,
        )
        self.retrieve = to_raw_response_wrapper(
            options.retrieve,
        )
        self.update = to_raw_response_wrapper(
            options.update,
        )
        self.list = to_raw_response_wrapper(
            options.list,
        )
        self.delete = to_raw_response_wrapper(
            options.delete,
        )


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.create = async_to_raw_response_wrapper(
            options.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            options.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            options.update,
        )
        self.list = async_to_raw_response_wrapper(
            options.list,
        )
        self.delete = async_to_raw_response_wrapper(
            options.delete,
        )


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.create = to_streamed_response_wrapper(
            options.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            options.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            options.update,
        )
        self.list = to_streamed_response_wrapper(
            options.list,
        )
        self.delete = to_streamed_response_wrapper(
            options.delete,
        )


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.create = async_to_streamed_response_wrapper(
            options.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            options.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            options.update,
        )
        self.list = async_to_streamed_response_wrapper(
            options.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            options.delete,
        )
