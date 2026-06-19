#!/usr/bin/env python3
"""
GitHub REST API MCP Server

An MCP server providing comprehensive coverage of the GitHub REST API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import json
import requests
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("github")

# Base URL for GitHub API
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")

# Headers for GitHub API requests
def get_headers() -> Dict[str, str]:
    """Get authentication headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def api_request(method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, 
                data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Make a GitHub API request.
    
    Args:
        method: HTTP method (GET, POST, PATCH, DELETE, PUT)
        endpoint: API endpoint path (e.g., "/repos/owner/repo/issues")
        params: Query parameters
        data: Request body for POST/PATCH/PUT
        
    Returns:
        API response as dictionary
    """
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    headers = get_headers()
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, params=params, json=data)
        elif method.upper() == "PATCH":
            response = requests.patch(url, headers=headers, params=params, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, params=params, json=data)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        # Handle successful response
        if 200 <= response.status_code < 300:
            if response.status_code == 204:
                return {"message": "Success - No content"}
            try:
                return response.json()
            except:
                return {"message": "Success", "status_code": response.status_code}
        
        # Handle error response
        error_msg = {
            "error": f"API request failed with status {response.status_code}",
            "status_code": response.status_code
        }
        try:
            error_data = response.json()
            if "message" in error_data:
                error_msg["message"] = error_data["message"]
        except:
            pass
        return error_msg
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ========== Repositories ==========

@mcp.tool()
def list_repositories(owner: str, type: str = "all", sort: str = "created", 
                      direction: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List repositories for an organization or user.
    
    Args:
        owner: The account owner (organization or username)
        type: Types of repositories to return. Can be one of: all, public, private, forks, sources, member
        sort: Property to sort results by. Can be one of: created, updated, pushed, full_name
        direction: Order to sort by. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of repositories
    """
    endpoint = f"/orgs/{owner}/repos" if owner and not "/" in owner else f"/user/repos"
    params = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_repository(owner: str, repo: str) -> Dict[str, Any]:
    """
    Get a repository by owner and name.
    
    Args:
        owner: Repository owner
        repo: Repository name
        
    Returns:
        Repository information
    """
    endpoint = f"/repos/{owner}/{repo}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_repository(name: str, description: Optional[str] = None, homepage: Optional[str] = None,
                      private: bool = False, visibility: str = "public",
                      has_issues: bool = True, has_projects: bool = True, 
                      has_wiki: bool = True, has_downloads: bool = True,
                      is_template: bool = False, auto_init: bool = False,
                      gitignore_template: Optional[str] = None,
                      license_template: Optional[str] = None,
                      allow_squash_merge: bool = True,
                      allow_merge_commit: bool = True,
                      allow_rebase_merge: bool = True,
                      allow_auto_merge: bool = False,
                      delete_branch_on_merge: bool = False) -> Dict[str, Any]:
    """
    Create a new repository.
    
    Args:
        name: Repository name (required)
        description: Short description
        homepage: URL with more information
        private: Whether the repository is private
        visibility: Repository visibility (public or private)
        has_issues: Enable issues
        has_projects: Enable projects
        has_wiki: Enable wiki
        has_downloads: Enable downloads
        is_template: Make this repo available as a template
        auto_init: Create initial commit with README
        gitignore_template: Language or platform gitignore template
        license_template: Open source license template
        allow_squash_merge: Allow squash-merging
        allow_merge_commit: Allow merge commits
        allow_rebase_merge: Allow rebase-merging
        allow_auto_merge: Allow auto-merge
        delete_branch_on_merge: Automatically delete head branches on merge
        
    Returns:
        Created repository information
    """
    data = {"name": name}
    if description:
        data["description"] = description
    if homepage:
        data["homepage"] = homepage
    data["private"] = private
    data["visibility"] = visibility
    data["has_issues"] = has_issues
    data["has_projects"] = has_projects
    data["has_wiki"] = has_wiki
    data["has_downloads"] = has_downloads
    data["is_template"] = is_template
    data["auto_init"] = auto_init
    if gitignore_template:
        data["gitignore_template"] = gitignore_template
    if license_template:
        data["license_template"] = license_template
    data["allow_squash_merge"] = allow_squash_merge
    data["allow_merge_commit"] = allow_merge_commit
    data["allow_rebase_merge"] = allow_rebase_merge
    data["allow_auto_merge"] = allow_auto_merge
    data["delete_branch_on_merge"] = delete_branch_on_merge
    
    endpoint = "/user/repos"
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def update_repository(owner: str, repo: str, name: Optional[str] = None,
                      description: Optional[str] = None, homepage: Optional[str] = None,
                      private: Optional[bool] = None,
                      has_issues: Optional[bool] = None,
                      has_projects: Optional[bool] = None,
                      has_wiki: Optional[bool] = None,
                      has_downloads: Optional[bool] = None,
                      is_template: Optional[bool] = None,
                      allow_squash_merge: Optional[bool] = None,
                      allow_merge_commit: Optional[bool] = None,
                      allow_rebase_merge: Optional[bool] = None,
                      allow_auto_merge: Optional[bool] = None,
                      delete_branch_on_merge: Optional[bool] = None,
                      default_branch: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: New repository name
        description: New description
        homepage: New homepage URL
        private: Whether the repository is private
        has_issues: Enable/disable issues
        has_projects: Enable/disable projects
        has_wiki: Enable/disable wiki
        has_downloads: Enable/disable downloads
        is_template: Enable/disable as template
        allow_squash_merge: Allow squash-merging
        allow_merge_commit: Allow merge commits
        allow_rebase_merge: Allow rebase-merging
        allow_auto_merge: Allow auto-merge
        delete_branch_on_merge: Automatically delete head branches on merge
        default_branch: Default branch name
        
    Returns:
        Updated repository information
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if homepage:
        data["homepage"] = homepage
    if private is not None:
        data["private"] = private
    if has_issues is not None:
        data["has_issues"] = has_issues
    if has_projects is not None:
        data["has_projects"] = has_projects
    if has_wiki is not None:
        data["has_wiki"] = has_wiki
    if has_downloads is not None:
        data["has_downloads"] = has_downloads
    if is_template is not None:
        data["is_template"] = is_template
    if allow_squash_merge is not None:
        data["allow_squash_merge"] = allow_squash_merge
    if allow_merge_commit is not None:
        data["allow_merge_commit"] = allow_merge_commit
    if allow_rebase_merge is not None:
        data["allow_rebase_merge"] = allow_rebase_merge
    if allow_auto_merge is not None:
        data["allow_auto_merge"] = allow_auto_merge
    if delete_branch_on_merge is not None:
        data["delete_branch_on_merge"] = delete_branch_on_merge
    if default_branch:
        data["default_branch"] = default_branch
    
    endpoint = f"/repos/{owner}/{repo}"
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def delete_repository(owner: str, repo: str) -> Dict[str, Any]:
    """
    Delete a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}"
    return api_request("DELETE", endpoint)

@mcp.tool()
def list_forks(owner: str, repo: str, sort: str = "newest", 
               per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List forks of a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sort: Sort order. Can be one of: newest, oldest, stargazers, watchers
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of forks
    """
    endpoint = f"/repos/{owner}/{repo}/forks"
    params = {
        "sort": sort,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def create_fork(owner: str, repo: str, organization: Optional[str] = None,
                name: Optional[str] = None, default_branch_only: bool = False) -> Dict[str, Any]:
    """
    Create a fork of a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        organization: Organization name if forking into an organization
        name: New name for the fork
        default_branch_only: Fork with only the default branch
        
    Returns:
        Fork creation status
    """
    endpoint = f"/repos/{owner}/{repo}/forks"
    data = {"default_branch_only": default_branch_only}
    if organization:
        data["organization"] = organization
    if name:
        data["name"] = name
    return api_request("POST", endpoint, data=data)

# ========== Branches ==========

@mcp.tool()
def list_branches(owner: str, repo: str, protected: Optional[bool] = None,
                  per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List branches for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        protected: Filter by protected status
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of branches
    """
    endpoint = f"/repos/{owner}/{repo}/branches"
    params = {
        "per_page": per_page,
        "page": page
    }
    if protected is not None:
        params["protected"] = protected
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """
    Get a branch by name.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        
    Returns:
        Branch information
    """
    endpoint = f"/repos/{owner}/{repo}/branches/{branch}"
    return api_request("GET", endpoint)

@mcp.tool()
def rename_branch(owner: str, repo: str, branch: str, new_name: str) -> Dict[str, Any]:
    """
    Rename a branch.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Current branch name
        new_name: New branch name
        
    Returns:
        Renamed branch information
    """
    endpoint = f"/repos/{owner}/{repo}/branches/{branch}/rename"
    data = {"new_name": new_name}
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def merge_branch(owner: str, repo: str, base: str, head: str, 
                 commit_message: Optional[str] = None) -> Dict[str, Any]:
    """
    Merge a branch into another branch.
    
    Args:
        owner: Repository owner
        repo: Repository name
        base: The base branch to merge into
        head: The branch to merge from
        commit_message: Optional commit message
        
    Returns:
        Merge result
    """
    endpoint = f"/repos/{owner}/{repo}/merges"
    data = {"base": base, "head": head}
    if commit_message:
        data["commit_message"] = commit_message
    return api_request("POST", endpoint, data=data)

# ========== Commits ==========

@mcp.tool()
def list_commits(owner: str, repo: str, sha: Optional[str] = None,
                 path: Optional[str] = None, author: Optional[str] = None,
                 committer: Optional[str] = None, since: Optional[str] = None,
                 until: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List commits in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: SHA or branch to start listing from
        path: Filter by file path
        author: Filter by author
        committer: Filter by committer
        since: Only show results after this time (ISO 8601)
        until: Only show results before this time (ISO 8601)
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of commits
    """
    endpoint = f"/repos/{owner}/{repo}/commits"
    params = {
        "per_page": per_page,
        "page": page
    }
    if sha:
        params["sha"] = sha
    if path:
        params["path"] = path
    if author:
        params["author"] = author
    if committer:
        params["committer"] = committer
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_commit(owner: str, repo: str, sha: str) -> Dict[str, Any]:
    """
    Get a specific commit by SHA.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
        
    Returns:
        Commit information
    """
    endpoint = f"/repos/{owner}/{repo}/commits/{sha}"
    return api_request("GET", endpoint)

@mcp.tool()
def list_pull_requests_for_commit(owner: str, repo: str, sha: str,
                                   per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List pull requests associated with a commit.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of pull requests
    """
    endpoint = f"/repos/{owner}/{repo}/commits/{sha}/pulls"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

# ========== Issues ==========

@mcp.tool()
def list_issues(owner: Optional[str] = None, repo: Optional[str] = None,
                filter: str = "assigned", state: str = "open", labels: Optional[str] = None,
                sort: str = "created", direction: str = "desc", 
                since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List issues assigned to the authenticated user or in a repository.
    
    Args:
        owner: Repository owner (optional, if not provided lists user's issues)
        repo: Repository name
        filter: Filter by type. Can be one of: assigned, created, mentioned, subscribed, repos, all
        state: Filter by state. Can be one of: open, closed, all
        labels: Filter by labels (comma-separated)
        sort: Sort by. Can be one of: created, updated, comments
        direction: Sort direction. Can be one of: asc, desc
        since: Only show results after this time (ISO 8601)
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of issues
    """
    if owner and repo:
        endpoint = f"/repos/{owner}/{repo}/issues"
    else:
        endpoint = "/issues"
    
    params = {
        "filter": filter,
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if labels:
        params["labels"] = labels
    if since:
        params["since"] = since
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """
    Get an issue by number.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        
    Returns:
        Issue information
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None,
                 assignees: Optional[List[str]] = None, 
                 labels: Optional[List[str]] = None,
                 milestone: Optional[int] = None) -> Dict[str, Any]:
    """
    Create a new issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Issue title
        body: Issue body
        assignees: List of logins to assign
        labels: List of label names
        milestone: Milestone number
        
    Returns:
        Created issue information
    """
    endpoint = f"/repos/{owner}/{repo}/issues"
    data = {"title": title}
    if body:
        data["body"] = body
    if assignees:
        data["assignees"] = assignees
    if labels:
        data["labels"] = labels
    if milestone:
        data["milestone"] = milestone
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, 
                 title: Optional[str] = None, body: Optional[str] = None,
                 state: Optional[str] = None,
                 assignees: Optional[List[str]] = None,
                 labels: Optional[List[str]] = None,
                 milestone: Optional[int] = None) -> Dict[str, Any]:
    """
    Update an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        title: New title
        body: New body
        state: New state (open or closed)
        assignees: New assignees list
        labels: New labels list
        milestone: New milestone number
        
    Returns:
        Updated issue information
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}"
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if assignees is not None:
        data["assignees"] = assignees
    if labels is not None:
        data["labels"] = labels
    if milestone is not None:
        data["milestone"] = milestone
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def delete_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """
    Delete an issue (requires admin permissions).
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}"
    return api_request("DELETE", endpoint)

# ========== Issue Comments ==========

@mcp.tool()
def list_issue_comments(owner: str, repo: str, sort: str = "created",
                        direction: str = "asc", since: Optional[str] = None,
                        per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List issue comments for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        sort: Sort by. Can be one of: created, updated
        direction: Sort direction. Can be one of: asc, desc
        since: Only show results after this time (ISO 8601)
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of issue comments
    """
    endpoint = f"/repos/{owner}/{repo}/issues/comments"
    params = {
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if since:
        params["since"] = since
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """
    Get a specific issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        
    Returns:
        Issue comment information
    """
    endpoint = f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, 
                         body: str) -> Dict[str, Any]:
    """
    Create a new issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        body: Comment body
        
    Returns:
        Created comment information
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/comments"
    data = {"body": body}
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def update_issue_comment(owner: str, repo: str, comment_id: int, 
                         body: str) -> Dict[str, Any]:
    """
    Update an issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        body: New comment body
        
    Returns:
        Updated comment information
    """
    endpoint = f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    data = {"body": body}
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """
    Delete an issue comment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    return api_request("DELETE", endpoint)

# ========== Issue Labels ==========

@mcp.tool()
def list_labels_for_issue(owner: str, repo: str, issue_number: int,
                           per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List labels for an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of labels
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def add_labels_to_issue(owner: str, repo: str, issue_number: int,
                         labels: List[str]) -> Dict[str, Any]:
    """
    Add labels to an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: List of label names to add
        
    Returns:
        Updated labels list
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def set_labels_for_issue(owner: str, repo: str, issue_number: int,
                          labels: List[str]) -> Dict[str, Any]:
    """
    Set labels for an issue (replaces existing labels).
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: New list of label names
        
    Returns:
        Updated labels list
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    return api_request("PUT", endpoint, data=data)

@mcp.tool()
def remove_all_labels_from_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """
    Remove all labels from an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    return api_request("DELETE", endpoint)

@mcp.tool()
def remove_label_from_issue(owner: str, repo: str, issue_number: int,
                            label_name: str) -> Dict[str, Any]:
    """
    Remove a specific label from an issue.
    
    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        label_name: Label name to remove
        
    Returns:
        Remaining labels
    """
    endpoint = f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label_name}"
    return api_request("DELETE", endpoint)

# ========== Pull Requests ==========

@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open",
                       head: Optional[str] = None, base: Optional[str] = None,
                       sort: str = "created", direction: str = "desc",
                       per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List pull requests in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state. Can be one of: open, closed, all
        head: Filter by head user or head organization and branch
        base: Filter by base branch
        sort: Sort by. Can be one of: created, updated, popularity, long-running
        direction: Sort direction. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of pull requests
    """
    endpoint = f"/repos/{owner}/{repo}/pulls"
    params = {
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if head:
        params["head"] = head
    if base:
        params["base"] = base
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
    """
    Get a pull request by number.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        
    Returns:
        Pull request information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str,
                        body: Optional[str] = None, 
                        maintainer_can_modify: bool = True,
                        draft: bool = False) -> Dict[str, Any]:
    """
    Create a new pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        title: Pull request title
        head: The name of the branch where your changes are implemented
        base: The name of the branch you want the changes pulled into
        body: Pull request body
        maintainer_can_modify: Whether maintainers can modify the PR
        draft: Whether to create a draft PR
        
    Returns:
        Created pull request information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls"
    data = {
        "title": title,
        "head": head,
        "base": base,
        "maintainer_can_modify": maintainer_can_modify,
        "draft": draft
    }
    if body:
        data["body"] = body
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def update_pull_request(owner: str, repo: str, pull_number: int,
                        title: Optional[str] = None, 
                        body: Optional[str] = None,
                        state: Optional[str] = None,
                        base: Optional[str] = None,
                        maintainer_can_modify: Optional[bool] = None) -> Dict[str, Any]:
    """
    Update a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        title: New title
        body: New body
        state: New state (open or closed)
        base: New base branch
        maintainer_can_modify: Whether maintainers can modify
        
    Returns:
        Updated pull request information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}"
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if base:
        data["base"] = base
    if maintainer_can_modify is not None:
        data["maintainer_can_modify"] = maintainer_can_modify
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int,
                       commit_title: Optional[str] = None,
                       commit_message: Optional[str] = None,
                       merge_method: str = "merge") -> Dict[str, Any]:
    """
    Merge a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        commit_title: Title for the merge commit
        commit_message: Message for the merge commit
        merge_method: Merge method. Can be one of: merge, squash, rebase
        
    Returns:
        Merge result
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    data = {"merge_method": merge_method}
    if commit_title:
        data["commit_title"] = commit_title
    if commit_message:
        data["commit_message"] = commit_message
    return api_request("PUT", endpoint, data=data)

# ========== Pull Request Reviews ==========

@mcp.tool()
def list_pull_request_reviews(owner: str, repo: str, pull_number: int,
                               per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List reviews for a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of reviews
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_pull_request_review(owner: str, repo: str, pull_number: int,
                             review_id: int) -> Dict[str, Any]:
    """
    Get a specific pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        
    Returns:
        Review information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_pull_request_review(owner: str, repo: str, pull_number: int,
                                body: Optional[str] = None,
                                event: str = "COMMENT",
                                comments: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Create a review for a pull request.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        body: Review body
        event: Review event. Can be one of: APPROVE, REQUEST_CHANGES, COMMENT
        comments: List of line comments
        
    Returns:
        Created review information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
    data = {"event": event}
    if body:
        data["body"] = body
    if comments:
        data["comments"] = comments
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def update_pull_request_review(owner: str, repo: str, pull_number: int,
                                review_id: int, body: str) -> Dict[str, Any]:
    """
    Update a pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        body: New review body
        
    Returns:
        Updated review information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
    data = {"body": body}
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def delete_pull_request_review(owner: str, repo: str, pull_number: int,
                                review_id: int) -> Dict[str, Any]:
    """
    Delete a pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"
    return api_request("DELETE", endpoint)

@mcp.tool()
def dismiss_pull_request_review(owner: str, repo: str, pull_number: int,
                                 review_id: int, message: str) -> Dict[str, Any]:
    """
    Dismiss a pull request review.
    
    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        message: Dismissal message
        
    Returns:
        Dismissed review information
    """
    endpoint = f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals"
    data = {"message": message}
    return api_request("PUT", endpoint, data=data)

# ========== Actions: Workflows ==========

@mcp.tool()
def list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List workflows in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of workflows
    """
    endpoint = f"/repos/{owner}/{repo}/actions/workflows"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id: int) -> Dict[str, Any]:
    """
    Get a specific workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
        
    Returns:
        Workflow information
    """
    endpoint = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def disable_workflow(owner: str, repo: str, workflow_id: int) -> Dict[str, Any]:
    """
    Disable a workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
        
    Returns:
        Disable status
    """
    endpoint = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable"
    return api_request("PUT", endpoint)

@mcp.tool()
def enable_workflow(owner: str, repo: str, workflow_id: int) -> Dict[str, Any]:
    """
    Enable a workflow.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
        
    Returns:
        Enable status
    """
    endpoint = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"
    return api_request("PUT", endpoint)

@mcp.tool()
def create_workflow_dispatch(owner: str, repo: str, workflow_id: int,
                              ref: str, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create a workflow dispatch event to trigger a workflow run.
    
    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID
        ref: Git reference (branch or tag)
        inputs: Input keys and values for the workflow
        
    Returns:
        Workflow run information
    """
    endpoint = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
    data = {"ref": ref}
    if inputs:
        data["inputs"] = inputs
    return api_request("POST", endpoint, data=data)

# ========== Actions: Secrets ==========

@mcp.tool()
def list_repository_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List secrets for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of repository secrets
    """
    endpoint = f"/repos/{owner}/{repo}/actions/secrets"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_repository_secret(owner: str, repo: str, secret_name: str) -> Dict[str, Any]:
    """
    Get a repository secret.
    
    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
        
    Returns:
        Secret information
    """
    endpoint = f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_or_update_repository_secret(owner: str, repo: str, secret_name: str,
                                        encrypted_value: str, key_id: str) -> Dict[str, Any]:
    """
    Create or update a repository secret.
    
    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
        encrypted_value: Encrypted secret value (using LibSodium)
        key_id: ID of the key used to encrypt the secret
        
    Returns:
        Secret creation/update status
    """
    endpoint = f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
    data = {
        "encrypted_value": encrypted_value,
        "key_id": key_id
    }
    return api_request("PUT", endpoint, data=data)

@mcp.tool()
def delete_repository_secret(owner: str, repo: str, secret_name: str) -> Dict[str, Any]:
    """
    Delete a repository secret.
    
    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/actions/secrets/{secret_name}"
    return api_request("DELETE", endpoint)

# ========== Actions: Artifacts ==========

@mcp.tool()
def list_artifacts(owner: str, repo: str, name: Optional[str] = None,
                   per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List artifacts for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        name: Filter by artifact name
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of artifacts
    """
    endpoint = f"/repos/{owner}/{repo}/actions/artifacts"
    params = {
        "per_page": per_page,
        "page": page
    }
    if name:
        params["name"] = name
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_artifact(owner: str, repo: str, artifact_id: int) -> Dict[str, Any]:
    """
    Get a specific artifact.
    
    Args:
        owner: Repository owner
        repo: Repository name
        artifact_id: Artifact ID
        
    Returns:
        Artifact information
    """
    endpoint = f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def download_artifact(owner: str, repo: str, artifact_id: int) -> Dict[str, Any]:
    """
    Download an artifact.
    
    Args:
        owner: Repository owner
        repo: Repository name
        artifact_id: Artifact ID
        
    Returns:
        Download URL
    """
    endpoint = f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip"
    return api_request("GET", endpoint)

# ========== Deployments ==========

@mcp.tool()
def list_deployments(owner: str, repo: str, ref: Optional[str] = None,
                     task: Optional[str] = None, environment: Optional[str] = None,
                     per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List deployments for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        ref: Filter by ref (branch, tag, or commit)
        task: Filter by task (deploy, deploy:preview, deploy:stop, deploy:refresh)
        environment: Filter by environment
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of deployments
    """
    endpoint = f"/repos/{owner}/{repo}/deployments"
    params = {
        "per_page": per_page,
        "page": page
    }
    if ref:
        params["ref"] = ref
    if task:
        params["task"] = task
    if environment:
        params["environment"] = environment
    return api_request("GET", endpoint, params)

@mcp.tool()
def create_deployment(owner: str, repo: str, ref: str, 
                      environment: str = "production",
                      description: Optional[str] = None,
                      transient_environment: bool = False,
                      production_environment: bool = True,
                      auto_merge: bool = True,
                      required_contexts: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Create a deployment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        ref: The reference to deploy (branch, tag, or commit)
        environment: Target environment name
        description: Deployment description
        transient_environment: Whether this is a transient environment
        production_environment: Whether this is a production environment
        auto_merge: Whether to automatically merge the default branch
        required_contexts: Status contexts to validate against
        
    Returns:
        Created deployment information
    """
    endpoint = f"/repos/{owner}/{repo}/deployments"
    data = {
        "ref": ref,
        "environment": environment,
        "auto_merge": auto_merge,
        "required_contexts": required_contexts or [],
        "transient_environment": transient_environment,
        "production_environment": production_environment
    }
    if description:
        data["description"] = description
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def get_deployment(owner: str, repo: str, deployment_id: int) -> Dict[str, Any]:
    """
    Get a specific deployment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
        
    Returns:
        Deployment information
    """
    endpoint = f"/repos/{owner}/{repo}/deployments/{deployment_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_deployment_status(owner: str, repo: str, deployment_id: int,
                              state: str, environment_url: Optional[str] = None,
                              log_url: Optional[str] = None,
                              description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a deployment status.
    
    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
        state: State of the deployment. Can be one of: pending, active, inactive, error, failure
        environment_url: URL for the deployed environment
        log_url: URL for deployment logs
        description: Status description
        
    Returns:
        Created deployment status
    """
    endpoint = f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
    data = {"state": state}
    if environment_url:
        data["environment_url"] = environment_url
    if log_url:
        data["log_url"] = log_url
    if description:
        data["description"] = description
    return api_request("POST", endpoint, data=data)

# ========== Deployments: Environments ==========

@mcp.tool()
def list_environments(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List environments for a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of environments
    """
    endpoint = f"/repos/{owner}/{repo}/environments"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_environment(owner: str, repo: str, environment_name: str) -> Dict[str, Any]:
    """
    Get a specific environment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
        
    Returns:
        Environment information
    """
    endpoint = f"/repos/{owner}/{repo}/environments/{environment_name}"
    return api_request("GET", endpoint)

@mcp.tool()
def create_or_update_environment(owner: str, repo: str, environment_name: str,
                                  wait_timer: Optional[int] = None,
                                  prevent_self_review: bool = False,
                                  reviewers: Optional[List[Dict[str, Any]]] = None,
                                  deployment_branch_policy: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create or update an environment with protection rules.
    
    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
        wait_timer: Wait timer in minutes (0-43200)
        prevent_self_review: Prevent self-review
        reviewers: List of reviewers (users or teams)
        deployment_branch_policy: Branch policy configuration
        
    Returns:
        Environment information
    """
    endpoint = f"/repos/{owner}/{repo}/environments/{environment_name}"
    data = {}
    if wait_timer is not None:
        data["wait_timer"] = wait_timer
    data["prevent_self_review"] = prevent_self_review
    if reviewers is not None:
        data["reviewers"] = reviewers
    if deployment_branch_policy is not None:
        data["deployment_branch_policy"] = deployment_branch_policy
    return api_request("PUT", endpoint, data=data)

@mcp.tool()
def delete_environment(owner: str, repo: str, environment_name: str) -> Dict[str, Any]:
    """
    Delete an environment.
    
    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
        
    Returns:
        Deletion status
    """
    endpoint = f"/repos/{owner}/{repo}/environments/{environment_name}"
    return api_request("DELETE", endpoint)

# ========== Repository Contents ==========

@mcp.tool()
def get_repository_content(owner: str, repo: str, path: str = "",
                           ref: Optional[str] = None) -> Dict[str, Any]:
    """
    Get repository contents at a path.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: Path to the content
        ref: Reference to get content from (branch, tag, commit)
        
    Returns:
        Content information
    """
    endpoint = f"/repos/{owner}/{repo}/contents/{path}"
    params = {}
    if ref:
        params["ref"] = ref
    return api_request("GET", endpoint, params)

@mcp.tool()
def create_or_update_file(owner: str, repo: str, path: str, message: str,
                          content: str, branch: Optional[str] = None,
                          committer_name: Optional[str] = None,
                          committer_email: Optional[str] = None,
                          author_name: Optional[str] = None,
                          author_email: Optional[str] = None) -> Dict[str, Any]:
    """
    Create or update a file in a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: Path to the file
        message: Commit message
        content: File content (base64 encoded)
        branch: Branch name
        committer_name: Committer name
        committer_email: Committer email
        author_name: Author name
        author_email: Author email
        
    Returns:
        File and commit information
    """
    endpoint = f"/repos/{owner}/{repo}/contents/{path}"
    data = {
        "message": message,
        "content": content
    }
    if branch:
        data["branch"] = branch
    if committer_name and committer_email:
        data["committer"] = {
            "name": committer_name,
            "email": committer_email
        }
    if author_name and author_email:
        data["author"] = {
            "name": author_name,
            "email": author_email
        }
    return api_request("PUT", endpoint, data=data)

@mcp.tool()
def delete_file(owner: str, repo: str, path: str, message: str, sha: str,
                branch: Optional[str] = None,
                committer_name: Optional[str] = None,
                committer_email: Optional[str] = None,
                author_name: Optional[str] = None,
                author_email: Optional[str] = None) -> Dict[str, Any]:
    """
    Delete a file from a repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        path: Path to the file
        message: Commit message
        sha: Blob SHA of the file
        branch: Branch name
        committer_name: Committer name
        committer_email: Committer email
        author_name: Author name
        author_email: Author email
        
    Returns:
        File and commit information
    """
    endpoint = f"/repos/{owner}/{repo}/contents/{path}"
    data = {
        "message": message,
        "sha": sha
    }
    if branch:
        data["branch"] = branch
    if committer_name and committer_email:
        data["committer"] = {
            "name": committer_name,
            "email": committer_email
        }
    if author_name and author_email:
        data["author"] = {
            "name": author_name,
            "email": author_email
        }
    return api_request("DELETE", endpoint, data=data)

# ========== Search ==========

@mcp.tool()
def search_issues_and_pull_requests(query: str, sort: Optional[str] = None,
                                    order: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    Search issues and pull requests.
    
    Args:
        query: Search query
        sort: Sort by. Can be one of: comments, reactions, created, updated
        order: Sort order. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        Search results
    """
    endpoint = "/search/issues"
    params = {
        "q": query,
        "sort": sort or "created",
        "order": order,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def search_repositories(query: str, sort: Optional[str] = None,
                        order: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    Search repositories.
    
    Args:
        query: Search query
        sort: Sort by. Can be one of: stars, forks, help-wanted-issues, updated
        order: Sort order. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        Search results
    """
    endpoint = "/search/repositories"
    params = {
        "q": query,
        "sort": sort or "stars",
        "order": order,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def search_users(query: str, sort: str = "followers", order: str = "desc",
                 per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    Search users.
    
    Args:
        query: Search query
        sort: Sort by. Can be one of: followers, repositories, joined
        order: Sort order. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        Search results
    """
    endpoint = "/search/users"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

# ========== Users ==========

@mcp.tool()
def get_authenticated_user() -> Dict[str, Any]:
    """
    Get the authenticated user.
    
    Returns:
        User information
    """
    endpoint = "/user"
    return api_request("GET", endpoint)

@mcp.tool()
def get_user(username: str) -> Dict[str, Any]:
    """
    Get a user by username.
    
    Args:
        username: GitHub username
        
    Returns:
        User information
    """
    endpoint = f"/users/{username}"
    return api_request("GET", endpoint)

@mcp.tool()
def list_user_repositories(username: str, type: str = "owner", sort: str = "created",
                           direction: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List repositories for a user.
    
    Args:
        username: GitHub username
        type: Types of repositories. Can be one of: all, owner, member
        sort: Sort by. Can be one of: created, updated, pushed, full_name
        direction: Sort direction. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of repositories
    """
    endpoint = f"/users/{username}/repos"
    params = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

# ========== Gists ==========

@mcp.tool()
def list_gists(per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List gists for the authenticated user.
    
    Args:
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of gists
    """
    endpoint = "/gists"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def list_public_gists(per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List public gists.
    
    Args:
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of public gists
    """
    endpoint = "/gists/public"
    params = {
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def create_gist(description: str, files: Dict[str, Dict[str, str]],
                public: bool = False) -> Dict[str, Any]:
    """
    Create a new gist.
    
    Args:
        description: Gist description
        files: Files to include in the gist
        public: Whether the gist is public
        
    Returns:
        Created gist information
    """
    endpoint = "/gists"
    data = {
        "description": description,
        "files": files,
        "public": public
    }
    return api_request("POST", endpoint, data=data)

@mcp.tool()
def get_gist(gist_id: str) -> Dict[str, Any]:
    """
    Get a gist by ID.
    
    Args:
        gist_id: Gist ID
        
    Returns:
        Gist information
    """
    endpoint = f"/gists/{gist_id}"
    return api_request("GET", endpoint)

@mcp.tool()
def update_gist(gist_id: str, description: Optional[str] = None,
                files: Optional[Dict[str, Dict[str, str]]] = None) -> Dict[str, Any]:
    """
    Update a gist.
    
    Args:
        gist_id: Gist ID
        description: New description
        files: New files
        
    Returns:
        Updated gist information
    """
    endpoint = f"/gists/{gist_id}"
    data = {}
    if description:
        data["description"] = description
    if files:
        data["files"] = files
    return api_request("PATCH", endpoint, data=data)

@mcp.tool()
def delete_gist(gist_id: str) -> Dict[str, Any]:
    """
    Delete a gist.
    
    Args:
        gist_id: Gist ID
        
    Returns:
        Deletion status
    """
    endpoint = f"/gists/{gist_id}"
    return api_request("DELETE", endpoint)

# ========== Organization ==========

@mcp.tool()
def list_organization_repositories(org: str, type: str = "all", sort: str = "created",
                                   direction: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """
    List repositories for an organization.
    
    Args:
        org: Organization name
        type: Types of repositories. Can be one of: all, public, private, forks, sources, member
        sort: Sort by. Can be one of: created, updated, pushed, full_name
        direction: Sort direction. Can be one of: asc, desc
        per_page: Results per page (max 100)
        page: Page number
        
    Returns:
        List of organization repositories
    """
    endpoint = f"/orgs/{org}/repos"
    params = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    return api_request("GET", endpoint, params)

@mcp.tool()
def get_organization(org: str) -> Dict[str, Any]:
    """
    Get an organization by name.
    
    Args:
        org: Organization name
        
    Returns:
        Organization information
    """
    endpoint = f"/orgs/{org}"
    return api_request("GET", endpoint)

@mcp.tool()
def update_organization(org: str, billing_email: Optional[str] = None,
                        company: Optional[str] = None, email: Optional[str] = None,
                        location: Optional[str] = None, name: Optional[str] = None,
                        description: Optional[str] = None, has_organization_projects: Optional[bool] = None,
                        has_repository_projects: Optional[bool] = None,
                        default_repository_permission: Optional[str] = None,
                        members_can_create_repositories: Optional[bool] = None,
                        members_can_create_public_repositories: Optional[bool] = None,
                        members_can_create_private_repositories: Optional[bool] = None,
                        members_can_create_internal_repositories: Optional[bool] = None) -> Dict[str, Any]:
    """
    Update an organization.
    
    Args:
        org: Organization name
        billing_email: Billing email
        company: Company name
        email: Public email
        location: Location
        name: Organization name
        description: Organization description
        has_organization_projects: Enable organization projects
        has_repository_projects: Enable repository projects
        default_repository_permission: Default permission for repositories
        members_can_create_repositories: Allow members to create repositories
        members_can_create_public_repositories: Allow members to create public repositories
        members_can_create_private_repositories: Allow members to create private repositories
        members_can_create_internal_repositories: Allow members to create internal repositories
        
    Returns:
        Updated organization information
    """
    endpoint = f"/orgs/{org}"
    data = {}
    if billing_email:
        data["billing_email"] = billing_email
    if company:
        data["company"] = company
    if email:
        data["email"] = email
    if location:
        data["location"] = location
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if has_organization_projects is not None:
        data["has_organization_projects"] = has_organization_projects
    if has_repository_projects is not None:
        data["has_repository_projects"] = has_repository_projects
    if default_repository_permission:
        data["default_repository_permission"] = default_repository_permission
    if members_can_create_repositories is not None:
        data["members_can_create_repositories"] = members_can_create_repositories
    if members_can_create_public_repositories is not None:
        data["members_can_create_public_repositories"] = members_can_create_public_repositories
    if members_can_create_private_repositories is not None:
        data["members_can_create_private_repositories"] = members_can_create_private_repositories
    if members_can_create_internal_repositories is not None:
        data["members_can_create_internal_repositories"] = members_can_create_internal_repositories
    return api_request("PATCH", endpoint, data=data)

# ========== Branch Protection ==========

@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """
    Get branch protection settings.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        
    Returns:
        Branch protection settings
    """
    endpoint = f"/repos/{owner}/{repo}/branches/{branch}/protection"
    return api_request("GET", endpoint)

@mcp.tool()
def update_branch_protection(owner: str, repo: str, branch: str,
                              required_status_checks: Optional[Dict[str, Any]] = None,
                              enforce_admins: Optional[bool] = None,
                              required_pull_request_reviews: Optional[Dict[str, Any]] = None,
                              required_linear_history: Optional[bool] = None,
                              allow_force_pushes: Optional[bool] = None,
                              allow_deletions: Optional[bool] = None,
                              restrictions: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Update branch protection settings.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        required_status_checks: Required status checks
        enforce_admins: Enforce restrictions for admins
        required_pull_request_reviews: Required pull request reviews
        required_linear_history: Require linear history
        allow_force_pushes: Allow force pushes
        allow_deletions: Allow deletions
        restrictions: Branch restrictions
        
    Returns:
        Updated branch protection settings
    """
    endpoint = f"/repos/{owner}/{repo}/branches/{branch}/protection"
    data = {}
    if required_status_checks is not None:
        data["required_status_checks"] = required_status_checks
    if enforce_admins is not None:
        data["enforce_admins"] = enforce_admins
    if required_pull_request_reviews is not None:
        data["required_pull_request_reviews"] = required_pull_request_reviews
    if required_linear_history is not None:
        data["required_linear_history"] = required_linear_history
    if allow_force_pushes is not None:
        data["allow_force_pushes"] = allow_force_pushes
    if allow_deletions is not None:
        data["allow_deletions"] = allow_deletions
    if restrictions is not None:
        data["restrictions"] = restrictions
    return api_request("PUT", endpoint, data=data)

@mcp.tool()
def remove_branch_protection(owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """
    Remove branch protection settings.
    
    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        
    Returns:
        Removal status
    """
    endpoint = f"/repos/{owner}/{repo}/branches/{branch}/protection"
    return api_request("DELETE", endpoint)

if __name__ == "__main__":
    mcp.run()
