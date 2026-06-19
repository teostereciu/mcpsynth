#!/usr/bin/env python3
"""
GitHub REST API MCP Server

An MCP server with comprehensive coverage of the GitHub REST API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("github")

# Get GitHub API configuration from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")


def _get_headers() -> dict[str, str]:
    """Get the authentication headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def _request(method: str, path: str, params: Optional[dict] = None, json: Optional[dict] = None) -> dict[str, Any]:
    """Make a GitHub API request and return the response."""
    url = f"{GITHUB_API_BASE_URL}{path}"
    headers = _get_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=30
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            if response.status_code == 204:  # No content
                return {"success": True}
            return response.json()
        else:
            error_detail = {
                "error": f"GitHub API error: {response.status_code}",
                "status_code": response.status_code,
                "path": path
            }
            
            # Try to include error message from GitHub
            try:
                error_data = response.json()
                if "message" in error_data:
                    error_detail["message"] = error_data["message"]
            except:
                pass
            
            return error_detail
            
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# =============================================================================
# Repository Operations
# =============================================================================

@mcp.tool()
def list_repositories(
    visibility: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    affiliation: Optional[str] = None
) -> dict[str, Any]:
    """List repositories for the authenticated user.
    
    Args:
        visibility: Filter by visibility (all, public, private)
        sort: Sort by (created, updated, pushed, full_name)
        direction: Sort direction (asc, desc)
        affiliation: Filter by affiliation (owner, collaborator, organization_member)
    
    Returns:
        List of repositories
    """
    params = {}
    if visibility:
        params["visibility"] = visibility
    if sort:
        params["sort"] = sort
    if direction:
        params["direction"] = direction
    if affiliation:
        params["affiliation"] = affiliation
    
    return _request("GET", "/user/repos", params=params)


@mcp.tool()
def get_repository(owner: str, repo: str) -> dict[str, Any]:
    """Get a repository by owner and name.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        Repository information
    """
    return _request("GET", f"/repos/{owner}/{repo}")


@mcp.tool()
def create_repository(
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    auto_init: bool = False,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
    allow_squash_merge: bool = True,
    allow_merge_commit: bool = True,
    allow_rebase_merge: bool = True,
    allow_auto_merge: bool = False,
    delete_branch_on_merge: bool = False,
    squash_merge_commit_title: Optional[str] = None,
    squash_merge_commit_message: Optional[str] = None,
    merge_commit_title: Optional[str] = None,
    merge_commit_message: Optional[str] = None
) -> dict[str, Any]:
    """Create a new repository for the authenticated user.
    
    Args:
        name: Repository name
        description: Repository description
        homepage: Repository homepage URL
        private: Whether repository is private
        has_issues: Whether issues are enabled
        has_projects: Whether projects are enabled
        has_wiki: Whether wiki is enabled
        auto_init: Whether to auto-initialize with README
        gitignore_template: Gitignore template to use
        license_template: License template to use
        allow_squash_merge: Allow squash merging
        allow_merge_commit: Allow merge commits
        allow_rebase_merge: Allow rebase merging
        allow_auto_merge: Allow auto-merge
        delete_branch_on_merge: Delete branch on merge
        squash_merge_commit_title: Squash merge commit title
        squash_merge_commit_message: Squash merge commit message
        merge_commit_title: Merge commit title
        merge_commit_message: Merge commit message
    
    Returns:
        Created repository information
    """
    json_data = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
    }
    
    if description:
        json_data["description"] = description
    if homepage:
        json_data["homepage"] = homepage
    if gitignore_template:
        json_data["gitignore_template"] = gitignore_template
    if license_template:
        json_data["license_template"] = license_template
    if squash_merge_commit_title:
        json_data["squash_merge_commit_title"] = squash_merge_commit_title
    if squash_merge_commit_message:
        json_data["squash_merge_commit_message"] = squash_merge_commit_message
    if merge_commit_title:
        json_data["merge_commit_title"] = merge_commit_title
    if merge_commit_message:
        json_data["merge_commit_message"] = merge_commit_message
    
    return _request("POST", "/user/repos", json=json_data)


