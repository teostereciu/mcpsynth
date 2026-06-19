import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import actions, issues, pulls, releases, repos, search, webhooks

mcp = FastMCP("github-rest")


def _split_repo(full: str) -> Dict[str, str]:
    if "/" not in full:
        return {"error": "Expected owner/repo"}
    owner, repo = full.split("/", 1)
    return {"owner": owner, "repo": repo}


@mcp.tool()
def github_get_repo(owner: str, repo: str) -> Any:
    return repos.get_repo(owner, repo)


@mcp.tool()
def github_list_user_repos(username: str, type: str = "owner", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Any:
    return repos.list_user_repos(username, type=type, sort=sort, per_page=per_page, page=page)


@mcp.tool()
def github_list_org_repos(org: str, type: str = "all", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Any:
    return repos.list_org_repos(org, type=type, sort=sort, per_page=per_page, page=page)


@mcp.tool()
def github_create_repo(name: str, description: str = "", private: bool = False, auto_init: bool = True) -> Any:
    return repos.create_repo_for_authenticated_user(name, description=description, private=private, auto_init=auto_init)


@mcp.tool()
def github_fork_repo(owner: str, repo: str, organization: str | None = None, name: str | None = None, default_branch_only: bool = False) -> Any:
    return repos.fork_repo(owner, repo, organization=organization, name=name, default_branch_only=default_branch_only)


@mcp.tool()
def github_list_branches(owner: str, repo: str, protected: bool | None = None, per_page: int = 30, page: int = 1) -> Any:
    return repos.list_branches(owner, repo, protected=protected, per_page=per_page, page=page)


@mcp.tool()
def github_get_branch(owner: str, repo: str, branch: str) -> Any:
    return repos.get_branch(owner, repo, branch)


@mcp.tool()
def github_get_commit(owner: str, repo: str, ref: str) -> Any:
    return repos.get_commit(owner, repo, ref)


@mcp.tool()
def github_list_commits(owner: str, repo: str, sha: str | None = None, path: str | None = None, author: str | None = None, since: str | None = None, until: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return repos.list_commits(owner, repo, sha=sha, path=path, author=author, since=since, until=until, per_page=per_page, page=page)


@mcp.tool()
def github_get_content(owner: str, repo: str, path: str, ref: str | None = None) -> Any:
    return repos.get_content(owner, repo, path, ref=ref)


@mcp.tool()
def github_create_or_update_file(owner: str, repo: str, path: str, message: str, content_base64: str, branch: str | None = None, sha: str | None = None, committer: Dict[str, str] | None = None, author: Dict[str, str] | None = None) -> Any:
    return repos.create_or_update_file(owner, repo, path, message, content_base64, branch=branch, sha=sha, committer=committer, author=author)


@mcp.tool()
def github_delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: str | None = None, committer: Dict[str, str] | None = None, author: Dict[str, str] | None = None) -> Any:
    return repos.delete_file(owner, repo, path, message, sha, branch=branch, committer=committer, author=author)


@mcp.tool()
def github_get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return repos.get_branch_protection(owner, repo, branch)


@mcp.tool()
def github_update_branch_protection(owner: str, repo: str, branch: str, protection: Dict[str, Any]) -> Any:
    return repos.update_branch_protection(owner, repo, branch, protection)


@mcp.tool()
def github_delete_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return repos.delete_branch_protection(owner, repo, branch)


@mcp.tool()
def github_list_repo_issues(owner: str, repo: str, state: str = "open", labels: str | None = None, assignee: str | None = None, creator: str | None = None, mentioned: str | None = None, since: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return issues.list_repo_issues(owner, repo, state=state, labels=labels, assignee=assignee, creator=creator, mentioned=mentioned, since=since, per_page=per_page, page=page)


@mcp.tool()
def github_get_issue(owner: str, repo: str, issue_number: int) -> Any:
    return issues.get_issue(owner, repo, issue_number)


@mcp.tool()
def github_create_issue(owner: str, repo: str, title: str, body: str = "", assignees: list[str] | None = None, labels: list[str] | None = None, milestone: int | None = None) -> Any:
    return issues.create_issue(owner, repo, title, body=body, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def github_update_issue(owner: str, repo: str, issue_number: int, title: str | None = None, body: str | None = None, state: str | None = None, assignees: list[str] | None = None, labels: list[str] | None = None, milestone: int | None = None) -> Any:
    return issues.update_issue(owner, repo, issue_number, title=title, body=body, state=state, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def github_lock_issue(owner: str, repo: str, issue_number: int, lock_reason: str | None = None) -> Any:
    return issues.lock_issue(owner, repo, issue_number, lock_reason=lock_reason)


@mcp.tool()
def github_unlock_issue(owner: str, repo: str, issue_number: int) -> Any:
    return issues.unlock_issue(owner, repo, issue_number)


@mcp.tool()
def github_list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    return issues.list_issue_comments(owner, repo, issue_number, per_page=per_page, page=page)


@mcp.tool()
def github_create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    return issues.create_issue_comment(owner, repo, issue_number, body)


@mcp.tool()
def github_update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    return issues.update_issue_comment(owner, repo, comment_id, body)


@mcp.tool()
def github_delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return issues.delete_issue_comment(owner, repo, comment_id)


@mcp.tool()
def github_add_labels(owner: str, repo: str, issue_number: int, labels: list[str]) -> Any:
    return issues.add_labels(owner, repo, issue_number, labels)


@mcp.tool()
def github_set_labels(owner: str, repo: str, issue_number: int, labels: list[str]) -> Any:
    return issues.set_labels(owner, repo, issue_number, labels)


@mcp.tool()
def github_remove_label_from_issue(owner: str, repo: str, issue_number: int, name: str) -> Any:
    return issues.remove_label(owner, repo, issue_number, name)


@mcp.tool()
def github_list_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return issues.list_labels(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_create_label(owner: str, repo: str, name: str, color: str, description: str = "") -> Any:
    return issues.create_label(owner, repo, name, color, description=description)


@mcp.tool()
def github_update_label(owner: str, repo: str, current_name: str, new_name: str | None = None, color: str | None = None, description: str | None = None) -> Any:
    return issues.update_label(owner, repo, current_name, new_name=new_name, color=color, description=description)


@mcp.tool()
def github_delete_label(owner: str, repo: str, name: str) -> Any:
    return issues.delete_label(owner, repo, name)


@mcp.tool()
def github_add_assignees(owner: str, repo: str, issue_number: int, assignees: list[str]) -> Any:
    return issues.add_assignees(owner, repo, issue_number, assignees)


@mcp.tool()
def github_remove_assignees(owner: str, repo: str, issue_number: int, assignees: list[str]) -> Any:
    return issues.remove_assignees(owner, repo, issue_number, assignees)


@mcp.tool()
def github_list_pull_requests(owner: str, repo: str, state: str = "open", head: str | None = None, base: str | None = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    return pulls.list_pull_requests(owner, repo, state=state, head=head, base=base, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def github_get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    return pulls.get_pull_request(owner, repo, pull_number)


@mcp.tool()
def github_create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = "", draft: bool = False, maintainer_can_modify: bool = True) -> Any:
    return pulls.create_pull_request(owner, repo, title, head, base, body=body, draft=draft, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def github_update_pull_request(owner: str, repo: str, pull_number: int, title: str | None = None, body: str | None = None, state: str | None = None, base: str | None = None, maintainer_can_modify: bool | None = None) -> Any:
    return pulls.update_pull_request(owner, repo, pull_number, title=title, body=body, state=state, base=base, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def github_list_pull_reviews(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    return pulls.list_pull_reviews(owner, repo, pull_number, per_page=per_page, page=page)


@mcp.tool()
def github_create_pull_review(owner: str, repo: str, pull_number: int, body: str = "", event: str = "COMMENT", comments: list[Dict[str, Any]] | None = None) -> Any:
    return pulls.create_pull_review(owner, repo, pull_number, body=body, event=event, comments=comments)


@mcp.tool()
def github_request_reviewers(owner: str, repo: str, pull_number: int, reviewers: list[str] | None = None, team_reviewers: list[str] | None = None) -> Any:
    return pulls.request_reviewers(owner, repo, pull_number, reviewers=reviewers, team_reviewers=team_reviewers)


@mcp.tool()
def github_merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str | None = None, commit_message: str | None = None, merge_method: str = "merge", sha: str | None = None) -> Any:
    return pulls.merge_pull_request(owner, repo, pull_number, commit_title=commit_title, commit_message=commit_message, merge_method=merge_method, sha=sha)


@mcp.tool()
def github_list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return releases.list_releases(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_release(owner: str, repo: str, release_id: int) -> Any:
    return releases.get_release(owner, repo, release_id)


@mcp.tool()
def github_get_latest_release(owner: str, repo: str) -> Any:
    return releases.get_latest_release(owner, repo)


@mcp.tool()
def github_create_release(owner: str, repo: str, tag_name: str, name: str | None = None, body: str = "", target_commitish: str = "main", draft: bool = False, prerelease: bool = False, generate_release_notes: bool = False) -> Any:
    return releases.create_release(owner, repo, tag_name, name=name, body=body, target_commitish=target_commitish, draft=draft, prerelease=prerelease, generate_release_notes=generate_release_notes)


@mcp.tool()
def github_update_release(owner: str, repo: str, release_id: int, tag_name: str | None = None, name: str | None = None, body: str | None = None, draft: bool | None = None, prerelease: bool | None = None, target_commitish: str | None = None) -> Any:
    return releases.update_release(owner, repo, release_id, tag_name=tag_name, name=name, body=body, draft=draft, prerelease=prerelease, target_commitish=target_commitish)


@mcp.tool()
def github_delete_release(owner: str, repo: str, release_id: int) -> Any:
    return releases.delete_release(owner, repo, release_id)


@mcp.tool()
def github_list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return actions.list_workflows(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_workflow(owner: str, repo: str, workflow_id: int) -> Any:
    return actions.get_workflow(owner, repo, workflow_id)


@mcp.tool()
def github_list_workflow_runs(owner: str, repo: str, workflow_id: int | None = None, branch: str | None = None, event: str | None = None, status: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return actions.list_workflow_runs(owner, repo, workflow_id=workflow_id, branch=branch, event=event, status=status, per_page=per_page, page=page)


@mcp.tool()
def github_get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return actions.get_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_rerun_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return actions.rerun_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return actions.cancel_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_dispatch_workflow(owner: str, repo: str, workflow_id: int, ref: str, inputs: Dict[str, Any] | None = None) -> Any:
    return actions.dispatch_workflow(owner, repo, workflow_id, ref, inputs=inputs)


@mcp.tool()
def github_search_code(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return search.search_code(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_issues_and_prs(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return search.search_issues_and_prs(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_repositories(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1) -> Any:
    return search.search_repositories(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return webhooks.list_repo_webhooks(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return webhooks.get_repo_webhook(owner, repo, hook_id)


@mcp.tool()
def github_create_repo_webhook(owner: str, repo: str, config: Dict[str, Any], events: list[str] | None = None, active: bool = True, name: str = "web") -> Any:
    return webhooks.create_repo_webhook(owner, repo, config, events=events, active=active, name=name)


@mcp.tool()
def github_update_repo_webhook(owner: str, repo: str, hook_id: int, config: Dict[str, Any] | None = None, events: list[str] | None = None, active: bool | None = None, add_events: list[str] | None = None, remove_events: list[str] | None = None) -> Any:
    return webhooks.update_repo_webhook(owner, repo, hook_id, config=config, events=events, active=active, add_events=add_events, remove_events=remove_events)


@mcp.tool()
def github_delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return webhooks.delete_repo_webhook(owner, repo, hook_id)


@mcp.tool()
def github_ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return webhooks.ping_repo_webhook(owner, repo, hook_id)


@mcp.tool()
def github_get_test_repo() -> Any:
    full = os.getenv("GITHUB_TEST_REPO", "")
    parts = _split_repo(full)
    if "error" in parts:
        return parts
    return repos.get_repo(parts["owner"], parts["repo"])


if __name__ == "__main__":
    mcp.run()
