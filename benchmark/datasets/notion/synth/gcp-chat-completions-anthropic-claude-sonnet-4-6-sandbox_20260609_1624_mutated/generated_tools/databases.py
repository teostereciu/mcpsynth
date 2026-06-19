"""Notion Databases tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request


def register(mcp: FastMCP):

    @mcp.tool()
    def retrieve_database(database_id: str) -> dict:
        """Retrieve a Notion database by its ID.

        Args:
            database_id: The ID of the database to retrieve.
        """
        return notion_request("GET", f"/databases/{database_id}")

    @mcp.tool()
    def create_database(
        parent: dict,
        title: Optional[list] = None,
        properties: Optional[dict] = None,
        description: Optional[list] = None,
        is_inline: Optional[bool] = None,
        icon: Optional[dict] = None,
        cover: Optional[dict] = None,
    ) -> dict:
        """Create a new Notion database.

        Args:
            parent: The parent page. E.g. {"type": "page_id", "page_id": "..."}.
            title: The title of the database as an array of rich text objects.
                   E.g. [{"text": {"content": "My Database"}}].
            properties: Property schema for the database. E.g. {"Name": {"title": {}}}.
            description: Description of the database as rich text objects.
            is_inline: Whether the database should be displayed inline in the parent page.
            icon: Icon for the database.
            cover: Cover image for the database.
        """
        body: dict[str, Any] = {"parent": parent}
        if title is not None:
            body["title"] = title
        if properties is not None:
            body["properties"] = properties
        if description is not None:
            body["description"] = description
        if is_inline is not None:
            body["is_inline"] = is_inline
        if icon is not None:
            body["icon"] = icon
        if cover is not None:
            body["cover"] = cover
        return notion_request("POST", "/databases", json=body)

    @mcp.tool()
    def update_database(
        database_id: str,
        title: Optional[list] = None,
        description: Optional[list] = None,
        properties: Optional[dict] = None,
        is_inline: Optional[bool] = None,
        icon: Optional[dict] = None,
        cover: Optional[dict] = None,
        in_trash: Optional[bool] = None,
        is_locked: Optional[bool] = None,
        parent: Optional[dict] = None,
    ) -> dict:
        """Update a Notion database's title, description, properties, or other settings.

        Args:
            database_id: The ID of the database to update.
            title: Updated title as rich text objects.
            description: Updated description as rich text objects.
            properties: Updated property schema. Set a property to null to remove it.
            is_inline: Whether the database should be displayed inline.
            icon: Updated icon for the database.
            cover: Updated cover image.
            in_trash: Move to or from trash.
            is_locked: Lock or unlock the database from editing.
            parent: Move the database to a different parent page.
        """
        body: dict[str, Any] = {}
        if title is not None:
            body["title"] = title
        if description is not None:
            body["description"] = description
        if properties is not None:
            body["properties"] = properties
        if is_inline is not None:
            body["is_inline"] = is_inline
        if icon is not None:
            body["icon"] = icon
        if cover is not None:
            body["cover"] = cover
        if in_trash is not None:
            body["in_trash"] = in_trash
        if is_locked is not None:
            body["is_locked"] = is_locked
        if parent is not None:
            body["parent"] = parent
        return notion_request("PATCH", f"/databases/{database_id}", json=body)

    @mcp.tool()
    def query_database(
        database_id: str,
        filter: Optional[dict] = None,
        sorts: Optional[list] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
        filter_properties: Optional[list] = None,
    ) -> dict:
        """Query a Notion database with optional filters and sorts.

        Args:
            database_id: The ID of the database to query.
            filter: Filter conditions. E.g. {"property": "Status", "select": {"equals": "Done"}}.
                    Supports compound filters with "and"/"or" arrays.
            sorts: Sort rules. E.g. [{"property": "Name", "direction": "ascending"}].
            start_cursor: Cursor for pagination (from previous response's next_cursor).
            page_size: Number of results per page (max 100).
            filter_properties: List of property IDs to include in the response.
        """
        body: dict[str, Any] = {}
        if filter is not None:
            body["filter"] = filter
        if sorts is not None:
            body["sorts"] = sorts
        if start_cursor is not None:
            body["start_cursor"] = start_cursor
        if page_size is not None:
            body["page_size"] = page_size

        params = {}
        if filter_properties:
            params["filter_properties"] = filter_properties

        return notion_request("POST", f"/databases/{database_id}/query", json=body, params=params)

    @mcp.tool()
    def list_databases(
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List all databases accessible to the integration (deprecated endpoint, use search instead).

        Args:
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/databases", params=params)