@mcp.tool()
def update_repository(
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
    default_branch: Optional[str] = None,
    is_template: Optional[bool] = None
) -> dict[str, Any]:
    """Update repository information.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: New repository name
        description: New repository description
        homepage: New homepage URL
        private: Whether repository is private
        has_issues: Whether issues are enabled
        has_projects: Whether projects are enabled
        has_wiki: Whether wiki is enabled
        allow_squash_merge: Allow squash merging
        allow_merge_commit: Allow merge commits
        allow_rebase_merge: Allow rebase merging
        allow_auto_merge: Allow auto-merge
        delete_branch_on_merge: Delete branch on merge
        default_branch: Default branch name
        is_template: Whether repository is a template
    
    Returns:
        Updated repository information
    """
    json_data = {}
    
    if name is not None:
        json_data["name"] = name
    if description is not None:
        json_data["description"] = description
    if homepage is not None:
        json_data["homepage"] = homepage
    if private is not None:
        json_data["private"] = private
    if has_issues is not None:
        json_data["has_issues"] = has_issues
    if has_projects is not None:
        json_data["has_projects"] = has_projects
    if has_wiki is not None:
        json_data["has_wiki"] = has_wiki
    if allow_squash_merge is not None:
        json_data["allow_squash_merge"] = allow_squash_merge
    if allow_merge_commit is not None:
        json_data["allow_merge_commit"] = allow_merge_commit
    if allow_rebase_merge is not None:
        json_data["allow_rebase_merge"] = allow_rebase_merge
    if allow_auto_merge is not None:
        json_data["allow_auto_merge"] = allow_auto_merge
    if delete_branch_on_merge is not None:
        json_data["delete_branch_on_merge"] = delete_branch_on_merge
    if default_branch is not None:
        json_data["default_branch"] = default_branch
    if is_template is not None:
        json_data["is_template"] = is_template
    
    return _request("PATCH", f"/repos/{owner}/{repo}", json=json_data)


@mcp.tool()
def delete_repository(owner: str, repo: str) -> dict[str, Any]:
    """Delete a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        Success status
    """
    return _request("DELETE", f"/repos/{owner}/{repo}")


@mcp.tool()
def list_branches(owner: str, repo: str, protected: Optional[bool] = None) -> dict[str, Any]:
    """List branches for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        protected: Filter by protected status
    
    Returns:
        List of branches
    """
    params = {}
    if protected is not None:
        params["protected"] = protected
    
    return _request("GET", f"/repos/{owner}/{repo}/branches", params=params)


@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> dict[str, Any]:
    """Get a branch by name.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    
    Returns:
        Branch information
    """
    return _request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


@mcp.tool()
def protect_branch(
    owner: str,
    repo: str,
    branch: str,
    require_pull_request_review: bool = True,
    require_status_checks: bool = False,
    strict: bool = False,
    contexts: Optional[list[str]] = None,
    require_code_owner_review: bool = False,
    dismiss_stale_reviews: bool = True,
    require_up_to_date_branch: bool = False,
    dismissal_restrictions: Optional[dict] = None,
    push_restrictions: Optional[dict] = None
) -> dict[str, Any]:
    """Configure branch protection settings.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name to protect
        require_pull_request_review: Require pull request reviews
        require_status_checks: Require status checks
        strict: Require status checks to be up to date
        contexts: List of required status check contexts
        require_code_owner_review: Require code owner review
        dismiss_stale_reviews: Dismiss stale reviews on push
        require_up_to_date_branch: Require branch to be up to date before merging
        dismissal_restrictions: Users/teams allowed to dismiss reviews
        push_restrictions: Users/teams allowed to push
    
    Returns:
        Branch protection settings
    """
    json_data = {
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": dismiss_stale_reviews,
            "require_code_owner_reviews": require_code_owner_review,
            "dismissal_restrictions": dismissal_restrictions or {},
        },
        "enforce_admins": False,
        "required_status_checks": {
            "strict": strict,
            "contexts": contexts or []
        } if require_status_checks else None,
        "required_linear_history": False,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "block_creates": False,
        "required_conversation_resolution": False,
        "required_signatures": False,
        "required_signed_commits": False,
        "restrictions": push_restrictions
    }
    
    if require_pull_request_review is False:
        json_data["required_pull_request_reviews"] = None
    
    return _request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=json_data)


# =============================================================================
# Pull Request Operations
# =============================================================================

