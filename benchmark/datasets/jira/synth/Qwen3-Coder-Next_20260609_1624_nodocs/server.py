#!/usr/bin/env python3
"""
Jira Cloud REST API v3 MCP Server

Provides comprehensive coverage of Jira Cloud REST API v3 for use by autonomous agents.
"""

import os
import requests
from typing import Any, Optional

from fastmcp import FastMCP
from fastmcp.tools import Tool

# Initialize MCP server
mcp = FastMCP(name="jira", log_level="info")

# Jira API base URL
JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")


def _get_auth() -> tuple[str, str]:
    """Get authentication credentials."""
    if not JIRA_EMAIL or not JIRA_API_TOKEN:
        raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set")
    return JIRA_EMAIL, JIRA_API_TOKEN


def _jira_request(
    method: str,
    path: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
) -> dict[str, Any]:
    """Make a Jira API request."""
    url = f"{JIRA_BASE_URL}/rest/api/3/{path}"
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            auth=_get_auth(),
            params=params,
            json=data,
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()
        
        if response.status_code == 204:
            return {"success": True}
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP {e.response.status_code}: {e.response.text}"
        return {"error": error_msg}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# =============================================================================
# Issues
# =============================================================================

@mcp.tool()
def create_issue(
    summary: str,
    project_key: str,
    issue_type: str,
    description: Optional[str] = None,
    assignee: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[list[str]] = None,
    components: Optional[list[str]] = None,
    custom_fields: Optional[dict] = None,
) -> dict[str, Any]:
    """
    Create a new issue in Jira.
    
    Args:
        summary: Issue summary (required)
        project_key: Project key (required)
        issue_type: Issue type name or ID (required)
        description: Issue description
        assignee: Assignee account ID or username
        priority: Priority name or ID
        labels: List of labels
        components: List of component names or IDs
        custom_fields: Dictionary of custom field values
    
    Returns:
        Created issue details
    """
    data = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": issue_type} if issue_type.isdigit() is False else {"id": issue_type},
        }
    }
    
    if description:
        data["fields"]["description"] = description
    
    if assignee:
        data["fields"]["assignee"] = {"accountId": assignee} if "@" in assignee else {"name": assignee}
    
    if priority:
        data["fields"]["priority"] = {"name": priority} if priority.isdigit() is False else {"id": priority}
    
    if labels:
        data["fields"]["labels"] = labels
    
    if components:
        data["fields"]["components"] = [
            {"name": c} if c.isdigit() is False else {"id": c} for c in components
        ]
    
    if custom_fields:
        for field, value in custom_fields.items():
            data["fields"][field] = value
    
    return _jira_request("POST", "issue", data=data)


@mcp.tool()
def get_issue(issue_key: str, fields: Optional[str] = None, expand: Optional[str] = None) -> dict[str, Any]:
    """
    Get an issue by its key.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        fields: Comma-separated list of fields to return
        expand: Fields to expand (e.g., "changelog")
    
    Returns:
        Issue details
    """
    params = {}
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    
    return _jira_request("GET", f"issue/{issue_key}", params=params)


@mcp.tool()
def update_issue(issue_key: str, summary: Optional[str] = None, description: Optional[str] = None,
                 assignee: Optional[str] = None, priority: Optional[str] = None,
                 labels: Optional[list[str]] = None, custom_fields: Optional[dict] = None) -> dict[str, Any]:
    """
    Update an existing issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        summary: New summary
        description: New description
        assignee: New assignee account ID or username
        priority: New priority name or ID
        labels: New list of labels
        custom_fields: Dictionary of custom field values
    
    Returns:
        Updated issue details
    """
    data = {"fields": {}}
    
    if summary is not None:
        data["fields"]["summary"] = summary
    if description is not None:
        data["fields"]["description"] = description
    if assignee is not None:
        data["fields"]["assignee"] = {"accountId": assignee} if "@" in assignee else {"name": assignee}
    if priority is not None:
        data["fields"]["priority"] = {"name": priority} if priority.isdigit() is False else {"id": priority}
    if labels is not None:
        data["fields"]["labels"] = labels
    if custom_fields is not None:
        data["fields"].update(custom_fields)
    
    return _jira_request("PUT", f"issue/{issue_key}", data=data)


@mcp.tool()
def delete_issue(issue_key: str, delete_subtasks: bool = True) -> dict[str, Any]:
    """
    Delete an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        delete_subtasks: Whether to delete subtasks (default: true)
    
    Returns:
        Success response
    """
    params = {"deleteSubtasks": str(delete_subtasks).lower()}
    return _jira_request("DELETE", f"issue/{issue_key}", params=params)


