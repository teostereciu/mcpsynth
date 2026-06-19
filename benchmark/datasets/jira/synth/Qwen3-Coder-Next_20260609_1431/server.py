#!/usr/bin/env python3
"""
Jira Cloud MCP Server
Comprehensive coverage of Jira Cloud REST API v3 for use by autonomous agents.
"""

import os
import json
from typing import Any

from fastmcp import FastMCP
import requests


# Initialize FastMCP server
mcp = FastMCP(name="jira", version="1.0.0")

# Base URL configuration
BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
if not BASE_URL:
    raise ValueError("JIRA_BASE_URL environment variable is required")
API_URL = f"{BASE_URL}/rest/api/3"

# Authentication headers
AUTH_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Grounding map - maps tool names to documentation
grounding_map = {}


def add_grounding(tool_name: str, doc: str, endpoint: str):
    """Register a tool's documentation mapping."""
    grounding_map[tool_name] = {"doc": doc, "endpoint": endpoint}


def jira_request(method: str, path: str, params: dict = None, data: dict = None) -> dict:
    """Make a Jira API request with proper authentication and error handling."""
    url = f"{API_URL}{path}"
    auth = (
        os.environ.get("JIRA_EMAIL"),
        os.environ.get("JIRA_API_TOKEN"),
    )
    
    if not auth[0] or not auth[1]:
        return {"error": "JIRA_EMAIL and JIRA_API_TOKEN environment variables are required"}
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=AUTH_HEADERS,
            auth=auth,
            params=params,
            json=data,
            timeout=60,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"data": response.text}
        else:
            return {
                "error": f"Jira API error: {response.status_code}",
                "details": response.text[:500],
            }
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# =============================================================================
# Issue Operations
# =============================================================================

@mcp.tool()
def get_issue(issue_id_or_key: str, expand: str = None) -> dict:
    """
    Get an issue by ID or key.
    
    Returns detailed information about the specified issue including all fields,
    comments, transitions, and more.
    
    Required scopes: read:jira-work
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", f"/issue/{issue_id_or_key}", params=params)
    add_grounding("get_issue", "docs/api_issues.md", "GET /rest/api/3/issue/{issueIdOrKey}")
    return result


@mcp.tool()
def create_issue(
    fields: dict,
    update_history: bool = None,
    history_metadata: dict = None,
    properties: list = None,
    transition: dict = None,
    update: dict = None,
) -> dict:
    """
    Create a new issue.
    
    Creates an issue or subtask. The fields parameter contains the issue data
    including project, issue type, summary, description, and any custom fields.
    
    Required scopes: write:jira-work
    """
    body = {"fields": fields}
    
    if update_history is not None:
        body["updateHistory"] = update_history
    if history_metadata:
        body["historyMetadata"] = history_metadata
    if properties:
        body["properties"] = properties
    if transition:
        body["transition"] = transition
    if update:
        body["update"] = update
    
    result = jira_request("POST", "/issue", data=body)
    add_grounding("create_issue", "docs/api_issues.md", "POST /rest/api/3/issue")
    return result


@mcp.tool()
def update_issue(issue_id_or_key: str, fields: dict, update: dict = None) -> dict:
    """
    Update an existing issue.
    
    Updates fields on an issue. Only fields that are editable by the current
    user will be updated.
    
    Required scopes: write:jira-work
    """
    body = {"fields": fields}
    if update:
        body["update"] = update
    
    result = jira_request("PUT", f"/issue/{issue_id_or_key}", data=body)
    add_grounding("update_issue", "docs/api_issues.md", "PUT /rest/api/3/issue/{issueIdOrKey}")
    return result


@mcp.tool()
def delete_issue(issue_id_or_key: str) -> dict:
    """
    Delete an issue.
    
    Permanently deletes the specified issue.
    
    Required scopes: delete:jira-work
    """
    result = jira_request("DELETE", f"/issue/{issue_id_or_key}")
    add_grounding("delete_issue", "docs/api_issues.md", "DEL /rest/api/3/issue/{issueIdOrKey}")
    return result


@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str) -> dict:
    """
    Assign an issue to a user.
    
    Sets the assignee of the issue to the specified user.
    
    Required scopes: write:jira-work
    """
    body = {"accountId": account_id}
    result = jira_request("PUT", f"/issue/{issue_id_or_key}/assignee", data=body)
    add_grounding("assign_issue", "docs/api_issues.md", "PUT /rest/api/3/issue/{issueIdOrKey}/assignee")
    return result


@mcp.tool()
def transition_issue(
    issue_id_or_key: str,
    transition_id: str,
    fields: dict = None,
    update: dict = None,
    comment: dict = None,
) -> dict:
    """
    Transition an issue through the workflow.
    
    Perform a workflow transition on the issue, optionally updating fields
    and adding a comment.
    
    Required scopes: write:jira-work
    """
    body = {"transition": {"id": transition_id}}
    
    if fields:
        body["fields"] = fields
    if update:
        body["update"] = update
    if comment:
        body["update"] = {"comment": [{"add": comment}]}
    
    result = jira_request("POST", f"/issue/{issue_id_or_key}/transitions", data=body)
    add_grounding("transition_issue", "docs/api_issues.md", "POST /rest/api/3/issue/{issueIdOrKey}/transitions")
    return result


@mcp.tool()
def get_issue_transitions(issue_id_or_key: str) -> dict:
    """
    Get available workflow transitions for an issue.
    
    Returns the transitions available for the issue based on the current
    workflow state and user permissions.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/issue/{issue_id_or_key}/transitions")
    add_grounding("get_issue_transitions", "docs/api_issues.md", "GET /rest/api/3/issue/{issueIdOrKey}/transitions")
    return result


