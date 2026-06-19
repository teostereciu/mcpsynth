from typing import Any, Dict, Optional

from .notion_client import NotionClient, omit_none


def search_by_title(
    *,
    query: Optional[str] = None,
    filter: Optional[Dict[str, Any]] = None,
    sort: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """POST /search

    Source: docs/post-search.md
    """
    body = omit_none(
        {
            "query": query,
            "filter": filter,
            "sort": sort,
            "start_cursor": start_cursor,
            "page_size": page_size,
        }
    )
    return NotionClient().request("POST", "/search", json=body)
