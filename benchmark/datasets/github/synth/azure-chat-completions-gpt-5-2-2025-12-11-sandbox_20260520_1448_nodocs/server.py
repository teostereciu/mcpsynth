import os

from mcp.server.fastmcp import FastMCP

from generated_tools import actions, issues, pulls, releases, repos, search, webhooks


mcp = FastMCP("github-rest")


@mcp.tool()
def github_list_issues(owner: str, repo: str, state: str = "open", labels: str | None = None, assignee: str | None = None, per_page: int = 30, page: int = 1):
    return issues.list_issues(owner, repo, state=state, labels=labels, assignee=assignee, per_page=per_page, page=page)


@mcp.tool()
def github_get_issue(owner: str, repo: str, issue_number: int):
    return issues.get_issue(owner, repo, issue_number)


@mcp.tool()
def github_create_issue(owner: str, repo: str, title: str, body: str | None = None, labels: list | None = None, assignees: list | None = None, milestone: int | None = None):
    return issues.create_issue(owner, repo, title, body=body, labels=labels, assignees=assignees, milestone=milestone)


@mcp.tool()
def github_update_issue(owner: str, repo: str, issue_number: int, title: str | None = None, body: str | None = None, state: str | None = None, labels: list | None = None, assignees: list | None = None):
    return issues.update_issue(owner, repo, issue_number, title=title, body=body, state=state, labels=labels, assignees=assignees)


@mcp.tool()
def github_lock_issue(owner: str, repo: str, issue_number: int, lock_reason: str | None = None):
    return issues.lock_issue(owner, repo, issue_number, lock_reason=lock_reason)


@mcp.tool()
def github_unlock_issue(owner: str, repo: str, issue_number: int):
    return issues.unlock_issue(owner, repo, issue_number)


@mcp.tool()
def github_list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1):
    return issues.list_issue_comments(owner, repo, issue_number, per_page=per_page, page=page)


@mcp.tool()
def github_create_issue_comment(owner: str, repo: str, issue_number: int, body: str):
    return issues.create_issue_comment(owner, repo, issue_number, body)


@mcp.tool()
def github_update_issue_comment(owner: str, repo: str, comment_id: int, body: str):
    return issues.update_issue_comment(owner, repo, comment_id, body)


@mcp.tool()
def github_delete_issue_comment(owner: str, repo: str, comment_id: int):
    return issues.delete_issue_comment(owner, repo, comment_id)


@mcp.tool()
def github_add_labels(owner: str, repo: str, issue_number: int, labels: list):
    return issues.add_labels(owner, repo, issue_number, labels)


@mcp.tool()
def github_remove_label(owner: str, repo: str, issue_number: int, name: str):
    return issues.remove_label(owner, repo, issue_number, name)


@mcp.tool()
def github_list_pull_requests(owner: str, repo: str, state: str = "open", base: str | None = None, head: str | None = None, per_page: int = 30, page: int = 1):
    return pulls.list_pull_requests(owner, repo, state=state, base=base, head=head, per_page=per_page, page=page)


@mcp.tool()
def github_get_pull_request(owner: str, repo: str, pull_number: int):
    return pulls.get_pull_request(owner, repo, pull_number)


@mcp.tool()
def github_create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str | None = None, draft: bool = False):
    return pulls.create_pull_request(owner, repo, title, head, base, body=body, draft=draft)


@mcp.tool()
def github_update_pull_request(owner: str, repo: str, pull_number: int, title: str | None = None, body: str | None = None, state: str | None = None):
    return pulls.update_pull_request(owner, repo, pull_number, title=title, body=body, state=state)


@mcp.tool()
def github_list_pull_reviews(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1):
    return pulls.list_pull_reviews(owner, repo, pull_number, per_page=per_page, page=page)


@mcp.tool()
def github_create_pull_review(owner: str, repo: str, pull_number: int, body: str, event: str = "COMMENT", comments: list | None = None, commit_id: str | None = None):
    return pulls.create_pull_review(owner, repo, pull_number, body, event=event, comments=comments, commit_id=commit_id)


@mcp.tool()
def github_merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str | None = None, commit_message: str | None = None, merge_method: str = "merge"):
    return pulls.merge_pull_request(owner, repo, pull_number, commit_title=commit_title, commit_message=commit_message, merge_method=merge_method)


@mcp.tool()
def github_get_repository(owner: str, repo: str):
    return repos.get_repository(owner, repo)


@mcp.tool()
def github_create_repository(name: str, description: str | None = None, private: bool = False, auto_init: bool = True):
    return repos.create_repository(name, description=description, private=private, auto_init=auto_init)


@mcp.tool()
def github_fork_repository(owner: str, repo: str, organization: str | None = None):
    return repos.fork_repository(owner, repo, organization=organization)


@mcp.tool()
def github_list_branches(owner: str, repo: str, protected: bool | None = None, per_page: int = 30, page: int = 1):
    return repos.list_branches(owner, repo, protected=protected, per_page=per_page, page=page)


