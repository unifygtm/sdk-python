# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)
from .records import (
    RecordsResource,
    AsyncRecordsResource,
    RecordsResourceWithRawResponse,
    AsyncRecordsResourceWithRawResponse,
    RecordsResourceWithStreamingResponse,
    AsyncRecordsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .attributes.attributes import (
    AttributesResource,
    AsyncAttributesResource,
    AttributesResourceWithRawResponse,
    AsyncAttributesResourceWithRawResponse,
    AttributesResourceWithStreamingResponse,
    AsyncAttributesResourceWithStreamingResponse,
)

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def attributes(self) -> AttributesResource:
        return AttributesResource(self._client)

    @cached_property
    def records(self) -> RecordsResource:
        return RecordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unify-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unify-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def attributes(self) -> AsyncAttributesResource:
        return AsyncAttributesResource(self._client)

    @cached_property
    def records(self) -> AsyncRecordsResource:
        return AsyncRecordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unify-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._data.objects)

    @cached_property
    def attributes(self) -> AttributesResourceWithRawResponse:
        return AttributesResourceWithRawResponse(self._data.attributes)

    @cached_property
    def records(self) -> RecordsResourceWithRawResponse:
        return RecordsResourceWithRawResponse(self._data.records)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._data.objects)

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithRawResponse:
        return AsyncAttributesResourceWithRawResponse(self._data.attributes)

    @cached_property
    def records(self) -> AsyncRecordsResourceWithRawResponse:
        return AsyncRecordsResourceWithRawResponse(self._data.records)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._data.objects)

    @cached_property
    def attributes(self) -> AttributesResourceWithStreamingResponse:
        return AttributesResourceWithStreamingResponse(self._data.attributes)

    @cached_property
    def records(self) -> RecordsResourceWithStreamingResponse:
        return RecordsResourceWithStreamingResponse(self._data.records)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._data.objects)

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithStreamingResponse:
        return AsyncAttributesResourceWithStreamingResponse(self._data.attributes)

    @cached_property
    def records(self) -> AsyncRecordsResourceWithStreamingResponse:
        return AsyncRecordsResourceWithStreamingResponse(self._data.records)
