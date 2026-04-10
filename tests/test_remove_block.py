"""Tests for remove_block tool."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from src.tools.remove_block import remove_block


class TestRemoveBlock:
    """Test cases for remove_block function."""

    @pytest.mark.asyncio
    async def test_remove_block_success(self, mock_env_vars, mock_aiohttp_session):
        """Test successful block removal."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=None)

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        result = await remove_block("block-uuid-123")

        assert len(result) == 1
        assert "✅ **BLOCK REMOVED SUCCESSFULLY**" in result[0].text
        assert "block-uuid-123" in result[0].text

    @pytest.mark.asyncio
    async def test_remove_block_http_error(self, mock_env_vars, mock_aiohttp_session):
        """Test block removal with HTTP error."""
        mock_response = MagicMock()
        mock_response.status = 500

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        result = await remove_block("block-uuid-123")

        assert len(result) == 1
        assert "❌ Failed to remove block: HTTP 500" in result[0].text

    @pytest.mark.asyncio
    async def test_remove_block_exception(self, mock_env_vars, mock_aiohttp_session):
        """Test block removal with exception."""
        mock_aiohttp_session._session_instance.post.side_effect = Exception(
            "Network error"
        )

        result = await remove_block("block-uuid-123")

        assert len(result) == 1
        assert "❌ Error removing block: Network error" in result[0].text
