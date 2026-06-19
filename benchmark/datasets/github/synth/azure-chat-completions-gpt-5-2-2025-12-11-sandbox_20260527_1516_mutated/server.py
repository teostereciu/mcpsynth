import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues
from generated_tools.pulls import list_pull_requests

mcp = FastMCP("github-rest")


@mcp.tool()
def github_list_my_issues(
    filter: str | None = None,
    state: str | None = None,
    labels: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    since: str | None = None,
    collab: bool | None = None,
    orgs: bool | None = None,
    owned: bool | None = None,
    pulls: bool | None = None,
    per_page: int | None = None,
    page: int | None = None,
    accept: str | None = None,
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
    state: str | None = None,
    head: str | None = None,
    base: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    per_page: int | None = None,
    page: int | None = None,
    accept: str | None = None,
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
    # FastMCP runs over stdio by default.
    # Environment variables:
    # - GITHUB_TOKEN
    # - GITHUB_API_BASE_URL
    # - GITHUB_TEST_REPO
    mcp.run()
