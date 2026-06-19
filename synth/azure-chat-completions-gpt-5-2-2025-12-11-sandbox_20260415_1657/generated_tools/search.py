from typing import Any, Dict, Optional

from ._client import get_client


def search(query: str, include: Optional[str] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = None, page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/search?query=..."""
    client = get_client()
    params: Dict[str, Any] = {"query": query}
    if include is not None:
        params["include"] = include
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    if page is not None:
        params["page"] = page
    return client.request("GET", f"{client.base_support}/search", params=params)  # type: ignore


def search_count(query: str) -> Dict[str, Any]:
    """GET /api/v2/search/count?query=..."""
    client = get_client()
    return client.request("GET", f"{client.base_support}/search/count", params={"query": query})  # type: ignore


def search_export(
    query: str,
    filter_type: Optional[str] = None,
    include: Optional[str] = None,
    page_after: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v2/search/export?query=...

    Use for >1000 results. Cursor pagination.
    """
    client = get_client()
    params: Dict[str, Any] = {"query": query}
    if filter_type is not None:
        params["filter[type]"] = filter_type
    if include is not None:
        params["include"] = include
    if page_after is not None:
        params["page[after]"] = page_after
    if page_size is not None:
        params["page[size]"] = page_size
    return client.request("GET", f"{client.base_support}/search/export", params=params)  # type: ignore