@mcp.tool()
def list_pull_requests(
    owner: str,
    repo: str,
    state: Optional[str] = None,
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None
) -> dict[str, Any]:
    """List pull requests for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state (open, closed, all)
        head: Filter by head branch
        base: Filter by base branch
        sort: Sort by (created, updated, popularity, long-running)
        direction: Sort direction (asc, desc)
    
    Returns:
        List of pull requests
    """
    params = {}
    if state:
        params["state"] = state
    if head:
        params["head"] = head
    if base:
        params["base"] = base
    if sort:
        params["sort"] = sort
    if direction:
        params["direction"] = direction
    
    return _request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict[str, Any]:
    """Get a pull request by number.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    
    Returns:
        Pull request information
    """
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: bool = False,
    maintainer_can_modify: bool = True
) -> dict[str, Any]:
    """Create a new pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Pull request title
        head: Branch name containing changes
        base: Branch name to merge into
        body: Pull request body
        draft: Whether to create as draft
        maintainer_can_modify: Whether maintainers can modify
    
    Returns:
        Created pull request information
    """
    json_data = {
        "title": title,
        "head": head,
        "base": base,
        "draft": draft,
        "maintainer_can_modify": maintainer_can_modify
    }
    
    if body:
        json_data["body"] = body
    
    return _request("POST", f"/repos/{owner}/{repo}/pulls", json=json_data)


@mcp.tool()
def update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    draft: Optional[bool] = None
) -> dict[str, Any]:
    """Update a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        title: New title
        body: New body
        state: New state (open, closed)
        base: New base branch
        draft: Draft status
    
    Returns:
        Updated pull request information
    """
    json_data = {}
    
    if title is not None:
        json_data["title"] = title
    if body is not None:
        json_data["body"] = body
    if state is not None:
        json_data["state"] = state
    if base is not None:
        json_data["base"] = base
    if draft is not None:
        json_data["draft"] = draft
    
    return _request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=json_data)


@mcp.tool()
def merge_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: str = "merge"
) -> dict[str, Any]:
    """Merge a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        commit_title: Commit title
        commit_message: Commit message
        merge_method: Merge method (merge, squash, rebase)
    
    Returns:
        Merge result information
    """
    json_data = {"merge_method": merge_method}
    
    if commit_title:
        json_data["commit_title"] = commit_title
    if commit_message:
        json_data["commit_message"] = commit_message
    
    return _request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=json_data)


@mcp.tool()
def list_pull_request_files(
    owner: str,
    repo: str,
    pull_number: int
) -> dict[str, Any]:
    """List files changed in a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    
    Returns:
        List of files changed
    """
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/files")


@mcp.tool()
def list_pull_request_comments(
    owner: str,
    repo: str,
    pull_number: int
) -> dict[str, Any]:
    """List comments on a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    
    Returns:
        List of comments
    """
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/comments")


@mcp.tool()
def create_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    commit_id: str,
    body: str,
    event: str,
    comments: Optional[list[dict]] = None
) -> dict[str, Any]:
    """Create a review for a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        commit_id: Commit ID to review
        body: Review body
        event: Review event (APPROVE, REQUEST_CHANGES, COMMENT, PENDING)
        comments: Array of comments
    
    Returns:
        Created review information
    """
    json_data = {
        "commit_id": commit_id,
        "body": body,
        "event": event
    }
    
    if comments:
        json_data["comments"] = comments
    
    return _request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=json_data)


@mcp.tool()
def list_pull_request_reviews(
    owner: str,
    repo: str,
    pull_number: int
) -> dict[str, Any]:
    """List reviews for a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    
    Returns:
        List of reviews
    """
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews")


@mcp.tool()
def get_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    review_id: int
) -> dict[str, Any]:
    """Get a specific pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
    
    Returns:
        Review information
    """
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")


