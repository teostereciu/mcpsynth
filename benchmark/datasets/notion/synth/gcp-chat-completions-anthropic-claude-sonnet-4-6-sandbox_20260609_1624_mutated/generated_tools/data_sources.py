"""Notion Data Sources tools."""
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
        """Create a new Notion data source (the underlying data layer of a database).

        Args:
            parent: The parent database. E.g. {"database_id": "..."}.
            title: Title of the data source as rich text objects.
                   E.g. [{"text": {"content": "My Data Source"}}].
            properties: Property schema. E.g. {"Name": {"title": {}}, "Status": {"select": {"options": []}}}.
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
        """Update a Notion data source's title, properties, or trash status.

        Args:
            data_source_id: The ID of the data source to update.
            title: Updated title as rich text objects.
            properties: Updated property schema. Set a property to null to remove it.
            in_trash: Move to or from trash.
            parent: Move the data source to a different parent database.
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
        query_filter: Optional[dict] = None,
        sort_rules: Optional[list] = None,
        start_cursor: Optional[str] = None,
        results_per_page: Optional[int] = None,
        filter_properties: Optional[list] = None,
        result_type: Optional[str] = None,
    ) -> dict:
        """Query a Notion data source with optional filters and sorts.

        Args:
            data_source_id: The ID of the data source to query.
            query_filter: Filter conditions. E.g. {"property": "Status", "select": {"equals": "Done"}}.
                          Supports compound filters with "and"/"or" arrays.
            sort_rules: Sort rules. E.g. [{"property": "Name", "direction": "ascending"}].
            start_cursor: Cursor for pagination.
            results_per_page: Number of results per page (max 100).
            filter_properties: List of property names/IDs to include in the response.
            result_type: Filter results by type. E.g. "page" or "data_source".
        """
        body: dict[str, Any] = {}
        if query_filter is not None:
            body["query_filter"] = query_filter
        if sort_rules is not None:
            body["sort_rules"] = sort_rules
        if start_cursor is not None:
            body["start_cursor"] = start_cursor
        if results_per_page is not None:
            body["results_per_page"] = results_per_page
        if result_type is not None:
            body["result_type"] = result_type

        params = {}
        if filter_properties:
            params["filter_properties[]"] = filter_properties

        return notion_request("POST", f"/data_sources/{data_source_id}/query", json=body, params=params)

    @mcp.tool()
    def list_data_source_templates(
        data_source_id: str,
        name_filter: Optional[str] = None,
        start_cursor: Optional[str] = None,
        results_per_page: Optional[int] = None,
    ) -> dict:
        """List available templates for a Notion data source.

        Args:
            data_source_id: The ID of the data source.
            name_filter: Filter templates by name (case-insensitive substring match).
            start_cursor: Cursor for pagination.
            results_per_page: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if name_filter:
            params["name_filter"] = name_filter
        if start_cursor:
            params["start_cursor"] = start_cursor
        if results_per_page is not None:
            params["results_per_page"] = results_per_page
        return notion_request("GET", f"/data_sources/{data_source_id}/templates", params=params)
