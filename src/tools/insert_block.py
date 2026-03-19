import os
from pathlib import Path
from typing import Any, List, Optional

import aiohttp
from dotenv import load_dotenv
from mcp.types import TextContent

# Load environment variables from .env file in project root
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)


async def insert_block(
    src_block: str,
    content: str,
    before: Optional[bool] = None,
    sibling: Optional[bool] = None,
    properties: Optional[dict] = None,
) -> List[TextContent]:
    """
    Insert a new block relative to an existing block in Logseq.

    Unlike append_block_in_page which only adds blocks at the page level,
    this tool inserts a block as a child (indented) or sibling of any existing block.
    This enables creating nested/hierarchical block structures.

    Args:
        src_block: UUID of the reference block to insert relative to
        content: The content of the new block
        before: If true, insert before the reference block instead of after. Defaults to false
        sibling: If true, insert as a sibling instead of a child. Defaults to false (inserts as child)
        properties: Optional dict of block properties to set
    """
    endpoint = os.getenv("LOGSEQ_API_ENDPOINT", "http://127.0.0.1:12315/api")
    token = os.getenv("LOGSEQ_API_TOKEN", "auth")

    headers = {"Authorization": f"Bearer {token}"}

    # Build options object
    options: dict[str, Any] = {}
    if before is not None:
        options["before"] = before
    if sibling is not None:
        options["sibling"] = sibling
    if properties is not None:
        options["properties"] = properties

    async with aiohttp.ClientSession() as session:
        try:
            payload = {
                "method": "logseq.Editor.insertBlock",
                "args": [src_block, content, options]
                if options
                else [src_block, content],
            }

            async with session.post(
                endpoint, json=payload, headers=headers
            ) as response:
                if response.status != 200:
                    return [
                        TextContent(
                            type="text",
                            text=f"❌ Failed to insert block: HTTP {response.status}",
                        )
                    ]

                result = await response.json()

                if result is None or result == "":
                    return [
                        TextContent(
                            type="text",
                            text="❌ Failed to insert block: No response from Logseq API",
                        )
                    ]

                # Extract new block info from response
                new_uuid = result.get("uuid", "N/A")
                new_id = result.get("id", "N/A")

                # Determine relationship description
                if sibling:
                    position = "before" if before else "after"
                    positioning = f"📍 Inserted as {position} sibling of: {src_block}"
                else:
                    position = "first child" if before else "last child"
                    positioning = f"📍 Inserted as {position} of: {src_block}"

                output_lines = [
                    "✅ **BLOCK INSERTED SUCCESSFULLY**",
                    f"🔑 New block UUID: {new_uuid}",
                    f"🆔 New block ID: {new_id}",
                    f"📝 Content: {content}",
                    positioning,
                ]

                if properties:
                    output_lines.append(f"⚙️ Properties: {properties}")

                output_lines.extend(
                    [
                        "",
                        "🔗 **NEXT STEPS:**",
                        "• Use insert_block with this UUID to add children under it",
                        "• Use get_block_content to verify the new block",
                        "• Use get_page_blocks to see the updated hierarchy",
                    ]
                )

                return [TextContent(type="text", text="\n".join(output_lines))]

        except Exception as e:
            return [
                TextContent(type="text", text=f"❌ Error inserting block: {str(e)}")
            ]