@mcp.tool()
def add_comment(
    issue_id_or_key: str,
    body: str,
    visibility: dict = None,
    properties: list = None,
) -> dict:
    """
    Add a comment to an issue.
    
    Creates a new comment on the issue with the specified body text.
    
    Required scopes: write:jira-work
    """
    body_obj = {"body": body}
    
    if visibility:
        body_obj["visibility"] = visibility
    if properties:
        body_obj["properties"] = properties
    
    result = jira_request("POST", f"/issue/{issue_id_or_key}/comment", data=body_obj)
    add_grounding("add_comment", "docs/api_issue-comments.md", "POST /rest/api/3/issue/{issueIdOrKey}/comment")
    return result


@mcp.tool()
def get_comments(issue_id_or_key: str, start: int = 0, max_results: int = 50) -> dict:
    """
    Get all comments for an issue.
    
    Returns a paginated list of comments on the issue.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", f"/issue/{issue_id_or_key}/comment", params=params)
    add_grounding("get_comments", "docs/api_issue-comments.md", "GET /rest/api/3/issue/{issueIdOrKey}/comment")
    return result


@mcp.tool()
def update_comment(
    issue_id_or_key: str,
    comment_id: str,
    body: str,
    visibility: dict = None,
) -> dict:
    """
    Update an existing comment.
    
    Modifies the body and/or visibility of an existing comment.
    
    Required scopes: write:jira-work
    """
    body_obj = {"body": body}
    
    if visibility:
        body_obj["visibility"] = visibility
    
    result = jira_request(
        "PUT",
        f"/issue/{issue_id_or_key}/comment/{comment_id}",
        data=body_obj,
    )
    add_grounding("update_comment", "docs/api_issue-comments.md", "PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}")
    return result


@mcp.tool()
def delete_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """
    Delete a comment from an issue.
    
    Permanently removes the comment from the issue.
    
    Required scopes: delete:jira-work
    """
    result = jira_request(
        "DELETE",
        f"/issue/{issue_id_or_key}/comment/{comment_id}",
    )
    add_grounding("delete_comment", "docs/api_issue-comments.md", "DEL /rest/api/3/issue/{issueIdOrKey}/comment/{id}")
    return result


@mcp.tool()
def get_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """
    Get a specific comment by ID.
    
    Returns details of a single comment on the issue.
    
    Required scopes: read:jira-work
    """
    result = jira_request(
        "GET",
        f"/issue/{issue_id_or_key}/comment/{comment_id}",
    )
    add_grounding("get_comment", "docs/api_issue-comments.md", "GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}")
    return result


# =============================================================================
# Issue Attachments
# =============================================================================

@mcp.tool()
def add_attachment(issue_id_or_key: str, filename: str, content_type: str = None) -> dict:
    """
    Add an attachment to an issue.
    
    Uploads a file as an attachment to the issue. Note: This requires
    multipart/form-data which is handled specially.
    
    Required scopes: write:jira-work
    """
    result = jira_request("POST", f"/issue/{issue_id_or_key}/attachments")
    add_grounding("add_attachment", "docs/api_issue-attachments.md", "POST /rest/api/3/issue/{issueIdOrKey}/attachments")
    return result


@mcp.tool()
def get_attachment(attachment_id: str) -> dict:
    """
    Get attachment details.
    
    Returns metadata about the attachment including filename, size,
    and content URL.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/attachment/{attachment_id}")
    add_grounding("get_attachment", "docs/api_issue-attachments.md", "GET /rest/api/3/attachment/{id}")
    return result


