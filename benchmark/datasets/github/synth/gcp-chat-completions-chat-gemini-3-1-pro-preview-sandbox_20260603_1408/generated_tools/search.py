from typing import Any, Dict, List, Optional
from .client import make_request

def search_code(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search code."""
    return make_request("GET", "/search/code", params={"q": q, "per_page": per_page, "page": page})

def search_issues(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search issues and pull requests."""
    return make_request("GET", "/search/issues", params={"q": q, "per_page": per_page, "page": page})

def search_repositories(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search repositories."""
    return make_request("GET", "/search/repositories", params={"q": q, "per_page": per_page, "page": page})
