"""Notion Blocks tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request


def register(mcp: FastMCP):

    @mcp.tool()
    def retrieve_block(block_id: str) -> dict:
        """Retrieve a Notion block by its ID.

        Args:
            block_id: The ID of the block to retrieve.
        """
        return notion_request("GET", f"/blocks/{block_id}")

    @mcp.tool()
    def retrieve_block_children(
        block_id: str,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """Retrieve the children blocks of a Notion block or page.

        Args:
            block_id: The ID of the block or page whose children to retrieve.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", f"/blocks/{block_id}/children", params=params)

    @mcp.tool()
    def append_block_children(
        block_id: str,
        children: list,
        position: Optional[dict] = None,
    ) -> dict:
        """Append new child blocks to a Notion block or page.

        Args:
            block_id: The ID of the parent block or page.
            children: Array of block objects to append. E.g.:
                      [{"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Hello!"}}]}}]
            position: Where to insert the blocks. Options:
                      {"type": "end"} (default), {"type": "start"},
                      {"type": "after_block", "after_block": {"id": "<block_id>"}}.
        """
        body: dict[str, Any] = {"children": children}
        if position is not None:
            body["position"] = position
        return notion_request("PATCH", f"/blocks/{block_id}/children", json=body)

    @mcp.tool()
    def update_block(block_id: str, block_content: dict) -> dict:
        """Update the content of a Notion block.

        Args:
            block_id: The ID of the block to update.
            block_content: A dict with the block type as key and its content as value.
                           E.g. {"paragraph": {"rich_text": [{"text": {"content": "Updated text"}}]}}
                           or {"to_do": {"checked": true, "rich_text": [{"text": {"content": "Task"}}]}}
        """
        return notion_request("PATCH", f"/blocks/{block_id}", json=block_content)

    @mcp.tool()
    def delete_block(block_id: str) -> dict:
        """Delete (archive) a Notion block.

        Args:
            block_id: The ID of the block to delete.
        """
        return notion_request("DELETE", f"/blocks/{block_id}")