@mcp.tool()
def delete_attachment(attachment_id: str) -> dict:
    """
    Delete an attachment.
    
    Removes the attachment from Jira and deletes the file.
    
    Required scopes: delete:jira-work
    """
    result = jira_request("DELETE", f"/attachment/{attachment_id}")
    add_grounding("delete_attachment", "docs/api_issue-attachments.md", "DEL /rest/api/3/attachment/{id}")
    return result


# =============================================================================
# Issue Worklogs
# =============================================================================

@mcp.tool()
def add_worklog(
    issue_id_or_key: str,
    time_spent: str = None,
    original_estimate: str = None,
    remaining_estimate: str = None,
    started: str = None,
    comment: str = None,
    visibility: dict = None,
) -> dict:
    """
    Add worklog to an issue.
    
    Records time spent working on the issue.
    
    Required scopes: write:jira-work
    """
    body = {}
    
    if time_spent:
        body["timeSpent"] = time_spent
    if original_estimate:
        body["originalEstimate"] = original_estimate
    if remaining_estimate:
        body["remainingEstimate"] = remaining_estimate
    if started:
        body["started"] = started
    if comment:
        body["comment"] = comment
    if visibility:
        body["visibility"] = visibility
    
    result = jira_request("POST", f"/issue/{issue_id_or_key}/worklog", data=body)
    add_grounding("add_worklog", "docs/api_issue-worklogs.md", "POST /rest/api/3/issue/{issueIdOrKey}/worklog")
    return result


@mcp.tool()
def get_worklogs(issue_id_or_key: str) -> dict:
    """
    Get all worklogs for an issue.
    
    Returns a list of all time tracking records for the issue.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/issue/{issue_id_or_key}/worklog")
    add_grounding("get_worklogs", "docs/api_issue-worklogs.md", "GET /rest/api/3/issue/{issueIdOrKey}/worklog")
    return result


@mcp.tool()
def update_worklog(
    issue_id_or_key: str,
    worklog_id: str,
    time_spent: str = None,
    original_estimate: str = None,
    remaining_estimate: str = None,
    comment: str = None,
) -> dict:
    """
    Update a worklog.
    
    Modifies the time tracking information for a worklog.
    
    Required scopes: write:jira-work
    """
    body = {}
    
    if time_spent:
        body["timeSpent"] = time_spent
    if original_estimate:
        body["originalEstimate"] = original_estimate
    if remaining_estimate:
        body["remainingEstimate"] = remaining_estimate
    if comment:
        body["comment"] = comment
    
    result = jira_request(
        "PUT",
        f"/issue/{issue_id_or_key}/worklog/{worklog_id}",
        data=body,
    )
    add_grounding("update_worklog", "docs/api_issue-worklogs.md", "PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}")
    return result


@mcp.tool()
def delete_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """
    Delete a worklog.
    
    Removes the time tracking record from the issue.
    
    Required scopes: delete:jira-work
    """
    result = jira_request(
        "DELETE",
        f"/issue/{issue_id_or_key}/worklog/{worklog_id}",
    )
    add_grounding("delete_worklog", "docs/api_issue-worklogs.md", "DEL /rest/api/3/issue/{issueIdOrKey}/worklog/{id}")
    return result


@mcp.tool()
def get_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """
    Get a specific worklog by ID.
    
    Returns details of a single worklog entry.
    
    Required scopes: read:jira-work
    """
    result = jira_request(
        "GET",
        f"/issue/{issue_id_or_key}/worklog/{worklog_id}",
    )
    add_grounding("get_worklog", "docs/api_issue-worklogs.md", "GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}")
    return result


# =============================================================================
# Issue Watchers
# =============================================================================

@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """
    Add a user as a watcher to an issue.
    
    Enables the user to receive notifications about issue updates.
    
    Required scopes: write:jira-work
    """
    body = {"accountId": account_id}
    result = jira_request("POST", f"/issue/{issue_id_or_key}/watchers", data=body)
    add_grounding("add_watcher", "docs/api_issue-watchers.md", "POST /rest/api/3/issue/{issueIdOrKey}/watchers")
    return result


@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """
    Remove a user from issue watchers.
    
    Stops the user from receiving notifications about issue updates.
    
    Required scopes: delete:jira-work
    """
    params = {"accountId": account_id}
    result = jira_request(
        "DELETE",
        f"/issue/{issue_id_or_key}/watchers",
        params=params,
    )
    add_grounding("remove_watcher", "docs/api_issue-watchers.md", "DEL /rest/api/3/issue/{issueIdOrKey}/watchers")
    return result


@mcp.tool()
def get_watchers(issue_id_or_key: str) -> dict:
    """
    Get list of watchers for an issue.
    
    Returns all users watching the issue.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/issue/{issue_id_or_key}/watchers")
    add_grounding("get_watchers", "docs/api_issue-watchers.md", "GET /rest/api/3/issue/{issueIdOrKey}/watchers")
    return result


