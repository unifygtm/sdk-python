# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unify import Unify, AsyncUnify
from tests.utils import assert_matches_type
from unify.types.data import (
    ObjectListResponse,
    ObjectCreateResponse,
    ObjectDeleteResponse,
    ObjectUpdateResponse,
    ObjectRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Unify) -> None:
        object_ = client.data.objects.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Unify) -> None:
        response = client.data.objects.with_raw_response.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Unify) -> None:
        with client.data.objects.with_streaming_response.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectCreateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Unify) -> None:
        object_ = client.data.objects.retrieve(
            "object_name",
        )
        assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Unify) -> None:
        response = client.data.objects.with_raw_response.retrieve(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Unify) -> None:
        with client.data.objects.with_streaming_response.retrieve(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.objects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Unify) -> None:
        object_ = client.data.objects.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Unify) -> None:
        response = client.data.objects.with_raw_response.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Unify) -> None:
        with client.data.objects.with_streaming_response.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.objects.with_raw_response.update(
                object_name="",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Unify) -> None:
        object_ = client.data.objects.list()
        assert_matches_type(ObjectListResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Unify) -> None:
        response = client.data.objects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectListResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Unify) -> None:
        with client.data.objects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectListResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Unify) -> None:
        object_ = client.data.objects.delete(
            "object_name",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Unify) -> None:
        response = client.data.objects.with_raw_response.delete(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Unify) -> None:
        with client.data.objects.with_streaming_response.delete(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.objects.with_raw_response.delete(
                "",
            )


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncUnify) -> None:
        object_ = await async_client.data.objects.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.objects.with_raw_response.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnify) -> None:
        async with async_client.data.objects.with_streaming_response.create(
            api_name="api_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectCreateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnify) -> None:
        object_ = await async_client.data.objects.retrieve(
            "object_name",
        )
        assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.objects.with_raw_response.retrieve(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnify) -> None:
        async with async_client.data.objects.with_streaming_response.retrieve(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectRetrieveResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.objects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncUnify) -> None:
        object_ = await async_client.data.objects.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.objects.with_raw_response.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnify) -> None:
        async with async_client.data.objects.with_streaming_response.update(
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectUpdateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.objects.with_raw_response.update(
                object_name="",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncUnify) -> None:
        object_ = await async_client.data.objects.list()
        assert_matches_type(ObjectListResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.objects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectListResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnify) -> None:
        async with async_client.data.objects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectListResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncUnify) -> None:
        object_ = await async_client.data.objects.delete(
            "object_name",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.objects.with_raw_response.delete(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnify) -> None:
        async with async_client.data.objects.with_streaming_response.delete(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.objects.with_raw_response.delete(
                "",
            )
