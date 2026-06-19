#!/usr/bin/env python3
"""
GitHub REST API MCP Server

A comprehensive MCP server implementation for the GitHub REST API,
providing tools for managing repositories, issues, pull requests,
and other GitHub resources.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("github-api")

# Configuration from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TEST_REPO = os.getenv("GITHUB_TEST_REPO", "")

# API version header
API_VERSION = "2026-03-10"

# Helper function to make API requests
def github_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    json_data: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> dict:
    """Make a request to the GitHub API."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    
    req_headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
    }
    
    if GITHUB_TOKEN:
        req_headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    
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
        
        # Handle different status codes
        if response.status_code in [200, 201, 204]:
            if response.text:
                return response.json()
            return {"status": "success"}
        elif response.status_code == 404:
            return {"error": "Not found", "status_code": 404}
        elif response.status_code == 403:
            return {"error": "Forbidden", "status_code": 403}
        elif response.status_code == 422:
            return {"error": "Validation failed", "status_code": 422, "details": response.text}
        else:
            return {"error": f"HTTP {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# REPOSITORIES
# ============================================================================

@mcp.tool()
def list_org_repos(org: str, type: str = "all", sort: str = "created", per_page: int = 30) -> dict:
    """List repositories for an organization.
    
    Args:
        org: The organization name
        type: Type of repos (all, public, private, forks, sources, member)
        sort: Sort by (created, updated, pushed, full_name)
        per_page: Results per page (max 100)
    """
    return github_request(
        "GET",
        f"/orgs/{org}/repos",
        params={"type": type, "sort": sort, "per_page": per_page}
    )


@mcp.tool()
def create_org_repo(org: str, name: str, description: str = "", private: bool = False, **kwargs) -> dict:
    """Create a new repository in an organization.
    
    Args:
        org: The organization name
        name: Repository name (required)
        description: Repository description
        private: Whether the repository is private
        **kwargs: Additional parameters (has_issues, has_projects, has_wiki, etc.)
    """
    data = {
        "name": name,
        "description": description,
        "private": private,
    }
    data.update(kwargs)
    
    return github_request("POST", f"/orgs/{org}/repos", json_data=data)


@mcp.tool()
def get_repo(owner: str, repo: str) -> dict:
    """Get repository information.
    
    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_request("GET", f"/repos/{owner}/{repo}")


@mcp.tool()
def update_repo(owner: str, repo: str, **kwargs) -> dict:
    """Update repository settings.
    
    Args:
        owner: Repository owner
        repo: Repository name
        **kwargs: Fields to update (description, private, has_issues, etc.)
    """
    return github_request("PATCH", f"/repos/{owner}/{repo}", json_data=kwargs)


@mcp.tool()
def delete_repo(owner: str, repo: str) -> dict:
    """Delete a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}")


@mcp.tool()
def fork_repo(owner: str, repo: str, org: str = "") -> dict:
    """Fork a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        org: Organization to fork into (optional)
    """
    data = {}
    if org:
        data["organization"] = org
    
    return github_request("POST", f"/repos/{owner}/{repo}/forks", json_data=data)


@mcp.tool()
def list_repo_branches(owner: str, repo: str, per_page: int = 30) -> dict:
    """List branches in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/branches",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> dict:
    """Get branch information.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


@mcp.tool()
def create_branch(owner: str, repo: str, branch: str, sha: str) -> dict:
    """Create a new branch.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: New branch name
        sha: Commit SHA to base the branch on
    """
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/git/refs",
        json_data={"ref": f"refs/heads/{branch}", "sha": sha}
    )


@mcp.tool()
def delete_branch(owner: str, repo: str, branch: str) -> dict:
    """Delete a branch.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/git/refs/heads/{branch}")


# ============================================================================
# ISSUES
# ============================================================================

@mcp.tool()
def list_repo_issues(owner: str, repo: str, state: str = "open", per_page: int = 30) -> dict:
    """List issues in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Issue state (open, closed, all)
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/issues",
        params={"state": state, "per_page": per_page}
    )


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Get an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    """
    return github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: str = "", **kwargs) -> dict:
    """Create an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Issue title (required)
        body: Issue description
        **kwargs: Additional fields (assignees, labels, milestone, etc.)
    """
    data = {"title": title, "body": body}
    data.update(kwargs)
    
    return github_request("POST", f"/repos/{owner}/{repo}/issues", json_data=data)


@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, **kwargs) -> dict:
    """Update an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        **kwargs: Fields to update (title, body, state, assignees, labels, etc.)
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/{issue_number}",
        json_data=kwargs
    )


@mcp.tool()
def add_issue_labels(owner: str, repo: str, issue_number: int, labels: list) -> dict:
    """Add labels to an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: List of label names
    """
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
        json_data={"labels": labels}
    )