# =============================================================================
# Issue Links
# =============================================================================

@mcp.tool()
def create_issue_link(
    link_type: str,
    inward_issue: str,
    outward_issue: str,
    comment: dict = None,
) -> dict:
    """
    Create a link between two issues.
    
    Creates a relationship between two issues using the specified link type.
    
    Required scopes: write:jira-work
    """
    body = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue},
        "outwardIssue": {"key": outward_issue},
    }
    
    if comment:
        body["comment"] = comment
    
    result = jira_request("POST", "/issueLink", data=body)
    add_grounding("create_issue_link", "docs/api_issue-links.md", "POST /rest/api/3/issueLink")
    return result


@mcp.tool()
def delete_issue_link(link_id: str) -> dict:
    """
    Delete an issue link.
    
    Removes the link between two issues.
    
    Required scopes: delete:jira-work
    """
    result = jira_request("DELETE", f"/issueLink/{link_id}")
    add_grounding("delete_issue_link", "docs/api_issue-links.md", "DEL /rest/api/3/issueLink/{id}")
    return result


# =============================================================================
# Issue Search (JQL)
# =============================================================================

@mcp.tool()
def search_issues(
    jql: str,
    start: int = 0,
    max_results: int = 50,
    fields: list = None,
    expand: str = None,
    validate_query: str = "warn",
) -> dict:
    """
    Search for issues using JQL.
    
    Performs a full-text search using JQL queries. Returns paginated results
    with the specified fields.
    
    Required scopes: read:jira-work
    """
    body = {
        "jql": jql,
        "startAt": start,
        "maxResults": max_results,
        "validateQuery": validate_query,
    }
    
    if fields:
        body["fields"] = fields
    if expand:
        body["expand"] = expand
    
    result = jira_request("POST", "/search", data=body)
    add_grounding("search_issues", "docs/api_issue-search.md", "POST /rest/api/3/search")
    return result


@mcp.tool()
def search_issues_get(
    jql: str,
    start: int = 0,
    max_results: int = 50,
    fields: list = None,
    expand: str = None,
    validate_query: str = "warn",
) -> dict:
    """
    Search for issues using JQL (GET method).
    
    Similar to search_issues but uses GET method for smaller queries.
    
    Required scopes: read:jira-work
    """
    params = {
        "jql": jql,
        "startAt": start,
        "maxResults": max_results,
        "validateQuery": validate_query,
    }
    
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", "/search", params=params)
    add_grounding("search_issues_get", "docs/api_issue-search.md", "GET /rest/api/3/search")
    return result


@mcp.tool()
def get_issue_picker(query: str, current_jql: str = None) -> dict:
    """
    Get issue picker suggestions.
    
    Returns auto-completion suggestions for issue keys and summaries.
    
    Required scopes: read:jira-work
    """
    params = {"query": query}
    if current_jql:
        params["currentJQL"] = current_jql
    
    result = jira_request("GET", "/issue/picker", params=params)
    add_grounding("get_issue_picker", "docs/api_issue-search.md", "GET /rest/api/3/issue/picker")
    return result


# =============================================================================
# Project Operations
# =============================================================================

@mcp.tool()
def get_projects(
    start: int = 0,
    max_results: int = 50,
    expand: str = None,
) -> dict:
    """
    Get all projects.
    
    Returns a paginated list of projects accessible to the user.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", "/project", params=params)
    add_grounding("get_projects", "docs/api_projects.md", "GET /rest/api/3/project")
    return result


@mcp.tool()
def get_project(project_key_or_id: str, expand: str = None) -> dict:
    """
    Get project details.
    
    Returns comprehensive information about a specific project.
    
    Required scopes: read:jira-work
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", f"/project/{project_key_or_id}", params=params)
    add_grounding("get_project", "docs/api_projects.md", "GET /rest/api/3/project/{projectKeyOrId}")
    return result


