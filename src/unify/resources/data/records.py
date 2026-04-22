# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.data import (
    ValidationMode,
    record_create_params,
    record_update_params,
    record_upsert_params,
    record_find_unique_params,
)
from ..._base_client import make_request_options
from ...types.data.validation_mode import ValidationMode
from ...types.data.record_create_response import RecordCreateResponse
from ...types.data.record_delete_response import RecordDeleteResponse
from ...types.data.record_update_response import RecordUpdateResponse
from ...types.data.record_upsert_response import RecordUpsertResponse
from ...types.data.record_retrieve_response import RecordRetrieveResponse
from ...types.data.u_record_attributes_param import URecordAttributesParam
from ...types.data.record_find_unique_response import RecordFindUniqueResponse

__all__ = ["RecordsResource", "AsyncRecordsResource"]


class RecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return RecordsResourceWithStreamingResponse(self)

    def create(
        self,
        object_name: str,
        *,
        data: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordCreateResponse:
        """
        Args:
          data: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._post(
            path_template("/data/v1/objects/{object_name}/records", object_name=object_name),
            body=maybe_transform({"data": data}, record_create_params.RecordCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"validation_mode": validation_mode}, record_create_params.RecordCreateParams),
            ),
            cast_to=RecordCreateResponse,
        )

    def retrieve(
        self,
        record_id: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._get(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordRetrieveResponse,
        )

    def update(
        self,
        record_id: str,
        *,
        object_name: str,
        data: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordUpdateResponse:
        """
        Args:
          data: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._patch(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            body=maybe_transform({"data": data}, record_update_params.RecordUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"validation_mode": validation_mode}, record_update_params.RecordUpdateParams),
            ),
            cast_to=RecordUpdateResponse,
        )

    def delete(
        self,
        record_id: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return self._delete(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordDeleteResponse,
        )

    def find_unique(
        self,
        object_name: str,
        *,
        match: URecordAttributesParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordFindUniqueResponse:
        """
        Args:
          match: Attribute key-value pairs associated with an object record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._post(
            path_template("/data/v1/objects/{object_name}/records/find-unique", object_name=object_name),
            body=maybe_transform({"match": match}, record_find_unique_params.RecordFindUniqueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordFindUniqueResponse,
        )

    def upsert(
        self,
        object_name: str,
        *,
        match: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        create: URecordAttributesParam | Omit = omit,
        create_or_update: URecordAttributesParam | Omit = omit,
        create_or_update_if_empty: URecordAttributesParam | Omit = omit,
        update: URecordAttributesParam | Omit = omit,
        update_if_empty: URecordAttributesParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordUpsertResponse:
        """
        Args:
          match: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          create: Attribute key-value pairs associated with an object record.

          create_or_update: Attribute key-value pairs associated with an object record.

          create_or_update_if_empty: Attribute key-value pairs associated with an object record.

          update: Attribute key-value pairs associated with an object record.

          update_if_empty: Attribute key-value pairs associated with an object record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._post(
            path_template("/data/v1/objects/{object_name}/records/upsert", object_name=object_name),
            body=maybe_transform(
                {
                    "match": match,
                    "create": create,
                    "create_or_update": create_or_update,
                    "create_or_update_if_empty": create_or_update_if_empty,
                    "update": update,
                    "update_if_empty": update_if_empty,
                },
                record_upsert_params.RecordUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"validation_mode": validation_mode}, record_upsert_params.RecordUpsertParams),
            ),
            cast_to=RecordUpsertResponse,
        )


class AsyncRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unifygtm/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unifygtm/sdk-python#with_streaming_response
        """
        return AsyncRecordsResourceWithStreamingResponse(self)

    async def create(
        self,
        object_name: str,
        *,
        data: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordCreateResponse:
        """
        Args:
          data: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._post(
            path_template("/data/v1/objects/{object_name}/records", object_name=object_name),
            body=await async_maybe_transform({"data": data}, record_create_params.RecordCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"validation_mode": validation_mode}, record_create_params.RecordCreateParams
                ),
            ),
            cast_to=RecordCreateResponse,
        )

    async def retrieve(
        self,
        record_id: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._get(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordRetrieveResponse,
        )

    async def update(
        self,
        record_id: str,
        *,
        object_name: str,
        data: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordUpdateResponse:
        """
        Args:
          data: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._patch(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            body=await async_maybe_transform({"data": data}, record_update_params.RecordUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"validation_mode": validation_mode}, record_update_params.RecordUpdateParams
                ),
            ),
            cast_to=RecordUpdateResponse,
        )

    async def delete(
        self,
        record_id: str,
        *,
        object_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        if not record_id:
            raise ValueError(f"Expected a non-empty value for `record_id` but received {record_id!r}")
        return await self._delete(
            path_template(
                "/data/v1/objects/{object_name}/records/{record_id}", object_name=object_name, record_id=record_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordDeleteResponse,
        )

    async def find_unique(
        self,
        object_name: str,
        *,
        match: URecordAttributesParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordFindUniqueResponse:
        """
        Args:
          match: Attribute key-value pairs associated with an object record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._post(
            path_template("/data/v1/objects/{object_name}/records/find-unique", object_name=object_name),
            body=await async_maybe_transform({"match": match}, record_find_unique_params.RecordFindUniqueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordFindUniqueResponse,
        )

    async def upsert(
        self,
        object_name: str,
        *,
        match: URecordAttributesParam,
        validation_mode: ValidationMode | Omit = omit,
        create: URecordAttributesParam | Omit = omit,
        create_or_update: URecordAttributesParam | Omit = omit,
        create_or_update_if_empty: URecordAttributesParam | Omit = omit,
        update: URecordAttributesParam | Omit = omit,
        update_if_empty: URecordAttributesParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordUpsertResponse:
        """
        Args:
          match: Attribute key-value pairs associated with an object record.

          validation_mode: Validation mode to use when validating request data.

              `strict` validation will fail requests if any attribute fails validation,
              including unrecognized attributes.

              `ignore_invalid` validation will strip out unknown attributes and replace known,
              non-required attributes with `undefined` if they fail validation. The request
              will still fail if the request body does not contain the proper structure or if
              any required attributes fail validation.

          create: Attribute key-value pairs associated with an object record.

          create_or_update: Attribute key-value pairs associated with an object record.

          create_or_update_if_empty: Attribute key-value pairs associated with an object record.

          update: Attribute key-value pairs associated with an object record.

          update_if_empty: Attribute key-value pairs associated with an object record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._post(
            path_template("/data/v1/objects/{object_name}/records/upsert", object_name=object_name),
            body=await async_maybe_transform(
                {
                    "match": match,
                    "create": create,
                    "create_or_update": create_or_update,
                    "create_or_update_if_empty": create_or_update_if_empty,
                    "update": update,
                    "update_if_empty": update_if_empty,
                },
                record_upsert_params.RecordUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"validation_mode": validation_mode}, record_upsert_params.RecordUpsertParams
                ),
            ),
            cast_to=RecordUpsertResponse,
        )


class RecordsResourceWithRawResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_raw_response_wrapper(
            records.create,
        )
        self.retrieve = to_raw_response_wrapper(
            records.retrieve,
        )
        self.update = to_raw_response_wrapper(
            records.update,
        )
        self.delete = to_raw_response_wrapper(
            records.delete,
        )
        self.find_unique = to_raw_response_wrapper(
            records.find_unique,
        )
        self.upsert = to_raw_response_wrapper(
            records.upsert,
        )


class AsyncRecordsResourceWithRawResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_raw_response_wrapper(
            records.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            records.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            records.update,
        )
        self.delete = async_to_raw_response_wrapper(
            records.delete,
        )
        self.find_unique = async_to_raw_response_wrapper(
            records.find_unique,
        )
        self.upsert = async_to_raw_response_wrapper(
            records.upsert,
        )


class RecordsResourceWithStreamingResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_streamed_response_wrapper(
            records.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            records.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            records.update,
        )
        self.delete = to_streamed_response_wrapper(
            records.delete,
        )
        self.find_unique = to_streamed_response_wrapper(
            records.find_unique,
        )
        self.upsert = to_streamed_response_wrapper(
            records.upsert,
        )


class AsyncRecordsResourceWithStreamingResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_streamed_response_wrapper(
            records.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            records.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            records.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            records.delete,
        )
        self.find_unique = async_to_streamed_response_wrapper(
            records.find_unique,
        )
        self.upsert = async_to_streamed_response_wrapper(
            records.upsert,
        )
