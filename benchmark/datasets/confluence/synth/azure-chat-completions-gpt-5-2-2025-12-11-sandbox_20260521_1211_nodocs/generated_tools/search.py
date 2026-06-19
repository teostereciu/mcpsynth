from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v1_cql_search(
    *,
    cql: str,
    limit: int = 25,
    start: int = 0,
    expand: Optional[str] = None,
) -> Any:
    """GET /rest/api/content/search"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"cql": cql, "limit": limit, "start": start}
    if expand:
        params["expand"] = expand
    return c.request("GET", "/rest/api/content/search", params=params)