@mcp.tool()
def get_project_components(
    project_key_or_id: str,
    start: int = 0,
    max_results: int = 50,
) -> dict:
    """
    Get project components.
    
    Returns all components associated with the project.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", f"/project/{project_key_or_id}/components", params=params)
    add_grounding("get_project_components", "docs/api_project-components.md", "GET /rest/api/3/project/{projectKeyOrId}/components")
    return result


@mcp.tool()
def create_project_component(
    project_key_or_id: str,
    name: str,
    description: str = None,
    lead: dict = None,
    assignee_type: str = None,
    archived: bool = False,
) -> dict:
    """
    Create a project component.
    
    Adds a new component to the project for categorizing issues.
    
    Required scopes: write:jira-work
    """
    body = {"name": name, "archived": archived}
    
    if description:
        body["description"] = description
    if lead:
        body["lead"] = lead
    if assignee_type:
        body["assigneeType"] = assignee_type
    
    result = jira_request("POST", f"/project/{project_key_or_id}/components", data=body)
    add_grounding("create_project_component", "docs/api_project-components.md", "POST /rest/api/3/project/{projectKeyOrId}/components")
    return result


@mcp.tool()
def update_project_component(
    component_id: str,
    name: str = None,
    description: str = None,
    lead: dict = None,
    assignee_type: str = None,
    archived: bool = None,
) -> dict:
    """
    Update a project component.
    
    Modifies component details including name, description, and lead.
    
    Required scopes: write:jira-work
    """
    body = {}
    
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    if lead:
        body["lead"] = lead
    if assignee_type:
        body["assigneeType"] = assignee_type
    if archived is not None:
        body["archived"] = archived
    
    result = jira_request("PUT", f"/component/{component_id}", data=body)
    add_grounding("update_project_component", "docs/api_project-components.md", "PUT /rest/api/3/component/{id}")
    return result


@mcp.tool()
def delete_project_component(component_id: str) -> dict:
    """
    Delete a project component.
    
    Removes the component from the project. Note: This may fail if
    the component is in use by issues.
    
    Required scopes: delete:jira-work
    """
    result = jira_request("DELETE", f"/component/{component_id}")
    add_grounding("delete_project_component", "docs/api_project-components.md", "DEL /rest/api/3/component/{id}")
    return result


# =============================================================================
# Version (Release) Operations
# =============================================================================

@mcp.tool()
def get_project_versions(
    project_key_or_id: str,
    start: int = 0,
    max_results: int = 50,
    order_by: str = None,
    expand: str = None,
) -> dict:
    """
    Get project versions (releases).
    
    Returns all versions for the project.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", f"/project/{project_key_or_id}/versions", params=params)
    add_grounding("get_project_versions", "docs/api_project-versions.md", "GET /rest/api/3/project/{projectKeyOrId}/versions")
    return result


@mcp.tool()
def create_version(
    project_key_or_id: str,
    name: str,
    description: str = None,
    release_date: str = None,
    start_date: str = None,
    archived: bool = False,
    released: bool = False,
) -> dict:
    """
    Create a version (release).
    
    Creates a new version/release for the project.
    
    Required scopes: write:jira-work
    """
    body = {"name": name, "archived": archived, "released": released}
    
    if description:
        body["description"] = description
    if release_date:
        body["releaseDate"] = release_date
    if start_date:
        body["startDate"] = start_date
    
    result = jira_request("POST", f"/project/{project_key_or_id}/version", data=body)
    add_grounding("create_version", "docs/api_project-versions.md", "POST /rest/api/3/project/{projectKeyOrId}/version")
    return result


@mcp.tool()
def update_version(version_id: str, **fields) -> dict:
    """
    Update a version.
    
    Modifies version details including name, description, release date, etc.
    
    Required scopes: write:jira-work
    """
    result = jira_request("PUT", f"/version/{version_id}", data=fields)
    add_grounding("update_version", "docs/api_project-versions.md", "PUT /rest/api/3/version/{id}")
    return result


@mcp.tool()
def delete_version(version_id: str, move_fix_issues_to: str = None, move_affected_issues_to: str = None) -> dict:
    """
    Delete a version.
    
    Removes the version. Issues can be moved to another version.
    
    Required scopes: delete:jira-work
    """
    params = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    
    result = jira_request("DELETE", f"/version/{version_id}", params=params)
    add_grounding("delete_version", "docs/api_project-versions.md", "DEL /rest/api/3/version/{id}")
    return result


# =============================================================================
# User and Group Operations
# =============================================================================

@mcp.tool()
def get_user(account_id: str) -> dict:
    """
    Get user details by account ID.
    
    Returns comprehensive information about the user including
    display name, email, and avatar URLs.
    
    Required scopes: read:jira-user
    """
    params = {"accountId": account_id}
    result = jira_request("GET", "/user", params=params)
    add_grounding("get_user", "docs/api_users.md", "GET /rest/api/3/user")
    return result


@mcp.tool()
def search_users(
    query: str,
    start: int = 0,
    max_results: int = 50,
    include_inactive: bool = False,
    include_active: bool = True,
) -> dict:
    """
    Search for users.
    
    Finds users by display name, email, or account ID.
    
    Required scopes: read:jira-user
    """
    params = {
        "query": query,
        "startAt": start,
        "maxResults": max_results,
        "includeInactive": include_inactive,
        "includeActive": include_active,
    }
    
    result = jira_request("GET", "/user/search", params=params)
    add_grounding("search_users", "docs/api_users.md", "GET /rest/api/3/user/search")
    return result