@mcp.tool()
def remove_issue_label(owner: str, repo: str, issue_number: int, label: str) -> dict:
    """Remove a label from an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        label: Label name
    """
    return github_request(
        "DELETE",
        f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}"
    )


@mcp.tool()
def list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30) -> dict:
    """List comments on an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        params={"per_page": per_page}
    )


@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict:
    """Create a comment on an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        body: Comment text
    """
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        json_data={"body": body}
    )


@mcp.tool()
def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> dict:
    """Update an issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        body: New comment text
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
        json_data={"body": body}
    )


@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
    """Delete an issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


# ============================================================================
# PULL REQUESTS
# ============================================================================

@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30) -> dict:
    """List pull requests in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: PR state (open, closed, all)
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls",
        params={"state": state, "per_page": per_page}
    )


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """Get a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    """
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = "", **kwargs) -> dict:
    """Create a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: PR title (required)
        head: Head branch (required)
        base: Base branch (required)
        body: PR description
        **kwargs: Additional fields (draft, maintainer_can_modify, etc.)
    """
    data = {"title": title, "head": head, "base": base, "body": body}
    data.update(kwargs)
    
    return github_request("POST", f"/repos/{owner}/{repo}/pulls", json_data=data)


@mcp.tool()
def update_pull_request(owner: str, repo: str, pull_number: int, **kwargs) -> dict:
    """Update a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        **kwargs: Fields to update (title, body, state, etc.)
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/pulls/{pull_number}",
        json_data=kwargs
    )


@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str = "", commit_message: str = "", merge_method: str = "merge") -> dict:
    """Merge a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        commit_title: Commit title
        commit_message: Commit message
        merge_method: Merge method (merge, squash, rebase)
    """
    data = {"merge_method": merge_method}
    if commit_title:
        data["commit_title"] = commit_title
    if commit_message:
        data["commit_message"] = commit_message
    
    return github_request(
        "PUT",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        json_data=data
    )


@mcp.tool()
def list_pull_request_reviews(owner: str, repo: str, pull_number: int, per_page: int = 30) -> dict:
    """List reviews on a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        params={"per_page": per_page}
    )


@mcp.tool()
def create_pull_request_review(owner: str, repo: str, pull_number: int, event: str = "COMMENT", body: str = "", **kwargs) -> dict:
    """Create a review on a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        event: Review event (APPROVE, REQUEST_CHANGES, COMMENT)
        body: Review body
        **kwargs: Additional fields (comments, etc.)
    """
    data = {"event": event}
    if body:
        data["body"] = body
    data.update(kwargs)
    
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        json_data=data
    )


@mcp.tool()
def list_pull_request_comments(owner: str, repo: str, pull_number: int, per_page: int = 30) -> dict:
    """List comments on a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        params={"per_page": per_page}
    )


@mcp.tool()
def create_pull_request_comment(owner: str, repo: str, pull_number: int, body: str, commit_id: str, path: str, position: int) -> dict:
    """Create a comment on a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        body: Comment text
        commit_id: Commit SHA
        path: File path
        position: Line position
    """
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        json_data={"body": body, "commit_id": commit_id, "path": path, "position": position}
    )


# ============================================================================
# RELEASES
# ============================================================================

@mcp.tool()
def list_releases(owner: str, repo: str, per_page: int = 30) -> dict:
    """List releases in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/releases",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> dict:
    """Get a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    """
    return github_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: str = "", body: str = "", draft: bool = False, prerelease: bool = False, **kwargs) -> dict:
    """Create a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        tag_name: Tag name (required)
        name: Release name
        body: Release description
        draft: Whether the release is a draft
        prerelease: Whether the release is a prerelease
        **kwargs: Additional fields
    """
    data = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
    }
    data.update(kwargs)
    
    return github_request("POST", f"/repos/{owner}/{repo}/releases", json_data=data)


@mcp.tool()
def update_release(owner: str, repo: str, release_id: int, **kwargs) -> dict:
    """Update a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
        **kwargs: Fields to update (name, body, draft, prerelease, etc.)
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/releases/{release_id}",
        json_data=kwargs
    )


@mcp.tool()
def delete_release(owner: str, repo: str, release_id: int) -> dict:
    """Delete a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")


# ============================================================================
# COMMITS
# ============================================================================

@mcp.tool()
def list_commits(owner: str, repo: str, sha: str = "", per_page: int = 30) -> dict:
    """List commits in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Branch/tag/commit SHA
        per_page: Results per page
    """
    params = {"per_page": per_page}
    if sha:
        params["sha"] = sha
    
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/commits",
        params=params
    )


