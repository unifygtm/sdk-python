# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unify import Unify, AsyncUnify
from tests.utils import assert_matches_type
from unify.types.data.attributes import (
    OptionListResponse,
    OptionCreateResponse,
    OptionDeleteResponse,
    OptionUpdateResponse,
    OptionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Unify) -> None:
        option = client.data.attributes.options.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        )
        assert_matches_type(OptionCreateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Unify) -> None:
        response = client.data.attributes.options.with_raw_response.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionCreateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Unify) -> None:
        with client.data.attributes.options.with_streaming_response.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionCreateResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.options.with_raw_response.create(
                attribute_name="attribute_name",
                object_name="",
                api_name="api_name",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.options.with_raw_response.create(
                attribute_name="",
                object_name="object_name",
                api_name="api_name",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Unify) -> None:
        option = client.data.attributes.options.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )
        assert_matches_type(OptionRetrieveResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Unify) -> None:
        response = client.data.attributes.options.with_raw_response.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionRetrieveResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Unify) -> None:
        with client.data.attributes.options.with_streaming_response.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionRetrieveResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.options.with_raw_response.retrieve(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.options.with_raw_response.retrieve(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            client.data.attributes.options.with_raw_response.retrieve(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Unify) -> None:
        option = client.data.attributes.options.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        )
        assert_matches_type(OptionUpdateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Unify) -> None:
        response = client.data.attributes.options.with_raw_response.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionUpdateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Unify) -> None:
        with client.data.attributes.options.with_streaming_response.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionUpdateResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.options.with_raw_response.update(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.options.with_raw_response.update(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            client.data.attributes.options.with_raw_response.update(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Unify) -> None:
        option = client.data.attributes.options.list(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(OptionListResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Unify) -> None:
        response = client.data.attributes.options.with_raw_response.list(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionListResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Unify) -> None:
        with client.data.attributes.options.with_streaming_response.list(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionListResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.options.with_raw_response.list(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.options.with_raw_response.list(
                attribute_name="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Unify) -> None:
        option = client.data.attributes.options.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )
        assert_matches_type(OptionDeleteResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Unify) -> None:
        response = client.data.attributes.options.with_raw_response.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionDeleteResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Unify) -> None:
        with client.data.attributes.options.with_streaming_response.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionDeleteResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.options.with_raw_response.delete(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.options.with_raw_response.delete(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            client.data.attributes.options.with_raw_response.delete(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
            )


class TestAsyncOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncUnify) -> None:
        option = await async_client.data.attributes.options.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        )
        assert_matches_type(OptionCreateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.options.with_raw_response.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionCreateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.options.with_streaming_response.create(
            attribute_name="attribute_name",
            object_name="object_name",
            api_name="api_name",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionCreateResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.create(
                attribute_name="attribute_name",
                object_name="",
                api_name="api_name",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.create(
                attribute_name="",
                object_name="object_name",
                api_name="api_name",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnify) -> None:
        option = await async_client.data.attributes.options.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )
        assert_matches_type(OptionRetrieveResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.options.with_raw_response.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionRetrieveResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.options.with_streaming_response.retrieve(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionRetrieveResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.retrieve(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.retrieve(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.retrieve(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncUnify) -> None:
        option = await async_client.data.attributes.options.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        )
        assert_matches_type(OptionUpdateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.options.with_raw_response.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionUpdateResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.options.with_streaming_response.update(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionUpdateResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.update(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.update(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.update(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncUnify) -> None:
        option = await async_client.data.attributes.options.list(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(OptionListResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.options.with_raw_response.list(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionListResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.options.with_streaming_response.list(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionListResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.list(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.list(
                attribute_name="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncUnify) -> None:
        option = await async_client.data.attributes.options.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )
        assert_matches_type(OptionDeleteResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.options.with_raw_response.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionDeleteResponse, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.options.with_streaming_response.delete(
            option_name="option_name",
            object_name="object_name",
            attribute_name="attribute_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionDeleteResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.delete(
                option_name="option_name",
                object_name="",
                attribute_name="attribute_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.delete(
                option_name="option_name",
                object_name="object_name",
                attribute_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_name` but received ''"):
            await async_client.data.attributes.options.with_raw_response.delete(
                option_name="",
                object_name="object_name",
                attribute_name="attribute_name",
            )
