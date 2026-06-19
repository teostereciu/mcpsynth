"""Ticketing: Unified Search tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_get


def search_list(query: str, per_page: int = 25, page: Optional[int] = None, include: Optional[str] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = None) -> Dict[str, Any]:
    """List search results.

    Maps to GET /api/v2/search?query=...

    Tip: to search tickets, use query like: "type:ticket MCP Test".
    """
    params: Dict[str, Any] = {"query": query, "per_page": per_page}
    if page is not None:
        params["page"] = page
    if include:
        params["include"] = include
    if sort_by:
        params["sort_by"] = sort_by
    if sort_order:
        params["sort_order"] = sort_order
    return zendesk_get("/search", params=params)


def search_count(query: str) -> Dict[str, Any]:
    """Count search results.

    Maps to GET /api/v2/search/count?query=...
    """
    return zendesk_get("/search/count", params={"query": query})
