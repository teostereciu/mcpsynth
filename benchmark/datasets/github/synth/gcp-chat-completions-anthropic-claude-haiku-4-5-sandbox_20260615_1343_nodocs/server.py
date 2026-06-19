#!/usr/bin/env python3
"""
MCP Server for GitHub REST API
Provides comprehensive tools for interacting with GitHub repositories, issues, PRs, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("github-api")

# Configuration from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TEST_REPO = os.getenv("GITHUB_TEST_REPO", "")

# Default headers for GitHub API
DEFAULT_HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}" if GITHUB_TOKEN else "",
}


def make_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    json_data: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> dict:
    """Make an HTTP request to the GitHub API."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    req_headers = DEFAULT_HEADERS.copy()
    if headers:
        req_headers.update(headers)

    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=req_headers,
            timeout=30,
        )
        response.raise_for_status()
        return response.json() if response.text else {}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# REPOSITORIES
# ============================================================================


@server.tool()
def get_repository(owner: str, repo: str) -> dict:
    """Get repository information."""
    return make_request("GET", f"/repos/{owner}/{repo}")


@server.tool()
def list_repositories(
    username: Optional[str] = None,
    sort: str = "updated",
    direction: str = "desc",
    per_page: int = 30,
) -> dict:
    """List repositories for a user or authenticated user."""
    endpoint = f"/users/{username}/repos" if username else "/user/repos"
    return make_request(
        "GET",
        endpoint,
        params={"sort": sort, "direction": direction, "per_page": per_page},
    )


@server.tool()
def create_repository(
    name: str,
    description: Optional[str] = None,
    private: bool = False,
    auto_init: bool = False,
) -> dict:
    """Create a new repository for the authenticated user."""
    return make_request(
        "POST",
        "/user/repos",
        json_data={
            "name": name,
            "description": description,
            "private": private,
            "auto_init": auto_init,
        },
    )


@server.tool()
def update_repository(
    owner: str,
    repo: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_downloads: Optional[bool] = None,
) -> dict:
    """Update repository settings."""
    data = {}
    if description is not None:
        data["description"] = description
    if homepage is not None:
        data["homepage"] = homepage
    if private is not None:
        data["private"] = private
    if has_issues is not None:
        data["has_issues"] = has_issues
    if has_projects is not None:
        data["has_projects"] = has_projects
    if has_downloads is not None:
        data["has_downloads"] = has_downloads

    return make_request("PATCH", f"/repos/{owner}/{repo}", json_data=data)


@server.tool()
def delete_repository(owner: str, repo: str) -> dict:
    """Delete a repository."""
    return make_request("DELETE", f"/repos/{owner}/{repo}")


@server.tool()
def fork_repository(owner: str, repo: str, organization: Optional[str] = None) -> dict:
    """Fork a repository."""
    data = {}
    if organization:
        data["organization"] = organization
    return make_request("POST", f"/repos/{owner}/{repo}/forks", json_data=data)


@server.tool()
def get_repository_topics(owner: str, repo: str) -> dict:
    """Get repository topics."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/topics",
        headers={"Accept": "application/vnd.github.mercy-preview+json"},
    )


@server.tool()
def set_repository_topics(owner: str, repo: str, topics: list) -> dict:
    """Set repository topics."""
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/topics",
        json_data={"names": topics},
        headers={"Accept": "application/vnd.github.mercy-preview+json"},
    )


# ============================================================================
# BRANCHES & COMMITS
# ============================================================================


@server.tool()
def list_branches(owner: str, repo: str, per_page: int = 30) -> dict:
    """List branches in a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/branches", params={"per_page": per_page}
    )


@server.tool()
def get_branch(owner: str, repo: str, branch: str) -> dict:
    """Get a specific branch."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


@server.tool()
def create_branch(owner: str, repo: str, branch: str, sha: str) -> dict:
    """Create a new branch."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/git/refs",
        json_data={"ref": f"refs/heads/{branch}", "sha": sha},
    )


@server.tool()
def delete_branch(owner: str, repo: str, branch: str) -> dict:
    """Delete a branch."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/git/refs/heads/{branch}")


@server.tool()
def list_commits(
    owner: str, repo: str, sha: Optional[str] = None, per_page: int = 30
) -> dict:
    """List commits in a repository."""
    params = {"per_page": per_page}
    if sha:
        params["sha"] = sha
    return make_request("GET", f"/repos/{owner}/{repo}/commits", params=params)


@server.tool()
def get_commit(owner: str, repo: str, sha: str) -> dict:
    """Get a specific commit."""
    return make_request("GET", f"/repos/{owner}/{repo}/commits/{sha}")


@server.tool()
def get_commit_diff(owner: str, repo: str, sha: str) -> dict:
    """Get commit diff."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/commits/{sha}",
        headers={"Accept": "application/vnd.github.v3.diff"},
    )


# ============================================================================
# ISSUES
# ============================================================================