@mcp.tool()
def assign_issue(issue_key: str, account_id: str) -> dict[str, Any]:
    """
    Assign an issue to a user.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        account_id: User's account ID
    
    Returns:
        Success response
    """
    data = {"accountId": account_id}
    return _jira_request("POST", f"issue/{issue_key}/assignee", data=data)


@mcp.tool()
def transition_issue(issue_key: str, transition_id: str,
                     comment: Optional[str] = None,
                     fields: Optional[dict] = None) -> dict[str, Any]:
    """
    Transition an issue to a new status.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        transition_id: Transition ID (e.g., "11")
        comment: Optional comment on the transition
        fields: Fields to set during transition
    
    Returns:
        Success response
    """
    data = {"transition": {"id": transition_id}}
    
    if comment:
        data["update"] = {"comment": [{"add": {"body": comment}}]}
    
    if fields:
        data["fields"] = fields
    
    return _jira_request("POST", f"issue/{issue_key}/transitions", data=data)


@mcp.tool()
def add_comment(issue_key: str, body: str) -> dict[str, Any]:
    """
    Add a comment to an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        body: Comment text
    
    Returns:
        Created comment details
    """
    data = {"body": body}
    return _jira_request("POST", f"issue/{issue_key}/comment", data=data)


@mcp.tool()
def get_comments(issue_key: str) -> dict[str, Any]:
    """
    Get all comments for an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
    
    Returns:
        List of comments
    """
    return _jira_request("GET", f"issue/{issue_key}/comment")


@mcp.tool()
def update_comment(comment_id: str, body: str, public: bool = True) -> dict[str, Any]:
    """
    Update a comment.
    
    Args:
        comment_id: Comment ID
        body: New comment text
        public: Whether comment is public
    
    Returns:
        Updated comment details
    """
    data = {"body": body}
    if not public:
        data["visibility"] = {"type": "role", "value": "Administrators"}
    return _jira_request("PUT", f"comment/{comment_id}", data=data)


@mcp.tool()
def delete_comment(comment_id: str) -> dict[str, Any]:
    """
    Delete a comment.
    
    Args:
        comment_id: Comment ID
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"comment/{comment_id}")


@mcp.tool()
def add_worklog(issue_key: str, time_spent: str, comment: Optional[str] = None,
                started: Optional[str] = None, billable: bool = True) -> dict[str, Any]:
    """
    Add a worklog to an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        time_spent: Time spent (e.g., "1h 30m")
        comment: Optional worklog comment
        started: Start time (ISO 8601)
        billable: Whether the worklog is billable
    
    Returns:
        Created worklog details
    """
    data = {"timeSpent": time_spent, "billable": str(billable).lower()}
    if comment:
        data["comment"] = comment
    if started:
        data["started"] = started
    return _jira_request("POST", f"issue/{issue_key}/worklog", data=data)


@mcp.tool()
def get_worklogs(issue_key: str) -> dict[str, Any]:
    """
    Get all worklogs for an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
    
    Returns:
        List of worklogs
    """
    return _jira_request("GET", f"issue/{issue_key}/worklog")


@mcp.tool()
def get_worklog(worklog_id: str) -> dict[str, Any]:
    """
    Get a specific worklog.
    
    Args:
        worklog_id: Worklog ID
    
    Returns:
        Worklog details
    """
    return _jira_request("GET", f"worklog/{worklog_id}")


@mcp.tool()
def update_worklog(worklog_id: str, time_spent: Optional[str] = None,
                   comment: Optional[str] = None, billable: Optional[bool] = None) -> dict[str, Any]:
    """
    Update a worklog.
    
    Args:
        worklog_id: Worklog ID
        time_spent: New time spent
        comment: New comment
        billable: Whether billable
    
    Returns:
        Updated worklog details
    """
    data = {}
    if time_spent:
        data["timeSpent"] = time_spent
    if comment is not None:
        data["comment"] = comment
    if billable is not None:
        data["billable"] = str(billable).lower()
    return _jira_request("PUT", f"worklog/{worklog_id}", data=data)


@mcp.tool()
def delete_worklog(worklog_id: str) -> dict[str, Any]:
    """
    Delete a worklog.
    
    Args:
        worklog_id: Worklog ID
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"worklog/{worklog_id}")


