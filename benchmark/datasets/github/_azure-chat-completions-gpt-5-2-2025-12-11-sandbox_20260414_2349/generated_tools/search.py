"""Search tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import github_request


@mcp.tool
def search_repositories(q: str, per_page: int = 30, page: int = 1, sort: Optional[str] = None, order: Optional[str] = None) -> Dict[str, Any]:
    """Search repositories."""
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return github_request("GET", "/search/repositories", params=params)


@mcp.tool
def search_issues(q: str, per_page: int = 30, page: int = 1, sort: Optional[str] = None, order: Optional[str] = None) -> Dict[str, Any]:
    """Search issues and pull requests."""
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return github_request("GET", "/search/issues", params=params)