@server.tool()
def list_issues(
    owner: str,
    repo: str,
    state: str = "open",
    labels: Optional[str] = None,
    assignee: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
) -> dict:
    """List issues in a repository."""
    params = {
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
    }
    if labels:
        params["labels"] = labels
    if assignee:
        params["assignee"] = assignee
    return make_request("GET", f"/repos/{owner}/{repo}/issues", params=params)


@server.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Get a specific issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@server.tool()
def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[list] = None,
    labels: Optional[list] = None,
    milestone: Optional[int] = None,
) -> dict:
    """Create a new issue."""
    data = {"title": title}
    if body:
        data["body"] = body
    if assignees:
        data["assignees"] = assignees
    if labels:
        data["labels"] = labels
    if milestone is not None:
        data["milestone"] = milestone
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json_data=data)


@server.tool()
def update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    assignees: Optional[list] = None,
    labels: Optional[list] = None,
) -> dict:
    """Update an issue."""
    data = {}
    if title is not None:
        data["title"] = title
    if body is not None:
        data["body"] = body
    if state is not None:
        data["state"] = state
    if assignees is not None:
        data["assignees"] = assignees
    if labels is not None:
        data["labels"] = labels
    return make_request(
        "PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_data=data
    )


@server.tool()
def close_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Close an issue."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/{issue_number}",
        json_data={"state": "closed"},
    )


@server.tool()
def add_issue_labels(
    owner: str, repo: str, issue_number: int, labels: list
) -> dict:
    """Add labels to an issue."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
        json_data={"labels": labels},
    )


@server.tool()
def remove_issue_label(owner: str, repo: str, issue_number: int, label: str) -> dict:
    """Remove a label from an issue."""
    return make_request(
        "DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}"
    )


@server.tool()
def list_issue_labels(owner: str, repo: str, per_page: int = 30) -> dict:
    """List all labels in a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/labels", params={"per_page": per_page}
    )


@server.tool()
def create_label(
    owner: str, repo: str, name: str, color: str, description: Optional[str] = None
) -> dict:
    """Create a new label."""
    data = {"name": name, "color": color}
    if description:
        data["description"] = description
    return make_request("POST", f"/repos/{owner}/{repo}/labels", json_data=data)


@server.tool()
def update_label(
    owner: str,
    repo: str,
    label: str,
    new_name: Optional[str] = None,
    color: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a label."""
    data = {}
    if new_name is not None:
        data["new_name"] = new_name
    if color is not None:
        data["color"] = color
    if description is not None:
        data["description"] = description
    return make_request(
        "PATCH", f"/repos/{owner}/{repo}/labels/{label}", json_data=data
    )


@server.tool()
def delete_label(owner: str, repo: str, label: str) -> dict:
    """Delete a label."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/labels/{label}")


@server.tool()
def assign_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
    """Assign users to an issue."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
        json_data={"assignees": assignees},
    )


@server.tool()
def unassign_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
    """Remove assignees from an issue."""
    return make_request(
        "DELETE",
        f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
        json_data={"assignees": assignees},
    )


# ============================================================================
# ISSUE COMMENTS
# ============================================================================


@server.tool()
def list_issue_comments(
    owner: str, repo: str, issue_number: int, per_page: int = 30
) -> dict:
    """List comments on an issue."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        params={"per_page": per_page},
    )


@server.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict:
    """Create a comment on an issue."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        json_data={"body": body},
    )


@server.tool()
def update_issue_comment(
    owner: str, repo: str, comment_id: int, body: str
) -> dict:
    """Update an issue comment."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
        json_data={"body": body},
    )


@server.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
    """Delete an issue comment."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


# ============================================================================
# PULL REQUESTS
# ============================================================================


@server.tool()
def list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open",
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
) -> dict:
    """List pull requests in a repository."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls",
        params={
            "state": state,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
        },
    )


@server.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """Get a specific pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@server.tool()
def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: bool = False,
) -> dict:
    """Create a new pull request."""
    data = {"title": title, "head": head, "base": base, "draft": draft}
    if body:
        data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls", json_data=data)


@server.tool()
def update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
) -> dict:
    """Update a pull request."""
    data = {}
    if title is not None:
        data["title"] = title
    if body is not None:
        data["body"] = body
    if state is not None:
        data["state"] = state
    if base is not None:
        data["base"] = base
    return make_request(
        "PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_data=data
    )


@server.tool()
def merge_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: str = "merge",
) -> dict:
    """Merge a pull request."""
    data = {"merge_method": merge_method}
    if commit_title:
        data["commit_title"] = commit_title
    if commit_message:
        data["commit_message"] = commit_message
    return make_request(
        "PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_data=data
    )


@server.tool()
def close_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """Close a pull request."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/pulls/{pull_number}",
        json_data={"state": "closed"},
    )


# ============================================================================
# PULL REQUEST REVIEWS
# ============================================================================