@mcp.tool()
def add_attachment(issue_key: str, file_path: str, filename: Optional[str] = None) -> dict[str, Any]:
    """
    Add an attachment to an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        file_path: Path to the file to attach
        filename: Optional filename override
    
    Returns:
        Created attachment details
    """
    if filename is None:
        filename = os.path.basename(file_path)
    
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}/attachments"
    try:
        with open(file_path, "rb") as f:
            files = {"file": (filename, f)}
            response = requests.post(
                url,
                auth=_get_auth(),
                headers={"X-Atlassian-Token": "no-check"},
                files=files,
            )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_attachments(issue_key: str) -> dict[str, Any]:
    """
    Get all attachments for an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
    
    Returns:
        List of attachments
    """
    return _jira_request("GET", f"issue/{issue_key}/attachments")


@mcp.tool()
def delete_attachment(attachment_id: str) -> dict[str, Any]:
    """
    Delete an attachment.
    
    Args:
        attachment_id: Attachment ID
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"attachment/{attachment_id}")


@mcp.tool()
def add_watcher(issue_key: str, account_id: str) -> dict[str, Any]:
    """
    Add a watcher to an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        account_id: User's account ID
    
    Returns:
        Success response
    """
    data = {"accountId": account_id}
    return _jira_request("POST", f"issue/{issue_key}/watchers", data=data)


@mcp.tool()
def remove_watcher(issue_key: str, account_id: str) -> dict[str, Any]:
    """
    Remove a watcher from an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
        account_id: User's account ID
    
    Returns:
        Success response
    """
    params = {"accountId": account_id}
    return _jira_request("DELETE", f"issue/{issue_key}/watchers", params=params)


@mcp.tool()
def get_watches(issue_key: str) -> dict[str, Any]:
    """
    Get watch information for an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
    
    Returns:
        Watch count and watching users
    """
    return _jira_request("GET", f"issue/{issue_key}/watchers")


@mcp.tool()
def add_issue_link(
    inward_issue_key: str,
    outward_issue_key: str,
    link_type: str,
    comment: Optional[str] = None,
) -> dict[str, Any]:
    """
    Create a link between two issues.
    
    Args:
        inward_issue_key: Issue key that will link from
        outward_issue_key: Issue key that will link to
        link_type: Link type name (e.g., "Duplicate", "Relates")
        comment: Optional comment on the link
    
    Returns:
        Created link details
    """
    data = {
        "outwardIssue": {"key": outward_issue_key},
        "inwardIssue": {"key": inward_issue_key},
        "type": {"name": link_type},
    }
    if comment:
        data["comment"] = {"body": comment}
    return _jira_request("POST", "issueLink", data=data)


@mcp.tool()
def get_issue_links(issue_key: str) -> dict[str, Any]:
    """
    Get all links for an issue.
    
    Args:
        issue_key: Issue key (e.g., "PROJ-123")
    
    Returns:
        List of issue links
    """
    return _jira_request("GET", f"issue/{issue_key}/remotelink")


@mcp.tool()
def get_issue_link(link_id: str) -> dict[str, Any]:
    """
    Get a specific issue link.
    
    Args:
        link_id: Link ID
    
    Returns:
        Issue link details
    """
    return _jira_request("GET", f"issueLink/{link_id}")


@mcp.tool()
def delete_issue_link(link_id: str) -> dict[str, Any]:
    """
    Delete an issue link.
    
    Args:
        link_id: Link ID
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"issueLink/{link_id}")


@mcp.tool()
def search_issues(
    jql: str,
    start: int = 0,
    max_results: int = 50,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
) -> dict[str, Any]:
    """
    Search issues using JQL.
    
    Args:
        jql: JQL query string
        start: Starting index (default: 0)
        max_results: Maximum results (default: 50, max: 100)
        fields: Comma-separated list of fields to return
        expand: Fields to expand
    
    Returns:
        Search results with issues
    """
    params = {
        "jql": jql,
        "start": start,
        "maxResults": max_results,
    }
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    return _jira_request("GET", "search", params=params)


# =============================================================================
# Projects
# =============================================================================

@mcp.tool()
def get_projects() -> dict[str, Any]:
    """
    Get all projects.
    
    Returns:
        List of projects
    """
    return _jira_request("GET", "project")


@mcp.tool()
def get_project(project_key: str) -> dict[str, Any]:
    """
    Get a project by key.
    
    Args:
        project_key: Project key (e.g., "PROJ")
    
    Returns:
        Project details
    """
    return _jira_request("GET", f"project/{project_key}")


