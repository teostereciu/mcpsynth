import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.github_client import GitHubClient
from generated_tools import actions_runs, contents, issue_comments, issues, pulls, releases, repos, search


mcp = FastMCP("github-rest")


def _client() -> GitHubClient:
    return GitHubClient(
        token=os.getenv("GITHUB_TOKEN"),
        base_url=os.getenv("GITHUB_API_BASE_URL"),
    )


@mcp.tool()
def github_get_repo(owner: str, repo: str) -> Any:
    """GET /repos/{owner}/{repo}"""
    return repos.get_repo(_client(), owner=owner, repo=repo)


@mcp.tool()
def github_list_org_repos(
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /orgs/{org}/repos"""
    return repos.list_org_repos(_client(), org=org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def github_create_org_repo(
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    visibility: Optional[str] = None,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    is_template: bool = False,
    auto_init: bool = False,
) -> Any:
    """POST /orgs/{org}/repos"""
    return repos.create_org_repo(
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
    )


@mcp.tool()
def github_update_repo(
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    default_branch: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    archived: Optional[bool] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}"""
    return repos.update_repo(
        _client(),
        owner=owner,
        repo=repo,
        name=name,
        description=description,
        homepage=homepage,
        private=private,
        default_branch=default_branch,
        has_issues=has_issues,
        has_projects=has_projects,
        has_wiki=has_wiki,
        archived=archived,
    )


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
    """GET /issues"""
    return issues.list_my_issues(
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
def github_list_repo_issues(
    owner: str,
    repo: str,
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
    """GET /repos/{owner}/{repo}/issues"""
    return issues.list_repo_issues(
        _client(),
        owner=owner,
        repo=repo,
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
def github_get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """GET /repos/{owner}/{repo}/issues/{issue_number}"""
    return issues.get_issue(_client(), owner=owner, repo=repo, issue_number=issue_number)


@mcp.tool()
def github_create_issue(
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/issues"""
    return issues.create_issue(
        _client(),
        owner=owner,
        repo=repo,
        title=title,
        body=body,
        assignees=assignees,
        milestone=milestone,
        labels=labels,
    )


@mcp.tool()
def github_update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/{issue_number}"""
    return issues.update_issue(
        _client(),
        owner=owner,
        repo=repo,
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
def github_list_issue_comments(owner: str, repo: str, issue_number: int, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    return issue_comments.list_issue_comments(_client(), owner=owner, repo=repo, issue_number=issue_number, since=since, per_page=per_page, page=page)


@mcp.tool()
def github_create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    return issue_comments.create_issue_comment(_client(), owner=owner, repo=repo, issue_number=issue_number, body=body)


@mcp.tool()
def github_update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return issue_comments.update_issue_comment(_client(), owner=owner, repo=repo, comment_id=comment_id, body=body)


@mcp.tool()
def github_delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return issue_comments.delete_issue_comment(_client(), owner=owner, repo=repo, comment_id=comment_id)


@mcp.tool()
def github_list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /repos/{owner}/{repo}/pulls"""
    return pulls.list_pull_requests(
        _client(),
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
def github_get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}"""
    return pulls.get_pull_request(_client(), owner=owner, repo=repo, pull_number=pull_number)


@mcp.tool()
def github_create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/pulls"""
    return pulls.create_pull_request(
        _client(),
        owner=owner,
        repo=repo,
        title=title,
        head=head,
        base=base,
        body=body,
        draft=draft,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def github_update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}/pulls/{pull_number}"""
    return pulls.update_pull_request(
        _client(),
        owner=owner,
        repo=repo,
        pull_number=pull_number,
        title=title,
        body=body,
        state=state,
        base=base,
        maintainer_can_modify=maintainer_can_modify,
    )


@mcp.tool()
def github_merge_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge"""
    return pulls.merge_pull_request(
        _client(),
        owner=owner,
        repo=repo,
        pull_number=pull_number,
        commit_title=commit_title,
        commit_message=commit_message,
        merge_method=merge_method,
        sha=sha,
    )


@mcp.tool()
def github_request_pull_reviewers(
    owner: str,
    repo: str,
    pull_number: int,
    reviewers: Optional[List[str]] = None,
    team_reviewers: Optional[List[str]] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"""
    return pulls.request_pull_reviewers(
        _client(),
        owner=owner,
        repo=repo,
        pull_number=pull_number,
        reviewers=reviewers,
        team_reviewers=team_reviewers,
    )


@mcp.tool()
def github_get_requested_reviewers(owner: str, repo: str, pull_number: int) -> Any:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers"""
    return pulls.get_requested_reviewers(_client(), owner=owner, repo=repo, pull_number=pull_number)


@mcp.tool()
def github_get_repo_content(
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    accept: str = "application/vnd.github.object+json",
) -> Any:
    """GET /repos/{owner}/{repo}/contents/{path}"""
    return contents.get_repo_content(_client(), owner=owner, repo=repo, path=path, ref=ref, accept=accept)


@mcp.tool()
def github_create_or_update_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_base64: Optional[str] = None,
    content_text: Optional[str] = None,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer_name: Optional[str] = None,
    committer_email: Optional[str] = None,
    author_name: Optional[str] = None,
    author_email: Optional[str] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/contents/{path}"""
    return contents.create_or_update_file(
        _client(),
        owner=owner,
        repo=repo,
        path=path,
        message=message,
        content_base64=content_base64,
        content_text=content_text,
        sha=sha,
        branch=branch,
        committer_name=committer_name,
        committer_email=committer_email,
        author_name=author_name,
        author_email=author_email,
    )


@mcp.tool()
def github_delete_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer_name: Optional[str] = None,
    committer_email: Optional[str] = None,
    author_name: Optional[str] = None,
    author_email: Optional[str] = None,
) -> Any:
    """DELETE /repos/{owner}/{repo}/contents/{path}"""
    return contents.delete_file(
        _client(),
        owner=owner,
        repo=repo,
        path=path,
        message=message,
        sha=sha,
        branch=branch,
        committer_name=committer_name,
        committer_email=committer_email,
        author_name=author_name,
        author_email=author_email,
    )


@mcp.tool()
def github_list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/releases"""
    return releases.list_releases(_client(), owner=owner, repo=repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_latest_release(owner: str, repo: str) -> Any:
    """GET /repos/{owner}/{repo}/releases/latest"""
    return releases.get_latest_release(_client(), owner=owner, repo=repo)


@mcp.tool()
def github_generate_release_notes(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/releases/generate-notes"""
    return releases.generate_release_notes(
        _client(),
        owner=owner,
        repo=repo,
        tag_name=tag_name,
        target_commitish=target_commitish,
        previous_tag_name=previous_tag_name,
        configuration_file_path=configuration_file_path,
    )


@mcp.tool()
def github_create_release(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: bool = False,
    make_latest: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/releases"""
    return releases.create_release(
        _client(),
        owner=owner,
        repo=repo,
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
def github_list_workflow_runs_for_repo(
    owner: str,
    repo: str,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    created: Optional[str] = None,
    exclude_pull_requests: bool = False,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs"""
    return actions_runs.list_workflow_runs_for_repo(
        _client(),
        owner=owner,
        repo=repo,
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
def github_get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id}"""
    return actions_runs.get_workflow_run(_client(), owner=owner, repo=repo, run_id=run_id)


@mcp.tool()
def github_cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel"""
    return actions_runs.cancel_workflow_run(_client(), owner=owner, repo=repo, run_id=run_id)


@mcp.tool()
def github_rerun_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun"""
    return actions_runs.rerun_workflow_run(_client(), owner=owner, repo=repo, run_id=run_id)


@mcp.tool()
def github_rerun_job(owner: str, repo: str, job_id: int, enable_debug_logging: bool = False) -> Any:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun"""
    return actions_runs.rerun_job(_client(), owner=owner, repo=repo, job_id=job_id, enable_debug_logging=enable_debug_logging)


@mcp.tool()
def github_search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /search/code"""
    return search.search_code(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_issues_and_prs(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /search/issues"""
    return search.search_issues_and_prs(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /search/repositories"""
    return search.search_repositories(_client(), q=q, sort=sort, order=order, per_page=per_page, page=page)


if __name__ == "__main__":
    mcp.run()
