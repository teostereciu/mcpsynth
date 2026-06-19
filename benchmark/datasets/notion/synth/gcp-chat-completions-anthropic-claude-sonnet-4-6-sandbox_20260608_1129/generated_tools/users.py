"""Notion Users API tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def list_users(
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List all users in the Notion workspace.

        Args:
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/users", params=params)

    @mcp.tool()
    def retrieve_user(user_id: str) -> dict:
        """Retrieve a specific Notion user by their ID.

        Args:
            user_id: The ID of the user to retrieve.
        """
        return notion_request("GET", f"/users/{user_id}")

    @mcp.tool()
    def get_bot_user() -> dict:
        """Retrieve the bot user associated with the current integration token."""
        return notion_request("GET", "/users/me")