@mcp.tool()
def get_project_versions(project_key: str, start: int = 0, max_results: int = 100) -> dict[str, Any]:
    """
    Get versions for a project.
    
    Args:
        project_key: Project key
        start: Starting index
        max_results: Maximum results
    
    Returns:
        List of versions
    """
    params = {"start": start, "maxResults": max_results}
    return _jira_request("GET", f"project/{project_key}/versions", params=params)


@mcp.tool()
def get_project_components(project_key: str, start: int = 0, max_results: int = 100) -> dict[str, Any]:
    """
    Get components for a project.
    
    Args:
        project_key: Project key
        start: Starting index
        max_results: Maximum results
    
    Returns:
        List of components
    """
    params = {"start": start, "maxResults": max_results}
    return _jira_request("GET", f"project/{project_key}/components", params=params)


# =============================================================================
# Issue Types, Priorities, Statuses
# =============================================================================

@mcp.tool()
def get_issue_types() -> dict[str, Any]:
    """
    Get all issue types.
    
    Returns:
        List of issue types
    """
    return _jira_request("GET", "issuetype")


@mcp.tool()
def get_priority(issue_priority_id: str) -> dict[str, Any]:
    """
    Get a priority by ID.
    
    Args:
        issue_priority_id: Priority ID
    
    Returns:
        Priority details
    """
    return _jira_request("GET", f"priority/{issue_priority_id}")


@mcp.tool()
def get_priorities() -> dict[str, Any]:
    """
    Get all priorities.
    
    Returns:
        List of priorities
    """
    return _jira_request("GET", "priority")


@mcp.tool()
def get_status() -> dict[str, Any]:
    """
    Get all statuses.
    
    Returns:
        List of statuses
    """
    return _jira_request("GET", "status")


@mcp.tool()
def get_status_by_id(status_id: str) -> dict[str, Any]:
    """
    Get a status by ID.
    
    Args:
        status_id: Status ID
    
    Returns:
        Status details
    """
    return _jira_request("GET", f"status/{status_id}")


# =============================================================================
# Users and Groups
# =============================================================================

@mcp.tool()
def search_users(
    query: str,
    start: int = 0,
    max_results: int = 50,
    account_type: Optional[str] = None,
    active: Optional[bool] = None,
) -> dict[str, Any]:
    """
    Search for users.
    
    Args:
        query: Search query
        start: Starting index
        max_results: Maximum results
        account_type: Filter by account type (e.g., "atlassian")
        active: Filter by active status
    
    Returns:
        List of matching users
    """
    params = {
        "query": query,
        "start": start,
        "maxResults": max_results,
    }
    if account_type:
        params["accountType"] = account_type
    if active is not None:
        params["active"] = str(active).lower()
    return _jira_request("GET", "user/search", params=params)


@mcp.tool()
def get_user(account_id: str) -> dict[str, Any]:
    """
    Get a user by account ID.
    
    Args:
        account_id: User's account ID
    
    Returns:
        User details
    """
    params = {"accountId": account_id}
    return _jira_request("GET", "user", params=params)


@mcp.tool()
def search_groups(
    query: str,
    max_results: int = 50,
) -> dict[str, Any]:
    """
    Search for groups.
    
    Args:
        query: Search query
        max_results: Maximum results
    
    Returns:
        List of matching groups
    """
    params = {
        "query": query,
        "maxResults": max_results,
    }
    return _jira_request("GET", "group", params=params)


@mcp.tool()
def get_group_members(
    group_id: str,
    start: int = 0,
    max_results: int = 50,
) -> dict[str, Any]:
    """
    Get members of a group.
    
    Args:
        group_id: Group ID
        start: Starting index
        max_results: Maximum results
    
    Returns:
        List of group members
    """
    params = {
        "groupId": group_id,
        "start": start,
        "maxResults": max_results,
    }
    return _jira_request("GET", "group/member", params=params)


# =============================================================================
# Filters and Favorites
# =============================================================================

@mcp.tool()
def get_filters() -> dict[str, Any]:
    """
    Get all filters.
    
    Returns:
        List of filters
    """
    return _jira_request("GET", "filter")


@mcp.tool()
def get_filter(filter_id: str) -> dict[str, Any]:
    """
    Get a filter by ID.
    
    Args:
        filter_id: Filter ID (or "recent", "shared")
    
    Returns:
        Filter details
    """
    return _jira_request("GET", f"filter/{filter_id}")


