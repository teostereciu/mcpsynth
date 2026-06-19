"""Notion Users tools."""
from typing import Optional
from mcp.server.fastmcp import FastMCP
from .client import notion_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_current_user() -> dict:
        """Retrieve the bot user associated with the current API token.

        Returns information about the integration's bot user including its ID, name, and owner.
        """
        return notion_request("GET", "/users/me")

    @mcp.tool()
    def retrieve_user(user_id: str) -> dict:
        """Retrieve a Notion user by their ID.

        Args:
            user_id: The ID of the user to retrieve.
        """
        return notion_request("GET", f"/users/{user_id}")

    @mcp.tool()
    def list_users(
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List all users in the Notion workspace.

        Args:
            start_cursor: Cursor for pagination (from previous response's next_cursor).
            page_size: Number of results per page (max 100).
        """
        params = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/users", params=params)
