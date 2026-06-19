from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def search_code(q: str, per_page: int = 30, page: int = 1) -> dict:
    """Search code."""
    return make_request("GET", "/search/code", params={"q": q, "per_page": per_page, "page": page})

@mcp.tool()
def search_issues(q: str, per_page: int = 30, page: int = 1) -> dict:
    """Search issues and pull requests."""
    return make_request("GET", "/search/issues", params={"q": q, "per_page": per_page, "page": page})

@mcp.tool()
def search_repositories(q: str, per_page: int = 30, page: int = 1) -> dict:
    """Search repositories."""
    return make_request("GET", "/search/repositories", params={"q": q, "per_page": per_page, "page": page})