@server.tool()
def list_pull_request_reviews(
    owner: str, repo: str, pull_number: int, per_page: int = 30
) -> dict:
    """List reviews on a pull request."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        params={"per_page": per_page},
    )


@server.tool()
def get_pull_request_review(
    owner: str, repo: str, pull_number: int, review_id: int
) -> dict:
    """Get a specific pull request review."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
    )


@server.tool()
def create_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    body: Optional[str] = None,
    event: str = "COMMENT",
    comments: Optional[list] = None,
) -> dict:
    """Create a review on a pull request."""
    data = {"event": event}
    if body:
        data["body"] = body
    if comments:
        data["comments"] = comments
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        json_data=data,
    )


@server.tool()
def submit_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    review_id: int,
    body: Optional[str] = None,
    event: str = "COMMENT",
) -> dict:
    """Submit a pull request review."""
    data = {"event": event}
    if body:
        data["body"] = body
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events",
        json_data=data,
    )


@server.tool()
def dismiss_pull_request_review(
    owner: str, repo: str, pull_number: int, review_id: int, message: str
) -> dict:
    """Dismiss a pull request review."""
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
        json_data={"message": message},
    )


@server.tool()
def list_pull_request_review_comments(
    owner: str, repo: str, pull_number: int, per_page: int = 30
) -> dict:
    """List review comments on a pull request."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        params={"per_page": per_page},
    )


@server.tool()
def create_pull_request_review_comment(
    owner: str,
    repo: str,
    pull_number: int,
    body: str,
    commit_id: str,
    path: str,
    line: Optional[int] = None,
    side: str = "RIGHT",
) -> dict:
    """Create a review comment on a pull request."""
    data = {"body": body, "commit_id": commit_id, "path": path, "side": side}
    if line is not None:
        data["line"] = line
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        json_data=data,
    )


@server.tool()
def update_pull_request_review_comment(
    owner: str, repo: str, comment_id: int, body: str
) -> dict:
    """Update a pull request review comment."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        json_data={"body": body},
    )


@server.tool()
def delete_pull_request_review_comment(
    owner: str, repo: str, comment_id: int
) -> dict:
    """Delete a pull request review comment."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")


# ============================================================================
# RELEASES
# ============================================================================


@server.tool()
def list_releases(owner: str, repo: str, per_page: int = 30) -> dict:
    """List releases in a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page}
    )


@server.tool()
def get_release(owner: str, repo: str, release_id: int) -> dict:
    """Get a specific release."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


@server.tool()
def get_release_by_tag(owner: str, repo: str, tag: str) -> dict:
    """Get a release by tag name."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")


@server.tool()
def create_release(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
) -> dict:
    """Create a new release."""
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if target_commitish:
        data["target_commitish"] = target_commitish
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/releases", json_data=data)


@server.tool()
def update_release(
    owner: str,
    repo: str,
    release_id: int,
    tag_name: Optional[str] = None,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
) -> dict:
    """Update a release."""
    data = {}
    if tag_name is not None:
        data["tag_name"] = tag_name
    if target_commitish is not None:
        data["target_commitish"] = target_commitish
    if name is not None:
        data["name"] = name
    if body is not None:
        data["body"] = body
    if draft is not None:
        data["draft"] = draft
    if prerelease is not None:
        data["prerelease"] = prerelease
    return make_request(
        "PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json_data=data
    )


@server.tool()
def delete_release(owner: str, repo: str, release_id: int) -> dict:
    """Delete a release."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")


# ============================================================================
# REPOSITORY CONTENTS
# ============================================================================


@server.tool()
def get_repository_content(
    owner: str, repo: str, path: str, ref: Optional[str] = None
) -> dict:
    """Get repository content (file or directory)."""
    params = {}
    if ref:
        params["ref"] = ref
    return make_request(
        "GET", f"/repos/{owner}/{repo}/contents/{path}", params=params
    )


@server.tool()
def create_or_update_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content: str,
    branch: Optional[str] = None,
    sha: Optional[str] = None,
) -> dict:
    """Create or update a file in a repository."""
    import base64

    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
    }
    if branch:
        data["branch"] = branch
    if sha:
        data["sha"] = sha
    return make_request(
        "PUT", f"/repos/{owner}/{repo}/contents/{path}", json_data=data
    )


@server.tool()
def delete_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
) -> dict:
    """Delete a file from a repository."""
    data = {"message": message, "sha": sha}
    if branch:
        data["branch"] = branch
    return make_request(
        "DELETE", f"/repos/{owner}/{repo}/contents/{path}", json_data=data
    )


# ============================================================================
# WEBHOOKS
# ============================================================================


@server.tool()
def list_webhooks(owner: str, repo: str, per_page: int = 30) -> dict:
    """List webhooks for a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page}
    )


@server.tool()
def get_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Get a specific webhook."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


@server.tool()
def create_webhook(
    owner: str,
    repo: str,
    url: str,
    events: list,
    content_type: str = "json",
    active: bool = True,
) -> dict:
    """Create a webhook for a repository."""
    data = {
        "config": {"url": url, "content_type": content_type},
        "events": events,
        "active": active,
    }
    return make_request("POST", f"/repos/{owner}/{repo}/hooks", json_data=data)


