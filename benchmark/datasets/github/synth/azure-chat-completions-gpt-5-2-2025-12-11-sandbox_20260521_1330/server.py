import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.github_client import GitHubClient, parse_owner_repo
from generated_tools import issues as issues_api
from generated_tools import pulls as pulls_api
from generated_tools import repos as repos_api
from generated_tools import contents as contents_api
from generated_tools import search as search_api
from generated_tools import actions_workflows as workflows_api
from generated_tools import actions_runs as runs_api
from generated_tools import releases as releases_api
from generated_tools import webhooks as webhooks_api
from generated_tools import branch_protection as branch_protection_api


mcp = FastMCP("github-rest")


def _client() -> GitHubClient:
    return GitHubClient()


def _resolve_owner_repo(owner: Optional[str], repo: Optional[str], owner_repo: Optional[str]) -> Dict[str, str]:
    if owner and repo:
        return {"owner": owner, "repo": repo}
    o, r, err = parse_owner_repo(owner_repo)
    if err:
        return err
    return {"owner": o, "repo": r}


# -------------------- Issues --------------------


@mcp.tool()
def list_my_issues(
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
) -> Dict[str, Any]:
    return issues_api.list_my_issues(
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


@mcp.tool()
def list_repo_issues(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    milestone: Optional[str] = None,
    state: Optional[str] = None,
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.list_repo_issues(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
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
def get_issue(
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.get_issue(_client(), owner=resolved["owner"], repo=resolved["repo"], issue_number=issue_number)


@mcp.tool()
def create_issue(
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.create_issue(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        title=title,
        body=body,
        assignees=assignees,
        milestone=milestone,
        labels=labels,
    )


@mcp.tool()
def update_issue(
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.update_issue(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
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
def lock_issue(
    issue_number: int,
    lock_reason: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.lock_issue(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        issue_number=issue_number,
        lock_reason=lock_reason,
    )


@mcp.tool()
def unlock_issue(
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.unlock_issue(_client(), owner=resolved["owner"], repo=resolved["repo"], issue_number=issue_number)


@mcp.tool()
def add_issue_assignees(
    issue_number: int,
    assignees: List[str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.add_assignees(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        issue_number=issue_number,
        assignees=assignees,
    )


@mcp.tool()
def remove_issue_assignees(
    issue_number: int,
    assignees: List[str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return issues_api.remove_assignees(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        issue_number=issue_number,
        assignees=assignees,
    )


# -------------------- Pull Requests --------------------


@mcp.tool()
def list_pulls(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    state: Optional[str] = None,
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return pulls_api.list_pulls(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        state=state,
        head=head,
        base=base,
        sort=sort,
        direction=direction,
        per_page=per_page,
        page=page,
    )


@mcp.tool()
def get_pull(
    pull_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return pulls_api.get_pull(_client(), owner=resolved["owner"], repo=resolved["repo"], pull_number=pull_number)


@mcp.tool()
def create_pull(
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return pulls_api.create_pull(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        title=title,
        head=head,
        base=base,
        body=body,
        draft=draft,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def update_pull(
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return pulls_api.update_pull(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        pull_number=pull_number,
        title=title,
        body=body,
        state=state,
        base=base,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def merge_pull(
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return pulls_api.merge_pull(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        pull_number=pull_number,
        commit_title=commit_title,
        commit_message=commit_message,
        merge_method=merge_method,
        sha=sha,
    )


# -------------------- Repositories --------------------


@mcp.tool()
def get_repo(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return repos_api.get_repo(_client(), owner=resolved["owner"], repo=resolved["repo"])


@mcp.tool()
def list_org_repos(
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    return repos_api.list_org_repos(_client(), org=org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def create_org_repo(
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    is_template: Optional[bool] = None,
    auto_init: Optional[bool] = None,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
) -> Dict[str, Any]:
    return repos_api.create_org_repo(
        _client(),
        org=org,
        name=name,
        description=description,
        homepage=homepage,
        private=private,
        visibility=visibility,
        has_issues=has_issues,
        has_projects=has_projects,
        has_wiki=has_wiki,
        is_template=is_template,
        auto_init=auto_init,
        gitignore_template=gitignore_template,
        license_template=license_template,
    )


@mcp.tool()
def update_repo(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    default_branch: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    is_template: Optional[bool] = None,
    archived: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return repos_api.update_repo(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        name=name,
        description=description,
        homepage=homepage,
        private=private,
        visibility=visibility,
        default_branch=default_branch,
        has_issues=has_issues,
        has_projects=has_projects,
        has_wiki=has_wiki,
        is_template=is_template,
        archived=archived,
        allow_squash_merge=allow_squash_merge,
        allow_merge_commit=allow_merge_commit,
        allow_rebase_merge=allow_rebase_merge,
        allow_auto_merge=allow_auto_merge,
        delete_branch_on_merge=delete_branch_on_merge,
    )


@mcp.tool()
def fork_repo(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    organization: Optional[str] = None,
    name: Optional[str] = None,
    default_branch_only: Optional[bool] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return repos_api.fork_repo(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        organization=organization,
        name=name,
        default_branch_only=default_branch_only,
    )


# -------------------- Contents --------------------


@mcp.tool()
def get_content(
    path: str,
    ref: Optional[str] = None,
    accept: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return contents_api.get_content(_client(), owner=resolved["owner"], repo=resolved["repo"], path=path, ref=ref, accept=accept)


@mcp.tool()
def create_or_update_file(
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
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return contents_api.create_or_update_file(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        path=path,
        message=message,
        content_base64=content_base64,
        sha=sha,
        branch=branch,
        committer=committer,
        author=author,
    )


@mcp.tool()
def delete_file(
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return contents_api.delete_file(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        path=path,
        message=message,
        sha=sha,
        branch=branch,
        committer=committer,
        author=author,
    )


# -------------------- Search --------------------


@mcp.tool()
def search_code(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Dict[str, Any]:
    return search_api.search_code(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page, text_match=text_match)


@mcp.tool()
def search_issues_and_prs(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Dict[str, Any]:
    return search_api.search_issues_and_prs(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page, text_match=text_match)


@mcp.tool()
def search_repositories(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    return search_api.search_repositories(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page)


# -------------------- Actions: Workflows --------------------


@mcp.tool()
def list_workflows(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.list_workflows(_client(), owner=resolved["owner"], repo=resolved["repo"], per_page=per_page, page=page)


@mcp.tool()
def get_workflow(workflow_id: str, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.get_workflow(_client(), owner=resolved["owner"], repo=resolved["repo"], workflow_id=workflow_id)


@mcp.tool()
def enable_workflow(workflow_id: str, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.enable_workflow(_client(), owner=resolved["owner"], repo=resolved["repo"], workflow_id=workflow_id)


@mcp.tool()
def disable_workflow(workflow_id: str, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.disable_workflow(_client(), owner=resolved["owner"], repo=resolved["repo"], workflow_id=workflow_id)


@mcp.tool()
def create_workflow_dispatch(
    workflow_id: str,
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.create_workflow_dispatch(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        workflow_id=workflow_id,
        ref=ref,
        inputs=inputs,
    )


@mcp.tool()
def get_workflow_timing(workflow_id: str, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return workflows_api.get_workflow_timing(_client(), owner=resolved["owner"], repo=resolved["repo"], workflow_id=workflow_id)


# -------------------- Actions: Runs --------------------


@mcp.tool()
def list_workflow_runs(
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return runs_api.list_workflow_runs(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        actor=actor,
        branch=branch,
        event=event,
        status=status,
        per_page=per_page,
        page=page,
        created=created,
        exclude_pull_requests=exclude_pull_requests,
        check_suite_id=check_suite_id,
        head_sha=head_sha,
    )


@mcp.tool()
def get_workflow_run(run_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return runs_api.get_workflow_run(_client(), owner=resolved["owner"], repo=resolved["repo"], run_id=run_id)


@mcp.tool()
def cancel_workflow_run(run_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return runs_api.cancel_workflow_run(_client(), owner=resolved["owner"], repo=resolved["repo"], run_id=run_id)


@mcp.tool()
def rerun_workflow_run(
    run_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return runs_api.rerun_workflow_run(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        run_id=run_id,
        enable_debug_logging=enable_debug_logging,
    )


@mcp.tool()
def rerun_job(
    job_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return runs_api.rerun_job(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        job_id=job_id,
        enable_debug_logging=enable_debug_logging,
    )


# -------------------- Releases --------------------


@mcp.tool()
def list_releases(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.list_releases(_client(), owner=resolved["owner"], repo=resolved["repo"], per_page=per_page, page=page)


@mcp.tool()
def get_release(release_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.get_release(_client(), owner=resolved["owner"], repo=resolved["repo"], release_id=release_id)


@mcp.tool()
def get_latest_release(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.get_latest_release(_client(), owner=resolved["owner"], repo=resolved["repo"])


@mcp.tool()
def create_release(
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: Optional[bool] = None,
    make_latest: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.create_release(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        tag_name=tag_name,
        target_commitish=target_commitish,
        name=name,
        body=body,
        draft=draft,
        prerelease=prerelease,
        discussion_category_name=discussion_category_name,
        generate_release_notes=generate_release_notes,
        make_latest=make_latest,
    )


@mcp.tool()
def update_release(
    release_id: int,
    tag_name: Optional[str] = None,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    make_latest: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.update_release(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        release_id=release_id,
        tag_name=tag_name,
        target_commitish=target_commitish,
        name=name,
        body=body,
        draft=draft,
        prerelease=prerelease,
        make_latest=make_latest,
    )


@mcp.tool()
def delete_release(release_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.delete_release(_client(), owner=resolved["owner"], repo=resolved["repo"], release_id=release_id)


@mcp.tool()
def generate_release_notes(
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return releases_api.generate_release_notes(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        tag_name=tag_name,
        target_commitish=target_commitish,
        previous_tag_name=previous_tag_name,
        configuration_file_path=configuration_file_path,
    )


# -------------------- Webhooks --------------------


@mcp.tool()
def list_repo_webhooks(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.list_repo_webhooks(_client(), owner=resolved["owner"], repo=resolved["repo"], per_page=per_page, page=page)


@mcp.tool()
def get_repo_webhook(hook_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.get_repo_webhook(_client(), owner=resolved["owner"], repo=resolved["repo"], hook_id=hook_id)


@mcp.tool()
def create_repo_webhook(
    config: Dict[str, Any],
    events: Optional[List[str]] = None,
    active: Optional[bool] = None,
    name: str = "web",
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.create_repo_webhook(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        config=config,
        events=events,
        active=active,
        name=name,
    )


@mcp.tool()
def update_repo_webhook(
    hook_id: int,
    config: Optional[Dict[str, Any]] = None,
    events: Optional[List[str]] = None,
    add_events: Optional[List[str]] = None,
    remove_events: Optional[List[str]] = None,
    active: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.update_repo_webhook(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        hook_id=hook_id,
        config=config,
        events=events,
        add_events=add_events,
        remove_events=remove_events,
        active=active,
    )


@mcp.tool()
def delete_repo_webhook(hook_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.delete_repo_webhook(_client(), owner=resolved["owner"], repo=resolved["repo"], hook_id=hook_id)


@mcp.tool()
def ping_repo_webhook(hook_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.ping_repo_webhook(_client(), owner=resolved["owner"], repo=resolved["repo"], hook_id=hook_id)


@mcp.tool()
def test_repo_webhook(hook_id: int, owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return webhooks_api.test_repo_webhook(_client(), owner=resolved["owner"], repo=resolved["repo"], hook_id=hook_id)


# -------------------- Branch Protection --------------------


@mcp.tool()
def get_branch_protection(
    branch: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return branch_protection_api.get_branch_protection(_client(), owner=resolved["owner"], repo=resolved["repo"], branch=branch)


@mcp.tool()
def update_branch_protection(
    branch: str,
    required_status_checks: Optional[Dict[str, Any]] = None,
    enforce_admins: Optional[bool] = None,
    required_pull_request_reviews: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    required_linear_history: Optional[Dict[str, Any]] = None,
    allow_force_pushes: Optional[Dict[str, Any]] = None,
    allow_deletions: Optional[Dict[str, Any]] = None,
    block_creations: Optional[Dict[str, Any]] = None,
    required_conversation_resolution: Optional[Dict[str, Any]] = None,
    lock_branch: Optional[Dict[str, Any]] = None,
    allow_fork_syncing: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return branch_protection_api.update_branch_protection(
        _client(),
        owner=resolved["owner"],
        repo=resolved["repo"],
        branch=branch,
        required_status_checks=required_status_checks,
        enforce_admins=enforce_admins,
        required_pull_request_reviews=required_pull_request_reviews,
        restrictions=restrictions,
        required_linear_history=required_linear_history,
        allow_force_pushes=allow_force_pushes,
        allow_deletions=allow_deletions,
        block_creations=block_creations,
        required_conversation_resolution=required_conversation_resolution,
        lock_branch=lock_branch,
        allow_fork_syncing=allow_fork_syncing,
    )


@mcp.tool()
def delete_branch_protection(
    branch: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Dict[str, Any]:
    resolved = _resolve_owner_repo(owner, repo, owner_repo)
    if "error" in resolved:
        return resolved
    return branch_protection_api.delete_branch_protection(_client(), owner=resolved["owner"], repo=resolved["repo"], branch=branch)


if __name__ == "__main__":
    # FastMCP runs over stdio by default
    mcp.run()
