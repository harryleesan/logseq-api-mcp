import os
from pathlib import Path
from typing import List

import aiohttp
from dotenv import load_dotenv
from mcp.types import TextContent

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)


async def remove_block(uuid: str) -> List[TextContent]:
    """
    Remove a block from the Logseq graph by its UUID.

    Uses logseq.Editor.removeBlock, which deletes the block directly via the
    data layer without requiring the Logseq window to be focused.

    Args:
        uuid: The UUID of the block to remove.
    """
    endpoint = os.getenv("LOGSEQ_API_ENDPOINT", "http://127.0.0.1:12315/api")
    token = os.getenv("LOGSEQ_API_TOKEN", "auth")

    headers = {"Authorization": f"Bearer {token}"}

    async with aiohttp.ClientSession() as session:
        try:
            payload = {
                "method": "logseq.Editor.removeBlock",
                "args": [uuid],
            }

            async with session.post(
                endpoint, json=payload, headers=headers
            ) as response:
                if response.status != 200:
                    return [
                        TextContent(
                            type="text",
                            text=f"❌ Failed to remove block: HTTP {response.status}",
                        )
                    ]

                await response.json()

                return [
                    TextContent(
                        type="text",
                        text="\n".join(
                            [
                                "✅ **BLOCK REMOVED SUCCESSFULLY**",
                                f"🗑️ Block UUID: {uuid}",
                                "",
                                "🔗 **NEXT STEPS:**",
                                "• Use get_page_blocks to confirm the block is gone",
                                "• Use get_all_pages to review the affected page",
                            ]
                        ),
                    )
                ]

        except Exception as e:
            return [TextContent(type="text", text=f"❌ Error removing block: {str(e)}")]
