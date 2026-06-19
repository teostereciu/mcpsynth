"""GitHub Search tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _headers():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_search_tools(mcp: FastMCP):

    @mcp.tool()
    def search_code(q: str, sort: str = "", order: str = "desc",
                    per_page: int = 30, page: int = 1) -> dict:
        """Search for code across GitHub repositories.
        Example q: 'addClass in:file language:js repo:jquery/jquery'"""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/code", params)

    @mcp.tool()
    def search_commits(q: str, sort: str = "", order: str = "desc",
                       per_page: int = 30, page: int = 1) -> dict:
        """Search for commits across GitHub.
        Example q: 'repo:octocat/Spoon-Knife css'"""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/commits", params)

    @mcp.tool()
    def search_issues(q: str, sort: str = "", order: str = "desc",
                      per_page: int = 30, page: int = 1) -> dict:
        """Search for issues and pull requests.
        Example q: 'windows label:bug language:python state:open'"""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/issues", params)

    @mcp.tool()
    def search_repositories(q: str, sort: str = "", order: str = "desc",
                            per_page: int = 30, page: int = 1) -> dict:
        """Search for repositories.
        Example q: 'tetris language:assembly'"""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/repositories", params)

    @mcp.tool()
    def search_users(q: str, sort: str = "", order: str = "desc",
                     per_page: int = 30, page: int = 1) -> dict:
        """Search for users.
        Example q: 'tom repos:>42 followers:>1000'"""
        params = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return _get("/search/users", params)

    @mcp.tool()
    def search_topics(q: str, per_page: int = 30, page: int = 1) -> dict:
        """Search for topics.
        Example q: 'ruby is:featured'"""
        return _get("/search/topics", {"q": q, "per_page": per_page, "page": page})

    @mcp.tool()
    def search_labels(repository_id: int, q: str, sort: str = "name",
                      order: str = "asc", per_page: int = 30, page: int = 1) -> dict:
        """Search for labels in a repository by repository ID."""
        return _get("/search/labels",
                    {"repository_id": repository_id, "q": q, "sort": sort,
                     "order": order, "per_page": per_page, "page": page})
