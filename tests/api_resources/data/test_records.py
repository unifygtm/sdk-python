# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unify import Unify, AsyncUnify
from tests.utils import assert_matches_type
from unify.types.data import (
    RecordCreateResponse,
    RecordDeleteResponse,
    RecordUpdateResponse,
    RecordUpsertResponse,
    RecordRetrieveResponse,
    RecordFindUniqueResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Unify) -> None:
        record = client.data.records.create(
            object_name="object_name",
            data={"foo": {}},
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Unify) -> None:
        record = client.data.records.create(
            object_name="object_name",
            data={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.create(
            object_name="object_name",
            data={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.create(
            object_name="object_name",
            data={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordCreateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.create(
                object_name="",
                data={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Unify) -> None:
        record = client.data.records.retrieve(
            record_id="record_id",
            object_name="object_name",
        )
        assert_matches_type(RecordRetrieveResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.retrieve(
            record_id="record_id",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordRetrieveResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.retrieve(
            record_id="record_id",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordRetrieveResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.retrieve(
                record_id="record_id",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.data.records.with_raw_response.retrieve(
                record_id="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Unify) -> None:
        record = client.data.records.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Unify) -> None:
        record = client.data.records.update(
            record_id="record_id",
            object_name="object_name",
            data={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordUpdateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.update(
                record_id="record_id",
                object_name="",
                data={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.data.records.with_raw_response.update(
                record_id="",
                object_name="object_name",
                data={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Unify) -> None:
        record = client.data.records.delete(
            record_id="record_id",
            object_name="object_name",
        )
        assert_matches_type(RecordDeleteResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.delete(
            record_id="record_id",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordDeleteResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.delete(
            record_id="record_id",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordDeleteResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.delete(
                record_id="record_id",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.data.records.with_raw_response.delete(
                record_id="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_unique(self, client: Unify) -> None:
        record = client.data.records.find_unique(
            object_name="object_name",
            match={"foo": {}},
        )
        assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_unique(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.find_unique(
            object_name="object_name",
            match={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_unique(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.find_unique(
            object_name="object_name",
            match={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_find_unique(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.find_unique(
                object_name="",
                match={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Unify) -> None:
        record = client.data.records.upsert(
            object_name="object_name",
            match={"foo": {}},
        )
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Unify) -> None:
        record = client.data.records.upsert(
            object_name="object_name",
            match={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
            create={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            create_or_update={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            create_or_update_if_empty={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            update={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            update_if_empty={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
        )
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Unify) -> None:
        response = client.data.records.with_raw_response.upsert(
            object_name="object_name",
            match={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Unify) -> None:
        with client.data.records.with_streaming_response.upsert(
            object_name="object_name",
            match={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordUpsertResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Unify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.data.records.with_raw_response.upsert(
                object_name="",
                match={"foo": {}},
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.create(
            object_name="object_name",
            data={"foo": {}},
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.create(
            object_name="object_name",
            data={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.create(
            object_name="object_name",
            data={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.create(
            object_name="object_name",
            data={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordCreateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.create(
                object_name="",
                data={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.retrieve(
            record_id="record_id",
            object_name="object_name",
        )
        assert_matches_type(RecordRetrieveResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.retrieve(
            record_id="record_id",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordRetrieveResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.retrieve(
            record_id="record_id",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordRetrieveResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.retrieve(
                record_id="record_id",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.data.records.with_raw_response.retrieve(
                record_id="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.update(
            record_id="record_id",
            object_name="object_name",
            data={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.update(
            record_id="record_id",
            object_name="object_name",
            data={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordUpdateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.update(
                record_id="record_id",
                object_name="",
                data={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.data.records.with_raw_response.update(
                record_id="",
                object_name="object_name",
                data={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.delete(
            record_id="record_id",
            object_name="object_name",
        )
        assert_matches_type(RecordDeleteResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.delete(
            record_id="record_id",
            object_name="object_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordDeleteResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.delete(
            record_id="record_id",
            object_name="object_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordDeleteResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.delete(
                record_id="record_id",
                object_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.data.records.with_raw_response.delete(
                record_id="",
                object_name="object_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_unique(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.find_unique(
            object_name="object_name",
            match={"foo": {}},
        )
        assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_unique(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.find_unique(
            object_name="object_name",
            match={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_unique(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.find_unique(
            object_name="object_name",
            match={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordFindUniqueResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_find_unique(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.find_unique(
                object_name="",
                match={"foo": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.upsert(
            object_name="object_name",
            match={"foo": {}},
        )
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncUnify) -> None:
        record = await async_client.data.records.upsert(
            object_name="object_name",
            match={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            validation_mode="strict",
            create={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            create_or_update={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            create_or_update_if_empty={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            update={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
            update_if_empty={
                "foo": {
                    "administrative_area": "administrativeArea",
                    "country": {
                        "code": "AD",
                        "name": "name",
                    },
                    "dependent_locality": "dependentLocality",
                    "locality": "locality",
                    "postal_code": "postalCode",
                    "premise": "premise",
                    "sub_administrative_area": "subAdministrativeArea",
                    "sub_premise": "subPremise",
                    "thoroughfare": "thoroughfare",
                }
            },
        )
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncUnify) -> None:
        response = await async_client.data.records.with_raw_response.upsert(
            object_name="object_name",
            match={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordUpsertResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncUnify) -> None:
        async with async_client.data.records.with_streaming_response.upsert(
            object_name="object_name",
            match={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordUpsertResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncUnify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.data.records.with_raw_response.upsert(
                object_name="",
                match={"foo": {}},
            )
