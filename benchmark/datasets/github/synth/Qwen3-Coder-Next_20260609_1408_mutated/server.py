#!/usr/bin/env python3
"""
GitHub MCP Server - An MCP server for GitHub REST API

This server provides tools to interact with GitHub's REST API, enabling
autonomous agents to perform GitHub operations.
"""

import os
import base64
from typing import Any
import requests
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("github")

# Base URL for GitHub API
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")


def get_auth_headers() -> dict:
    """Get authentication headers for GitHub API requests."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is required")
    
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }


def github_request(method: str, endpoint: str, params: dict = None, 
                   data: dict = None) -> dict:
    """Make a request to the GitHub API."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    headers = get_auth_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return {"error": error_data.get("message", f"API error: {response.status_code}")}
            except:
                return {"error": f"API error: {response.status_code}"}
        
        if response.status_code == 204:
            return {"success": True}
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Issues tools

@mcp.tool()
def list_issues_for_authenticated_user(
    filter: str = "assigned",
    state: str = "open",
    labels: str = "",
    sort: str = "created",
    direction: str = "desc",
    since: str = None,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List issues assigned to the authenticated user across all visible repositories.
    
    Args:
        filter: Which sorts of issues to return. Can be one of: assigned, created, mentioned, subscribed, repos, all
        state: Indicates the issue_state of the issues to return. Can be one of: open, closed, all
        labels: A list of comma separated label names
        sort: What to sort results by. Can be one of: created, updated, comments
        direction: The direction to sort the results by. Can be one of: asc, desc
        since: Only show results that were last updated after the given time (ISO 8601 timestamp)
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "filter": filter,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if since:
        params["since"] = since
    
    return github_request("GET", "/issues", params=params)


@mcp.tool()
def list_organization_issues(
    org: str,
    filter: str = "assigned",
    state: str = "open",
    labels: str = "",
    sort: str = "created",
    direction: str = "desc",
    since: str = None,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List issues in an organization assigned to the authenticated user.
    
    Args:
        org: The organization name
        filter: Which sorts of issues to return
        state: Indicates the issue_state of the issues to return
        labels: A list of comma separated label names
        sort: What to sort results by
        direction: The direction to sort the results by
        since: Only show results that were last updated after the given time
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "filter": filter,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if since:
        params["since"] = since
    
    return github_request("GET", f"/orgs/{org}/issues", params=params)


@mcp.tool()
def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: str = None,
    assignees: list = None,
    milestone: int = None,
    labels: list = None
) -> dict:
    """
    Create a new issue in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        title: The title of the issue
        body: The body text of the issue in Markdown format
        assignees: Usernames of people to assign this issue to
        milestone: The number of the milestone to associate this issue with
        labels: Labels to associate with this issue
    """
    data = {
        "title": title,
    }
    
    if body:
        data["body"] = body
    if assignees:
        data["assignees"] = assignees
    if milestone:
        data["milestone"] = milestone
    if labels:
        data["labels"] = labels
    
    return github_request("POST", f"/repos/{owner}/{repo}/issues", data=data)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """
    Get an issue in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
    """
    return github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    title: str = None,
    body: str = None,
    state: str = None,
    assignees: list = None,
    milestone: int = None,
    labels: list = None
) -> dict:
    """
    Update an issue in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        title: The title of the issue
        body: The body text of the issue in Markdown format
        state: The state of the issue (open or closed)
        assignees: Usernames of people to assign this issue to
        milestone: The number of the milestone to associate this issue with
        labels: Labels to associate with this issue
    """
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if assignees:
        data["assignees"] = assignees
    if milestone:
        data["milestone"] = milestone
    if labels:
        data["labels"] = labels
    
    return github_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", data=data)