@mcp.tool()
def get_favourite_filters() -> dict[str, Any]:
    """
    Get favourite filters for the current user.
    
    Returns:
        List of favourite filters
    """
    return _jira_request("GET", "filter/favourite")


# =============================================================================
# Components
# =============================================================================

@mcp.tool()
def create_component(
    name: str,
    project_key: str,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    Create a new project component.
    
    Args:
        name: Component name (required)
        project_key: Project key (required)
        description: Component description
        lead_account_id: Lead's account ID
    
    Returns:
        Created component details
    """
    data = {
        "name": name,
        "projectId": project_key,
    }
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    return _jira_request("POST", "component", data=data)


@mcp.tool()
def get_component(component_id: str) -> dict[str, Any]:
    """
    Get a component by ID.
    
    Args:
        component_id: Component ID
    
    Returns:
        Component details
    """
    return _jira_request("GET", f"component/{component_id}")


@mcp.tool()
def update_component(
    component_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    Update a component.
    
    Args:
        component_id: Component ID
        name: New name
        description: New description
        lead_account_id: New lead's account ID
    
    Returns:
        Updated component details
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    return _jira_request("PUT", f"component/{component_id}", data=data)


@mcp.tool()
def delete_component(component_id: str, move_fix_issues_to: Optional[str] = None,
                     move_affected_issues_to: Optional[str] = None) -> dict[str, Any]:
    """
    Delete a component.
    
    Args:
        component_id: Component ID
        move_fix_issues_to: Component ID to move fix versions to
        move_affected_issues_to: Component ID to move affected versions to
    
    Returns:
        Success response
    """
    params = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return _jira_request("DELETE", f"component/{component_id}", params=params)


# =============================================================================
# Versions
# =============================================================================

@mcp.tool()
def create_version(
    name: str,
    project_key: str,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    archived: bool = False,
    released: bool = False,
) -> dict[str, Any]:
    """
    Create a new version.
    
    Args:
        name: Version name (required)
        project_key: Project key (required)
        description: Version description
        start_date: Start date (YYYY-MM-DD)
        release_date: Release date (YYYY-MM-DD)
        archived: Whether version is archived
        released: Whether version is released
    
    Returns:
        Created version details
    """
    data = {
        "name": name,
        "projectId": project_key,
        "archived": archived,
        "released": released,
    }
    if description:
        data["description"] = description
    if start_date:
        data["startDate"] = start_date
    if release_date:
        data["releaseDate"] = release_date
    return _jira_request("POST", "version", data=data)


@mcp.tool()
def get_version(version_id: str) -> dict[str, Any]:
    """
    Get a version by ID.
    
    Args:
        version_id: Version ID
    
    Returns:
        Version details
    """
    return _jira_request("GET", f"version/{version_id}")


@mcp.tool()
def update_version(
    version_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    archived: Optional[bool] = None,
    released: Optional[bool] = None,
) -> dict[str, Any]:
    """
    Update a version.
    
    Args:
        version_id: Version ID
        name: New name
        description: New description
        start_date: New start date
        release_date: New release date
        archived: Whether archived
        released: Whether released
    
    Returns:
        Updated version details
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if start_date:
        data["startDate"] = start_date
    if release_date:
        data["releaseDate"] = release_date
    if archived is not None:
        data["archived"] = archived
    if released is not None:
        data["released"] = released
    return _jira_request("PUT", f"version/{version_id}", data=data)


@mcp.tool()
def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None,
                   move_affected_issues_to: Optional[str] = None) -> dict[str, Any]:
    """
    Delete a version.
    
    Args:
        version_id: Version ID
        move_fix_issues_to: Version ID to move fix versions to
        move_affected_issues_to: Version ID to move affected versions to
    
    Returns:
        Success response
    """
    params = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return _jira_request("DELETE", f"version/{version_id}", params=params)


@mcp.tool()
def move_version(version_id: str, after: Optional[str] = None,
                 before: Optional[str] = None) -> dict[str, Any]:
    """
    Move a version's position in the version order.
    
    Args:
        version_id: Version ID
        after: Version ID to move after
        before: Version ID to move before
    
    Returns:
        Success response
    """
    data = {}
    if after:
        data["after"] = after
    if before:
        data["before"] = before
    return _jira_request("POST", f"version/{version_id}/move", data=data)