@server.tool()
def update_webhook(
    owner: str,
    repo: str,
    hook_id: int,
    url: Optional[str] = None,
    events: Optional[list] = None,
    active: Optional[bool] = None,
) -> dict:
    """Update a webhook."""
    data = {"config": {}}
    if url:
        data["config"]["url"] = url
    if events is not None:
        data["events"] = events
    if active is not None:
        data["active"] = active
    return make_request(
        "PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json_data=data
    )


@server.tool()
def delete_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Delete a webhook."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


@server.tool()
def test_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Test a webhook."""
    return make_request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")


# ============================================================================
# BRANCH PROTECTION
# ============================================================================


@server.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Get branch protection rules."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        headers={"Accept": "application/vnd.github.luke-cage-preview+json"},
    )


@server.tool()
def update_branch_protection(
    owner: str,
    repo: str,
    branch: str,
    required_status_checks: Optional[dict] = None,
    enforce_admins: Optional[bool] = None,
    required_pull_request_reviews: Optional[dict] = None,
    restrictions: Optional[dict] = None,
) -> dict:
    """Update branch protection rules."""
    data = {}
    if required_status_checks is not None:
        data["required_status_checks"] = required_status_checks
    if enforce_admins is not None:
        data["enforce_admins"] = enforce_admins
    if required_pull_request_reviews is not None:
        data["required_pull_request_reviews"] = required_pull_request_reviews
    if restrictions is not None:
        data["restrictions"] = restrictions
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        json_data=data,
        headers={"Accept": "application/vnd.github.luke-cage-preview+json"},
    )


@server.tool()
def delete_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Delete branch protection rules."""
    return make_request(
        "DELETE",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        headers={"Accept": "application/vnd.github.luke-cage-preview+json"},
    )


# ============================================================================
# ACTIONS (WORKFLOWS & RUNS)
# ============================================================================


@server.tool()
def list_workflows(owner: str, repo: str, per_page: int = 30) -> dict:
    """List workflows in a repository."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows",
        params={"per_page": per_page},
    )


@server.tool()
def get_workflow(owner: str, repo: str, workflow_id: str) -> dict:
    """Get a specific workflow."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


@server.tool()
def list_workflow_runs(
    owner: str, repo: str, workflow_id: str, per_page: int = 30
) -> dict:
    """List runs for a workflow."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
        params={"per_page": per_page},
    )


@server.tool()
def get_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Get a specific workflow run."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


@server.tool()
def cancel_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Cancel a workflow run."""
    return make_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


@server.tool()
def rerun_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Rerun a workflow run."""
    return make_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


@server.tool()
def delete_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Delete a workflow run."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


@server.tool()
def list_workflow_run_artifacts(owner: str, repo: str, run_id: int) -> dict:
    """List artifacts from a workflow run."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts"
    )


@server.tool()
def list_workflow_run_logs(owner: str, repo: str, run_id: int) -> dict:
    """Get logs for a workflow run."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")


# ============================================================================
# CODE SEARCH
# ============================================================================


@server.tool()
def search_code(query: str, per_page: int = 30) -> dict:
    """Search for code across GitHub."""
    return make_request(
        "GET", "/search/code", params={"q": query, "per_page": per_page}
    )


@server.tool()
def search_repositories(query: str, sort: str = "stars", per_page: int = 30) -> dict:
    """Search for repositories."""
    return make_request(
        "GET",
        "/search/repositories",
        params={"q": query, "sort": sort, "per_page": per_page},
    )


@server.tool()
def search_issues(query: str, per_page: int = 30) -> dict:
    """Search for issues and pull requests."""
    return make_request(
        "GET", "/search/issues", params={"q": query, "per_page": per_page}
    )


@server.tool()
def search_users(query: str, per_page: int = 30) -> dict:
    """Search for users."""
    return make_request(
        "GET", "/search/users", params={"q": query, "per_page": per_page}
    )


# ============================================================================
# USERS & AUTHENTICATION
# ============================================================================


@server.tool()
def get_authenticated_user() -> dict:
    """Get the authenticated user's profile."""
    return make_request("GET", "/user")


@server.tool()
def get_user(username: str) -> dict:
    """Get a user's public profile."""
    return make_request("GET", f"/users/{username}")


@server.tool()
def list_user_repos(username: str, per_page: int = 30) -> dict:
    """List repositories for a user."""
    return make_request(
        "GET", f"/users/{username}/repos", params={"per_page": per_page}
    )


@server.tool()
def list_user_followers(username: str, per_page: int = 30) -> dict:
    """List followers of a user."""
    return make_request(
        "GET", f"/users/{username}/followers", params={"per_page": per_page}
    )


@server.tool()
def list_user_following(username: str, per_page: int = 30) -> dict:
    """List users that a user is following."""
    return make_request(
        "GET", f"/users/{username}/following", params={"per_page": per_page}
    )


