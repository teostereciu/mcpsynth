from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def search_content(
    *,
    cql: str,
    cqlcontext: Optional[str] = None,
    cursor: Optional[str] = None,
    next: Optional[bool] = None,
    prev: Optional[bool] = None,
    limit: Optional[int] = 25,
    start: Optional[int] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
    excerpt: Optional[str] = None,
    expand: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """GET /wiki/rest/api/search"""
    params: Dict[str, Any] = {"cql": cql}
    if cqlcontext is not None:
        params["cqlcontext"] = cqlcontext
    if cursor is not None:
        params["cursor"] = cursor
    if next is not None:
        params["next"] = next
    if prev is not None:
        params["prev"] = prev
    if limit is not None:
        params["limit"] = limit
    if start is not None:
        params["start"] = start
    if include_archived_spaces is not None:
        params["includeArchivedSpaces"] = include_archived_spaces
    if exclude_current_spaces is not None:
        params["excludeCurrentSpaces"] = exclude_current_spaces
    if excerpt is not None:
        params["excerpt"] = excerpt
    if expand:
        params["expand"] = expand

    return ConfluenceClient().request("GET", "/rest/api/search", params=params)  # type: ignore[return-value]


def search_users(*, cql: str, start: Optional[int] = None, limit: Optional[int] = 25, expand: Optional[List[str]] = None,
                 site_permission_type_filter: Optional[str] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/search/user"""
    params: Dict[str, Any] = {"cql": cql}
    if start is not None:
        params["start"] = start
    if limit is not None:
        params["limit"] = limit
    if expand:
        params["expand"] = expand
    if site_permission_type_filter is not None:
        params["sitePermissionTypeFilter"] = site_permission_type_filter

    return ConfluenceClient().request("GET", "/rest/api/search/user", params=params)  # type: ignore[return-value]
