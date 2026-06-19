from typing import Any, Dict, Optional

from .http import confluence_request


def cql_search(cql: str, limit: int = 25, start: int = 0, expand: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"cql": cql, "limit": limit, "start": start}
    if expand:
        params["expand"] = expand
    return confluence_request("GET", "/rest/api/content/search", params=params)
