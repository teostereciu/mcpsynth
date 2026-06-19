"""Notion Views API tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def list_views(
        database_id: Optional[str] = None,
        data_source_id: Optional[str] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List views for a Notion database or data source.

        Args:
            database_id: ID of the database to list views for.
            data_source_id: ID of the data source to list views for.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if database_id:
            params["database_id"] = database_id
        if data_source_id:
            params["data_source_id"] = data_source_id
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/views", params=params)

    @mcp.tool()
    def retrieve_view(view_id: str) -> dict:
        """Retrieve a Notion view by its ID.

        Args:
            view_id: The ID of the view to retrieve.
        """
        return notion_request("GET", f"/views/{view_id}")

    @mcp.tool()
    def create_view(
        data_source_id: str,
        type: str,
        name: Optional[str] = None,
        database_id: Optional[str] = None,
        view_id: Optional[str] = None,
        filter: Optional[dict] = None,
        sorts: Optional[list] = None,
        quick_filters: Optional[dict] = None,
        layout: Optional[dict] = None,
        position: Optional[dict] = None,
        create_database: Optional[dict] = None,
    ) -> dict:
        """Create a new Notion view for a database or data source.

        Args:
            data_source_id: The ID of the data source this view is scoped to.
            type: The type of view (e.g. 'table', 'board', 'list', 'calendar', 'gallery', 'timeline').
            name: The name of the view.
            database_id: The ID of the database to create the view in.
            view_id: The ID of a dashboard view to add this view to as a widget.
            filter: Filter to apply to the view.
            sorts: Sorts to apply to the view.
            quick_filters: Quick filters to pin in the view's filter bar.
            layout: View presentation configuration.
            position: Where to place the new view.
            create_database: Config to create a new linked database block.
        """
        body: dict[str, Any] = {"data_source_id": data_source_id, "type": type}
        if name is not None:
            body["name"] = name
        if database_id is not None:
            body["database_id"] = database_id
        if view_id is not None:
            body["view_id"] = view_id
        if filter is not None:
            body["filter"] = filter
        if sorts is not None:
            body["sorts"] = sorts
        if quick_filters is not None:
            body["quick_filters"] = quick_filters
        if layout is not None:
            body["layout"] = layout
        if position is not None:
            body["position"] = position
        if create_database is not None:
            body["create_database"] = create_database
        return notion_request("POST", "/views", json=body)

    @mcp.tool()
    def update_view(
        view_id: str,
        name: Optional[str] = None,
        filter: Optional[dict] = None,
        sorts: Optional[list] = None,
        quick_filters: Optional[dict] = None,
        layout: Optional[dict] = None,
    ) -> dict:
        """Update a Notion view's name, filter, sorts, or layout.

        Args:
            view_id: The ID of the view to update.
            name: New name for the view.
            filter: New filter to apply (pass null to clear).
            sorts: New sorts to apply (pass null to clear).
            quick_filters: Quick filters for the filter bar.
            layout: View presentation configuration.
        """
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if filter is not None:
            body["filter"] = filter
        if sorts is not None:
            body["sorts"] = sorts
        if quick_filters is not None:
            body["quick_filters"] = quick_filters
        if layout is not None:
            body["layout"] = layout
        return notion_request("PATCH", f"/views/{view_id}", json=body)

    @mcp.tool()
    def delete_view(view_id: str) -> dict:
        """Delete a Notion view.

        Args:
            view_id: The ID of the view to delete.
        """
        return notion_request("DELETE", f"/views/{view_id}")

    @mcp.tool()
    def create_view_query(view_id: str, page_size: Optional[int] = None) -> dict:
        """Create a query against a Notion view to get paginated results.

        Args:
            view_id: The ID of the view to query.
            page_size: Number of results per page (max 100).
        """
        body: dict[str, Any] = {}
        if page_size is not None:
            body["page_size"] = page_size
        return notion_request("POST", f"/views/{view_id}/queries", json=body)

    @mcp.tool()
    def get_view_query_results(
        view_id: str,
        query_id: str,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """Get paginated results from a previously created Notion view query.

        Args:
            view_id: The ID of the view.
            query_id: The ID of the query.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", f"/views/{view_id}/queries/{query_id}", params=params)

    @mcp.tool()
    def delete_view_query(view_id: str, query_id: str) -> dict:
        """Delete a Notion view query.

        Args:
            view_id: The ID of the view.
            query_id: The ID of the query to delete.
        """
        return notion_request("DELETE", f"/views/{view_id}/queries/{query_id}")