@mcp.tool()
def delete_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    review_id: int
) -> dict[str, Any]:
    """Delete a pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
    
    Returns:
        Success status
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")


# =============================================================================
# Issue Operations
# =============================================================================

@mcp.tool()
def list_issues(
    owner: str,
    repo: str,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None
) -> dict[str, Any]:
    """List issues for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state (open, closed, all)
        labels: Filter by labels (comma-separated)
        sort: Sort by (created, updated, comments)
        direction: Sort direction (asc, desc)
        since: Only issues updated after this time
    
    Returns:
        List of issues
    """
    params = {}
    if state:
        params["state"] = state
    if labels:
        params["labels"] = labels
    if sort:
        params["sort"] = sort
    if direction:
        params["direction"] = direction
    if since:
        params["since"] = since
    
    return _request("GET", f"/repos/{owner}/{repo}/issues", params=params)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict[str, Any]:
    """Get an issue by number.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    
    Returns:
        Issue information
    """
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    labels: Optional[list[str]] = None,
    milestone: Optional[int] = None
) -> dict[str, Any]:
    """Create a new issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Issue title
        body: Issue body
        assignees: List of assignees
        labels: List of labels
        milestone: Milestone number
    
    Returns:
        Created issue information
    """
    json_data = {"title": title}
    
    if body:
        json_data["body"] = body
    if assignees:
        json_data["assignees"] = assignees
    if labels:
        json_data["labels"] = labels
    if milestone:
        json_data["milestone"] = milestone
    
    return _request("POST", f"/repos/{owner}/{repo}/issues", json=json_data)


@mcp.tool()
def update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    labels: Optional[list[str]] = None,
    milestone: Optional[int] = None
) -> dict[str, Any]:
    """Update an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        title: New title
        body: New body
        state: New state (open, closed)
        assignees: New list of assignees
        labels: New list of labels
        milestone: New milestone number
    
    Returns:
        Updated issue information
    """
    json_data = {}
    
    if title is not None:
        json_data["title"] = title
    if body is not None:
        json_data["body"] = body
    if state is not None:
        json_data["state"] = state
    if assignees is not None:
        json_data["assignees"] = assignees
    if labels is not None:
        json_data["labels"] = labels
    if milestone is not None:
        json_data["milestone"] = milestone
    
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=json_data)


@mcp.tool()
def add_issue_labels(
    owner: str,
    repo: str,
    issue_number: int,
    labels: list[str]
) -> dict[str, Any]:
    """Add labels to an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: List of labels to add
    
    Returns:
        List of labels after adding
    """
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})


@mcp.tool()
def remove_issue_label(
    owner: str,
    repo: str,
    issue_number: int,
    label: str
) -> dict[str, Any]:
    """Remove a label from an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        label: Label to remove
    
    Returns:
        List of remaining labels
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}")


@mcp.tool()
def list_issue_comments(
    owner: str,
    repo: str,
    issue_number: int
) -> dict[str, Any]:
    """List comments on an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    
    Returns:
        List of comments
    """
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")


@mcp.tool()
def create_issue_comment(
    owner: str,
    repo: str,
    issue_number: int,
    body: str
) -> dict[str, Any]:
    """Create a comment on an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        body: Comment body
    
    Returns:
        Created comment information
    """
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


@mcp.tool()
def list_issue_events(
    owner: str,
    repo: str,
    issue_number: int
) -> dict[str, Any]:
    """List events for an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    
    Returns:
        List of events
    """
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/events")


# =============================================================================
# Label Operations
# =============================================================================

@mcp.tool()
def list_labels(owner: str, repo: str) -> dict[str, Any]:
    """List labels for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of labels
    """
    return _request("GET", f"/repos/{owner}/{repo}/labels")


@mcp.tool()
def get_label(owner: str, repo: str, name: str) -> dict[str, Any]:
    """Get a label by name.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    
    Returns:
        Label information
    """
    return _request("GET", f"/repos/{owner}/{repo}/labels/{name}")


@mcp.tool()
def create_label(
    owner: str,
    repo: str,
    name: str,
    color: str,
    description: Optional[str] = None
) -> dict[str, Any]:
    """Create a new label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
        color: Hex color code without # prefix
        description: Label description
    
    Returns:
        Created label information
    """
    json_data = {
        "name": name,
        "color": color
    }
    
    if description:
        json_data["description"] = description
    
    return _request("POST", f"/repos/{owner}/{repo}/labels", json=json_data)


@mcp.tool()
def update_label(
    owner: str,
    repo: str,
    name: str,
    new_name: Optional[str] = None,
    color: Optional[str] = None,
    description: Optional[str] = None
) -> dict[str, Any]:
    """Update a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Current label name
        new_name: New label name
        color: New hex color code
        description: New description
    
    Returns:
        Updated label information
    """
    json_data = {}
    
    if new_name is not None:
        json_data["new_name"] = new_name
    if color is not None:
        json_data["color"] = color
    if description is not None:
        json_data["description"] = description
    
    return _request("PATCH", f"/repos/{owner}/{repo}/labels/{name}", json=json_data)