@mcp.tool()
def get_myself() -> dict:
    """
    Get current user's details.
    
    Returns information about the authenticated user.
    
    Required scopes: read:jira-user
    """
    result = jira_request("GET", "/myself")
    add_grounding("get_myself", "docs/api_myself.md", "GET /rest/api/3/myself")
    return result


@mcp.tool()
def get_groups(query: str = None, exclude: str = None, start: int = 0, max_results: int = 50) -> dict:
    """
    Search for groups.
    
    Finds groups by name.
    
    Required scopes: read:jira-user
    """
    params = {"startAt": start, "maxResults": max_results}
    if query:
        params["query"] = query
    if exclude:
        params["exclude"] = exclude
    
    result = jira_request("GET", "/group", params=params)
    add_grounding("get_groups", "docs/api_groups.md", "GET /rest/api/3/group")
    return result


@mcp.tool()
def get_group_members(
    group_id: str,
    include_inactive: bool = False,
    start: int = 0,
    max_results: int = 50,
) -> dict:
    """
    Get members of a group.
    
    Returns paginated list of users in the group.
    
    Required scopes: read:jira-user
    """
    params = {
        "groupId": group_id,
        "includeInactiveUsers": include_inactive,
        "startAt": start,
        "maxResults": max_results,
    }
    
    result = jira_request("GET", "/group/member", params=params)
    add_grounding("get_group_members", "docs/api_groups.md", "GET /rest/api/3/group/member")
    return result


# =============================================================================
# Issue Type, Priority, Status Operations
# =============================================================================

@mcp.tool()
def get_issue_types(start: int = 0, max_results: int = 50) -> dict:
    """
    Get all issue types.
    
    Returns list of issue types available in the system.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/issuetype", params=params)
    add_grounding("get_issue_types", "docs/api_issue-types.md", "GET /rest/api/3/issuetype")
    return result


@mcp.tool()
def get_priorities(start: int = 0, max_results: int = 50) -> dict:
    """
    Get all priorities.
    
    Returns list of priority levels available in the system.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/priority", params=params)
    add_grounding("get_priorities", "docs/api_issue-priorities.md", "GET /rest/api/3/priority")
    return result


@mcp.tool()
def get_statuses(start: int = 0, max_results: int = 50) -> dict:
    """
    Get all statuses.
    
    Returns list of status values available in the system.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/status", params=params)
    add_grounding("get_statuses", "docs/api_status.md", "GET /rest/api/3/status")
    return result


# =============================================================================
# Filter and Dashboard Operations
# =============================================================================

@mcp.tool()
def get_filters(start: int = 0, max_results: int = 50) -> dict:
    """
    Get user's saved filters.
    
    Returns filters created or saved by the current user.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/filter/my", params=params)
    add_grounding("get_filters", "docs/api_filters.md", "GET /rest/api/3/filter/my")
    return result


@mcp.tool()
def get_filter(filter_id: str) -> dict:
    """
    Get filter details.
    
    Returns comprehensive information about a specific filter.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/filter/{filter_id}")
    add_grounding("get_filter", "docs/api_filters.md", "GET /rest/api/3/filter/{id}")
    return result


@mcp.tool()
def create_filter(name: str, jql: str, description: str = None) -> dict:
    """
    Create a new saved filter.
    
    Saves a JQL query as a reusable filter.
    
    Required scopes: write:jira-work
    """
    body = {"name": name, "jql": jql}
    if description:
        body["description"] = description
    
    result = jira_request("POST", "/filter", data=body)
    add_grounding("create_filter", "docs/api_filters.md", "POST /rest/api/3/filter")
    return result


@mcp.tool()
def update_filter(filter_id: str, name: str = None, jql: str = None, description: str = None) -> dict:
    """
    Update a saved filter.
    
    Modifies filter name, JQL, or description.
    
    Required scopes: write:jira-work
    """
    body = {}
    
    if name:
        body["name"] = name
    if jql:
        body["jql"] = jql
    if description:
        body["description"] = description
    
    result = jira_request("PUT", f"/filter/{filter_id}", data=body)
    add_grounding("update_filter", "docs/api_filters.md", "PUT /rest/api/3/filter/{id}")
    return result


@mcp.tool()
def delete_filter(filter_id: str) -> dict:
    """
    Delete a saved filter.
    
    Permanently removes the filter.
    
    Required scopes: delete:jira-work
    """
    result = jira_request("DELETE", f"/filter/{filter_id}")
    add_grounding("delete_filter", "docs/api_filters.md", "DEL /rest/api/3/filter/{id}")
    return result


@mcp.tool()
def get_dashboards(start: int = 0, max_results: int = 50) -> dict:
    """
    Get dashboards.
    
    Returns dashboards accessible to the current user.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/dashboard", params=params)
    add_grounding("get_dashboards", "docs/api_dashboards.md", "GET /rest/api/3/dashboard")
    return result