@mcp.tool()
def release_version(version_id: str, release_date: Optional[str] = None,
                    move_future_issues: bool = True) -> dict[str, Any]:
    """
    Release a version.
    
    Args:
        version_id: Version ID
        release_date: Release date
        move_future_issues: Whether to move future issues to next version
    
    Returns:
        Success response
    """
    data = {"released": True}
    if release_date:
        data["releaseDate"] = release_date
    if move_future_issues:
        data["moveFutureIssuesToNextUnreleasedVersion"] = True
    return _jira_request("PUT", f"version/{version_id}", data=data)


@mcp.tool()
def unreleased_version(version_id: str, move_issues: bool = True) -> dict[str, Any]:
    """
    Set a version as unreleased.
    
    Args:
        version_id: Version ID
        move_issues: Whether to move issues to next version
    
    Returns:
        Success response
    """
    data = {"released": False}
    if move_issues:
        data["moveFixIssuesTo"] = "nextUnreleasedVersion"
    return _jira_request("PUT", f"version/{version_id}", data=data)


# =============================================================================
# Comments
# =============================================================================

@mcp.tool()
def get_comment(comment_id: str) -> dict[str, Any]:
    """
    Get a comment by ID.
    
    Args:
        comment_id: Comment ID
    
    Returns:
        Comment details
    """
    return _jira_request("GET", f"comment/{comment_id}")


@mcp.tool()
def get_comment_property(comment_id: str, property_key: str) -> dict[str, Any]:
    """
    Get a comment property.
    
    Args:
        comment_id: Comment ID
        property_key: Property key
    
    Returns:
        Property value
    """
    return _jira_request("GET", f"comment/{comment_id}/property/{property_key}")


@mcp.tool()
def update_comment_property(comment_id: str, property_key: str, value: dict) -> dict[str, Any]:
    """
    Update a comment property.
    
    Args:
        comment_id: Comment ID
        property_key: Property key
        value: Property value
    
    Returns:
        Updated property
    """
    return _jira_request("PUT", f"comment/{comment_id}/property/{property_key}", data=value)


@mcp.tool()
def delete_comment_property(comment_id: str, property_key: str) -> dict[str, Any]:
    """
    Delete a comment property.
    
    Args:
        comment_id: Comment ID
        property_key: Property key
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"comment/{comment_id}/property/{property_key}")


# =============================================================================
# Worklogs
# =============================================================================

@mcp.tool()
def update_worklog_property(worklog_id: str, property_key: str, value: dict) -> dict[str, Any]:
    """
    Update a worklog property.
    
    Args:
        worklog_id: Worklog ID
        property_key: Property key
        value: Property value
    
    Returns:
        Updated property
    """
    return _jira_request("PUT", f"worklog/{worklog_id}/property/{property_key}", data=value)


@mcp.tool()
def get_worklog_property(worklog_id: str, property_key: str) -> dict[str, Any]:
    """
    Get a worklog property.
    
    Args:
        worklog_id: Worklog ID
        property_key: Property key
    
    Returns:
        Property value
    """
    return _jira_request("GET", f"worklog/{worklog_id}/property/{property_key}")


@mcp.tool()
def delete_worklog_property(worklog_id: str, property_key: str) -> dict[str, Any]:
    """
    Delete a worklog property.
    
    Args:
        worklog_id: Worklog ID
        property_key: Property key
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"worklog/{worklog_id}/property/{property_key}")


# =============================================================================
# Issue Properties
# =============================================================================

@mcp.tool()
def get_issue_property(issue_key: str, property_key: str) -> dict[str, Any]:
    """
    Get an issue property.
    
    Args:
        issue_key: Issue key
        property_key: Property key
    
    Returns:
        Property value
    """
    return _jira_request("GET", f"issue/{issue_key}/properties/{property_key}")


@mcp.tool()
def set_issue_property(issue_key: str, property_key: str, value: dict) -> dict[str, Any]:
    """
    Set an issue property.
    
    Args:
        issue_key: Issue key
        property_key: Property key
        value: Property value
    
    Returns:
        Success response
    """
    return _jira_request("PUT", f"issue/{issue_key}/properties/{property_key}", data=value)


@mcp.tool()
def delete_issue_property(issue_key: str, property_key: str) -> dict[str, Any]:
    """
    Delete an issue property.
    
    Args:
        issue_key: Issue key
        property_key: Property key
    
    Returns:
        Success response
    """
    return _jira_request("DELETE", f"issue/{issue_key}/properties/{property_key}")


@mcp.tool()
def get_issue_properties(issue_key: str) -> dict[str, Any]:
    """
    Get all issue properties.
    
    Args:
        issue_key: Issue key
    
    Returns:
        List of properties
    """
    return _jira_request("GET", f"issue/{issue_key}/properties")