# ============================================================================
# GISTS
# ============================================================================


@server.tool()
def list_gists(per_page: int = 30) -> dict:
    """List gists for the authenticated user."""
    return make_request("GET", "/user/gists", params={"per_page": per_page})


@server.tool()
def get_gist(gist_id: str) -> dict:
    """Get a specific gist."""
    return make_request("GET", f"/gists/{gist_id}")


@server.tool()
def create_gist(
    files: dict, description: Optional[str] = None, public: bool = False
) -> dict:
    """Create a new gist."""
    data = {"files": files, "public": public}
    if description:
        data["description"] = description
    return make_request("POST", "/user/gists", json_data=data)


@server.tool()
def update_gist(gist_id: str, files: dict, description: Optional[str] = None) -> dict:
    """Update a gist."""
    data = {"files": files}
    if description is not None:
        data["description"] = description
    return make_request("PATCH", f"/gists/{gist_id}", json_data=data)


@server.tool()
def delete_gist(gist_id: str) -> dict:
    """Delete a gist."""
    return make_request("DELETE", f"/gists/{gist_id}")


# ============================================================================
# COLLABORATORS
# ============================================================================


@server.tool()
def list_collaborators(owner: str, repo: str, per_page: int = 30) -> dict:
    """List collaborators on a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/collaborators", params={"per_page": per_page}
    )


@server.tool()
def get_collaborator(owner: str, repo: str, username: str) -> dict:
    """Get a collaborator's permission level."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/collaborators/{username}/permission"
    )


@server.tool()
def add_collaborator(
    owner: str, repo: str, username: str, permission: str = "push"
) -> dict:
    """Add a collaborator to a repository."""
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/collaborators/{username}",
        json_data={"permission": permission},
    )


@server.tool()
def remove_collaborator(owner: str, repo: str, username: str) -> dict:
    """Remove a collaborator from a repository."""
    return make_request(
        "DELETE", f"/repos/{owner}/{repo}/collaborators/{username}"
    )


# ============================================================================
# MILESTONES
# ============================================================================


@server.tool()
def list_milestones(
    owner: str, repo: str, state: str = "open", per_page: int = 30
) -> dict:
    """List milestones in a repository."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/milestones",
        params={"state": state, "per_page": per_page},
    )


@server.tool()
def get_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Get a specific milestone."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/milestones/{milestone_number}"
    )


@server.tool()
def create_milestone(
    owner: str,
    repo: str,
    title: str,
    description: Optional[str] = None,
    due_on: Optional[str] = None,
) -> dict:
    """Create a new milestone."""
    data = {"title": title}
    if description:
        data["description"] = description
    if due_on:
        data["due_on"] = due_on
    return make_request("POST", f"/repos/{owner}/{repo}/milestones", json_data=data)


@server.tool()
def update_milestone(
    owner: str,
    repo: str,
    milestone_number: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    due_on: Optional[str] = None,
    state: Optional[str] = None,
) -> dict:
    """Update a milestone."""
    data = {}
    if title is not None:
        data["title"] = title
    if description is not None:
        data["description"] = description
    if due_on is not None:
        data["due_on"] = due_on
    if state is not None:
        data["state"] = state
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/milestones/{milestone_number}",
        json_data=data,
    )


@server.tool()
def delete_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Delete a milestone."""
    return make_request(
        "DELETE", f"/repos/{owner}/{repo}/milestones/{milestone_number}"
    )


# ============================================================================
# STARGAZERS & WATCHERS
# ============================================================================


@server.tool()
def list_stargazers(owner: str, repo: str, per_page: int = 30) -> dict:
    """List users who have starred a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/stargazers", params={"per_page": per_page}
    )


@server.tool()
def list_watchers(owner: str, repo: str, per_page: int = 30) -> dict:
    """List users watching a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/subscribers", params={"per_page": per_page}
    )


@server.tool()
def star_repository(owner: str, repo: str) -> dict:
    """Star a repository."""
    return make_request("PUT", f"/user/starred/{owner}/{repo}")


@server.tool()
def unstar_repository(owner: str, repo: str) -> dict:
    """Unstar a repository."""
    return make_request("DELETE", f"/user/starred/{owner}/{repo}")


@server.tool()
def check_if_starred(owner: str, repo: str) -> dict:
    """Check if the authenticated user has starred a repository."""
    return make_request("GET", f"/user/starred/{owner}/{repo}")


# ============================================================================
# FORKS
# ============================================================================