@mcp.tool()
def get_dashboard(dashboard_id: str) -> dict:
    """
    Get dashboard details.
    
    Returns comprehensive information about a specific dashboard.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/dashboard/{dashboard_id}")
    add_grounding("get_dashboard", "docs/api_dashboards.md", "GET /rest/api/3/dashboard/{id}")
    return result


# =============================================================================
# Metadata and Lookup Operations
# =============================================================================

@mcp.tool()
def get_issue_create_metadata(
    project_key_or_id: str = None,
    issue_type_id: str = None,
    expand: str = None,
) -> dict:
    """
    Get metadata for creating issues.
    
    Returns information about required and available fields when creating issues.
    This is essential for understanding what fields can be set.
    
    Required scopes: read:jira-work
    """
    if project_key_or_id and issue_type_id:
        path = f"/issue/createmeta/{project_key_or_id}/issuetypes/{issue_type_id}"
    elif project_key_or_id:
        path = f"/issue/createmeta/{project_key_or_id}/issuetypes"
    else:
        path = "/issue/createmeta"
    
    params = {}
    if expand:
        params["expand"] = expand
    
    result = jira_request("GET", path, params=params)
    add_grounding("get_issue_create_metadata", "docs/api_issues.md", "GET /rest/api/3/issue/createmeta")
    return result


@mcp.tool()
def get_issue_edit_metadata(issue_id_or_key: str) -> dict:
    """
    Get metadata for editing an issue.
    
    Returns information about which fields can be edited on the issue.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/issue/{issue_id_or_key}/editmeta")
    add_grounding("get_issue_edit_metadata", "docs/api_issues.md", "GET /rest/api/3/issue/{issueIdOrKey}/editmeta")
    return result


@mcp.tool()
def get_fields() -> dict:
    """
    Get all fields.
    
    Returns list of all fields available in the Jira instance.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", "/field")
    add_grounding("get_fields", "docs/api_issue-fields.md", "GET /rest/api/3/field")
    return result


@mcp.tool()
def get_field(field_id: str) -> dict:
    """
    Get field details.
    
    Returns comprehensive information about a specific field.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/field/{field_id}")
    add_grounding("get_field", "docs/api_issue-fields.md", "GET /rest/api/3/field/{id}")
    return result


# =============================================================================
# Application and Server Information
# =============================================================================

@mcp.tool()
def get_server_info() -> dict:
    """
    Get Jira server information.
    
    Returns version, base URL, and other server details.
    
    Required scopes: None (anonymous access)
    """
    result = jira_request("GET", "/serverInfo")
    add_grounding("get_server_info", "docs/api_server-info.md", "GET /rest/api/3/serverInfo")
    return result


@mcp.tool()
def get_application_roles() -> dict:
    """
    Get application roles.
    
    Returns list of application roles in Jira (Software, Core, Service Desk).
    
    Required scopes: read:jira-application
    """
    result = jira_request("GET", "/applicationrole")
    add_grounding("get_application_roles", "docs/api_application-roles.md", "GET /rest/api/3/applicationrole")
    return result


