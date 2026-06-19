import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.github_client import GitHubClient
from generated_tools.issues import list_issues_assigned_to_authenticated_user


mcp = FastMCP("github-rest")


def _client() -> GitHubClient:
    return GitHubClient(
        token=os.getenv("GITHUB_TOKEN"),
        base_url=os.getenv("GITHUB_API_BASE_URL"),
    )


@mcp.tool()
def github_list_issues_assigned_to_me(
    filter: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    """List issues assigned to the authenticated user across all visible repositories."""
    return list_issues_assigned_to_authenticated_user(
        _client(),
        filter=filter,
        state=state,
        labels=labels,
        sort=sort,
        direction=direction,
        since=since,
        collab=collab,
        orgs=orgs,
        owned=owned,
        pulls=pulls,
        per_page=per_page,
        page=page,
    )


if __name__ == "__main__":
    mcp.run_stdio()