@mcp.tool()
def get_commit(owner: str, repo: str, commit_sha: str) -> dict:
    """Get a commit.
    
    Args:
        owner: Repository owner
        repo: Repository name
        commit_sha: Commit SHA
    """
    return github_request("GET", f"/repos/{owner}/{repo}/commits/{commit_sha}")


@mcp.tool()
def get_repo_contents(owner: str, repo: str, path: str = "", ref: str = "") -> dict:
    """Get repository contents.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File or directory path
        ref: Branch/tag/commit SHA
    """
    params = {}
    if ref:
        params["ref"] = ref
    
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/contents/{path}",
        params=params
    )


@mcp.tool()
def create_or_update_file(owner: str, repo: str, path: str, message: str, content: str, branch: str = "", sha: str = "") -> dict:
    """Create or update a file in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        message: Commit message
        content: File content (base64 encoded)
        branch: Branch name
        sha: File SHA (for updates)
    """
    import base64
    
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
    }
    if branch:
        data["branch"] = branch
    if sha:
        data["sha"] = sha
    
    return github_request(
        "PUT",
        f"/repos/{owner}/{repo}/contents/{path}",
        json_data=data
    )


@mcp.tool()
def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: str = "") -> dict:
    """Delete a file from a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        message: Commit message
        sha: File SHA
        branch: Branch name
    """
    data = {"message": message, "sha": sha}
    if branch:
        data["branch"] = branch
    
    return github_request(
        "DELETE",
        f"/repos/{owner}/{repo}/contents/{path}",
        json_data=data
    )


# ============================================================================
# LABELS
# ============================================================================

@mcp.tool()
def list_labels(owner: str, repo: str, per_page: int = 30) -> dict:
    """List labels in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/labels",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_label(owner: str, repo: str, name: str) -> dict:
    """Get a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    """
    return github_request("GET", f"/repos/{owner}/{repo}/labels/{name}")


@mcp.tool()
def create_label(owner: str, repo: str, name: str, color: str, description: str = "") -> dict:
    """Create a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
        color: Label color (hex without #)
        description: Label description
    """
    return github_request(
        "POST",
        f"/repos/{owner}/{repo}/labels",
        json_data={"name": name, "color": color, "description": description}
    )


@mcp.tool()
def update_label(owner: str, repo: str, name: str, **kwargs) -> dict:
    """Update a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
        **kwargs: Fields to update (new_name, color, description)
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/labels/{name}",
        json_data=kwargs
    )


@mcp.tool()
def delete_label(owner: str, repo: str, name: str) -> dict:
    """Delete a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")


# ============================================================================
# BRANCH PROTECTION
# ============================================================================

@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Get branch protection rules.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


@mcp.tool()
def update_branch_protection(owner: str, repo: str, branch: str, **kwargs) -> dict:
    """Update branch protection rules.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        **kwargs: Protection settings
    """
    return github_request(
        "PUT",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        json_data=kwargs
    )


@mcp.tool()
def delete_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Delete branch protection rules.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")


# ============================================================================
# WEBHOOKS
# ============================================================================

@mcp.tool()
def list_webhooks(owner: str, repo: str, per_page: int = 30) -> dict:
    """List webhooks in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/hooks",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Get a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


@mcp.tool()
def create_webhook(owner: str, repo: str, url: str, events: list, active: bool = True, **kwargs) -> dict:
    """Create a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        url: Webhook URL
        events: List of events to trigger on
        active: Whether the webhook is active
        **kwargs: Additional config
    """
    data = {
        "config": {"url": url},
        "events": events,
        "active": active,
    }
    data.update(kwargs)
    
    return github_request("POST", f"/repos/{owner}/{repo}/hooks", json_data=data)


@mcp.tool()
def update_webhook(owner: str, repo: str, hook_id: int, **kwargs) -> dict:
    """Update a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        **kwargs: Fields to update
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/hooks/{hook_id}",
        json_data=kwargs
    )


@mcp.tool()
def delete_webhook(owner: str, repo: str, hook_id: int) -> dict:
    """Delete a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


# ============================================================================
# ACTIONS (Workflows)
# ============================================================================

@mcp.tool()
def list_workflows(owner: str, repo: str, per_page: int = 30) -> dict:
    """List workflows in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id: str) -> dict:
    """Get a workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or filename
    """
    return github_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


@mcp.tool()
def list_workflow_runs(owner: str, repo: str, workflow_id: str, per_page: int = 30) -> dict:
    """List workflow runs.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or filename
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
        params={"per_page": per_page}
    )


@mcp.tool()
def get_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Get a workflow run.
    
    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