@server.tool()
def list_forks(owner: str, repo: str, per_page: int = 30) -> dict:
    """List forks of a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/forks", params={"per_page": per_page}
    )


# ============================================================================
# TEAMS
# ============================================================================


@server.tool()
def list_teams(org: str, per_page: int = 30) -> dict:
    """List teams in an organization."""
    return make_request(
        "GET", f"/orgs/{org}/teams", params={"per_page": per_page}
    )


@server.tool()
def get_team(org: str, team_slug: str) -> dict:
    """Get a team in an organization."""
    return make_request("GET", f"/orgs/{org}/teams/{team_slug}")


@server.tool()
def create_team(
    org: str,
    name: str,
    description: Optional[str] = None,
    privacy: str = "closed",
) -> dict:
    """Create a new team in an organization."""
    data = {"name": name, "privacy": privacy}
    if description:
        data["description"] = description
    return make_request("POST", f"/orgs/{org}/teams", json_data=data)


@server.tool()
def update_team(
    org: str,
    team_slug: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    privacy: Optional[str] = None,
) -> dict:
    """Update a team."""
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if privacy is not None:
        data["privacy"] = privacy
    return make_request(
        "PATCH", f"/orgs/{org}/teams/{team_slug}", json_data=data
    )


@server.tool()
def delete_team(org: str, team_slug: str) -> dict:
    """Delete a team."""
    return make_request("DELETE", f"/orgs/{org}/teams/{team_slug}")


@server.tool()
def list_team_members(org: str, team_slug: str, per_page: int = 30) -> dict:
    """List members of a team."""
    return make_request(
        "GET",
        f"/orgs/{org}/teams/{team_slug}/members",
        params={"per_page": per_page},
    )


@server.tool()
def add_team_member(org: str, team_slug: str, username: str) -> dict:
    """Add a member to a team."""
    return make_request(
        "PUT", f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
    )


@server.tool()
def remove_team_member(org: str, team_slug: str, username: str) -> dict:
    """Remove a member from a team."""
    return make_request(
        "DELETE", f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
    )


# ============================================================================
# ORGANIZATIONS
# ============================================================================


@server.tool()
def get_organization(org: str) -> dict:
    """Get organization information."""
    return make_request("GET", f"/orgs/{org}")


@server.tool()
def list_organization_repos(org: str, per_page: int = 30) -> dict:
    """List repositories in an organization."""
    return make_request(
        "GET", f"/orgs/{org}/repos", params={"per_page": per_page}
    )


@server.tool()
def list_organization_members(org: str, per_page: int = 30) -> dict:
    """List members of an organization."""
    return make_request(
        "GET", f"/orgs/{org}/members", params={"per_page": per_page}
    )


# ============================================================================
# REPOSITORY STATISTICS
# ============================================================================


@server.tool()
def get_repository_stats(owner: str, repo: str) -> dict:
    """Get repository statistics."""
    return make_request("GET", f"/repos/{owner}/{repo}/stats/contributors")


@server.tool()
def get_code_frequency(owner: str, repo: str) -> dict:
    """Get code frequency statistics."""
    return make_request("GET", f"/repos/{owner}/{repo}/stats/code_frequency")


@server.tool()
def get_commit_activity(owner: str, repo: str) -> dict:
    """Get commit activity statistics."""
    return make_request("GET", f"/repos/{owner}/{repo}/stats/commit_activity")


@server.tool()
def get_punch_card(owner: str, repo: str) -> dict:
    """Get punch card statistics."""
    return make_request("GET", f"/repos/{owner}/{repo}/stats/punch_card")


# ============================================================================
# COMPARE COMMITS
# ============================================================================


@server.tool()
def compare_commits(owner: str, repo: str, base: str, head: str) -> dict:
    """Compare two commits."""
    return make_request("GET", f"/repos/{owner}/{repo}/compare/{base}...{head}")


# ============================================================================
# MERGE BRANCHES
# ============================================================================


@server.tool()
def merge_branches(
    owner: str, repo: str, base: str, head: str, commit_message: Optional[str] = None
) -> dict:
    """Merge a branch into another branch."""
    data = {"base": base, "head": head}
    if commit_message:
        data["commit_message"] = commit_message
    return make_request("POST", f"/repos/{owner}/{repo}/merges", json_data=data)


# ============================================================================
# DEPLOY KEYS
# ============================================================================


@server.tool()
def list_deploy_keys(owner: str, repo: str, per_page: int = 30) -> dict:
    """List deploy keys for a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/keys", params={"per_page": per_page}
    )


@server.tool()
def get_deploy_key(owner: str, repo: str, key_id: int) -> dict:
    """Get a deploy key."""
    return make_request("GET", f"/repos/{owner}/{repo}/keys/{key_id}")


@server.tool()
def create_deploy_key(owner: str, repo: str, title: str, key: str, read_only: bool = True) -> dict:
    """Create a deploy key."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/keys",
        json_data={"title": title, "key": key, "read_only": read_only},
    )


@server.tool()
def delete_deploy_key(owner: str, repo: str, key_id: int) -> dict:
    """Delete a deploy key."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/keys/{key_id}")


# ============================================================================
# REPOSITORY INVITATIONS
# ============================================================================


