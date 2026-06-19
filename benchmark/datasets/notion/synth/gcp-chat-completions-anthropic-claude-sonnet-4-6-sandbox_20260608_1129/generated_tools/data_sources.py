"""Notion Data Sources API tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def create_data_source(
        parent: dict,
        title: Optional[list] = None,
        properties: Optional[dict] = None,
    ) -> dict:
        """Create a new Notion data source (database).

        Args:
            parent: The parent of the data source. E.g. {"database_id": "..."}.
            title: Title of the data source as rich text objects.
            properties: Property schema for the data source.
        """
        body: dict[str, Any] = {"parent": parent}
        if title is not None:
            body["title"] = title
        if properties is not None:
            body["properties"] = properties
        return notion_request("POST", "/data_sources", json=body)

    @mcp.tool()
    def retrieve_data_source(data_source_id: str) -> dict:
        """Retrieve a Notion data source by its ID.

        Args:
            data_source_id: The ID of the data source to retrieve.
        """
        return notion_request("GET", f"/data_sources/{data_source_id}")

    @mcp.tool()
    def update_data_source(
        data_source_id: str,
        title: Optional[list] = None,
        properties: Optional[dict] = None,
        in_trash: Optional[bool] = None,
        parent: Optional[dict] = None,
    ) -> dict:
        """Update a Notion data source's schema or metadata.

        Args:
            data_source_id: The ID of the data source to update.
            title: New title as rich text objects.
            properties: Updated property schema. Set a property to null to remove it.
            in_trash: Set to True to trash, False to restore.
            parent: New parent to move the data source to.
        """
        body: dict[str, Any] = {}
        if title is not None:
            body["title"] = title
        if properties is not None:
            body["properties"] = properties
        if in_trash is not None:
            body["in_trash"] = in_trash
        if parent is not None:
            body["parent"] = parent
        return notion_request("PATCH", f"/data_sources/{data_source_id}", json=body)

    @mcp.tool()
    def query_data_source(
        data_source_id: str,
        filter: Optional[dict] = None,
        sorts: Optional[list] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
        filter_properties: Optional[list] = None,
        result_type: Optional[str] = None,
    ) -> dict:
        """Query a Notion data source with optional filters and sorts.

        Args:
            data_source_id: The ID of the data source to query.
            filter: Filter conditions. E.g. {"property": "Status", "select": {"equals": "Done"}}.
            sorts: Sort conditions. E.g. [{"property": "Name", "direction": "ascending"}].
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
            filter_properties: List of property IDs to include in the response.
            result_type: Filter results to 'page' or 'data_source' types only.
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
        if result_type is not None:
            body["result_type"] = result_type
        params: dict[str, Any] = {}
        if filter_properties:
            params["filter_properties"] = filter_properties
        return notion_request("POST", f"/data_sources/{data_source_id}/query", json=body, params=params)

    @mcp.tool()
    def list_data_source_templates(
        data_source_id: str,
        name: Optional[str] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List templates available in a Notion data source.

        Args:
            data_source_id: The ID of the data source.
            name: Filter templates by name (case-insensitive substring match).
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", f"/data_sources/{data_source_id}/templates", params=params)
