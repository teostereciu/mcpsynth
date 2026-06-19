import os

from mcp.server.fastmcp import FastMCP

from generated_tools import actions, branch_protection, issues, pulls, releases, repos, search, webhooks


mcp = FastMCP("github-rest")


def _default_repo(repo: str | None) -> str:
    return repo or os.getenv("GITHUB_TEST_REPO") or ""


# Repos
@mcp.tool()
def get_repo(repo: str | None = None):
    return repos.get_repo(_default_repo(repo))


@mcp.tool()
def create_repo(name: str, description: str | None = None, private: bool = False, auto_init: bool = True, gitignore_template: str | None = None, license_template: str | None = None):
    return repos.create_repo(name, description=description, private=private, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template)


@mcp.tool()
def fork_repo(repo: str | None = None, organization: str | None = None, name: str | None = None, default_branch_only: bool | None = None):
    return repos.fork_repo(_default_repo(repo), organization=organization, name=name, default_branch_only=default_branch_only)


@mcp.tool()
def list_branches(repo: str | None = None, protected: bool | None = None, per_page: int = 30, page: int = 1):
    return repos.list_branches(_default_repo(repo), protected=protected, per_page=per_page, page=page)


@mcp.tool()
def get_branch(repo: str | None = None, branch: str = "main"):
    return repos.get_branch(_default_repo(repo), branch)


@mcp.tool()
def list_commits(repo: str | None = None, sha: str | None = None, path: str | None = None, author: str | None = None, since: str | None = None, until: str | None = None, per_page: int = 30, page: int = 1):
    return repos.list_commits(_default_repo(repo), sha=sha, path=path, author=author, since=since, until=until, per_page=per_page, page=page)


@mcp.tool()
def get_commit(repo: str | None = None, ref: str = "HEAD"):
    return repos.get_commit(_default_repo(repo), ref)


@mcp.tool()
def get_content(repo: str | None = None, path: str = "", ref: str | None = None):
    return repos.get_content(_default_repo(repo), path, ref=ref)


@mcp.tool()
def get_file_text(repo: str | None = None, path: str = "", ref: str | None = None):
    return repos.get_file_text(_default_repo(repo), path, ref=ref)


@mcp.tool()
def create_or_update_file(repo: str | None = None, path: str = "", message: str = "update via mcp", content_text: str = "", branch: str | None = None, sha: str | None = None, committer: dict | None = None, author: dict | None = None):
    return repos.create_or_update_file(_default_repo(repo), path, message, content_text, branch=branch, sha=sha, committer=committer, author=author)


@mcp.tool()
def delete_file(repo: str | None = None, path: str = "", message: str = "delete via mcp", sha: str = "", branch: str | None = None, committer: dict | None = None, author: dict | None = None):
    return repos.delete_file(_default_repo(repo), path, message, sha, branch=branch, committer=committer, author=author)


# Issues
@mcp.tool()
def list_issues(repo: str | None = None, state: str = "open", labels: str | None = None, assignee: str | None = None, creator: str | None = None, mentioned: str | None = None, since: str | None = None, per_page: int = 30, page: int = 1):
    return issues.list_issues(_default_repo(repo), state=state, labels=labels, assignee=assignee, creator=creator, mentioned=mentioned, since=since, per_page=per_page, page=page)


@mcp.tool()
def get_issue(repo: str | None = None, issue_number: int = 1):
    return issues.get_issue(_default_repo(repo), issue_number)


