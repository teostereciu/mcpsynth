import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues
from generated_tools.pulls import list_pull_requests

mcp = FastMCP("github-rest")


@mcp.tool()
def github_list_my_issues(
    filter: str = "assigned",
    state: str = "open",
    labels: str | None = None,
    sort: str = "created",
    direction: str = "desc",
    since: str | None = None,
    collab: bool | None = None,
    orgs: bool | None = None,
    owned: bool | None = None,
    pulls: bool | None = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    return list_my_issues(
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
        accept=accept,
    )


@mcp.tool()
def github_list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open",
    head: str | None = None,
    base: str | None = None,
    sort: str = "created",
    direction: str | None = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    return list_pull_requests(
        owner=owner,
        repo=repo,
        state=state,
        head=head,
        base=base,
        sort=sort,
        direction=direction,
        per_page=per_page,
        page=page,
        accept=accept,
    )


if __name__ == "__main__":
    # Helpful default for local testing.
    if not os.getenv("GITHUB_API_BASE_URL"):
        os.environ["GITHUB_API_BASE_URL"] = "https://api.github.com"
    mcp.run()
