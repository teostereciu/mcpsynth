import json

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues, list_org_issues_assigned_to_me
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
    per_page: int = 30,
    page: int = 1,
    accept: str | None = None,
):
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
def github_list_org_issues_assigned_to_me(
    org: str,
    filter: str | None = None,
    state: str | None = None,
    labels: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    since: str | None = None,
    per_page: int = 30,
    page: int = 1,
    accept: str | None = None,
):
    return list_org_issues_assigned_to_me(
        org=org,
        filter=filter,
        state=state,
        labels=labels,
        sort=sort,
        direction=direction,
        since=since,
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
    per_page: int = 30,
    page: int = 1,
    accept: str | None = None,
):
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
    mcp.run()
