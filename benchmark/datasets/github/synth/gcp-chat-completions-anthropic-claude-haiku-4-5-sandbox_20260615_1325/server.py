#!/usr/bin/env python3
"""GitHub REST API MCP Server - Comprehensive coverage of GitHub API endpoints."""

import os
import json
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github-api")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")

DEFAULT_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}
if GITHUB_TOKEN:
    DEFAULT_HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def make_request(method: str, endpoint: str, params: Optional[dict] = None, json_data: Optional[dict] = None) -> dict:
    """Make an HTTP request to the GitHub API."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=DEFAULT_HEADERS, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, json=json_data, headers=DEFAULT_HEADERS, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, params=params, json=json_data, headers=DEFAULT_HEADERS, timeout=30)
        elif method.upper() == "PATCH":
            response = requests.patch(url, params=params, json=json_data, headers=DEFAULT_HEADERS, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, headers=DEFAULT_HEADERS, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}", "message": response.text[:500]}
        if response.status_code == 204:
            return {"success": True}
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"success": True, "body": response.text[:1000]}
    except requests.RequestException as e:
        return {"error": str(e)}


# ISSUES
@mcp.tool()
def list_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> dict:
    """List issues in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues", {"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Get a specific issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, labels: Optional[list] = None) -> dict:
    """Create a new issue."""
    data = {"title": title}
    if body:
        data["body"] = body
    if labels:
        data["labels"] = labels
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json_data=data)

@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> dict:
    """Update an issue."""
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_data=data)

@mcp.tool()
def close_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Close an issue."""
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_data={"state": "closed"})

@mcp.tool()
def add_issue_labels(owner: str, repo: str, issue_number: int, labels: list) -> dict:
    """Add labels to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json_data={"labels": labels})

@mcp.tool()
def remove_issue_label(owner: str, repo: str, issue_number: int, label: str) -> dict:
    """Remove a label from an issue."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}")

@mcp.tool()
def list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> dict:
    """List comments on an issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", {"per_page": per_page, "page": page})

@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict:
    """Create a comment on an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json_data={"body": body})

@mcp.tool()
def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> dict:
    """Update an issue comment."""
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json_data={"body": body})

@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
    """Delete an issue comment."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")

@mcp.tool()
def assign_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
    """Assign users to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json_data={"assignees": assignees})

# PULL REQUESTS
@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> dict:
    """List pull requests in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls", {"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """Get a specific pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None) -> dict:
    """Create a new pull request."""
    data = {"title": title, "head": head, "base": base}
    if body:
        data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls", json_data=data)

@mcp.tool()
def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> dict:
    """Update a pull request."""
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_data=data)

@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, merge_method: str = "merge") -> dict:
    """Merge a pull request."""
    return make_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_data={"merge_method": merge_method})

@mcp.tool()
def list_pull_request_reviews(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> dict:
    """List reviews on a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", {"per_page": per_page, "page": page})

@mcp.tool()
def create_pull_request_review(owner: str, repo: str, pull_number: int, body: Optional[str] = None, event: str = "COMMENT") -> dict:
    """Create a review on a pull request."""
    data = {"event": event}
    if body:
        data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json_data=data)

@mcp.tool()
def request_pull_request_reviewers(owner: str, repo: str, pull_number: int, reviewers: Optional[list] = None) -> dict:
    """Request reviewers for a pull request."""
    data = {}
    if reviewers:
        data["reviewers"] = reviewers
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json_data=data)

