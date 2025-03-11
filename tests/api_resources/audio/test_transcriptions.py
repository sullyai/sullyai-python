# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sullyai import SullyAI, AsyncSullyAI
from tests.utils import assert_matches_type
from sullyai.types import DeleteResponse
from sullyai.types.audio import TranscriptionCreateResponse, TranscriptionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: SullyAI) -> None:
        transcription = client.audio.transcriptions.create(
            audio=b"raw file contents",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: SullyAI) -> None:
        transcription = client.audio.transcriptions.create(
            audio=b"raw file contents",
            language="en-US",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: SullyAI) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            audio=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: SullyAI) -> None:
        with client.audio.transcriptions.with_streaming_response.create(
            audio=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: SullyAI) -> None:
        transcription = client.audio.transcriptions.retrieve(
            "transcriptionId",
        )
        assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: SullyAI) -> None:
        response = client.audio.transcriptions.with_raw_response.retrieve(
            "transcriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: SullyAI) -> None:
        with client.audio.transcriptions.with_streaming_response.retrieve(
            "transcriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: SullyAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcription_id` but received ''"):
            client.audio.transcriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: SullyAI) -> None:
        transcription = client.audio.transcriptions.delete(
            "transcriptionId",
        )
        assert_matches_type(DeleteResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: SullyAI) -> None:
        response = client.audio.transcriptions.with_raw_response.delete(
            "transcriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(DeleteResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: SullyAI) -> None:
        with client.audio.transcriptions.with_streaming_response.delete(
            "transcriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(DeleteResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: SullyAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcription_id` but received ''"):
            client.audio.transcriptions.with_raw_response.delete(
                "",
            )


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncSullyAI) -> None:
        transcription = await async_client.audio.transcriptions.create(
            audio=b"raw file contents",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSullyAI) -> None:
        transcription = await async_client.audio.transcriptions.create(
            audio=b"raw file contents",
            language="en-US",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSullyAI) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create(
            audio=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSullyAI) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create(
            audio=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSullyAI) -> None:
        transcription = await async_client.audio.transcriptions.retrieve(
            "transcriptionId",
        )
        assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSullyAI) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.retrieve(
            "transcriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSullyAI) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.retrieve(
            "transcriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(TranscriptionRetrieveResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSullyAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcription_id` but received ''"):
            await async_client.audio.transcriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncSullyAI) -> None:
        transcription = await async_client.audio.transcriptions.delete(
            "transcriptionId",
        )
        assert_matches_type(DeleteResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSullyAI) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.delete(
            "transcriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(DeleteResponse, transcription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSullyAI) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.delete(
            "transcriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(DeleteResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSullyAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcription_id` but received ''"):
            await async_client.audio.transcriptions.with_raw_response.delete(
                "",
            )
