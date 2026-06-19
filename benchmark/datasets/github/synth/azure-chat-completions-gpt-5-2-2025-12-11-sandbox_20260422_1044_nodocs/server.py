import os

from mcp.server.fastmcp import FastMCP

from generated_tools import actions, branch_protection, issues, misc, pulls, releases, repos, search, webhooks


mcp = FastMCP("github-rest")


# --- Misc / Auth ---
@mcp.tool()
def github_get_authenticated_user():
    return misc.get_authenticated_user()


@mcp.tool()
def github_get_rate_limit():
    return misc.get_rate_limit()


@mcp.tool()
def github_get_test_repo():
    return misc.get_test_repo()


# --- Repos / Contents / Commits / Branches ---
@mcp.tool()
def github_get_repo(owner_repo: str):
    return repos.get_repo(owner_repo)


@mcp.tool()
def github_list_repos_for_user(username: str, per_page: int = 100, max_pages: int = 5):
    return repos.list_repos_for_user(username, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_list_repos_for_authenticated_user(visibility: str = "all", affiliation: str = "owner,collaborator,organization_member", per_page: int = 100, max_pages: int = 5):
    return repos.list_repos_for_authenticated_user(visibility=visibility, affiliation=affiliation, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_create_repo(name: str, description: str | None = None, private: bool = False, auto_init: bool = True, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True):
    return repos.create_repo(name=name, description=description, private=private, auto_init=auto_init, has_issues=has_issues, has_projects=has_projects, has_wiki=has_wiki)


@mcp.tool()
def github_fork_repo(owner_repo: str, organization: str | None = None, name: str | None = None, default_branch_only: bool = False):
    return repos.fork_repo(owner_repo, organization=organization, name=name, default_branch_only=default_branch_only)


@mcp.tool()
def github_list_branches(owner_repo: str, protected: bool | None = None, per_page: int = 100, max_pages: int = 5):
    return repos.list_branches(owner_repo, protected=protected, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_branch(owner_repo: str, branch: str):
    return repos.get_branch(owner_repo, branch)


@mcp.tool()
def github_list_commits(owner_repo: str, sha: str | None = None, path: str | None = None, author: str | None = None, since: str | None = None, until: str | None = None, per_page: int = 100, max_pages: int = 5):
    return repos.list_commits(owner_repo, sha=sha, path=path, author=author, since=since, until=until, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_commit(owner_repo: str, ref: str):
    return repos.get_commit(owner_repo, ref)


@mcp.tool()
def github_get_contents(owner_repo: str, path: str, ref: str | None = None):
    return repos.get_contents(owner_repo, path, ref=ref)


@mcp.tool()
def github_get_file_text(owner_repo: str, path: str, ref: str | None = None):
    return repos.get_file_text(owner_repo, path, ref=ref)


@mcp.tool()
def github_create_or_update_file(owner_repo: str, path: str, message: str, content_text: str, branch: str | None = None, sha: str | None = None, committer: dict | None = None, author: dict | None = None):
    return repos.create_or_update_file(owner_repo, path, message, content_text, branch=branch, sha=sha, committer=committer, author=author)


@mcp.tool()
def github_delete_file(owner_repo: str, path: str, message: str, sha: str, branch: str | None = None):
    return repos.delete_file(owner_repo, path, message, sha, branch=branch)


# --- Issues ---
@mcp.tool()
def github_list_issues(owner_repo: str, state: str = "open", labels: str | None = None, assignee: str | None = None, creator: str | None = None, mentioned: str | None = None, since: str | None = None, per_page: int = 100, max_pages: int = 5):
    return issues.list_issues(owner_repo, state=state, labels=labels, assignee=assignee, creator=creator, mentioned=mentioned, since=since, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_issue(owner_repo: str, issue_number: int):
    return issues.get_issue(owner_repo, issue_number)


@mcp.tool()
def github_create_issue(owner_repo: str, title: str, body: str | None = None, assignees: list | None = None, labels: list | None = None, milestone: int | None = None):
    return issues.create_issue(owner_repo, title, body=body, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def github_update_issue(owner_repo: str, issue_number: int, title: str | None = None, body: str | None = None, state: str | None = None, assignees: list | None = None, labels: list | None = None, milestone: int | None = None):
    return issues.update_issue(owner_repo, issue_number, title=title, body=body, state=state, assignees=assignees, labels=labels, milestone=milestone)


@mcp.tool()
def github_lock_issue(owner_repo: str, issue_number: int, lock_reason: str | None = None):
    return issues.lock_issue(owner_repo, issue_number, lock_reason=lock_reason)


@mcp.tool()
def github_unlock_issue(owner_repo: str, issue_number: int):
    return issues.unlock_issue(owner_repo, issue_number)


@mcp.tool()
def github_list_issue_comments(owner_repo: str, issue_number: int, per_page: int = 100, max_pages: int = 5):
    return issues.list_issue_comments(owner_repo, issue_number, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_create_issue_comment(owner_repo: str, issue_number: int, body: str):
    return issues.create_issue_comment(owner_repo, issue_number, body)


@mcp.tool()
def github_update_issue_comment(owner_repo: str, comment_id: int, body: str):
    return issues.update_issue_comment(owner_repo, comment_id, body)


@mcp.tool()
def github_delete_issue_comment(owner_repo: str, comment_id: int):
    return issues.delete_issue_comment(owner_repo, comment_id)


@mcp.tool()
def github_add_labels(owner_repo: str, issue_number: int, labels: list):
    return issues.add_labels(owner_repo, issue_number, labels)


@mcp.tool()
def github_set_labels(owner_repo: str, issue_number: int, labels: list):
    return issues.set_labels(owner_repo, issue_number, labels)


@mcp.tool()
def github_remove_label(owner_repo: str, issue_number: int, name: str):
    return issues.remove_label(owner_repo, issue_number, name)


@mcp.tool()
def github_add_assignees(owner_repo: str, issue_number: int, assignees: list):
    return issues.add_assignees(owner_repo, issue_number, assignees)


@mcp.tool()
def github_remove_assignees(owner_repo: str, issue_number: int, assignees: list):
    return issues.remove_assignees(owner_repo, issue_number, assignees)


# --- Pull Requests ---
@mcp.tool()
def github_list_pulls(owner_repo: str, state: str = "open", base: str | None = None, head: str | None = None, sort: str = "created", direction: str = "desc", per_page: int = 100, max_pages: int = 5):
    return pulls.list_pulls(owner_repo, state=state, base=base, head=head, sort=sort, direction=direction, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_pull(owner_repo: str, pull_number: int):
    return pulls.get_pull(owner_repo, pull_number)


@mcp.tool()
def github_create_pull(owner_repo: str, title: str, head: str, base: str, body: str | None = None, draft: bool = False, maintainer_can_modify: bool | None = None):
    return pulls.create_pull(owner_repo, title, head, base, body=body, draft=draft, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def github_update_pull(owner_repo: str, pull_number: int, title: str | None = None, body: str | None = None, state: str | None = None, base: str | None = None, maintainer_can_modify: bool | None = None):
    return pulls.update_pull(owner_repo, pull_number, title=title, body=body, state=state, base=base, maintainer_can_modify=maintainer_can_modify)


@mcp.tool()
def github_list_pull_commits(owner_repo: str, pull_number: int, per_page: int = 100, max_pages: int = 5):
    return pulls.list_pull_commits(owner_repo, pull_number, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_list_pull_files(owner_repo: str, pull_number: int, per_page: int = 100, max_pages: int = 5):
    return pulls.list_pull_files(owner_repo, pull_number, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_create_review(owner_repo: str, pull_number: int, body: str | None = None, event: str = "COMMENT", comments: list | None = None, commit_id: str | None = None):
    return pulls.create_review(owner_repo, pull_number, body=body, event=event, comments=comments, commit_id=commit_id)


@mcp.tool()
def github_merge_pull(owner_repo: str, pull_number: int, commit_title: str | None = None, commit_message: str | None = None, merge_method: str = "merge", sha: str | None = None):
    return pulls.merge_pull(owner_repo, pull_number, commit_title=commit_title, commit_message=commit_message, merge_method=merge_method, sha=sha)


# --- Releases ---
@mcp.tool()
def github_list_releases(owner_repo: str, per_page: int = 100, max_pages: int = 5):
    return releases.list_releases(owner_repo, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_release(owner_repo: str, release_id: int):
    return releases.get_release(owner_repo, release_id)


@mcp.tool()
def github_get_latest_release(owner_repo: str):
    return releases.get_latest_release(owner_repo)


@mcp.tool()
def github_create_release(owner_repo: str, tag_name: str, name: str | None = None, body: str | None = None, target_commitish: str | None = None, draft: bool = False, prerelease: bool = False, generate_release_notes: bool = False):
    return releases.create_release(owner_repo, tag_name, name=name, body=body, target_commitish=target_commitish, draft=draft, prerelease=prerelease, generate_release_notes=generate_release_notes)


@mcp.tool()
def github_update_release(owner_repo: str, release_id: int, tag_name: str | None = None, name: str | None = None, body: str | None = None, draft: bool | None = None, prerelease: bool | None = None, target_commitish: str | None = None, make_latest: str | None = None):
    return releases.update_release(owner_repo, release_id, tag_name=tag_name, name=name, body=body, draft=draft, prerelease=prerelease, target_commitish=target_commitish, make_latest=make_latest)


@mcp.tool()
def github_delete_release(owner_repo: str, release_id: int):
    return releases.delete_release(owner_repo, release_id)


# --- Actions ---
@mcp.tool()
def github_list_workflows(owner_repo: str, per_page: int = 100, max_pages: int = 3):
    return actions.list_workflows(owner_repo, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_workflow(owner_repo: str, workflow_id_or_file: str):
    return actions.get_workflow(owner_repo, workflow_id_or_file)


@mcp.tool()
def github_list_workflow_runs(owner_repo: str, workflow_id_or_file: str | None = None, branch: str | None = None, event: str | None = None, status: str | None = None, per_page: int = 100):
    return actions.list_workflow_runs(owner_repo, workflow_id_or_file=workflow_id_or_file, branch=branch, event=event, status=status, per_page=per_page)


@mcp.tool()
def github_get_workflow_run(owner_repo: str, run_id: int):
    return actions.get_workflow_run(owner_repo, run_id)


@mcp.tool()
def github_rerun_workflow_run(owner_repo: str, run_id: int):
    return actions.rerun_workflow_run(owner_repo, run_id)


@mcp.tool()
def github_cancel_workflow_run(owner_repo: str, run_id: int):
    return actions.cancel_workflow_run(owner_repo, run_id)


@mcp.tool()
def github_dispatch_workflow(owner_repo: str, workflow_id_or_file: str, ref: str, inputs: dict | None = None):
    return actions.dispatch_workflow(owner_repo, workflow_id_or_file, ref, inputs=inputs)


# --- Search ---
@mcp.tool()
def github_search_code(q: str, sort: str | None = None, order: str | None = None, per_page: int = 100, page: int = 1):
    return search.search_code(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_issues(q: str, sort: str | None = None, order: str | None = None, per_page: int = 100, page: int = 1):
    return search.search_issues(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_repositories(q: str, sort: str | None = None, order: str | None = None, per_page: int = 100, page: int = 1):
    return search.search_repositories(q, sort=sort, order=order, per_page=per_page, page=page)


@mcp.tool()
def github_search_users(q: str, sort: str | None = None, order: str | None = None, per_page: int = 100, page: int = 1):
    return search.search_users(q, sort=sort, order=order, per_page=per_page, page=page)


# --- Webhooks ---
@mcp.tool()
def github_list_repo_webhooks(owner_repo: str, per_page: int = 100, max_pages: int = 5):
    return webhooks.list_repo_webhooks(owner_repo, per_page=per_page, max_pages=max_pages)


@mcp.tool()
def github_get_repo_webhook(owner_repo: str, hook_id: int):
    return webhooks.get_repo_webhook(owner_repo, hook_id)


@mcp.tool()
def github_create_repo_webhook(owner_repo: str, config: dict, events: list | None = None, active: bool = True, name: str = "web"):
    return webhooks.create_repo_webhook(owner_repo, config=config, events=events, active=active, name=name)


@mcp.tool()
def github_update_repo_webhook(owner_repo: str, hook_id: int, config: dict | None = None, events: list | None = None, active: bool | None = None, name: str | None = None):
    return webhooks.update_repo_webhook(owner_repo, hook_id, config=config, events=events, active=active, name=name)


@mcp.tool()
def github_delete_repo_webhook(owner_repo: str, hook_id: int):
    return webhooks.delete_repo_webhook(owner_repo, hook_id)


@mcp.tool()
def github_ping_repo_webhook(owner_repo: str, hook_id: int):
    return webhooks.ping_repo_webhook(owner_repo, hook_id)


# --- Branch Protection ---
@mcp.tool()
def github_get_branch_protection(owner_repo: str, branch: str):
    return branch_protection.get_branch_protection(owner_repo, branch)


@mcp.tool()
def github_update_branch_protection(owner_repo: str, branch: str, protection: dict):
    return branch_protection.update_branch_protection(owner_repo, branch, protection)


@mcp.tool()
def github_delete_branch_protection(owner_repo: str, branch: str):
    return branch_protection.delete_branch_protection(owner_repo, branch)


def main():
    # FastMCP runs over stdio by default
    # Ensure token presence is discoverable but not required for unauth endpoints
    if not os.getenv("GITHUB_TOKEN"):
        pass
    mcp.run()


if __name__ == "__main__":
    main()
