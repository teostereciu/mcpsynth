"""Notion Views tools."""
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
            database_id: ID of a Notion database to list views for.
                         At least one of database_id or data_source_id is required.
            data_source_id: ID of a data source to list all views for.
                            At least one of database_id or data_source_id is required.
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
        view_type: str,
        name: Optional[str] = None,
        database_id: Optional[str] = None,
        view_id: Optional[str] = None,
        filter: Optional[dict] = None,
        sort_rules: Optional[list] = None,
        quick_filters: Optional[dict] = None,
        layout: Optional[dict] = None,
    ) -> dict:
        """Create a new view for a Notion database.

        Args:
            data_source_id: The ID of the data source this view should be scoped to.
            view_type: The type of view to create. E.g. "table", "board", "list", "calendar",
                       "gallery", "timeline", "gantt".
            name: The name of the view.
            database_id: The ID of the database to create a view in.
                         Mutually exclusive with view_id.
            view_id: The ID of a dashboard view to add this view to as a widget.
                     Mutually exclusive with database_id.
            filter: Filter to apply to the view (same format as data source query filter).
            sort_rules: Sorts to apply to the view.
            quick_filters: Quick filters to pin in the view's filter bar.
            layout: View presentation configuration.
        """
        body: dict[str, Any] = {
            "data_source_id": data_source_id,
            "type": view_type,
        }
        if name is not None:
            body["name"] = name
        if database_id is not None:
            body["database_id"] = database_id
        if view_id is not None:
            body["view_id"] = view_id
        if filter is not None:
            body["filter"] = filter
        if sort_rules is not None:
            body["sort_rules"] = sort_rules
        if quick_filters is not None:
            body["quick_filters"] = quick_filters
        if layout is not None:
            body["layout"] = layout
        return notion_request("POST", "/views", json=body)

    @mcp.tool()
    def update_view(
        view_id: str,
        name: Optional[str] = None,
        filter: Optional[dict] = None,
        sort_rules: Optional[list] = None,
        quick_filters: Optional[dict] = None,
        layout: Optional[dict] = None,
    ) -> dict:
        """Update a Notion view's name, filter, sorts, or layout.

        Args:
            view_id: The ID of the view to update.
            name: New name for the view.
            filter: Filter to apply to the view. Pass null to clear.
            sort_rules: Sort rules to apply. Pass null to clear.
            quick_filters: Quick filters for the view's filter bar.
            layout: View presentation configuration.
        """
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if filter is not None:
            body["filter"] = filter
        if sort_rules is not None:
            body["sort_rules"] = sort_rules
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
    def create_view_query(
        view_id: str,
        results_per_page: Optional[int] = None,
    ) -> dict:
        """Create a cached query for a Notion view and get the first page of results.

        Args:
            view_id: The ID of the view to query.
            results_per_page: Number of results per page (max 100).
        """
        body: dict[str, Any] = {}
        if results_per_page is not None:
            body["results_per_page"] = results_per_page
        return notion_request("POST", f"/views/{view_id}/queries", json=body)

    @mcp.tool()
    def get_view_query_results(
        view_id: str,
        query_id: str,
        start_cursor: Optional[str] = None,
        results_per_page: Optional[int] = None,
    ) -> dict:
        """Get paginated results from a previously created view query.

        Args:
            view_id: The ID of the view.
            query_id: The ID of the query (from create_view_query response).
            start_cursor: Cursor for the next page of results.
            results_per_page: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if results_per_page is not None:
            params["results_per_page"] = results_per_page
        return notion_request("GET", f"/views/{view_id}/queries/{query_id}/results", params=params)

    @mcp.tool()
    def delete_view_query(view_id: str, query_id: str) -> dict:
        """Delete a cached view query.

        Args:
            view_id: The ID of the view.
            query_id: The ID of the query to delete.
        """
        return notion_request("DELETE", f"/views/{view_id}/queries/{query_id}")
