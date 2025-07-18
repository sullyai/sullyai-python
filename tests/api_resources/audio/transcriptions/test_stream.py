# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sullyai import SullyAI, AsyncSullyAI
from tests.utils import assert_matches_type
from sullyai.types.audio.transcriptions import StreamCreateTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStream:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_token(self, client: SullyAI) -> None:
        stream = client.audio.transcriptions.stream.create_token(
            expires_in=3600,
        )
        assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_token(self, client: SullyAI) -> None:
        response = client.audio.transcriptions.stream.with_raw_response.create_token(
            expires_in=3600,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_token(self, client: SullyAI) -> None:
        with client.audio.transcriptions.stream.with_streaming_response.create_token(
            expires_in=3600,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStream:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_token(self, async_client: AsyncSullyAI) -> None:
        stream = await async_client.audio.transcriptions.stream.create_token(
            expires_in=3600,
        )
        assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncSullyAI) -> None:
        response = await async_client.audio.transcriptions.stream.with_raw_response.create_token(
            expires_in=3600,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncSullyAI) -> None:
        async with async_client.audio.transcriptions.stream.with_streaming_response.create_token(
            expires_in=3600,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamCreateTokenResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True
