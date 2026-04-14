# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unify import Unify, AsyncUnify
from tests.utils import assert_matches_type
from unify.types.data import (
    AttributeListResponse,
    AttributeCreateResponse,
    AttributeDeleteResponse,
    AttributeUpdateResponse,
    AttributeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttributes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="ADDRESS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="BOOLEAN",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_3(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="COUNTRY",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_4(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="CURRENCY",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_5(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DATE",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_6(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_6(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DATETIME",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_7(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_7(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DECIMAL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_8(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_8(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="EMAIL_ADDRESS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_9(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_9(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="INTEGER",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_10(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_10(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                options=[
                    {
                        "api_name": "api_name",
                        "display_name": "display_name",
                    }
                ],
                type="MULTI_SELECT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_11(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_11(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_11(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_11(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="PHONE_NUMBER",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_12(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_12(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_12(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_12(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
                type="REFERENCE",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_13(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_13(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_13(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_13(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                options=[
                    {
                        "api_name": "api_name",
                        "display_name": "display_name",
                    }
                ],
                type="SELECT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_14(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_14(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_14(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_14(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="TEXT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_15(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_15(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_15(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_15(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="URL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_16(self, client: Unify) -> None:
        attribute = client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_16(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_16(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_16(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="UUID",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Unify) -> None:
        attribute = client.data.attributes.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.retrieve(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.retrieve(
                attribute_name="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_5(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_6(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_6(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_7(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_7(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_8(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_8(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_9(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_9(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_9(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_9(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_10(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_10(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_10(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_10(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_11(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_11(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_11(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_11(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_12(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_12(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_12(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_12(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_13(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_13(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_13(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_13(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_14(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_14(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_14(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_14(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_15(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_15(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_15(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_15(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_16(self, client: Unify) -> None:
        attribute = client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_16(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_16(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_16(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Unify) -> None:
        attribute = client.data.attributes.list(
            "object_name",
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.list(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.list(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeListResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Unify) -> None:
        attribute = client.data.attributes.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Unify) -> None:
        response = client.data.attributes.with_raw_response.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = response.parse()
        assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Unify) -> None:
        with client.data.attributes.with_streaming_response.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = response.parse()
            assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.attributes.with_raw_response.delete(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            client.data.attributes.with_raw_response.delete(
                attribute_name="",
                object_name="object_name",
            )


class TestAsyncAttributes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="ADDRESS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="BOOLEAN",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="COUNTRY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="COUNTRY",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="CURRENCY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="CURRENCY",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DATE",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DATETIME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DATETIME",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="DECIMAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="DECIMAL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="EMAIL_ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="EMAIL_ADDRESS",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="INTEGER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="INTEGER",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="MULTI_SELECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                options=[
                    {
                        "api_name": "api_name",
                        "display_name": "display_name",
                    }
                ],
                type="MULTI_SELECT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="PHONE_NUMBER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_11(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="PHONE_NUMBER",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
            type="REFERENCE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_12(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
                type="REFERENCE",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            options=[
                {
                    "api_name": "api_name",
                    "display_name": "display_name",
                }
            ],
            type="SELECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_13(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                options=[
                    {
                        "api_name": "api_name",
                        "display_name": "display_name",
                    }
                ],
                type="SELECT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="TEXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_14(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="TEXT",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_15(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_15(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="URL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        )
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_16(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.create(
            object_name="object_name",
            api_name="api_name",
            description="description",
            display_name="display_name",
            is_required=True,
            is_unique=True,
            type="UUID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeCreateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_16(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.create(
                object_name="",
                api_name="api_name",
                description="description",
                display_name="display_name",
                is_required=True,
                is_unique=True,
                type="UUID",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.retrieve(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeRetrieveResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.retrieve(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.retrieve(
                attribute_name="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_11(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_12(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            cardinality="ONE",
            description="description",
            display_name="display_name",
            related_attribute={
                "api_name": "api_name",
                "cardinality": "ONE",
                "display_name": "display_name",
            },
            related_object="related_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_12(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                cardinality="ONE",
                description="description",
                display_name="display_name",
                related_attribute={
                    "api_name": "api_name",
                    "cardinality": "ONE",
                    "display_name": "display_name",
                },
                related_object="related_object",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_13(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_13(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_13(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
            options=[{"display_name": "display_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_13(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
                options=[{"display_name": "display_name"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_14(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_14(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_14(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_14(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_15(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_15(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_15(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_15(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_16(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_16(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_16(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.update(
            attribute_name="attribute_name",
            object_name="object_name",
            description="description",
            display_name="display_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeUpdateResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_16(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="attribute_name",
                object_name="",
                description="description",
                display_name="display_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.update(
                attribute_name="",
                object_name="object_name",
                description="description",
                display_name="display_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.list(
            "object_name",
        )
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.list(
            "object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeListResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.list(
            "object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeListResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncUnify) -> None:
        attribute = await async_client.data.attributes.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        )
        assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.attributes.with_raw_response.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attribute = await response.parse()
        assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnify) -> None:
        async with async_client.data.attributes.with_streaming_response.delete(
            attribute_name="attribute_name",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attribute = await response.parse()
            assert_matches_type(AttributeDeleteResponse, attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.attributes.with_raw_response.delete(
                attribute_name="attribute_name",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attribute_name` but received ''"):
            await async_client.data.attributes.with_raw_response.delete(
                attribute_name="",
                object_name="object_name",
            )
