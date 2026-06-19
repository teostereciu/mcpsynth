"""Notion Comments API tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def create_comment(
        rich_text: list,
        parent: Optional[dict] = None,
        discussion_id: Optional[str] = None,
    ) -> dict:
        """Create a comment on a Notion page or block.

        Args:
            rich_text: Array of rich text objects for the comment content.
                       E.g. [{"text": {"content": "This is a comment"}}].
            parent: The parent page or block. E.g. {"page_id": "..."}.
                    Required when creating a new discussion thread.
            discussion_id: The ID of an existing discussion thread to reply to.
        """
        body: dict[str, Any] = {"rich_text": rich_text}
        if parent is not None:
            body["parent"] = parent
        if discussion_id is not None:
            body["discussion_id"] = discussion_id
        return notion_request("POST", "/comments", json=body)

    @mcp.tool()
    def retrieve_comment(comment_id: str) -> dict:
        """Retrieve a specific Notion comment by its ID.

        Args:
            comment_id: The ID of the comment to retrieve.
        """
        return notion_request("GET", f"/comments/{comment_id}")

    @mcp.tool()
    def list_comments(
        block_id: str,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List comments on a Notion page or block.

        Args:
            block_id: The ID of the page or block whose comments to list.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {"block_id": block_id}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/comments", params=params)