@mcp.tool()
def list_pull_request_commits(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> dict:
    """List commits in a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/commits", {"per_page": per_page, "page": page})

@mcp.tool()
def list_pull_request_files(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> dict:
    """List files changed in a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/files", {"per_page": per_page, "page": page})

@mcp.tool()
def list_pull_request_comments(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> dict:
    """List review comments on a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", {"per_page": per_page, "page": page})

@mcp.tool()
def create_pull_request_comment(owner: str, repo: str, pull_number: int, body: str, commit_id: str, path: str, position: int) -> dict:
    """Create a review comment on a pull request."""
    data = {"body": body, "commit_id": commit_id, "path": path, "position": position}
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", json_data=data)

# REPOSITORIES
@mcp.tool()
def get_repository(owner: str, repo: str) -> dict:
    """Get repository information."""
    return make_request("GET", f"/repos/{owner}/{repo}")

@mcp.tool()
def list_user_repositories(username: str, per_page: int = 30, page: int = 1) -> dict:
    """List repositories for a user."""
    return make_request("GET", f"/users/{username}/repos", {"per_page": per_page, "page": page})

@mcp.tool()
def list_organization_repositories(org: str, per_page: int = 30, page: int = 1) -> dict:
    """List repositories in an organization."""
    return make_request("GET", f"/orgs/{org}/repos", {"per_page": per_page, "page": page})

@mcp.tool()
def create_repository(name: str, description: Optional[str] = None, private: bool = False, org: Optional[str] = None) -> dict:
    """Create a new repository."""
    data = {"name": name, "private": private}
    if description:
        data["description"] = description
    endpoint = f"/orgs/{org}/repos" if org else "/user/repos"
    return make_request("POST", endpoint, json_data=data)

@mcp.tool()
def update_repository(owner: str, repo: str, description: Optional[str] = None, private: Optional[bool] = None) -> dict:
    """Update repository settings."""
    data = {}
    if description is not None:
        data["description"] = description
    if private is not None:
        data["private"] = private
    return make_request("PATCH", f"/repos/{owner}/{repo}", json_data=data)

@mcp.tool()
def delete_repository(owner: str, repo: str) -> dict:
    """Delete a repository."""
    return make_request("DELETE", f"/repos/{owner}/{repo}")

@mcp.tool()
def fork_repository(owner: str, repo: str, org: Optional[str] = None) -> dict:
    """Fork a repository."""
    data = {}
    if org:
        data["organization"] = org
    return make_request("POST", f"/repos/{owner}/{repo}/forks", json_data=data)

@mcp.tool()
def get_repository_readme(owner: str, repo: str, ref: Optional[str] = None) -> dict:
    """Get the README file for a repository."""
    params = {}
    if ref:
        params["ref"] = ref
    return make_request("GET", f"/repos/{owner}/{repo}/readme", params)

@mcp.tool()
def list_repository_languages(owner: str, repo: str) -> dict:
    """List programming languages used in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/languages")

@mcp.tool()
def list_repository_contributors(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List contributors to a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/contributors", {"per_page": per_page, "page": page})

# BRANCHES
@mcp.tool()
def list_branches(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List branches in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches", {"per_page": per_page, "page": page})

@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> dict:
    """Get a specific branch."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")

@mcp.tool()
def create_branch(owner: str, repo: str, branch: str, sha: str) -> dict:
    """Create a new branch."""
    return make_request("POST", f"/repos/{owner}/{repo}/git/refs", json_data={"ref": f"refs/heads/{branch}", "sha": sha})

@mcp.tool()
def delete_branch(owner: str, repo: str, branch: str) -> dict:
    """Delete a branch."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/git/refs/heads/{branch}")

@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Get branch protection rules."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")

@mcp.tool()
def update_branch_protection(owner: str, repo: str, branch: str, enforce_admins: Optional[bool] = None) -> dict:
    """Update branch protection rules."""
    data = {}
    if enforce_admins is not None:
        data["enforce_admins"] = enforce_admins
    return make_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json_data=data)

# COMMITS
@mcp.tool()
def list_commits(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List commits in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/commits", {"per_page": per_page, "page": page})

@mcp.tool()
def get_commit(owner: str, repo: str, sha: str) -> dict:
    """Get a specific commit."""
    return make_request("GET", f"/repos/{owner}/{repo}/commits/{sha}")

@mcp.tool()
def list_commit_comments(owner: str, repo: str, sha: str, per_page: int = 30, page: int = 1) -> dict:
    """List comments on a commit."""
    return make_request("GET", f"/repos/{owner}/{repo}/commits/{sha}/comments", {"per_page": per_page, "page": page})

@mcp.tool()
def create_commit_comment(owner: str, repo: str, sha: str, body: str) -> dict:
    """Create a comment on a commit."""
    return make_request("POST", f"/repos/{owner}/{repo}/commits/{sha}/comments", json_data={"body": body})

# RELEASES
@mcp.tool()
def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List releases in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases", {"per_page": per_page, "page": page})

@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> dict:
    """Get a specific release."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")

@mcp.tool()
def get_latest_release(owner: str, repo: str) -> dict:
    """Get the latest release."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/latest")

@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: bool = False, prerelease: bool = False) -> dict:
    """Create a new release."""
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/releases", json_data=data)

