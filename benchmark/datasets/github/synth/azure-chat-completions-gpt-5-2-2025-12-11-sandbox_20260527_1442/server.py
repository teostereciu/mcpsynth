import os
from mcp.server.fastmcp import FastMCP

from generated_tools.pulls import list_pull_requests
from generated_tools.repos import create_org_repo, list_org_repos

mcp = FastMCP("github-rest")


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
    )


@mcp.tool()
def github_list_org_repos(
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: str | None = None,
    per_page: int = 30,
    page: int = 1,
):
    return list_org_repos(
        org=org,
        type=type,
        sort=sort,
        direction=direction,
        per_page=per_page,
        page=page,
    )


@mcp.tool()
def github_create_org_repo(
    org: str,
    name: str,
    description: str | None = None,
    homepage: str | None = None,
    private: bool = False,
    visibility: str | None = None,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    auto_init: bool = False,
    is_template: bool = False,
):
    return create_org_repo(
        org=org,
        name=name,
        description=description,
        homepage=homepage,
        private=private,
        visibility=visibility,
        has_issues=has_issues,
        has_projects=has_projects,
        has_wiki=has_wiki,
        auto_init=auto_init,
        is_template=is_template,
    )


if __name__ == "__main__":
    # FastMCP runs over stdio by default.
    # Ensure token is present for write operations.
    if not os.getenv("GITHUB_API_BASE_URL"):
        os.environ["GITHUB_API_BASE_URL"] = "https://api.github.com"
    mcp.run()
