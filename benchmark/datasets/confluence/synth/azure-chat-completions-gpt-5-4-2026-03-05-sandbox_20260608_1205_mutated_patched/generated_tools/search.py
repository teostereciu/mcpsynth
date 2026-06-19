from typing import Any, List, Optional

from generated_tools.core import client


def search_content(
    query: str,
    cqlcontext: Optional[str] = None,
    cursor: Optional[str] = None,
    next: Optional[bool] = None,
    prev: Optional[bool] = None,
    max_results: Optional[int] = None,
    offset: Optional[int] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
    excerpt: Optional[str] = None,
    include: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/search",
        params={
            "cql": query,
            "cqlcontext": cqlcontext,
            "cursor": cursor,
            "next": next,
            "prev": prev,
            "limit": max_results,
            "start": offset,
            "includeArchivedSpaces": include_archived_spaces,
            "excludeCurrentSpaces": exclude_current_spaces,
            "excerpt": excerpt,
            "expand": include,
            "expand": expand,
        },
    )


def search_users(
    query: str,
    offset: Optional[int] = None,
    max_results: Optional[int] = None,
    include: Optional[List[str]] = None,
    site_permission_type_filter: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/search/user",
        params={
            "cql": query,
            "start": offset,
            "limit": max_results,
            "expand": include,
            "sitePermissionTypeFilter": site_permission_type_filter,
        },
    )
