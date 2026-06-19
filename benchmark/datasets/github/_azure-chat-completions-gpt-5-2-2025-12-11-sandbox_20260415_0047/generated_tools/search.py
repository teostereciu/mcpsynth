from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import GitHubClient


@mcp.tool()
def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """Search repositories."""
    try:
        client = GitHubClient.from_env()
        params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
        if sort is not None:
            params["sort"] = sort
        if order is not None:
            params["order"] = order
        status, payload = client.request("GET", "/search/repositories", params=params)
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_issues(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """Search issues and pull requests."""
    try:
        client = GitHubClient.from_env()
        params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
        if sort is not None:
            params["sort"] = sort
        if order is not None:
            params["order"] = order
        status, payload = client.request("GET", "/search/issues", params=params)
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}
