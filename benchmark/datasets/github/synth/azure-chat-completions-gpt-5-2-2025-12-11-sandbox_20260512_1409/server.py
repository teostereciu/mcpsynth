import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.github_client import GitHubClient, split_owner_repo
from generated_tools import issues as issues_api
from generated_tools import pulls as pulls_api
from generated_tools import repos as repos_api
from generated_tools import contents as contents_api
from generated_tools import search as search_api
from generated_tools import actions_workflows as actions_workflows_api
from generated_tools import actions_runs as actions_runs_api
from generated_tools import releases as releases_api
from generated_tools import branch_protection as branch_protection_api


mcp = FastMCP("github-rest")
client = GitHubClient()


def _resolve_owner_repo(owner: Optional[str], repo: Optional[str], owner_repo: Optional[str]) -> Dict[str, str]:
    if owner and repo:
        return {"owner": owner, "repo": repo}
    o, r = split_owner_repo(owner_repo or os.getenv("GITHUB_TEST_REPO"))
    if not o or not r:
        raise ValueError("owner/repo not provided and GITHUB_TEST_REPO not set")
    return {"owner": o, "repo": r}


@mcp.tool()
def github_list_my_issues(
    filter: str = "assigned",
    state: str = "open",
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    return issues_api.list_my_issues(
        client,
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


@mcp.tool()
def github_list_repo_issues(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    milestone: Optional[str] = None,
    state: str = "open",
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.list_repo_issues(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        milestone=milestone,
        state=state,
        assignee=assignee,
        creator=creator,
        mentioned=mentioned,
        labels=labels,
        sort=sort,
        direction=direction,
        since=since,
        per_page=per_page,
        page=page,
    )


@mcp.tool()
def github_get_issue(
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.get_issue(client, owner=orr["owner"], repo=orr["repo"], issue_number=issue_number)


@mcp.tool()
def github_create_issue(
    title: str,
    body: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.create_issue(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        title=title,
        body=body,
        assignees=assignees,
        milestone=milestone,
        labels=labels,
    )


@mcp.tool()
def github_update_issue(
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.update_issue(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        issue_number=issue_number,
        title=title,
        body=body,
        state=state,
        state_reason=state_reason,
        assignees=assignees,
        milestone=milestone,
        labels=labels,
    )


@mcp.tool()
def github_lock_issue(
    issue_number: int,
    lock_reason: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.lock_issue(client, owner=orr["owner"], repo=orr["repo"], issue_number=issue_number, lock_reason=lock_reason)


@mcp.tool()
def github_unlock_issue(
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return issues_api.unlock_issue(client, owner=orr["owner"], repo=orr["repo"], issue_number=issue_number)


@mcp.tool()
def github_list_pulls(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.list_pulls(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        state=state,
        head=head,
        base=base,
        sort=sort,
        direction=direction,
        per_page=per_page,
        page=page,
    )


@mcp.tool()
def github_get_pull(
    pull_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.get_pull(client, owner=orr["owner"], repo=orr["repo"], pull_number=pull_number)


@mcp.tool()
def github_create_pull(
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.create_pull(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        title=title,
        head=head,
        base=base,
        body=body,
        draft=draft,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def github_update_pull(
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.update_pull(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        pull_number=pull_number,
        title=title,
        body=body,
        state=state,
        base=base,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def github_merge_pull(
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.merge_pull(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        pull_number=pull_number,
        commit_title=commit_title,
        commit_message=commit_message,
        merge_method=merge_method,
        sha=sha,
    )


@mcp.tool()
def github_list_pull_commits(
    pull_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.list_pull_commits(client, owner=orr["owner"], repo=orr["repo"], pull_number=pull_number, per_page=per_page, page=page)


@mcp.tool()
def github_list_pull_files(
    pull_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.list_pull_files(client, owner=orr["owner"], repo=orr["repo"], pull_number=pull_number, per_page=per_page, page=page)


@mcp.tool()
def github_create_pull_review(
    pull_number: int,
    body: Optional[str] = None,
    event: Optional[str] = None,
    comments: Optional[list[dict]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return pulls_api.create_pull_review(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        pull_number=pull_number,
        body=body,
        event=event,
        comments=comments,
    )


@mcp.tool()
def github_get_repo(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return repos_api.get_repo(client, owner=orr["owner"], repo=orr["repo"])


@mcp.tool()
def github_list_org_repos(org: str, type: str = "all", sort: str = "created", direction: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    return repos_api.list_org_repos(client, org=org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def github_create_org_repo(org: str, name: str, description: Optional[str] = None, private: Optional[bool] = None) -> Any:
    return repos_api.create_org_repo(client, org=org, name=name, description=description, private=private)


@mcp.tool()
def github_delete_repo(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return repos_api.delete_repo(client, owner=orr["owner"], repo=orr["repo"])


@mcp.tool()
def github_get_content(
    path: str,
    ref: Optional[str] = None,
    media: str = "object",
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return contents_api.get_content(client, owner=orr["owner"], repo=orr["repo"], path=path, ref=ref, media=media)


@mcp.tool()
def github_create_or_update_file(
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return contents_api.create_or_update_file(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        path=path,
        message=message,
        content_base64=content_base64,
        sha=sha,
        branch=branch,
        committer=committer,
        author=author,
    )


@mcp.tool()
def github_delete_file(
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return contents_api.delete_file(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        path=path,
        message=message,
        sha=sha,
        branch=branch,
        committer=committer,
        author=author,
    )


@mcp.tool()
def github_search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1, text_match: bool = False) -> Any:
    return search_api.search_code(client, q=q, sort=sort, order=order, per_page=per_page, page=page, text_match=text_match)


@mcp.tool()
def github_search_issues_and_prs(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1, text_match: bool = False) -> Any:
    return search_api.search_issues_and_prs(client, q=q, sort=sort, order=order, per_page=per_page, page=page, text_match=text_match)


@mcp.tool()
def github_search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    return search_api.search_repositories(client, q=q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_list_workflows(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return actions_workflows_api.list_workflows(client, owner=orr["owner"], repo=orr["repo"], per_page=per_page, page=page)


@mcp.tool()
def github_create_workflow_dispatch(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, workflow_id: str = "", ref: str = "", inputs: Optional[Dict[str, Any]] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return actions_workflows_api.create_workflow_dispatch(client, owner=orr["owner"], repo=orr["repo"], workflow_id=workflow_id, ref=ref, inputs=inputs)


@mcp.tool()
def github_list_workflow_runs(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: int = 30, page: int = 1, actor: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return actions_runs_api.list_workflow_runs(client, owner=orr["owner"], repo=orr["repo"], per_page=per_page, page=page, actor=actor, branch=branch, event=event, status=status)


@mcp.tool()
def github_cancel_workflow_run(run_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return actions_runs_api.cancel_workflow_run(client, owner=orr["owner"], repo=orr["repo"], run_id=run_id)


@mcp.tool()
def github_rerun_workflow_run(run_id: int, enable_debug_logging: bool = False, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return actions_runs_api.rerun_workflow_run(client, owner=orr["owner"], repo=orr["repo"], run_id=run_id, enable_debug_logging=enable_debug_logging)


@mcp.tool()
def github_list_releases(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return releases_api.list_releases(client, owner=orr["owner"], repo=orr["repo"], per_page=per_page, page=page)


@mcp.tool()
def github_create_release(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, tag_name: str = "", name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return releases_api.create_release(client, owner=orr["owner"], repo=orr["repo"], tag_name=tag_name, name=name, body=body, draft=draft, prerelease=prerelease)


@mcp.tool()
def github_get_branch_protection(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, branch: str = "main") -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return branch_protection_api.get_branch_protection(client, owner=orr["owner"], repo=orr["repo"], branch=branch)


@mcp.tool()
def github_update_branch_protection(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, branch: str = "main", required_status_checks: Optional[Dict[str, Any]] = None, enforce_admins: Optional[bool] = None, required_pull_request_reviews: Optional[Dict[str, Any]] = None, restrictions: Optional[Dict[str, Any]] = None) -> Any:
    try:
        orr = _resolve_owner_repo(owner, repo, owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return branch_protection_api.update_branch_protection(
        client,
        owner=orr["owner"],
        repo=orr["repo"],
        branch=branch,
        required_status_checks=required_status_checks,
        enforce_admins=enforce_admins,
        required_pull_request_reviews=required_pull_request_reviews,
        restrictions=restrictions,
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