@mcp.tool()
def cancel_workflow_run(owner: str, repo: str, run_id: int) -> dict:
    """Cancel a workflow run.
    
    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


# ============================================================================
# SEARCH
# ============================================================================

@mcp.tool()
def search_code(q: str, per_page: int = 30) -> dict:
    """Search for code.
    
    Args:
        q: Search query
        per_page: Results per page
    """
    return github_request(
        "GET",
        "/search/code",
        params={"q": q, "per_page": per_page}
    )


@mcp.tool()
def search_repos(q: str, sort: str = "stars", per_page: int = 30) -> dict:
    """Search for repositories.
    
    Args:
        q: Search query
        sort: Sort by (stars, forks, updated)
        per_page: Results per page
    """
    return github_request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "per_page": per_page}
    )


@mcp.tool()
def search_issues(q: str, per_page: int = 30) -> dict:
    """Search for issues and pull requests.
    
    Args:
        q: Search query
        per_page: Results per page
    """
    return github_request(
        "GET",
        "/search/issues",
        params={"q": q, "per_page": per_page}
    )


# ============================================================================
# USERS
# ============================================================================

@mcp.tool()
def get_user(username: str) -> dict:
    """Get user information.
    
    Args:
        username: GitHub username
    """
    return github_request("GET", f"/users/{username}")


@mcp.tool()
def get_authenticated_user() -> dict:
    """Get authenticated user information."""
    return github_request("GET", "/user")


@mcp.tool()
def list_user_repos(username: str, type: str = "owner", per_page: int = 30) -> dict:
    """List repositories for a user.
    
    Args:
        username: GitHub username
        type: Type of repos (all, owner, member)
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/users/{username}/repos",
        params={"type": type, "per_page": per_page}
    )


# ============================================================================
# ORGANIZATIONS
# ============================================================================

@mcp.tool()
def get_org(org: str) -> dict:
    """Get organization information.
    
    Args:
        org: Organization name
    """
    return github_request("GET", f"/orgs/{org}")


@mcp.tool()
def list_org_members(org: str, per_page: int = 30) -> dict:
    """List organization members.
    
    Args:
        org: Organization name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/orgs/{org}/members",
        params={"per_page": per_page}
    )


@mcp.tool()
def list_org_teams(org: str, per_page: int = 30) -> dict:
    """List organization teams.
    
    Args:
        org: Organization name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/orgs/{org}/teams",
        params={"per_page": per_page}
    )


# ============================================================================
# COLLABORATORS
# ============================================================================

@mcp.tool()
def list_collaborators(owner: str, repo: str, per_page: int = 30) -> dict:
    """List collaborators on a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/collaborators",
        params={"per_page": per_page}
    )


@mcp.tool()
def add_collaborator(owner: str, repo: str, username: str, permission: str = "push") -> dict:
    """Add a collaborator to a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        username: GitHub username
        permission: Permission level (pull, push, admin, maintain, triage)
    """
    return github_request(
        "PUT",
        f"/repos/{owner}/{repo}/collaborators/{username}",
        json_data={"permission": permission}
    )


@mcp.tool()
def remove_collaborator(owner: str, repo: str, username: str) -> dict:
    """Remove a collaborator from a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        username: GitHub username
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/collaborators/{username}")


# ============================================================================
# MILESTONES
# ============================================================================

@mcp.tool()
def list_milestones(owner: str, repo: str, state: str = "open", per_page: int = 30) -> dict:
    """List milestones in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Milestone state (open, closed, all)
        per_page: Results per page
    """
    return github_request(
        "GET",
        f"/repos/{owner}/{repo}/milestones",
        params={"state": state, "per_page": per_page}
    )


@mcp.tool()
def get_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Get a milestone.
    
    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
    """
    return github_request("GET", f"/repos/{owner}/{repo}/milestones/{milestone_number}")


@mcp.tool()
def create_milestone(owner: str, repo: str, title: str, description: str = "", due_on: str = "") -> dict:
    """Create a milestone.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Milestone title
        description: Milestone description
        due_on: Due date (ISO 8601 format)
    """
    data = {"title": title}
    if description:
        data["description"] = description
    if due_on:
        data["due_on"] = due_on
    
    return github_request("POST", f"/repos/{owner}/{repo}/milestones", json_data=data)


@mcp.tool()
def update_milestone(owner: str, repo: str, milestone_number: int, **kwargs) -> dict:
    """Update a milestone.
    
    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
        **kwargs: Fields to update (title, description, state, due_on)
    """
    return github_request(
        "PATCH",
        f"/repos/{owner}/{repo}/milestones/{milestone_number}",
        json_data=kwargs
    )


@mcp.tool()
def delete_milestone(owner: str, repo: str, milestone_number: int) -> dict:
    """Delete a milestone.
    
    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/milestones/{milestone_number}")


if __name__ == "__main__":
    mcp.run()