# =============================================================================
# Watchers
# =============================================================================

@mcp.tool()
def get_issue_watches(issue_key: str) -> dict[str, Any]:
    """
    Get watches for an issue.
    
    Args:
        issue_key: Issue key
    
    Returns:
        Watch count and watching users
    """
    return _jira_request("GET", f"issue/{issue_key}/watchers")


@mcp.tool()
def add_issue_watchers(issue_key: str, account_ids: list[str]) -> dict[str, Any]:
    """
    Add multiple watchers to an issue.
    
    Args:
        issue_key: Issue key
        account_ids: List of user account IDs
    
    Returns:
        Updated watcher count
    """
    data = {"accountId": account_ids}
    return _jira_request("POST", f"issue/{issue_key}/watchers", data=data)


@mcp.tool()
def remove_issue_watchers(issue_key: str, account_ids: list[str]) -> dict[str, Any]:
    """
    Remove multiple watchers from an issue.
    
    Args:
        issue_key: Issue key
        account_ids: List of user account IDs
    
    Returns:
        Updated watcher count
    """
    data = {"accountId": account_ids}
    return _jira_request("DELETE", f"issue/{issue_key}/watchers", data=data)


# =============================================================================
# Transition
# =============================================================================

@mcp.tool()
def get_transitions(issue_key: str) -> dict[str, Any]:
    """
    Get available transitions for an issue.
    
    Args:
        issue_key: Issue key
    
    Returns:
        List of available transitions
    """
    return _jira_request("GET", f"issue/{issue_key}/transitions")


# =============================================================================
# Priority
# =============================================================================

@mcp.tool()
def get_priority_by_id(priority_id: str) -> dict[str, Any]:
    """
    Get a priority by ID.
    
    Args:
        priority_id: Priority ID
    
    Returns:
        Priority details
    """
    return _jira_request("GET", f"priority/{priority_id}")


# =============================================================================
# User Permissions
# =============================================================================

@mcp.tool()
def get_my_permissions(
    project_key: Optional[str] = None,
    project_id: Optional[str] = None,
    issue_key: Optional[str] = None,
) -> dict[str, Any]:
    """
    Get permissions for the current user.
    
    Args:
        project_key: Project key to check permissions in
        project_id: Project ID to check permissions in
        issue_key: Issue key to check permissions on
    
    Returns:
        User's permissions
    """
    params = {}
    if project_key:
        params["projectKey"] = project_key
    if project_id:
        params["projectId"] = project_id
    if issue_key:
        params["issueKey"] = issue_key
    return _jira_request("GET", "mypermissions", params=params)


@mcp.tool()
def has_issue_permission(issue_key: str, permission: str) -> dict[str, Any]:
    """
    Check if current user has a specific permission on an issue.
    
    Args:
        issue_key: Issue key
        permission: Permission to check (e.g., "EDIT_ISSUE", "DELETE_ISSUE")
    
    Returns:
        Permission check result
    """
    params = {"permission": permission}
    return _jira_request("GET", f"issue/{issue_key}/permissions/{permission}", params=params)


# =============================================================================
# Labels
# =============================================================================

@mcp.tool()
def add_label(issue_key: str, label: str) -> dict[str, Any]:
    """
    Add a label to an issue.
    
    Args:
        issue_key: Issue key
        label: Label to add
    
    Returns:
        Updated labels
    """
    data = {"update": {"labels": [{"add": label}]}}
    return _jira_request("PUT", f"issue/{issue_key}", data=data)


@mcp.tool()
def remove_label(issue_key: str, label: str) -> dict[str, Any]:
    """
    Remove a label from an issue.
    
    Args:
        issue_key: Issue key
        label: Label to remove
    
    Returns:
        Updated labels
    """
    data = {"update": {"labels": [{"remove": label}]}}
    return _jira_request("PUT", f"issue/{issue_key}", data=data)


# =============================================================================
# TimeTracking
# =============================================================================

