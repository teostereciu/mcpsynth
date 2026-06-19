from typing import Any, Optional

from confluence_client import client


def search_content(
    cql: str,
    cqlcontext: Optional[str] = None,
    cursor: Optional[str] = None,
    next: Optional[bool] = None,
    prev: Optional[bool] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
    excerpt: Optional[str] = None,
    expand: Optional[list[str]] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/search",
        params={
            "cql": cql,
            "cqlcontext": cqlcontext,
            "cursor": cursor,
            "next": next,
            "prev": prev,
            "limit": limit,
            "start": start,
            "includeArchivedSpaces": include_archived_spaces,
            "excludeCurrentSpaces": exclude_current_spaces,
            "excerpt": excerpt,
            "expand": expand,
        },
    )


def search_users(
    cql: str,
    start: Optional[int] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    site_permission_type_filter: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/search/user",
        params={
            "cql": cql,
            "start": start,
            "limit": limit,
            "expand": expand,
            "sitePermissionTypeFilter": site_permission_type_filter,
        },
    )