@mcp.tool()
def github_get_branch(owner: str, repo: str, branch: str):
    return repos.get_branch(owner, repo, branch)


@mcp.tool()
def github_list_commits(owner: str, repo: str, sha: str | None = None, path: str | None = None, per_page: int = 30, page: int = 1):
    return repos.list_commits(owner, repo, sha=sha, path=path, per_page=per_page, page=page)


@mcp.tool()
def github_get_commit(owner: str, repo: str, ref: str):
    return repos.get_commit(owner, repo, ref)


@mcp.tool()
def github_get_content(owner: str, repo: str, path: str, ref: str | None = None):
    return repos.get_content(owner, repo, path, ref=ref)


@mcp.tool()
def github_put_content(owner: str, repo: str, path: str, message: str, content: str, branch: str | None = None, sha: str | None = None):
    return repos.put_content(owner, repo, path, message, content, branch=branch, sha=sha)


@mcp.tool()
def github_delete_content(owner: str, repo: str, path: str, message: str, sha: str, branch: str | None = None):
    return repos.delete_content(owner, repo, path, message, sha, branch=branch)


@mcp.tool()
def github_get_branch_protection(owner: str, repo: str, branch: str):
    return repos.get_branch_protection(owner, repo, branch)


@mcp.tool()
def github_update_branch_protection(owner: str, repo: str, branch: str, protection: dict):
    return repos.update_branch_protection(owner, repo, branch, protection)


@mcp.tool()
def github_list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1):
    return releases.list_releases(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_release(owner: str, repo: str, release_id: int):
    return releases.get_release(owner, repo, release_id)


@mcp.tool()
def github_create_release(owner: str, repo: str, tag_name: str, name: str | None = None, body: str | None = None, target_commitish: str | None = None, draft: bool = False, prerelease: bool = False):
    return releases.create_release(owner, repo, tag_name, name=name, body=body, target_commitish=target_commitish, draft=draft, prerelease=prerelease)


@mcp.tool()
def github_update_release(owner: str, repo: str, release_id: int, tag_name: str | None = None, name: str | None = None, body: str | None = None, draft: bool | None = None, prerelease: bool | None = None):
    return releases.update_release(owner, repo, release_id, tag_name=tag_name, name=name, body=body, draft=draft, prerelease=prerelease)


@mcp.tool()
def github_delete_release(owner: str, repo: str, release_id: int):
    return releases.delete_release(owner, repo, release_id)


@mcp.tool()
def github_list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1):
    return actions.list_workflows(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_workflow(owner: str, repo: str, workflow_id: int):
    return actions.get_workflow(owner, repo, workflow_id)


@mcp.tool()
def github_list_workflow_runs(owner: str, repo: str, workflow_id: int | None = None, branch: str | None = None, status: str | None = None, per_page: int = 30, page: int = 1):
    return actions.list_workflow_runs(owner, repo, workflow_id=workflow_id, branch=branch, status=status, per_page=per_page, page=page)


@mcp.tool()
def github_get_workflow_run(owner: str, repo: str, run_id: int):
    return actions.get_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_rerun_workflow_run(owner: str, repo: str, run_id: int):
    return actions.rerun_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_cancel_workflow_run(owner: str, repo: str, run_id: int):
    return actions.cancel_workflow_run(owner, repo, run_id)


@mcp.tool()
def github_dispatch_workflow(owner: str, repo: str, workflow_id: str, ref: str, inputs: dict | None = None):
    return actions.dispatch_workflow(owner, repo, workflow_id, ref, inputs=inputs)


@mcp.tool()
def github_search_code(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_code(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_issues(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_issues(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_repositories(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_repositories(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1):
    return webhooks.list_repo_webhooks(owner, repo, per_page=per_page, page=page)


@mcp.tool()
def github_get_repo_webhook(owner: str, repo: str, hook_id: int):
    return webhooks.get_repo_webhook(owner, repo, hook_id)


@mcp.tool()
def github_create_repo_webhook(owner: str, repo: str, config: dict, events: list | None = None, active: bool = True, name: str = "web"):
    return webhooks.create_repo_webhook(owner, repo, config, events=events, active=active, name=name)


@mcp.tool()
def github_update_repo_webhook(owner: str, repo: str, hook_id: int, config: dict | None = None, events: list | None = None, active: bool | None = None):
    return webhooks.update_repo_webhook(owner, repo, hook_id, config=config, events=events, active=active)


@mcp.tool()
def github_delete_repo_webhook(owner: str, repo: str, hook_id: int):
    return webhooks.delete_repo_webhook(owner, repo, hook_id)


@mcp.tool()
def github_ping_repo_webhook(owner: str, repo: str, hook_id: int):
    return webhooks.ping_repo_webhook(owner, repo, hook_id)


if __name__ == "__main__":
    # Optional sanity check env
    _ = os.getenv("GITHUB_TOKEN")
    mcp.run()