@mcp.tool()
def timetracking_estimate(issue_key: str, time_spent: Optional[str] = None,
                          remaining_estimate: Optional[str] = None,
                          original_estimate: Optional[str] = None) -> dict[str, Any]:
    """
    Set time tracking estimates.
    
    Args:
        issue_key: Issue key
        time_spent: Time already spent
        remaining_estimate: Remaining time estimate
        original_estimate: Original time estimate
    
    Returns:
        Updated time tracking info
    """
    data = {"fields": {}}
    if time_spent:
        data["fields"]["timetracking"] = {
            "originalEstimate": original_estimate,
            "remainingEstimate": remaining_estimate,
            "timeSpent": time_spent,
        }
    elif remaining_estimate:
        data["fields"]["timetracking"] = {
            "remainingEstimate": remaining_estimate,
        }
    elif original_estimate:
        data["fields"]["timetracking"] = {
            "originalEstimate": original_estimate,
        }
    return _jira_request("PUT", f"issue/{issue_key}", data=data)


# =============================================================================
# Issue Security
# =============================================================================

@mcp.tool()
def get_issue_security_level(issue_key: str) -> dict[str, Any]:
    """
    Get the security level for an issue.
    
    Args:
        issue_key: Issue key
    
    Returns:
        Security level details
    """
    return _jira_request("GET", f"issue/{issue_key}/securitylevel")


@mcp.tool()
def set_issue_security_level(issue_key: str, security_level_id: str) -> dict[str, Any]:
    """
    Set the security level for an issue.
    
    Args:
        issue_key: Issue key
        security_level_id: Security level ID
    
    Returns:
        Updated issue details
    """
    data = {"fields": {"security": {"id": security_level_id}}}
    return _jira_request("PUT", f"issue/{issue_key}", data=data)


# =============================================================================
# Subtasks
# =============================================================================

@mcp.tool()
def create_subtask(
    summary: str,
    project_key: str,
    parent_issue_key: str,
    description: Optional[str] = None,
    assignee: Optional[str] = None,
    priority: Optional[str] = None,
    custom_fields: Optional[dict] = None,
) -> dict[str, Any]:
    """
    Create a subtask.
    
    Args:
        summary: Subtask summary (required)
        project_key: Project key (required)
        parent_issue_key: Parent issue key (required)
        description: Subtask description
        assignee: Assignee account ID
        priority: Priority name or ID
        custom_fields: Custom field values
    
    Returns:
        Created subtask details
    """
    data = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": "Subtask"},
            "parent": {"key": parent_issue_key},
        }
    }
    if description:
        data["fields"]["description"] = description
    if assignee:
        data["fields"]["assignee"] = {"accountId": assignee}
    if priority:
        data["fields"]["priority"] = {"name": priority}
    if custom_fields:
        data["fields"].update(custom_fields)
    return _jira_request("POST", "issue", data=data)


# =============================================================================
# Comments Properties
# =============================================================================

@mcp.tool()
def get_comment_property(comment_id: str, property_key: str) -> dict[str, Any]:
    """
    Get a comment property.
    
    Args:
        comment_id: Comment ID
        property_key: Property key
    
    Returns:
        Property value
    """
    return _jira_request("GET", f"comment/{comment_id}/property/{property_key}")


# =============================================================================
# User Preferences
# =============================================================================

@mcp.tool()
def get_user_preferences(account_id: str) -> dict[str, Any]:
    """
    Get user preferences.
    
    Args:
        account_id: User's account ID
    
    Returns:
        User preferences
    """
    params = {"accountId": account_id}
    return _jira_request("GET", "user/preferences", params=params)


# =============================================================================
# Notifications
# =============================================================================

@mcp.tool()
def get_notification_recipients(issue_key: str, notification_scheme_id: Optional[str] = None) -> dict[str, Any]:
    """
    Get notification recipients for an issue.
    
    Args:
        issue_key: Issue key
        notification_scheme_id: Notification scheme ID
    
    Returns:
        List of notification recipients
    """
    params = {}
    if notification_scheme_id:
        params["notificationSchemeId"] = notification_scheme_id
    return _jira_request("GET", f"issue/{issue_key}/notificationrecipients", params=params)


# =============================================================================
# Email
# =============================================================================

@mcp.tool()
def send_email(issue_key: str, subject: str, body: str, to_users: Optional[list[str]] = None,
               to_groups: Optional[list[str]] = None) -> dict[str, Any]:
    """
    Send an email notification for an issue.
    
    Args:
        issue_key: Issue key
        subject: Email subject
        body: Email body
        to_users: List of user account IDs to email
        to_groups: List of group names to email
    
    Returns:
        Success response
    """
    data = {
        "subject": subject,
        "body": body,
        "issueKey": issue_key,
    }
    if to_users:
        data["toUsers"] = to_users
    if to_groups:
        data["toGroups"] = to_groups
    return _jira_request("POST", "email", data=data)


if __name__ == "__main__":
    mcp.run()
