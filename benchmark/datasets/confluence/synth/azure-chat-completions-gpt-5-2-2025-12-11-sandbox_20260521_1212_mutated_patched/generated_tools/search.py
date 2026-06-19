from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def cql_search(
    query: str,
    cursor: Optional[str] = None,
    next: Optional[bool] = None,
    prev: Optional[bool] = None,
    max_results: int = 25,
    start: Optional[int] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
    excerpt: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/rest/api/search"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"cql": query, "limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if next is not None:
        params["next"] = next
    if prev is not None:
        params["prev"] = prev
    if start is not None:
        params["start"] = start
    if include_archived_spaces is not None:
        params["includeArchivedSpaces"] = include_archived_spaces
    if exclude_current_spaces is not None:
        params["excludeCurrentSpaces"] = exclude_current_spaces
    if excerpt is not None:
        params["excerpt"] = excerpt
    return client.request("GET", "/rest/api/search", params=params)


def cql_user_search(
    query: str,
    start: Optional[int] = None,
    max_results: int = 25,
    include: Optional[list[str]] = None,
    site_permission_type_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/rest/api/search/user"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"cql": query, "limit": max_results}
    if start is not None:
        params["start"] = start
    if include is not None:
        params["expand"] = include
    if site_permission_type_filter is not None:
        params["sitePermissionTypeFilter"] = site_permission_type_filter
    return client.request("GET", "/rest/api/search/user", params=params)
