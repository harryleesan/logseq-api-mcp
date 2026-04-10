import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import aiohttp
from dotenv import load_dotenv
from mcp.types import TextContent

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)


async def update_block(
    uuid: str,
    content: str,
    properties: Optional[Dict[str, Any]] = None,
) -> List[TextContent]:
    """
    Update a block's content in Logseq directly via the data layer.

    Uses logseq.Editor.updateBlock, which writes directly to the graph without
    requiring the Logseq window to be focused.

    Args:
        uuid: The UUID of the block to update.
        content: New Markdown content for the block.
        properties: Optional dictionary of block properties to set alongside the
                    content update (e.g. {"priority": "A", "done": True}).
    """
    endpoint = os.getenv("LOGSEQ_API_ENDPOINT", "http://127.0.0.1:12315/api")
    token = os.getenv("LOGSEQ_API_TOKEN", "auth")

    headers = {"Authorization": f"Bearer {token}"}

    args: list[Any] = [uuid, content]
    if properties is not None:
        args.append({"properties": properties})

    async with aiohttp.ClientSession() as session:
        try:
            payload = {
                "method": "logseq.Editor.updateBlock",
                "args": args,
            }

            async with session.post(
                endpoint, json=payload, headers=headers
            ) as response:
                if response.status != 200:
                    return [
                        TextContent(
                            type="text",
                            text=f"❌ Failed to update block: HTTP {response.status}",
                        )
                    ]

                result = await response.json()

                if result is None:
                    return [
                        TextContent(
                            type="text",
                            text="❌ Failed to update block: No response from Logseq API",
                        )
                    ]

                content_preview = (
                    content[:100] + "..." if len(content) > 100 else content
                )

                output_lines = [
                    "✅ **BLOCK UPDATED SUCCESSFULLY**",
                    f"🔗 Block UUID: {uuid}",
                    "",
                    "📝 **UPDATED CONTENT:**",
                    "```",
                    content_preview,
                    "```",
                ]

                if properties:
                    output_lines += [
                        "",
                        "⚙️ **UPDATED PROPERTIES:**",
                        *[f"• {k}: {v}" for k, v in properties.items()],
                    ]

                output_lines += [
                    "",
                    "🔗 **NEXT STEPS:**",
                    "• Use get_block_content to verify the changes",
                    "• Use get_page_blocks to see the block in context",
                ]

                return [TextContent(type="text", text="\n".join(output_lines))]

        except Exception as e:
            return [TextContent(type="text", text=f"❌ Error updating block: {str(e)}")]
