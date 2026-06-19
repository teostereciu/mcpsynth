from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def cql_search(
    query: str,
    *,
    cursor: Optional[str] = None,
    max_results: int = 25,
    include_archived_spaces: Optional[bool] = None,
    excerpt: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /rest/api/search"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"query": query, "max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    if include_archived_spaces is not None:
        params["includeArchivedSpaces"] = str(include_archived_spaces).lower()
    if excerpt:
        params["excerpt"] = excerpt
    status, body, headers = c.request("GET", "/rest/api/search", params=params)
    return ok_or_error(status, body, headers)


def cql_search_users(query: str, *, max_results: int = 25, offset: int = 0) -> Dict[str, Any]:
    """GET /rest/api/search/user"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"query": query, "max_results": max_results, "offset": offset}
    status, body, headers = c.request("GET", "/rest/api/search/user", params=params)
    return ok_or_error(status, body, headers)
