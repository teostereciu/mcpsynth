"""GitHub Search tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_search_tools(mcp: FastMCP):

    @mcp.tool()
    def search_code(q: str, sort: str = None, order: str = "desc",
                    per_page: int = 30, page: int = 1) -> dict:
        """Search for code across GitHub repositories. Use qualifiers like repo:owner/name, language:python, path:src/."""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/code", params)

    @mcp.tool()
    def search_commits(q: str, sort: str = None, order: str = "desc",
                       per_page: int = 30, page: int = 1) -> dict:
        """Search for commits. Use qualifiers like repo:owner/name, author:login, committer-date:>2020-01-01."""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/commits", params)

    @mcp.tool()
    def search_issues(q: str, sort: str = None, order: str = "desc",
                      per_page: int = 30, page: int = 1) -> dict:
        """Search for issues and pull requests. Use qualifiers like repo:owner/name, is:issue, state:open, label:bug."""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/issues", params)

    @mcp.tool()
    def search_repositories(q: str, sort: str = None, order: str = "desc",
                            per_page: int = 30, page: int = 1) -> dict:
        """Search for repositories. Use qualifiers like language:python, stars:>100, user:octocat."""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/repositories", params)

    @mcp.tool()
    def search_users(q: str, sort: str = None, order: str = "desc",
                     per_page: int = 30, page: int = 1) -> dict:
        """Search for users. Use qualifiers like type:user, location:london, followers:>100."""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/users", params)

    @mcp.tool()
    def search_topics(q: str, per_page: int = 30, page: int = 1) -> dict:
        """Search for topics on GitHub."""
        return _get("/search/topics", {"q": q, "per_page": per_page, "page": page})

    @mcp.tool()
    def search_labels(repository_id: int, q: str, sort: str = None,
                      order: str = "desc", per_page: int = 30, page: int = 1) -> dict:
        """Search for labels in a repository by repository ID."""
        params = {"repository_id": repository_id, "q": q, "order": order,
                  "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/labels", params)
