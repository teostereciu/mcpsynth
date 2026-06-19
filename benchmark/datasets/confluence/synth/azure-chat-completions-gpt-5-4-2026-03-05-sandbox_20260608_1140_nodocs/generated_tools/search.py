from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def search_content(cql: str, limit: int = 25, cursor: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    params = {"cql": cql, "limit": limit}
    if cursor:
        params["cursor"] = cursor
    if expand:
        params["expand"] = expand
    return client.request("GET", "/rest/api/search", params=params)