@mcp.tool()
def delete_label(owner: str, repo: str, name: str) -> dict[str, Any]:
    """Delete a label.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    
    Returns:
        Success status
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")


# =============================================================================
# Assignee Operations
# =============================================================================

@mcp.tool()
def list_assignees(owner: str, repo: str) -> dict[str, Any]:
    """List assignees for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of assignees
    """
    return _request("GET", f"/repos/{owner}/{repo}/assignees")


@mcp.tool()
def add_assignees(
    owner: str,
    repo: str,
    issue_number: int,
    assignees: list[str]
) -> dict[str, Any]:
    """Add assignees to an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        assignees: List of assignees to add
    
    Returns:
        List of assignees after adding
    """
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})


@mcp.tool()
def remove_assignees(
    owner: str,
    repo: str,
    issue_number: int,
    assignees: list[str]
) -> dict[str, Any]:
    """Remove assignees from an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        assignees: List of assignees to remove
    
    Returns:
        List of remaining assignees
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})


# =============================================================================
# Commit Operations
# =============================================================================

@mcp.tool()
def list_commits(
    owner: str,
    repo: str,
    sha: Optional[str] = None,
    path: Optional[str] = None,
    author: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """List commits in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: SHA or branch to start listing commits from
        path: Path to filter commits by
        author: GitHub username to filter by
        since: Only commits after this date
        until: Only commits before this date
        page: Page number
        per_page: Number of results per page
    
    Returns:
        List of commits
    """
    params = {}
    if sha:
        params["sha"] = sha
    if path:
        params["path"] = path
    if author:
        params["author"] = author
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", f"/repos/{owner}/{repo}/commits", params=params)


@mcp.tool()
def get_commit(owner: str, repo: str, sha: str) -> dict[str, Any]:
    """Get a specific commit.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
    
    Returns:
        Commit information
    """
    return _request("GET", f"/repos/{owner}/{repo}/commits/{sha}")


@mcp.tool()
def list_commit_comments(owner: str, repo: str, sha: str) -> dict[str, Any]:
    """List comments on a commit.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
    
    Returns:
        List of comments
    """
    return _request("GET", f"/repos/{owner}/{repo}/commits/{sha}/comments")


@mcp.tool()
def create_commit_comment(
    owner: str,
    repo: str,
    sha: str,
    body: str,
    path: Optional[str] = None,
    position: Optional[int] = None,
    line: Optional[int] = None
) -> dict[str, Any]:
    """Create a commit comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
        body: Comment body
        path: Path to file
        position: Position in the diff
        line: Line number
    
    Returns:
        Created comment information
    """
    json_data = {"body": body}
    
    if path is not None:
        json_data["path"] = path
    if position is not None:
        json_data["position"] = position
    if line is not None:
        json_data["line"] = line
    
    return _request("POST", f"/repos/{owner}/{repo}/commits/{sha}/comments", json=json_data)


# =============================================================================
# File Operations
# =============================================================================

@mcp.tool()
def get_contents(
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None
) -> dict[str, Any]:
    """Get file contents.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        ref: Branch, tag, or commit SHA
    
    Returns:
        File content information
    """
    params = {}
    if ref:
        params["ref"] = ref
    
    return _request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)


@mcp.tool()
def create_file(
    owner: str,
    repo: str,
    path: str,
    content: str,
    message: str,
    branch: Optional[str] = None,
    committer: Optional[dict] = None,
    author: Optional[dict] = None
) -> dict[str, Any]:
    """Create a new file.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        content: File content (base64 encoded)
        message: Commit message
        branch: Branch to create the file in
        committer: Committer information
        author: Author information
    
    Returns:
        Created file information
    """
    import base64
    import json
    
    json_data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode()
    }
    
    if branch:
        json_data["branch"] = branch
    if committer:
        json_data["committer"] = committer
    if author:
        json_data["author"] = author
    
    return _request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=json_data)


@mcp.tool()
def update_file(
    owner: str,
    repo: str,
    path: str,
    content: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[dict] = None,
    author: Optional[dict] = None
) -> dict[str, Any]:
    """Update an existing file.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        content: New file content (base64 encoded)
        message: Commit message
        sha: File's current SHA
        branch: Branch to update the file in
        committer: Committer information
        author: Author information
    
    Returns:
        Updated file information
    """
    import base64
    
    json_data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "sha": sha
    }
    
    if branch:
        json_data["branch"] = branch
    if committer:
        json_data["committer"] = committer
    if author:
        json_data["author"] = author
    
    return _request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=json_data)