@mcp.tool()
def delete_issue(owner: str, repo: str, issue_number: int) -> dict:
    """
    Delete an issue in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}")


# Issue labels tools

@mcp.tool()
def list_labels_for_issue(owner: str, repo: str, issue_number: int) -> dict:
    """
    List all labels for an issue.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
    """
    return github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/label_filters")


@mcp.tool()
def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: list) -> dict:
    """
    Add labels to an issue.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        labels: The names of the labels to add to the issue
    """
    return github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/label_filters", data={"labels": labels})


@mcp.tool()
def set_labels_for_issue(owner: str, repo: str, issue_number: int, labels: list) -> dict:
    """
    Set labels for an issue (replaces existing labels).
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        labels: The names of the labels to set for the issue
    """
    return github_request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/label_filters", data={"labels": labels})


@mcp.tool()
def remove_label_from_issue(owner: str, repo: str, issue_number: int, label: str) -> dict:
    """
    Remove a label from an issue.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        label: The name of the label to remove
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/label_filters/{label}")


# Issue assignees tools

@mcp.tool()
def list_assignees(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """
    List the available assignees for issues in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {"per_page": per_page, "page": page}
    return github_request("GET", f"/repos/{owner}/{repo}/assignees", params=params)


@mcp.tool()
def check_if_user_can_be_assigned(owner: str, repo: str, assignee: str) -> dict:
    """
    Check if a user can be assigned to an issue in this repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        assignee: The username to check
    """
    return github_request("GET", f"/repos/{owner}/{repo}/assignees/{assignee}")


@mcp.tool()
def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
    """
    Add assignees to an issue.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        assignees: Usernames of people to assign this issue to
    """
    return github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", data={"assignees": assignees})


@mcp.tool()
def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
    """
    Remove assignees from an issue.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        issue_number: The number that identifies the issue
        assignees: Usernames of assignees to remove from an issue
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", data={"assignees": assignees})


# Issue comments tools

@mcp.tool()
def list_issue_comments_for_repository(
    owner: str,
    repo: str,
    sort: str = "created",
    direction: str = "asc",
    since: str = None,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List issue comments for a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        sort: The property to sort the results by
        direction: Either asc or desc
        since: Only show results that were last updated after the given time
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if since:
        params["since"] = since
    
    return github_request("GET", f"/repos/{owner}/{repo}/issues/comments", params=params)


@mcp.tool()
def get_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
    """
    Get an issue comment.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        comment_id: The unique identifier of the comment
    """
    return github_request("GET", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


@mcp.tool()
def update_issue_comment(
    owner: str,
    repo: str,
    comment_id: int,
    body: str
) -> dict:
    """
    Update an issue comment.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        comment_id: The unique identifier of the comment
        body: The contents of the comment
    """
    return github_request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", data={"body": body})


@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
    """
    Delete an issue comment.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        comment_id: The unique identifier of the comment
    """
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


# Pull request tools

@mcp.tool()
def list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open",
    head: str = None,
    base: str = None,
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List pull requests in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        state: Either open, closed, or all to filter by issue_state
        head: Filter pulls by head user or head organization and branch name
        base: Filter pulls by base branch name
        sort: What to sort results by
        direction: The direction of the sort
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
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
    
    return github_request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


@mcp.tool()
def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: str = None,
    draft: bool = False,
    maintainer_can_modify: bool = True
) -> dict:
    """
    Create a new pull request in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        title: The title of the pull request
        head: The name of the branch where your changes are implemented
        base: The name of the branch you want the changes pulled into
        body: The body text of the pull request in Markdown format
        draft: Set to True to create a draft pull request
        maintainer_can_modify: Indicates whether maintainers can modify the pull request
    """
    data = {
        "title": title,
        "head": head,
        "base": base,
        "draft": draft,
        "maintainer_can_modify": maintainer_can_modify
    }
    
    if body:
        data["body"] = body
    
    return github_request("POST", f"/repos/{owner}/{repo}/pulls", data=data)


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """
    Get a pull request in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        pull_number: The number that identifies the pull request
    """
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: str = None,
    body: str = None,
    state: str = None,
    base: str = None,
    maintainers_can_modify: bool = None
) -> dict:
    """
    Update a pull request in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        pull_number: The number that identifies the pull request
        title: The title of the pull request
        body: The body text of the pull request in Markdown format
        state: The state of the pull request (open or closed)
        base: The name of the branch you want the changes pulled into
        maintainers_can_modify: Indicates whether maintainers can modify the pull request
    """
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if base:
        data["base"] = base
    if maintainers_can_modify is not None:
        data["maintainers_can_modify"] = maintainers_can_modify
    
    return github_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", data=data)


# Pull request reviews tools

@mcp.tool()
def list_pull_request_reviews(
    owner: str,
    repo: str,
    pull_number: int,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List all reviews for a specified pull request.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        pull_number: The number that identifies the pull request
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {"per_page": per_page, "page": page}
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", params=params)


@mcp.tool()
def create_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    event: str,
    body: str = None,
    commit_id: str = None,
    comments: list = None
) -> dict:
    """
    Create a review on a specified pull request.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        pull_number: The number that identifies the pull request
        event: The review action (APPROVE, REQUEST_CHANGES, or COMMENT)
        body: The body text of the pull request review
        commit_id: The SHA of the commit that needs a review
        comments: Array of review comments with path, position, and body
    """
    data = {
        "event": event,
    }
    
    if body:
        data["body"] = body
    if commit_id:
        data["commit_id"] = commit_id
    if comments:
        data["comments"] = comments
    
    return github_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", data=data)


# Repositories tools

@mcp.tool()
def list_organization_repositories(
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List repositories for an organization.
    
    Args:
        org: The organization name
        type: Specifies the types of repositories you want returned
        sort: The property to sort the results by
        direction: The order to sort by
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    return github_request("GET", f"/orgs/{org}/repos", params=params)


@mcp.tool()
def create_organization_repository(
    org: str,
    name: str,
    description: str = None,
    homepage: str = None,
    private: bool = False,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    is_template: bool = False,
    team_id: int = None,
    auto_init: bool = False,
    gitignore_template: str = None,
    license_template: str = None,
    allow_squash_merge: bool = True,
    allow_merge_commit: bool = True,
    allow_rebase_merge: bool = True,
    allow_auto_merge: bool = False,
    delete_branch_on_merge: bool = False
) -> dict:
    """
    Create a new repository in an organization.
    
    Args:
        org: The organization name
        name: The name of the repository
        description: A short description of the repository
        homepage: A URL with more information about the repository
        private: Whether the repository is private
        has_issues: Either true to enable issues for this repository or false to disable them
        has_projects: Either true to enable projects for this repository or false to disable them
        has_wiki: Either true to enable the wiki for this repository or false to disable it
        is_template: Either true to make this repo available as a template repository or false to prevent it
        team_id: The id of the team that will be granted access to this repository
        auto_init: Pass true to create an initial commit with empty README
        gitignore_template: Desired language or platform.gitignore template
        license_template: Choose an open source license template
        allow_squash_merge: Either true to allow squash-merging pull requests or false to prevent squash-merging
        allow_merge_commit: Either true to allow merging pull requests with a merge commit or false to prevent merging pull requests with merge commits
        allow_rebase_merge: Either true to allow rebase-merging pull requests or false to prevent rebase-merging
        allow_auto_merge: Either true to allow auto-merge on pull requests or false to disallow auto-merge
        delete_branch_on_merge: Either true to allow automatically deleting head branches when pull requests are merged or false to prevent automatic deletion
    """
    data = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "is_template": is_template,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge
    }
    
    if description:
        data["description"] = description
    if homepage:
        data["homepage"] = homepage
    if team_id:
        data["team_id"] = team_id
    if auto_init:
        data["auto_init"] = auto_init
    if gitignore_template:
        data["gitignore_template"] = gitignore_template
    if license_template:
        data["license_template"] = license_template
    
    return github_request("POST", f"/orgs/{org}/repos", data=data)


@mcp.tool()
def get_repository(owner: str, repo: str) -> dict:
    """
    Get a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
    """
    return github_request("GET", f"/repos/{owner}/{repo}")


@mcp.tool()
def update_repository(
    owner: str,
    repo: str,
    name: str = None,
    description: str = None,
    homepage: str = None,
    private: bool = None,
    has_issues: bool = None,
    has_projects: bool = None,
    has_wiki: bool = None,
    is_template: bool = None,
    allow_squash_merge: bool = None,
    allow_merge_commit: bool = None,
    allow_rebase_merge: bool = None,
    allow_auto_merge: bool = None,
    delete_branch_on_merge: bool = None
) -> dict:
    """
    Update a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        name: The name of the repository
        description: A short description of the repository
        homepage: A URL with more information about the repository
        private: Whether the repository is private
        has_issues: Either true to enable issues for this repository or false to disable them
        has_projects: Either true to enable projects for this repository or false to disable them
        has_wiki: Either true to enable the wiki for this repository or false to disable it
        is_template: Either true to make this repo available as a template repository or false to prevent it
        allow_squash_merge: Either true to allow squash-merging pull requests or false to prevent squash-merging
        allow_merge_commit: Either true to allow merging pull requests with a merge commit or false to prevent merging pull requests with merge commits
        allow_rebase_merge: Either true to allow rebase-merging pull requests or false to prevent rebase-merging
        allow_auto_merge: Either true to allow auto-merge on pull requests or false to disallow auto-merge
        delete_branch_on_merge: Either true to allow automatically deleting head branches when pull requests are merged or false to prevent automatic deletion
    """
    data = {}
    if name is not None:
        data["name"] = name
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
    if has_wiki is not None:
        data["has_wiki"] = has_wiki
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
    
    return github_request("PATCH", f"/repos/{owner}/{repo}", data=data)


# Branches tools

@mcp.tool()
def list_branches(
    owner: str,
    repo: str,
    protected: bool = None,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List branches for a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        protected: Setting to true returns only branches protected by branch protections
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = protected
    
    return github_request("GET", f"/repos/{owner}/{repo}/branches", params=params)


@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> dict:
    """
    Get a branch in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        branch: The name of the branch
    """
    return github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


@mcp.tool()
def rename_branch(owner: str, repo: str, branch: str, new_name: str) -> dict:
    """
    Rename a branch in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        branch: The name of the branch
        new_name: The new name of the branch
    """
    return github_request("POST", f"/repos/{owner}/{repo}/branches/{branch}/rename", data={"new_name": new_name})


@mcp.tool()
def merge_branch(owner: str, repo: str, base: str, head: str) -> dict:
    """
    Merge a branch in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        base: The name of the branch you want the changes pulled into
        head: The name of the branch you want to merge
    """
    return github_request("POST", f"/repos/{owner}/{repo}/merges", data={"base": base, "head": head})


# Repository contents tools

@mcp.tool()
def get_repository_content(
    owner: str,
    repo: str,
    path: str = "",
    ref: str = None
) -> dict:
    """
    Get the contents of a file or directory in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        path: The content path
        ref: The name of the commit/branch/tag
    """
    params = {}
    if ref:
        params["ref"] = ref
    
    return github_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)


@mcp.tool()
def create_or_update_file_content(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content: str,
    sha: str = None,
    branch: str = None,
    committer_name: str = None,
    committer_email: str = None
) -> dict:
    """
    Create a new file or replace an existing file in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        path: The content path
        message: The commit message
        content: The new file content, using Base64 encoding
        sha: Required if you are updating a file. The blob SHA of the file being replaced
        branch: The branch name
        committer_name: The name of the committer
        committer_email: The email of the committer
    """
    # The content parameter is already Base64 encoded from the MCP client
    data = {
        "message": message,
        "content": content
    }
    
    if sha:
        data["sha"] = sha
    if branch:
        data["branch"] = branch
    if committer_name and committer_email:
        data["committer"] = {
            "name": committer_name,
            "email": committer_email
        }
    
    return github_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", data=data)


@mcp.tool()
def delete_file_content(
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: str = None,
    committer_name: str = None,
    committer_email: str = None
) -> dict:
    """
    Delete a file in a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        path: The content path
        message: The commit message
        sha: The blob SHA of the file being deleted
        branch: The branch name
        committer_name: The name of the committer
        committer_email: The email of the committer
    """
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
    
    return github_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", data=data)


# Releases tools

@mcp.tool()
def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """
    List releases for a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {"per_page": per_page, "page": page}
    return github_request("GET", f"/repos/{owner}/{repo}/releases", params=params)


@mcp.tool()
def create_release(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: str = None,
    name: str = None,
    body: str = None,
    draft: bool = False,
    prerelease: bool = False,
    discussion_category_name: str = None,
    generate_release_notes: bool = False
) -> dict:
    """
    Create a new release for a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        tag_name: The name of the tag
        target_commitish: Specifies the commitish value that determines where the Git tag is created from
        name: The name of the release
        body: Text describing the contents of the tag
        draft: True to create a draft (unpublished) release, false to create a published one
        prerelease: True to identify the release as a prerelease, false to identify the release as a full release
        discussion_category_name: If specified, a discussion of the specified category is created and linked to the release
        generate_release_notes: Whether to automatically generate the name and body for this release
    """
    data = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes
    }
    
    if target_commitish:
        data["target_commitish"] = target_commitish
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    if discussion_category_name:
        data["discussion_category_name"] = discussion_category_name
    
    return github_request("POST", f"/repos/{owner}/{repo}/releases", data=data)


@mcp.tool()
def get_release_by_tag(owner: str, repo: str, tag: str) -> dict:
    """
    Get a release by its tag name.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        tag: The name of the tag
    """
    return github_request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")


# Actions workflows tools

@mcp.tool()
def list_repository_workflows(
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    List workflows for a repository.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {"per_page": per_page, "page": page}
    return github_request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=params)


@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id) -> dict:
    """
    Get a workflow by ID.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    """
    return github_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


@mcp.tool()
def disable_workflow(owner: str, repo: str, workflow_id) -> dict:
    """
    Disable a workflow.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    """
    return github_request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


@mcp.tool()
def enable_workflow(owner: str, repo: str, workflow_id) -> dict:
    """
    Enable a workflow.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    """
    return github_request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


@mcp.tool()
def create_workflow_dispatch_event(
    owner: str,
    repo: str,
    workflow_id,
    ref: str,
    inputs: dict = None
) -> dict:
    """
    Create a workflow dispatch event to trigger a workflow run.
    
    Args:
        owner: The account owner of the repository
        repo: The name of the repository
        workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
        ref: The git reference for the workflow. The reference can be a branch or tag name.
        inputs: Input keys and values configured in the workflow file.
    """
    data = {
        "ref": ref
    }
    if inputs:
        data["inputs"] = inputs
    
    return github_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", data=data)


# Search tools

@mcp.tool()
def search_code(
    q: str,
    sort: str = "indexed",
    order: str = "desc",
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    Search for code across GitHub.
    
    Args:
        q: The query contains one or more search keywords and qualifiers
        sort: This field is closing down. Can only be indexed
        order: Determines whether the first search result returned is the highest or lowest number of matches
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "q": q,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    return github_request("GET", "/search/code", params=params)


@mcp.tool()
def search_issues(
    q: str,
    sort: str = None,
    order: str = "desc",
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    Search for issues and pull requests across GitHub.
    
    Args:
        q: The query contains one or more search keywords and qualifiers
        sort: What to sort results by
        order: Determines whether the first search result returned is the highest or lowest number of matches
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "q": q,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    if sort:
        params["sort"] = sort
    
    return github_request("GET", "/search/issues", params=params)


@mcp.tool()
def search_repositories(
    q: str,
    sort: str = None,
    order: str = "desc",
    per_page: int = 30,
    page: int = 1
) -> dict:
    """
    Search for repositories across GitHub.
    
    Args:
        q: The query contains one or more search keywords and qualifiers
        sort: What to sort results by
        order: Determines whether the first search result returned is the highest or lowest number of matches
        per_page: The number of results per page (max 100)
        page: The page_number number of the results to fetch
    """
    params = {
        "q": q,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    if sort:
        params["sort"] = sort
    
    return github_request("GET", "/search/repositories", params=params)


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
