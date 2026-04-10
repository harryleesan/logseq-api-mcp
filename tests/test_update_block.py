"""Tests for update_block tool."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from src.tools.update_block import update_block


class TestUpdateBlock:
    """Test cases for update_block function."""

    @pytest.mark.asyncio
    async def test_update_block_success_null_response(
        self, mock_env_vars, mock_aiohttp_session
    ):
        """Test that a null body (Promise<void>) is treated as success, not an error."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=None)

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        result = await update_block("block-uuid-123", content="Updated content")

        assert len(result) == 1
        assert "✅ **BLOCK UPDATED SUCCESSFULLY**" in result[0].text

    @pytest.mark.asyncio
    async def test_update_block_success_content(
        self, mock_env_vars, mock_aiohttp_session
    ):
        """Test successful block update with content."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=None)

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        result = await update_block("block-uuid-123", content="Updated content")

        assert len(result) == 1
        assert "✅ **BLOCK UPDATED SUCCESSFULLY**" in result[0].text
        assert "📝 **UPDATED CONTENT:**" in result[0].text

    @pytest.mark.asyncio
    async def test_update_block_success_with_properties(
        self, mock_env_vars, mock_aiohttp_session
    ):
        """Test successful block update with content and properties."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=None)

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        properties = {"status": "completed", "priority": "high"}
        result = await update_block(
            "block-uuid-123", content="Updated content", properties=properties
        )

        assert len(result) == 1
        assert "✅ **BLOCK UPDATED SUCCESSFULLY**" in result[0].text
        assert "⚙️ **UPDATED PROPERTIES:**" in result[0].text

    @pytest.mark.asyncio
    async def test_update_block_http_error(self, mock_env_vars, mock_aiohttp_session):
        """Test block update with HTTP error."""
        mock_response = MagicMock()
        mock_response.status = 500

        mock_aiohttp_session._post_context.__aenter__ = AsyncMock(
            return_value=mock_response
        )
        mock_aiohttp_session._post_context.__aexit__ = AsyncMock(return_value=None)

        result = await update_block("block-uuid-123", content="Updated content")

        assert len(result) == 1
        assert "❌ Failed to update block: HTTP 500" in result[0].text

    @pytest.mark.asyncio
    async def test_update_block_exception(self, mock_env_vars, mock_aiohttp_session):
        """Test block update with exception."""
        mock_aiohttp_session._session_instance.post.side_effect = Exception(
            "Network error"
        )

        result = await update_block("block-uuid-123", content="Updated content")

        assert len(result) == 1
        assert "❌ Error updating block: Network error" in result[0].text
