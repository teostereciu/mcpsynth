import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues
from generated_tools.pulls import list_pull_requests
from generated_tools.repos import create_org_repo, list_org_repos


mcp = FastMCP("github-rest")


def _default_repo_parts() -> Dict[str, str]:
    repo = os.getenv("GITHUB_TEST_REPO", "").strip()
    if repo and "/" in repo:
        owner, name = repo.split("/", 1)
        return {"owner": owner, "repo": name}
    return {"owner": "", "repo": ""}


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
    owner: str | None = None,
    repo: str | None = None,
    state: str | None = None,
    head: str | None = None,
    base: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    per_page: int | None = None,
    page: int | None = None,
    accept: str | None = None,
) -> Any:
    defaults = _default_repo_parts()
    owner = owner or defaults["owner"]
    repo = repo or defaults["repo"]
    if not owner or not repo:
        return {"error": "owner and repo are required (or set GITHUB_TEST_REPO=owner/repo)"}
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


@mcp.tool()
def github_list_org_repos(
    org: str,
    type: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    per_page: int | None = None,
    page: int | None = None,
    accept: str | None = None,
) -> Any:
    return list_org_repos(
        org=org,
        type=type,
        sort=sort,
        direction=direction,
        per_page=per_page,
        page=page,
        accept=accept,
    )


@mcp.tool()
def github_create_org_repo(
    org: str,
    name: str,
    description: str | None = None,
    homepage: str | None = None,
    private: bool | None = None,
    visibility: str | None = None,
    has_issues: bool | None = None,
    has_projects: bool | None = None,
    has_wiki: bool | None = None,
    has_downloads: bool | None = None,
    is_template: bool | None = None,
    team_id: int | None = None,
    auto_init: bool | None = None,
    gitignore_template: str | None = None,
    license_template: str | None = None,
    allow_squash_merge: bool | None = None,
    allow_merge_commit: bool | None = None,
    allow_rebase_merge: bool | None = None,
    allow_auto_merge: bool | None = None,
    delete_branch_on_merge: bool | None = None,
    squash_merge_commit_title: str | None = None,
    squash_merge_commit_message: str | None = None,
    merge_commit_title: str | None = None,
    merge_commit_message: str | None = None,
    custom_properties: Dict[str, Any] | None = None,
    accept: str | None = None,
) -> Any:
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
        has_downloads=has_downloads,
        is_template=is_template,
        team_id=team_id,
        auto_init=auto_init,
        gitignore_template=gitignore_template,
        license_template=license_template,
        allow_squash_merge=allow_squash_merge,
        allow_merge_commit=allow_merge_commit,
        allow_rebase_merge=allow_rebase_merge,
        allow_auto_merge=allow_auto_merge,
        delete_branch_on_merge=delete_branch_on_merge,
        squash_merge_commit_title=squash_merge_commit_title,
        squash_merge_commit_message=squash_merge_commit_message,
        merge_commit_title=merge_commit_title,
        merge_commit_message=merge_commit_message,
        custom_properties=custom_properties,
        accept=accept,
    )


if __name__ == "__main__":
    mcp.run()