@server.tool()
def list_repository_invitations(owner: str, repo: str, per_page: int = 30) -> dict:
    """List pending repository invitations."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/invitations",
        params={"per_page": per_page},
    )


@server.tool()
def update_repository_invitation(
    owner: str, repo: str, invitation_id: int, permission: str
) -> dict:
    """Update a repository invitation."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/invitations/{invitation_id}",
        json_data={"permission": permission},
    )


@server.tool()
def delete_repository_invitation(owner: str, repo: str, invitation_id: int) -> dict:
    """Delete a repository invitation."""
    return make_request(
        "DELETE", f"/repos/{owner}/{repo}/invitations/{invitation_id}"
    )


# ============================================================================
# TAGS
# ============================================================================


@server.tool()
def list_tags(owner: str, repo: str, per_page: int = 30) -> dict:
    """List tags in a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/tags", params={"per_page": per_page}
    )


@server.tool()
def get_tag(owner: str, repo: str, tag: str) -> dict:
    """Get a specific tag."""
    return make_request("GET", f"/repos/{owner}/{repo}/git/refs/tags/{tag}")


@server.tool()
def create_tag(
    owner: str, repo: str, tag: str, sha: str, message: Optional[str] = None
) -> dict:
    """Create a new tag."""
    data = {"tag": tag, "sha": sha}
    if message:
        data["message"] = message
        data["type"] = "commit"
    return make_request("POST", f"/repos/{owner}/{repo}/git/tags", json_data=data)


# ============================================================================
# PULL REQUEST CHECKS
# ============================================================================


@server.tool()
def list_pull_request_checks(owner: str, repo: str, pull_number: int) -> dict:
    """List check runs for a pull request."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/check-runs",
        headers={"Accept": "application/vnd.github.antiope-preview+json"},
    )


# ============================================================================
# REPOSITORY PERMISSIONS
# ============================================================================


@server.tool()
def get_repository_permission(owner: str, repo: str, username: str) -> dict:
    """Get a user's permission level for a repository."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/collaborators/{username}/permission"
    )


# ============================================================================
# ISSUES TIMELINE
# ============================================================================


@server.tool()
def list_issue_timeline(owner: str, repo: str, issue_number: int, per_page: int = 30) -> dict:
    """List timeline events for an issue."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/timeline",
        params={"per_page": per_page},
        headers={"Accept": "application/vnd.github.mockingbird-preview+json"},
    )


# ============================================================================
# PULL REQUEST MERGE STATUS
# ============================================================================


@server.tool()
def check_pull_request_merge_status(owner: str, repo: str, pull_number: int) -> dict:
    """Check if a pull request can be merged."""
    return make_request(
        "GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    )


# ============================================================================
# COMMIT COMMENTS
# ============================================================================


@server.tool()
def list_commit_comments(owner: str, repo: str, sha: str, per_page: int = 30) -> dict:
    """List comments on a commit."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/commits/{sha}/comments",
        params={"per_page": per_page},
    )


@server.tool()
def create_commit_comment(
    owner: str, repo: str, sha: str, body: str, path: Optional[str] = None, position: Optional[int] = None
) -> dict:
    """Create a comment on a commit."""
    data = {"body": body}
    if path:
        data["path"] = path
    if position is not None:
        data["position"] = position
    return make_request(
        "POST", f"/repos/{owner}/{repo}/commits/{sha}/comments", json_data=data
    )


@server.tool()
def update_commit_comment(owner: str, repo: str, comment_id: int, body: str) -> dict:
    """Update a commit comment."""
    return make_request(
        "PATCH",
        f"/repos/{owner}/{repo}/comments/{comment_id}",
        json_data={"body": body},
    )


@server.tool()
def delete_commit_comment(owner: str, repo: str, comment_id: int) -> dict:
    """Delete a commit comment."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/comments/{comment_id}")


# ============================================================================
# REPOSITORY LANGUAGES
# ============================================================================


@server.tool()
def get_repository_languages(owner: str, repo: str) -> dict:
    """Get programming languages used in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/languages")


# ============================================================================
# REPOSITORY README
# ============================================================================


@server.tool()
def get_repository_readme(owner: str, repo: str, ref: Optional[str] = None) -> dict:
    """Get the README file for a repository."""
    params = {}
    if ref:
        params["ref"] = ref
    return make_request(
        "GET", f"/repos/{owner}/{repo}/readme", params=params
    )


# ============================================================================
# ISSUES REACTIONS
# ============================================================================


@server.tool()
def list_issue_reactions(owner: str, repo: str, issue_number: int) -> dict:
    """List reactions on an issue."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/reactions",
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


@server.tool()
def create_issue_reaction(
    owner: str, repo: str, issue_number: int, reaction: str
) -> dict:
    """Create a reaction on an issue."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/reactions",
        json_data={"content": reaction},
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


# ============================================================================
# PULL REQUEST REACTIONS
# ============================================================================


@server.tool()
def list_pull_request_reactions(owner: str, repo: str, pull_number: int) -> dict:
    """List reactions on a pull request."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reactions",
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