@mcp.tool()
def get_workflow_statuses() -> dict:
    """
    Get workflow status categories.
    
    Returns the categories that workflow statuses can belong to.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", "/statuscategory")
    add_grounding("get_workflow_statuses", "docs/api_workflow-status-categories.md", "GET /rest/api/3/statuscategory")
    return result


# =============================================================================
# Issue Archive/Unarchive Operations
# =============================================================================

@mcp.tool()
def archive_issues(issue_ids_or_keys: list) -> dict:
    """
    Archive multiple issues by ID or key.
    
    Archives issues in bulk (up to 1000 issues). Only works for software,
    service management, and business projects.
    
    Required scopes: write:jira-work
    """
    body = {"issueIdsOrKeys": issue_ids_or_keys}
    result = jira_request("PUT", "/issue/archive", data=body)
    add_grounding("archive_issues", "docs/api_issues.md", "PUT /rest/api/3/issue/archive")
    return result


@mcp.tool()
def unarchive_issues(issue_ids_or_keys: list) -> dict:
    """
    Unarchive multiple issues by ID or key.
    
    Restores archived issues in bulk (up to 1000 issues).
    
    Required scopes: write:jira-work
    """
    body = {"issueIdsOrKeys": issue_ids_or_keys}
    result = jira_request("PUT", "/issue/unarchive", data=body)
    add_grounding("unarchive_issues", "docs/api_issues.md", "PUT /rest/api/3/issue/unarchive")
    return result


# =============================================================================
# Issue Changelog
# =============================================================================

@mcp.tool()
def get_issue_changelog(issue_id_or_key: str) -> dict:
    """
    Get changelog for an issue.
    
    Returns the history of all changes made to the issue.
    
    Required scopes: read:jira-work
    """
    result = jira_request("GET", f"/issue/{issue_id_or_key}/changelog")
    add_grounding("get_issue_changelog", "docs/api_issues.md", "GET /rest/api/3/issue/{issueIdOrKey}/changelog")
    return result


@mcp.tool()
def bulk_fetch_changelogs(issue_ids_or_keys: list, field_ids: list = None) -> dict:
    """
    Bulk fetch changelogs for multiple issues.
    
    Returns changelogs for multiple issues in a single request.
    
    Required scopes: read:jira-work
    """
    body = {"issueIdsOrKeys": issue_ids_or_keys}
    if field_ids:
        body["fieldIds"] = field_ids
    
    result = jira_request("POST", "/changelog/bulkfetch", data=body)
    add_grounding("bulk_fetch_changelogs", "docs/api_issues.md", "POST /rest/api/3/changelog/bulkfetch")
    return result


# =============================================================================
# Issue Notification
# =============================================================================

@mcp.tool()
def send_issue_notification(
    issue_id_or_key: str,
    subject: str,
    body: str,
    to: dict = None,
    group: dict = None,
) -> dict:
    """
    Send a notification about an issue.
    
    Sends an email notification about the issue to specified users or groups.
    
    Required scopes: write:jira-work
    """
    body_obj = {
        "subject": subject,
        "body": body,
    }
    
    if to:
        body_obj["to"] = to
    if group:
        body_obj["group"] = group
    
    result = jira_request("POST", f"/issue/{issue_id_or_key}/notify", data=body_obj)
    add_grounding("send_issue_notification", "docs/api_issues.md", "POST /rest/api/3/issue/{issueIdOrKey}/notify")
    return result


# =============================================================================
# Issue Resolution
# =============================================================================

@mcp.tool()
def get_resolutions(start: int = 0, max_results: int = 50) -> dict:
    """
    Get all resolutions.
    
    Returns list of resolution values available in the system.
    
    Required scopes: read:jira-work
    """
    params = {"startAt": start, "maxResults": max_results}
    result = jira_request("GET", "/resolution", params=params)
    add_grounding("get_resolutions", "docs/api_issue-resolutions.md", "GET /rest/api/3/resolution")
    return result


# =============================================================================
# Issue Security
# =============================================================================

@mcp.tool()
def get_issue_security_levels(project_id: str) -> dict:
    """
    Get issue security levels for a project.
    
    Returns the security levels configured for the project.
    
    Required scopes: read:jira-work
    """
    params = {"projectId": project_id}
    result = jira_request("GET", "/issuesecurityschemes/project", params=params)
    add_grounding("get_issue_security_levels", "docs/api_issue-security-schemes.md", "GET /rest/api/3/issuesecurityschemes/project")
    return result


# =============================================================================
# Custom Fields
# =============================================================================

@mcp.tool()
def get_custom_fields(start: int = 0, max_results: int = 50) -> dict:
    """
    Get all custom fields.
    
    Returns list of all custom fields in the system.
    
    Required scopes: read:jira-work
    """
    # Custom fields are identified by the "custom" prefix in field ID
    all_fields = get_fields()
    if "error" not in all_fields:
        custom_fields = [f for f in all_fields.get("values", []) if f.get("key", "").startswith("custom")]
        return {"values": custom_fields, "total": len(custom_fields)}
    return all_fields


# =============================================================================
# Additional JQL Search Operations
# =============================================================================

@mcp.tool()
def jql_match(issue_ids: list, jqls: list) -> dict:
    """
    Check if issues match JQL queries.
    
    Determines which issues would be returned by each JQL query.
    
    Required scopes: read:jira-work
    """
    body = {"issueIds": issue_ids, "jqls": jqls}
    result = jira_request("POST", "/jql/match", data=body)
    add_grounding("jql_match", "docs/api_issue-search.md", "POST /rest/api/3/jql/match")
    return result


# =============================================================================
# Main entry point
# =============================================================================

if __name__ == "__main__":
    # Print grounding map for verification
    print(json.dumps(grounding_map, indent=2))