@mcp.tool()
def update_release(owner: str, repo: str, release_id: int, name: Optional[str] = None, body: Optional[str] = None) -> dict:
    """Update a release."""
    data = {}
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    return make_request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json_data=data)

@mcp.tool()
def delete_release(owner: str, repo: str, release_id: int) -> dict:
    """Delete a release."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")

# REPOSITORY CONTENTS
@mcp.tool()
def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> dict:
    """Get repository content (file or directory)."""
    params = {}
    if ref:
        params["ref"] = ref
    return make_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params)

@mcp.tool()
def create_or_update_file(owner: str, repo: str, path: str, message: str, content: str, sha: Optional[str] = None) -> dict:
    """Create or update a file in a repository."""
    import base64
    data = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        data["sha"] = sha
    return make_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json_data=data)

@mcp.tool()
def delete_file(owner: str, repo: str, path: str, message: str, sha: str) -> dict:
    """Delete a file from a repository."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json_data={"message": message, "sha": sha})

# LABELS
@mcp.tool()
def list_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List labels in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/labels", {"per_page": per_page, "page": page})

@mcp.tool()
def get_label(owner: str, repo: str, name: str) -> dict:
    """Get a specific label."""
    return make_request("GET", f"/repos/{owner}/{repo}/labels/{name}")

@mcp.tool()
def create_label(owner: str, repo: str, name: str, color: str, description: Optional[str] = None) -> dict:
    """Create a new label."""
    data = {"name": name, "color": color}
    if description:
        data["description"] = description
    return make_request("POST", f"/repos/{owner}/{repo}/labels", json_data=data)

@mcp.tool()
def update_label(owner: str, repo: str, name: str, new_name: Optional[str] = None, color: Optional[str] = None) -> dict:
    """Update a label."""
    data = {}
    if new_name:
        data["new_name"] = new_name
    if color:
        data["color"] = color
    return make_request("PATCH", f"/repos/{owner}/{repo}/labels/{name}", json_data=data)

@mcp.tool()
def delete_label(owner: str, repo: str, name: str) -> dict:
    """Delete a label."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")

# MILESTONES
@mcp.tool()
def list_milestones(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> dict:
    """List milestones in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/milestones", {"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def get_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Get a specific milestone."""
    return make_request("GET", f"/repos/{owner}/{repo}/milestones/{milestone_number}")

@mcp.tool()
def create_milestone(owner: str, repo: str, title: str, description: Optional[str] = None) -> dict:
    """Create a new milestone."""
    data = {"title": title}
    if description:
        data["description"] = description
    return make_request("POST", f"/repos/{owner}/{repo}/milestones", json_data=data)

@mcp.tool()
def update_milestone(owner: str, repo: str, milestone_number: int, title: Optional[str] = None, state: Optional[str] = None) -> dict:
    """Update a milestone."""
    data = {}
    if title:
        data["title"] = title
    if state:
        data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/milestones/{milestone_number}", json_data=data)

@mcp.tool()
def delete_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Delete a milestone."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/milestones/{milestone_number}")

# WEBHOOKS
@mcp.tool()
def list_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List webhooks in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks", {"per_page": per_page, "page": page})

@mcp.tool()
def get_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Get a specific webhook."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")

@mcp.tool()
def create_webhook(owner: str, repo: str, url: str, events: list, active: bool = True) -> dict:
    """Create a new webhook."""
    data = {"config": {"url": url, "content_type": "json"}, "events": events, "active": active}
    return make_request("POST", f"/repos/{owner}/{repo}/hooks", json_data=data)

@mcp.tool()
def update_webhook(owner: str, repo: str, hook_id: int, url: Optional[str] = None, events: Optional[list] = None) -> dict:
    """Update a webhook."""
    data = {"config": {}}
    if url:
        data["config"]["url"] = url
    if events:
        data["events"] = events
    return make_request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json_data=data)

@mcp.tool()
def delete_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Delete a webhook."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")

# COLLABORATORS
@mcp.tool()
def list_collaborators(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List collaborators in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/collaborators", {"per_page": per_page, "page": page})

@mcp.tool()
def add_collaborator(owner: str, repo: str, username: str, permission: str = "push") -> dict:
    """Add a collaborator to a repository."""
    return make_request("PUT", f"/repos/{owner}/{repo}/collaborators/{username}", json_data={"permission": permission})

@mcp.tool()
def remove_collaborator(owner: str, repo: str, username: str) -> dict:
    """Remove a collaborator from a repository."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/collaborators/{username}")