@server.tool()
def create_pull_request_reaction(
    owner: str, repo: str, pull_number: int, reaction: str
) -> dict:
    """Create a reaction on a pull request."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reactions",
        json_data={"content": reaction},
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


# ============================================================================
# COMMIT REACTIONS
# ============================================================================


@server.tool()
def list_commit_reactions(owner: str, repo: str, sha: str) -> dict:
    """List reactions on a commit."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/commits/{sha}/reactions",
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


@server.tool()
def create_commit_reaction(owner: str, repo: str, sha: str, reaction: str) -> dict:
    """Create a reaction on a commit."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/commits/{sha}/reactions",
        json_data={"content": reaction},
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


# ============================================================================
# ISSUE COMMENT REACTIONS
# ============================================================================


@server.tool()
def list_issue_comment_reactions(owner: str, repo: str, comment_id: int) -> dict:
    """List reactions on an issue comment."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


@server.tool()
def create_issue_comment_reaction(
    owner: str, repo: str, comment_id: int, reaction: str
) -> dict:
    """Create a reaction on an issue comment."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
        json_data={"content": reaction},
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


# ============================================================================
# PULL REQUEST COMMENT REACTIONS
# ============================================================================


@server.tool()
def list_pull_request_comment_reactions(owner: str, repo: str, comment_id: int) -> dict:
    """List reactions on a pull request comment."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions",
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


@server.tool()
def create_pull_request_comment_reaction(
    owner: str, repo: str, comment_id: int, reaction: str
) -> dict:
    """Create a reaction on a pull request comment."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions",
        json_data={"content": reaction},
        headers={"Accept": "application/vnd.github.squirrel-girl-preview+json"},
    )


# ============================================================================
# REPOSITORY AUTOLINKS
# ============================================================================


@server.tool()
def list_autolinks(owner: str, repo: str) -> dict:
    """List autolinks for a repository."""
    return make_request(
        "GET",
        f"/repos/{owner}/{repo}/autolinks",
        headers={"Accept": "application/vnd.github.v3+json"},
    )


@server.tool()
def create_autolink(
    owner: str, repo: str, url_template: str, key_prefix: str
) -> dict:
    """Create an autolink for a repository."""
    return make_request(
        "POST",
        f"/repos/{owner}/{repo}/autolinks",
        json_data={"url_template": url_template, "key_prefix": key_prefix},
        headers={"Accept": "application/vnd.github.v3+json"},
    )


@server.tool()
def delete_autolink(owner: str, repo: str, autolink_id: int) -> dict:
    """Delete an autolink."""
    return make_request(
        "DELETE",
        f"/repos/{owner}/{repo}/autolinks/{autolink_id}",
        headers={"Accept": "application/vnd.github.v3+json"},
    )


# ============================================================================
# REPOSITORY TRAFFIC
# ============================================================================


@server.tool()
def get_traffic_clones(owner: str, repo: str) -> dict:
    """Get repository clone traffic."""
    return make_request("GET", f"/repos/{owner}/{repo}/traffic/clones")


@server.tool()
def get_traffic_views(owner: str, repo: str) -> dict:
    """Get repository view traffic."""
    return make_request("GET", f"/repos/{owner}/{repo}/traffic/views")


# ============================================================================
# REPOSITORY NOTIFICATIONS
# ============================================================================


@server.tool()
def list_notifications(all: bool = False, participating: bool = False) -> dict:
    """List notifications for the authenticated user."""
    return make_request(
        "GET",
        "/notifications",
        params={"all": all, "participating": participating},
    )


@server.tool()
def mark_notifications_as_read() -> dict:
    """Mark all notifications as read."""
    return make_request("PUT", "/notifications", json_data={})


# ============================================================================
# REPOSITORY SECURITY & ANALYSIS
# ============================================================================


@server.tool()
def enable_vulnerability_alerts(owner: str, repo: str) -> dict:
    """Enable vulnerability alerts for a repository."""
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/vulnerability-alerts",
        headers={"Accept": "application/vnd.github.dorian-preview+json"},
    )


@server.tool()
def disable_vulnerability_alerts(owner: str, repo: str) -> dict:
    """Disable vulnerability alerts for a repository."""
    return make_request(
        "DELETE",
        f"/repos/{owner}/{repo}/vulnerability-alerts",
        headers={"Accept": "application/vnd.github.dorian-preview+json"},
    )


@server.tool()
def enable_secret_scanning(owner: str, repo: str) -> dict:
    """Enable secret scanning for a repository."""
    return make_request(
        "PUT",
        f"/repos/{owner}/{repo}/secret-scanning",
        headers={"Accept": "application/vnd.github.dorian-preview+json"},
    )


@server.tool()
def disable_secret_scanning(owner: str, repo: str) -> dict:
    """Disable secret scanning for a repository."""
    return make_request(
        "DELETE",
        f"/repos/{owner}/{repo}/secret-scanning",
        headers={"Accept": "application/vnd.github.dorian-preview+json"},
    )


if __name__ == "__main__":
    server.run()
