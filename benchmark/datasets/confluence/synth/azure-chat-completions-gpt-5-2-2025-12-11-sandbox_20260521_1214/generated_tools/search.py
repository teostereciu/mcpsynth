from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def cql_search(
    *,
    cql: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    start: Optional[int] = None,
    expand: Optional[list[str]] = None,
    excerpt: Optional[str] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /wiki/rest/api/search"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"cql": cql, "limit": limit}
    if cursor:
        params["cursor"] = cursor
    if start is not None:
        params["start"] = start
    if expand:
        params["expand"] = expand
    if excerpt:
        params["excerpt"] = excerpt
    if include_archived_spaces is not None:
        params["includeArchivedSpaces"] = include_archived_spaces
    if exclude_current_spaces is not None:
        params["excludeCurrentSpaces"] = exclude_current_spaces
    return client.request("GET", "/rest/api/search", params=params)