# WORKFLOWS & ACTIONS
@mcp.tool()
def list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List workflows in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows", {"per_page": per_page, "page": page})

@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id: str) -> dict:
    """Get a specific workflow."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")

@mcp.tool()
def list_workflow_runs(owner: str, repo: str, workflow_id: str, per_page: int = 30, page: int = 1) -> dict:
    """List workflow runs for a workflow."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", {"per_page": per_page, "page": page})

@mcp.tool()
def list_repository_workflow_runs(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List all workflow runs in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs", {"per_page": per_page, "page": page})

@mcp.tool()
def get_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Get a specific workflow run."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")

@mcp.tool()
def cancel_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Cancel a workflow run."""
    return make_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")

@mcp.tool()
def rerun_workflow(owner: str, repo: str, run_id: int) -> dict:
    """Rerun a workflow."""
    return make_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")

@mcp.tool()
def list_workflow_jobs(owner: str, repo: str, run_id: int, per_page: int = 30, page: int = 1) -> dict:
    """List jobs in a workflow run."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs", {"per_page": per_page, "page": page})

@mcp.tool()
def list_artifacts(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List artifacts in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/artifacts", {"per_page": per_page, "page": page})

@mcp.tool()
def get_artifact(owner: str, repo: str, artifact_id: int) -> dict:
    """Get a specific artifact."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")

@mcp.tool()
def delete_artifact(owner: str, repo: str, artifact_id: int) -> dict:
    """Delete an artifact."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")

# SEARCH
@mcp.tool()
def search_repositories(query: str, sort: str = "stars", per_page: int = 30) -> dict:
    """Search for repositories."""
    return make_request("GET", "/search/repositories", {"q": query, "sort": sort, "per_page": per_page})

@mcp.tool()
def search_issues(query: str, sort: str = "updated", per_page: int = 30) -> dict:
    """Search for issues and pull requests."""
    return make_request("GET", "/search/issues", {"q": query, "sort": sort, "per_page": per_page})

@mcp.tool()
def search_code(query: str, per_page: int = 30) -> dict:
    """Search for code."""
    return make_request("GET", "/search/code", {"q": query, "per_page": per_page})

# USERS
@mcp.tool()
def get_user(username: str) -> dict:
    """Get user information."""
    return make_request("GET", f"/users/{username}")

@mcp.tool()
def get_authenticated_user() -> dict:
    """Get authenticated user information."""
    return make_request("GET", "/user")

@mcp.tool()
def list_user_followers(username: str, per_page: int = 30, page: int = 1) -> dict:
    """List followers of a user."""
    return make_request("GET", f"/users/{username}/followers", {"per_page": per_page, "page": page})

@mcp.tool()
def list_user_following(username: str, per_page: int = 30, page: int = 1) -> dict:
    """List users that a user is following."""
    return make_request("GET", f"/users/{username}/following", {"per_page": per_page, "page": page})

# ORGANIZATIONS
@mcp.tool()
def get_organization(org: str) -> dict:
    """Get organization information."""
    return make_request("GET", f"/orgs/{org}")

@mcp.tool()
def list_organization_members(org: str, per_page: int = 30, page: int = 1) -> dict:
    """List members of an organization."""
    return make_request("GET", f"/orgs/{org}/members", {"per_page": per_page, "page": page})

@mcp.tool()
def list_organization_teams(org: str, per_page: int = 30, page: int = 1) -> dict:
    """List teams in an organization."""
    return make_request("GET", f"/orgs/{org}/teams", {"per_page": per_page, "page": page})

# GISTS
@mcp.tool()
def list_gists(username: str, per_page: int = 30, page: int = 1) -> dict:
    """List gists for a user."""
    return make_request("GET", f"/users/{username}/gists", {"per_page": per_page, "page": page})

@mcp.tool()
def get_gist(gist_id: str) -> dict:
    """Get a specific gist."""
    return make_request("GET", f"/gists/{gist_id}")

@mcp.tool()
def create_gist(files: dict, description: Optional[str] = None, public: bool = False) -> dict:
    """Create a new gist."""
    data = {"files": files, "public": public}
    if description:
        data["description"] = description
    return make_request("POST", "/gists", json_data=data)

# RATE LIMIT
@mcp.tool()
def get_rate_limit() -> dict:
    """Get rate limit information."""
    return make_request("GET", "/rate_limit")


if __name__ == "__main__":
    mcp.run()
