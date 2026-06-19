"""MCP tools for GitHub Search API."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get

def register(mcp: FastMCP):

    @mcp.tool()
    def search_repositories(
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search repositories. sort: stars|forks|help-wanted-issues|updated."""
        params: dict = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/repositories", params=params)

    @mcp.tool()
    def search_code(
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search code across GitHub. q supports qualifiers like repo:, path:, language:."""
        params: dict = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/code", params=params)

    @mcp.tool()
    def search_issues_and_prs(
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search issues and pull requests. sort: comments|reactions|created|updated."""
        params: dict = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/issues", params=params)

    @mcp.tool()
    def search_commits(
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search commits. sort: author-date|committer-date."""
        params: dict = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/commits", params=params)

    @mcp.tool()
    def search_users(
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search users and organizations. sort: followers|repositories|joined."""
        params: dict = {"q": q, "order": order, "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/users", params=params)

    @mcp.tool()
    def search_topics(q: str, per_page: int = 30, page: int = 1) -> dict | list:
        """Search topics."""
        return gh_get("/search/topics", params={"q": q, "per_page": per_page, "page": page})

    @mcp.tool()
    def search_labels(
        repository_id: int,
        q: str,
        sort: str = "",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """Search labels in a repository by repository_id (numeric)."""
        params: dict = {"repository_id": repository_id, "q": q, "order": order,
                        "per_page": per_page, "page": page}
        if sort:
            params["sort"] = sort
        return gh_get("/search/labels", params=params)