@mcp.tool()
def create_issue(repo: str | None = None, title: str = "", body: str | None = None, assignees: list | None = None, labels: list | None = None, milestone: int | None = None):
    return issues.create_issue(_default_repo(repo), title, body=body, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def update_issue(repo: str | None = None, issue_number: int = 1, title: str | None = None, body: str | None = None, state: str | None = None, assignees: list | None = None, labels: list | None = None, milestone: int | None = None):
    return issues.update_issue(_default_repo(repo), issue_number, title=title, body=body, state=state, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def lock_issue(repo: str | None = None, issue_number: int = 1, lock_reason: str | None = None):
    return issues.lock_issue(_default_repo(repo), issue_number, lock_reason=lock_reason)


@mcp.tool()
def unlock_issue(repo: str | None = None, issue_number: int = 1):
    return issues.unlock_issue(_default_repo(repo), issue_number)


@mcp.tool()
def list_issue_comments(repo: str | None = None, issue_number: int = 1, per_page: int = 30, page: int = 1):
    return issues.list_issue_comments(_default_repo(repo), issue_number, per_page=per_page, page=page)


@mcp.tool()
def create_issue_comment(repo: str | None = None, issue_number: int = 1, body: str = ""):
    return issues.create_issue_comment(_default_repo(repo), issue_number, body)


@mcp.tool()
def update_issue_comment(repo: str | None = None, comment_id: int = 0, body: str = ""):
    return issues.update_issue_comment(_default_repo(repo), comment_id, body)


@mcp.tool()
def delete_issue_comment(repo: str | None = None, comment_id: int = 0):
    return issues.delete_issue_comment(_default_repo(repo), comment_id)


@mcp.tool()
def list_labels(repo: str | None = None, per_page: int = 30, page: int = 1):
    return issues.list_labels(_default_repo(repo), per_page=per_page, page=page)


@mcp.tool()
def create_label(repo: str | None = None, name_label: str = "", color: str = "ffffff", description: str | None = None):
    return issues.create_label(_default_repo(repo), name_label, color, description=description)


@mcp.tool()
def update_label(repo: str | None = None, current_name: str = "", new_name: str | None = None, color: str | None = None, description: str | None = None):
    return issues.update_label(_default_repo(repo), current_name, new_name=new_name, color=color, description=description)


@mcp.tool()
def delete_label(repo: str | None = None, name_label: str = ""):
    return issues.delete_label(_default_repo(repo), name_label)


@mcp.tool()
def add_issue_labels(repo: str | None = None, issue_number: int = 1, labels: list | None = None):
    return issues.add_issue_labels(_default_repo(repo), issue_number, labels or [])


@mcp.tool()
def set_issue_labels(repo: str | None = None, issue_number: int = 1, labels: list | None = None):
    return issues.set_issue_labels(_default_repo(repo), issue_number, labels or [])


@mcp.tool()
def remove_issue_label(repo: str | None = None, issue_number: int = 1, name_label: str = ""):
    return issues.remove_issue_label(_default_repo(repo), issue_number, name_label)


# Pull Requests
@mcp.tool()
def list_pull_requests(repo: str | None = None, state: str = "open", base: str | None = None, head: str | None = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1):
    return pulls.list_pull_requests(_default_repo(repo), state=state, base=base, head=head, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def get_pull_request(repo: str | None = None, pull_number: int = 1):
    return pulls.get_pull_request(_default_repo(repo), pull_number)


@mcp.tool()
def create_pull_request(repo: str | None = None, title: str = "", head: str = "", base: str = "main", body: str | None = None, draft: bool | None = None, maintainer_can_modify: bool | None = None):
    return pulls.create_pull_request(_default_repo(repo), title, head, base, body=body, draft=draft, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def update_pull_request(repo: str | None = None, pull_number: int = 1, title: str | None = None, body: str | None = None, state: str | None = None, base: str | None = None, maintainer_can_modify: bool | None = None):
    return pulls.update_pull_request(_default_repo(repo), pull_number, title=title, body=body, state=state, base=base, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def merge_pull_request(repo: str | None = None, pull_number: int = 1, commit_title: str | None = None, commit_message: str | None = None, merge_method: str | None = None, sha: str | None = None):
    return pulls.merge_pull_request(_default_repo(repo), pull_number, commit_title=commit_title, commit_message=commit_message, merge_method=merge_method, sha=sha)


@mcp.tool()
def list_pull_reviews(repo: str | None = None, pull_number: int = 1, per_page: int = 30, page: int = 1):
    return pulls.list_pull_reviews(_default_repo(repo), pull_number, per_page=per_page, page=page)


@mcp.tool()
def create_pull_review(repo: str | None = None, pull_number: int = 1, body: str | None = None, event: str | None = None, comments: list | None = None, commit_id: str | None = None):
    return pulls.create_pull_review(_default_repo(repo), pull_number, body=body, event=event, comments=comments, commit_id=commit_id)


@mcp.tool()
def request_reviewers(repo: str | None = None, pull_number: int = 1, reviewers: list | None = None, team_reviewers: list | None = None):
    return pulls.request_reviewers(_default_repo(repo), pull_number, reviewers=reviewers, team_reviewers=team_reviewers)


@mcp.tool()
def list_pull_commits(repo: str | None = None, pull_number: int = 1, per_page: int = 30, page: int = 1):
    return pulls.list_pull_commits(_default_repo(repo), pull_number, per_page=per_page, page=page)


@mcp.tool()
def list_pull_files(repo: str | None = None, pull_number: int = 1, per_page: int = 30, page: int = 1):
    return pulls.list_pull_files(_default_repo(repo), pull_number, per_page=per_page, page=page)


# Releases
@mcp.tool()
def list_releases(repo: str | None = None, per_page: int = 30, page: int = 1):
    return releases.list_releases(_default_repo(repo), per_page=per_page, page=page)


@mcp.tool()
def get_release(repo: str | None = None, release_id: int = 0):
    return releases.get_release(_default_repo(repo), release_id)


@mcp.tool()
def create_release(repo: str | None = None, tag_name: str = "", name: str | None = None, body: str | None = None, target_commitish: str | None = None, draft: bool = False, prerelease: bool = False, generate_release_notes: bool | None = None):
    return releases.create_release(_default_repo(repo), tag_name, name=name, body=body, target_commitish=target_commitish, draft=draft, prerelease=prerelease, generate_release_notes=generate_release_notes)


@mcp.tool()
def update_release(repo: str | None = None, release_id: int = 0, tag_name: str | None = None, name: str | None = None, body: str | None = None, target_commitish: str | None = None, draft: bool | None = None, prerelease: bool | None = None, make_latest: str | None = None):
    return releases.update_release(_default_repo(repo), release_id, tag_name=tag_name, name=name, body=body, target_commitish=target_commitish, draft=draft, prerelease=prerelease, make_latest=make_latest)


@mcp.tool()
def delete_release(repo: str | None = None, release_id: int = 0):
    return releases.delete_release(_default_repo(repo), release_id)


# Actions
@mcp.tool()
def list_workflows(repo: str | None = None, per_page: int = 30, page: int = 1):
    return actions.list_workflows(_default_repo(repo), per_page=per_page, page=page)


@mcp.tool()
def get_workflow(repo: str | None = None, workflow_id: str = ""):
    return actions.get_workflow(_default_repo(repo), workflow_id)


@mcp.tool()
def list_workflow_runs(repo: str | None = None, workflow_id: str | None = None, branch: str | None = None, event: str | None = None, status: str | None = None, per_page: int = 30, page: int = 1):
    return actions.list_workflow_runs(_default_repo(repo), workflow_id=workflow_id, branch=branch, event=event, status=status, per_page=per_page, page=page)


@mcp.tool()
def get_workflow_run(repo: str | None = None, run_id: int = 0):
    return actions.get_workflow_run(_default_repo(repo), run_id)


@mcp.tool()
def rerun_workflow_run(repo: str | None = None, run_id: int = 0):
    return actions.rerun_workflow_run(_default_repo(repo), run_id)


@mcp.tool()
def cancel_workflow_run(repo: str | None = None, run_id: int = 0):
    return actions.cancel_workflow_run(_default_repo(repo), run_id)


@mcp.tool()
def dispatch_workflow(repo: str | None = None, workflow_id: str = "", ref: str = "main", inputs: dict | None = None):
    return actions.dispatch_workflow(_default_repo(repo), workflow_id, ref, inputs=inputs)


# Search
@mcp.tool()
def search_code(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_code(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def search_issues_and_prs(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_issues_and_prs(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def search_repositories(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_repositories(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def search_users(q: str, sort: str | None = None, order: str | None = None, per_page: int = 30, page: int = 1):
    return search.search_users(q, sort=sort, order=order, per_page=per_page, page=page)


# Webhooks
@mcp.tool()
def list_repo_webhooks(repo: str | None = None, per_page: int = 30, page: int = 1):
    return webhooks.list_repo_webhooks(_default_repo(repo), per_page=per_page, page=page)


@mcp.tool()
def get_repo_webhook(repo: str | None = None, hook_id: int = 0):
    return webhooks.get_repo_webhook(_default_repo(repo), hook_id)


@mcp.tool()
def create_repo_webhook(repo: str | None = None, config: dict | None = None, events: list | None = None, active: bool = True, name: str = "web"):
    return webhooks.create_repo_webhook(_default_repo(repo), config=config or {}, events=events, active=active, name=name)


@mcp.tool()
def update_repo_webhook(repo: str | None = None, hook_id: int = 0, config: dict | None = None, events: list | None = None, active: bool | None = None, name: str | None = None):
    return webhooks.update_repo_webhook(_default_repo(repo), hook_id, config=config, events=events, active=active, name=name)


@mcp.tool()
def delete_repo_webhook(repo: str | None = None, hook_id: int = 0):
    return webhooks.delete_repo_webhook(_default_repo(repo), hook_id)


@mcp.tool()
def ping_repo_webhook(repo: str | None = None, hook_id: int = 0):
    return webhooks.ping_repo_webhook(_default_repo(repo), hook_id)


# Branch protection
@mcp.tool()
def get_branch_protection(repo: str | None = None, branch: str = "main"):
    return branch_protection.get_branch_protection(_default_repo(repo), branch)


@mcp.tool()
def update_branch_protection(repo: str | None = None, branch: str = "main", required_status_checks: dict | None = None, enforce_admins: bool | None = None, required_pull_request_reviews: dict | None = None, restrictions: dict | None = None, required_linear_history: bool | None = None, allow_force_pushes: bool | None = None, allow_deletions: bool | None = None, block_creations: bool | None = None, required_conversation_resolution: bool | None = None, lock_branch: bool | None = None, allow_fork_syncing: bool | None = None):
    return branch_protection.update_branch_protection(
        _default_repo(repo),
        branch,
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
def delete_branch_protection(repo: str | None = None, branch: str = "main"):
    return branch_protection.delete_branch_protection(_default_repo(repo), branch)


if __name__ == "__main__":
    mcp.run()
