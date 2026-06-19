"""Notion Search tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request


def register(mcp: FastMCP):

    @mcp.tool()
    def search(
        query: Optional[str] = None,
        filter: Optional[dict] = None,
        sort: Optional[dict] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """Search Notion pages and databases by title.

        Args:
            query: The text to search for in page/database titles.
            filter: Filter results by object type. E.g. {"property": "object", "value": "page"}
                    or {"property": "object", "value": "database"}.
            sort: Sort order for results. E.g. {"direction": "descending", "timestamp": "last_edited_time"}.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        body: dict[str, Any] = {}
        if query is not None:
            body["query"] = query
        if filter is not None:
            body["filter"] = filter
        if sort is not None:
            body["sort"] = sort
        if start_cursor is not None:
            body["start_cursor"] = start_cursor
        if page_size is not None:
            body["page_size"] = page_size
        return notion_request("POST", "/search", json=body)