@mcp.tool()
def delete_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[dict] = None,
    author: Optional[dict] = None
) -> dict[str, Any]:
    """Delete a file.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        message: Commit message
        sha: File's current SHA
        branch: Branch to delete the file in
        committer: Committer information
        author: Author information
    
    Returns:
        Deleted file information
    """
    json_data = {
        "message": message,
        "sha": sha
    }
    
    if branch:
        json_data["branch"] = branch
    if committer:
        json_data["committer"] = committer
    if author:
        json_data["author"] = author
    
    return _request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=json_data)


# =============================================================================
# Release Operations
# =============================================================================

@mcp.tool()
def list_releases(owner: str, repo: str) -> dict[str, Any]:
    """List releases for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of releases
    """
    return _request("GET", f"/repos/{owner}/{repo}/releases")


@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> dict[str, Any]:
    """Get a release by ID.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    
    Returns:
        Release information
    """
    return _request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


@mcp.tool()
def create_release(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
    generate_release_notes: bool = False
) -> dict[str, Any]:
    """Create a new release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        tag_name: Tag name for the release
        target_commitish: Branch or commit SHA
        name: Release title
        body: Release notes
        draft: Whether to create as draft
        prerelease: Whether to mark as prerelease
        generate_release_notes: Automatically generate release notes
    
    Returns:
        Created release information
    """
    json_data = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease
    }
    
    if target_commitish:
        json_data["target_commitish"] = target_commitish
    if name:
        json_data["name"] = name
    if body:
        json_data["body"] = body
    if generate_release_notes:
        json_data["generate_release_notes"] = generate_release_notes
    
    return _request("POST", f"/repos/{owner}/{repo}/releases", json=json_data)


@mcp.tool()
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
    make_latest: Optional[bool] = None
) -> dict[str, Any]:
    """Update a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
        tag_name: New tag name
        target_commitish: New branch or commit SHA
        name: New release title
        body: New release notes
        draft: New draft status
        prerelease: New prerelease status
        make_latest: Update 'latest' release
    
    Returns:
        Updated release information
    """
    json_data = {}
    
    if tag_name is not None:
        json_data["tag_name"] = tag_name
    if target_commitish is not None:
        json_data["target_commitish"] = target_commitish
    if name is not None:
        json_data["name"] = name
    if body is not None:
        json_data["body"] = body
    if draft is not None:
        json_data["draft"] = draft
    if prerelease is not None:
        json_data["prerelease"] = prerelease
    if make_latest is not None:
        json_data["make_latest"] = make_latest
    
    return _request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=json_data)


