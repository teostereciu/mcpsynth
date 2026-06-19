from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues

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
):
    """List issues assigned to the authenticated user (across all visible repositories)."""
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


if __name__ == "__main__":
    mcp.run_stdio()