@mcp.tool()
def delete_release(owner: str, repo: str, release_id: int) -> dict[str, Any]:
    """Delete a release.
    
    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    
    Returns:
        Success status
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")


# =============================================================================
# GitHub Actions Operations
# =============================================================================

@mcp.tool()
def list_workflow_runs(
    owner: str,
    repo: str,
    workflow_id: Optional[int] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_name: Optional[str] = None,
    commit_sha: Optional[str] = None,
    performer: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """List workflow runs for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Filter by workflow ID
        branch: Filter by branch
        event: Filter by event type
        status: Filter by status (completed, in_progress, queued, waiting, requested, pending, in_progress, cancelled, failure, neutral, skipped, stale, success, timed_out, action_required)
        created: Filter by creation time
        exclude_pull_requests: Exclude pull requests
        check_name: Filter by check name
        commit_sha: Filter by commit SHA
        performer: Filter by performer
        page: Page number
        per_page: Results per page
    
    Returns:
        List of workflow runs
    """
    params = {}
    if workflow_id:
        params["workflow_id"] = workflow_id
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    if status:
        params["status"] = status
    if created:
        params["created"] = created
    if exclude_pull_requests is not None:
        params["exclude_pull_requests"] = exclude_pull_requests
    if check_name:
        params["check_name"] = check_name
    if commit_sha:
        params["commit_sha"] = commit_sha
    if performer:
        params["performer"] = performer
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)


@mcp.tool()
def get_workflow_run(owner: str, repo: str, run_id: int) -> dict[str, Any]:
    """Get a specific workflow run.
    
    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    
    Returns:
        Workflow run information
    """
    return _request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


@mcp.tool()
def rerun_workflow_run(owner: str, repo: str, run_id: int) -> dict[str, Any]:
    """Rerun a workflow run.
    
    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    
    Returns:
        Rerun result
    """
    return _request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


@mcp.tool()
def list_workflows(owner: str, repo: str) -> dict[str, Any]:
    """List workflows for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of workflows
    """
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows")


@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id: int) -> dict[str, Any]:
    """Get a specific workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
    
    Returns:
        Workflow information
    """
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


@mcp.tool()
def enable_workflow(owner: str, repo: str, workflow_id: int) -> dict[str, Any]:
    """Enable a workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
    
    Returns:
        Success status
    """
    return _request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


@mcp.tool()
def disable_workflow(owner: str, repo: str, workflow_id: int) -> dict[str, Any]:
    """Disable a workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
    
    Returns:
        Success status
    """
    return _request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


# =============================================================================
# Search Operations
# =============================================================================

@mcp.tool()
def search_repositories(
    query: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """Search repositories.
    
    Args:
        query: Search query
        sort: Sort by (stars, forks, help-wanted-issues, updated)
        order: Sort order (asc, desc)
        page: Page number
        per_page: Results per page
    
    Returns:
        Search results
    """
    params = {"q": query}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", "/search/repositories", params=params)


@mcp.tool()
def search_code(
    query: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """Search code.
    
    Args:
        query: Search query
        sort: Sort by (indexed)
        order: Sort order (asc, desc)
        page: Page number
        per_page: Results per page
    
    Returns:
        Search results
    """
    params = {"q": query}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", "/search/code", params=params)


@mcp.tool()
def search_issues(
    query: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """Search issues and pull requests.
    
    Args:
        query: Search query
        sort: Sort by (comments, created, updated, reactions, popularity, long-running)
        order: Sort order (asc, desc)
        page: Page number
        per_page: Results per page
    
    Returns:
        Search results
    """
    params = {"q": query}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", "/search/issues", params=params)


@mcp.tool()
def search_users(
    query: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None
) -> dict[str, Any]:
    """Search users.
    
    Args:
        query: Search query
        sort: Sort by (followers, repositories, joined)
        order: Sort order (asc, desc)
        page: Page number
        per_page: Results per page
    
    Returns:
        Search results
    """
    params = {"q": query}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    
    return _request("GET", "/search/users", params=params)


# =============================================================================
# User Operations
# =============================================================================

@mcp.tool()
def get_authenticated_user() -> dict[str, Any]:
    """Get the authenticated user.
    
    Returns:
        User information
    """
    return _request("GET", "/user")


@mcp.tool()
def update_authenticated_user(
    name: Optional[str] = None,
    email: Optional[str] = None,
    blog: Optional[str] = None,
    company: Optional[str] = None,
    location: Optional[str] = None,
    hireable: Optional[bool] = None,
    bio: Optional[str] = None
) -> dict[str, Any]:
    """Update the authenticated user.
    
    Args:
        name: User's display name
        email: Publicly visible email
        blog: Blog URL
        company: Company name
        location: Location
        hireable: Whether user is available for hire
        bio: Publicly visible biography
    
    Returns:
        Updated user information
    """
    json_data = {}
    
    if name is not None:
        json_data["name"] = name
    if email is not None:
        json_data["email"] = email
    if blog is not None:
        json_data["blog"] = blog
    if company is not None:
        json_data["company"] = company
    if location is not None:
        json_data["location"] = location
    if hireable is not None:
        json_data["hireable"] = hireable
    if bio is not None:
        json_data["bio"] = bio
    
    return _request("PATCH", "/user", json=json_data)


@mcp.tool()
def list_user_repositories(
    username: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None
) -> dict[str, Any]:
    """List repositories for a user.
    
    Args:
        username: GitHub username
        type: Type of repositories (owner, member)
        sort: Sort by (created, updated, pushed, full_name)
        direction: Sort direction (asc, desc)
    
    Returns:
        List of repositories
    """
    params = {}
    if type:
        params["type"] = type
    if sort:
        params["sort"] = sort
    if direction:
        params["direction"] = direction
    
    return _request("GET", f"/users/{username}/repos", params=params)


@mcp.tool()
def get_user(username: str) -> dict[str, Any]:
    """Get a user by username.
    
    Args:
        username: GitHub username
    
    Returns:
        User information
    """
    return _request("GET", f"/users/{username}")


# =============================================================================
# Organization Operations
# =============================================================================

@mcp.tool()
def list_org_repositories(
    org: str,
    type: Optional[str] = None
) -> dict[str, Any]:
    """List repositories for an organization.
    
    Args:
        org: Organization name
        type: Type of repositories (all, public, private, forks, sources, member)
    
    Returns:
        List of repositories
    """
    params = {}
    if type:
        params["type"] = type
    
    return _request("GET", f"/orgs/{org}/repos", params=params)


@mcp.tool()
def get_org(org: str) -> dict[str, Any]:
    """Get an organization by name.
    
    Args:
        org: Organization name
    
    Returns:
        Organization information
    """
    return _request("GET", f"/orgs/{org}")


# =============================================================================
# Hook Operations
# =============================================================================

@mcp.tool()
def list_hooks(owner: str, repo: str) -> dict[str, Any]:
    """List webhooks for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of webhooks
    """
    return _request("GET", f"/repos/{owner}/{repo}/hooks")


@mcp.tool()
def get_hook(owner: str, repo: str, hook_id: int) -> dict[str, Any]:
    """Get a webhook by ID.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    
    Returns:
        Webhook information
    """
    return _request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


@mcp.tool()
def create_hook(
    owner: str,
    repo: str,
    name: str,
    config: dict,
    events: Optional[list[str]] = None,
    active: bool = True
) -> dict[str, Any]:
    """Create a new webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Hook name (web)
        config: Hook configuration
        events: List of events to trigger the hook
        active: Whether the hook is active
    
    Returns:
        Created webhook information
    """
    json_data = {
        "name": name,
        "config": config,
        "active": active
    }
    
    if events:
        json_data["events"] = events
    
    return _request("POST", f"/repos/{owner}/{repo}/hooks", json=json_data)


@mcp.tool()
def update_hook(
    owner: str,
    repo: str,
    hook_id: int,
    config: Optional[dict] = None,
    events: Optional[list[str]] = None,
    add_events: Optional[list[str]] = None,
    remove_events: Optional[list[str]] = None,
    active: Optional[bool] = None
) -> dict[str, Any]:
    """Update a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        config: New hook configuration
        events: New list of events
        add_events: Events to add
        remove_events: Events to remove
        active: New active status
    
    Returns:
        Updated webhook information
    """
    json_data = {}
    
    if config is not None:
        json_data["config"] = config
    if events is not None:
        json_data["events"] = events
    if add_events is not None:
        json_data["add_events"] = add_events
    if remove_events is not None:
        json_data["remove_events"] = remove_events
    if active is not None:
        json_data["active"] = active
    
    return _request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=json_data)


@mcp.tool()
def delete_hook(owner: str, repo: str, hook_id: int) -> dict[str, Any]:
    """Delete a webhook.
    
    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    
    Returns:
        Success status
    """
    return _request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


# =============================================================================
# Repository Info Operations
# =============================================================================

@mcp.tool()
def list_stargazers(owner: str, repo: str) -> dict[str, Any]:
    """List stargazers for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        List of stargazers
    """
    return _request("GET", f"/repos/{owner}/{repo}/stargazers")


@mcp.tool()
def list_forks(owner: str, repo: str, sort: Optional[str] = None) -> dict[str, Any]:
    """List forks for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sort: Sort by (newest, oldest, watchers)
    
    Returns:
        List of forks
    """
    params = {}
    if sort:
        params["sort"] = sort
    
    return _request("GET", f"/repos/{owner}/{repo}/forks", params=params)


@mcp.tool()
def create_fork(owner: str, repo: str, organization: Optional[str] = None) -> dict[str, Any]:
    """Create a fork of a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        organization: Organization to fork to
    
    Returns:
        Forked repository information
    """
    json_data = {}
    
    if organization:
        json_data["organization"] = organization
    
    return _request("POST", f"/repos/{owner}/{repo}/forks", json=json_data)


@mcp.tool()
def get_license(owner: str, repo: str) -> dict[str, Any]:
    """Get the license for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
    
    Returns:
        License information
    """
    return _request("GET", f"/repos/{owner}/{repo}/license")


# Run the server
if __name__ == "__main__":
    mcp.run()
