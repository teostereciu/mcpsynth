#!/usr/bin/env python3
"""
Jira Cloud REST API v3 MCP Server

This server provides comprehensive access to the Jira Cloud REST API v3,
enabling autonomous agents to perform real-world Jira operations.
"""

import os
import json
import base64
from typing import Any, Optional
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("jira-mcp")

# Configuration from environment
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# API base URL
API_BASE = f"{JIRA_BASE_URL}/rest/api/3"

# Setup authentication
def get_auth_header():
    """Generate HTTP Basic Auth header for Jira API."""
    credentials = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def make_request(method: str, endpoint: str, **kwargs) -> dict:
    """Make an authenticated HTTP request to Jira API."""
    url = f"{API_BASE}{endpoint}"
    headers = get_auth_header()
    headers["Accept"] = "application/json"
    
    if "json" in kwargs:
        headers["Content-Type"] = "application/json"
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        
        # Handle different status codes
        if response.status_code in [200, 201, 204]:
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found"}
        elif response.status_code == 400:
            try:
                return response.json()
            except:
                return {"error": "Bad request"}
        elif response.status_code == 401:
            return {"error": "Unauthorized - check credentials"}
        elif response.status_code == 403:
            return {"error": "Forbidden - insufficient permissions"}
        else:
            return {"error": f"HTTP {response.status_code}: {response.text[:200]}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# ISSUE OPERATIONS
# ============================================================================

@mcp.tool()
def create_issue(
    project_key: str,
    issue_type: str,
    summary: str,
    description: Optional[str] = None,
    assignee_id: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[list] = None,
    components: Optional[list] = None,
    due_date: Optional[str] = None,
) -> dict:
    """Create a new issue in Jira."""
    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": issue_type},
        "summary": summary,
    }
    
    if description:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": description}]
                }
            ]
        }
    
    if assignee_id:
        fields["assignee"] = {"id": assignee_id}
    
    if priority:
        fields["priority"] = {"name": priority}
    
    if labels:
        fields["labels"] = labels
    
    if components:
        fields["components"] = [{"id": c} for c in components]
    
    if due_date:
        fields["duedate"] = due_date
    
    return make_request("POST", "/issue", json={"fields": fields})

@mcp.tool()
def get_issue(issue_key: str, expand: Optional[str] = None) -> dict:
    """Get details of a specific issue."""
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", f"/issue/{issue_key}", params=params)

@mcp.tool()
def update_issue(
    issue_key: str,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    assignee_id: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[list] = None,
) -> dict:
    """Update an existing issue."""
    fields = {}
    
    if summary:
        fields["summary"] = summary
    
    if description:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": description}]
                }
            ]
        }
    
    if assignee_id:
        fields["assignee"] = {"id": assignee_id}
    
    if priority:
        fields["priority"] = {"name": priority}
    
    if labels:
        fields["labels"] = labels
    
    return make_request("PUT", f"/issue/{issue_key}", json={"fields": fields})

@mcp.tool()
def delete_issue(issue_key: str) -> dict:
    """Delete an issue."""
    return make_request("DELETE", f"/issue/{issue_key}")

@mcp.tool()
def search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[list] = None,
    expand: Optional[str] = None,
) -> dict:
    """Search for issues using JQL."""
    body = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
    }
    
    if fields:
        body["fields"] = fields
    
    if expand:
        body["expand"] = expand
    
    return make_request("POST", "/search", json=body)

@mcp.tool()
def get_issue_transitions(issue_key: str) -> dict:
    """Get available transitions for an issue."""
    return make_request("GET", f"/issue/{issue_key}/transitions")

@mcp.tool()
def transition_issue(issue_key: str, transition_id: str, comment: Optional[str] = None) -> dict:
    """Transition an issue to a new status."""
    body = {"transition": {"id": transition_id}}
    
    if comment:
        body["update"] = {
            "comment": [
                {
                    "add": {
                        "body": {
                            "type": "doc",
                            "version": 1,
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [{"type": "text", "text": comment}]
                                }
                            ]
                        }
                    }
                }
            ]
        }
    
    return make_request("POST", f"/issue/{issue_key}/transitions", json=body)

@mcp.tool()
def assign_issue(issue_key: str, assignee_id: str) -> dict:
    """Assign an issue to a user."""
    return make_request("PUT", f"/issue/{issue_key}/assignee", json={"accountId": assignee_id})

# ============================================================================
# ISSUE COMMENTS
# ============================================================================

@mcp.tool()
def add_comment(issue_key: str, comment_text: str, visibility_type: Optional[str] = None, visibility_value: Optional[str] = None) -> dict:
    """Add a comment to an issue."""
    body = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment_text}]
                }
            ]
        }
    }
    
    if visibility_type and visibility_value:
        body["visibility"] = {
            "type": visibility_type,
            "value": visibility_value
        }
    
    return make_request("POST", f"/issue/{issue_key}/comment", json=body)

@mcp.tool()
def get_comments(issue_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Get all comments for an issue."""
    params = {"startAt": start_at, "maxResults": max_results}
    return make_request("GET", f"/issue/{issue_key}/comment", params=params)

@mcp.tool()
def get_comment(issue_key: str, comment_id: str) -> dict:
    """Get a specific comment."""
    return make_request("GET", f"/issue/{issue_key}/comment/{comment_id}")

@mcp.tool()
def update_comment(issue_key: str, comment_id: str, comment_text: str) -> dict:
    """Update a comment."""
    body = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment_text}]
                }
            ]
        }
    }
    return make_request("PUT", f"/issue/{issue_key}/comment/{comment_id}", json=body)

@mcp.tool()
def delete_comment(issue_key: str, comment_id: str) -> dict:
    """Delete a comment."""
    return make_request("DELETE", f"/issue/{issue_key}/comment/{comment_id}")

# ============================================================================
# ISSUE WORKLOGS
# ============================================================================

@mcp.tool()
def add_worklog(
    issue_key: str,
    time_spent_seconds: int,
    started: Optional[str] = None,
    comment: Optional[str] = None,
) -> dict:
    """Add a worklog entry to an issue."""
    body = {"timeSpentSeconds": time_spent_seconds}
    
    if started:
        body["started"] = started
    
    if comment:
        body["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    
    return make_request("POST", f"/issue/{issue_key}/worklog", json=body)

@mcp.tool()
def get_worklogs(issue_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Get all worklogs for an issue."""
    params = {"startAt": start_at, "maxResults": max_results}
    return make_request("GET", f"/issue/{issue_key}/worklog", params=params)

@mcp.tool()
def get_worklog(issue_key: str, worklog_id: str) -> dict:
    """Get a specific worklog."""
    return make_request("GET", f"/issue/{issue_key}/worklog/{worklog_id}")

@mcp.tool()
def update_worklog(
    issue_key: str,
    worklog_id: str,
    time_spent_seconds: Optional[int] = None,
    comment: Optional[str] = None,
) -> dict:
    """Update a worklog entry."""
    body = {}
    
    if time_spent_seconds:
        body["timeSpentSeconds"] = time_spent_seconds
    
    if comment:
        body["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    
    return make_request("PUT", f"/issue/{issue_key}/worklog/{worklog_id}", json=body)

@mcp.tool()
def delete_worklog(issue_key: str, worklog_id: str) -> dict:
    """Delete a worklog entry."""
    return make_request("DELETE", f"/issue/{issue_key}/worklog/{worklog_id}")

# ============================================================================
# PROJECTS
# ============================================================================

@mcp.tool()
def get_all_projects(expand: Optional[str] = None) -> dict:
    """Get all projects visible to the user."""
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", "/project", params=params)

@mcp.tool()
def get_projects_paginated(
    start_at: int = 0,
    max_results: int = 50,
    order_by: Optional[str] = None,
    query: Optional[str] = None,
) -> dict:
    """Get projects with pagination."""
    params = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if query:
        params["query"] = query
    return make_request("GET", "/project/search", params=params)

@mcp.tool()
def get_project(project_key: str, expand: Optional[str] = None) -> dict:
    """Get details of a specific project."""
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", f"/project/{project_key}", params=params)

@mcp.tool()
def create_project(
    key: str,
    name: str,
    project_type_key: str,
    project_template_key: str,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
) -> dict:
    """Create a new project."""
    body = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
    }
    
    if description:
        body["description"] = description
    
    if lead_account_id:
        body["leadAccountId"] = lead_account_id
    
    return make_request("POST", "/project", json=body)

@mcp.tool()
def update_project(
    project_key: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a project."""
    body = {}
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    
    return make_request("PUT", f"/project/{project_key}", json=body)

@mcp.tool()
def delete_project(project_key: str) -> dict:
    """Delete a project."""
    return make_request("DELETE", f"/project/{project_key}")

@mcp.tool()
def get_project_statuses(project_key: str) -> dict:
    """Get all statuses available in a project."""
    return make_request("GET", f"/project/{project_key}/statuses")

# ============================================================================
# USERS
# ============================================================================

@mcp.tool()
def get_user(account_id: Optional[str] = None, username: Optional[str] = None) -> dict:
    """Get user details."""
    params = {}
    if account_id:
        params["accountId"] = account_id
    elif username:
        params["username"] = username
    
    return make_request("GET", "/user", params=params)

@mcp.tool()
def get_users_bulk(
    account_ids: list,
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Get multiple users by account IDs."""
    params = {
        "startAt": start_at,
        "maxResults": max_results,
        "accountId": account_ids,
    }
    return make_request("GET", "/user/bulk", params=params)

@mcp.tool()
def search_users(
    query: str,
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Search for users."""
    params = {
        "query": query,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return make_request("GET", "/users/search", params=params)

@mcp.tool()
def create_user(
    email: str,
    display_name: Optional[str] = None,
) -> dict:
    """Create a new user."""
    body = {
        "emailAddress": email,
        "products": ["jira-software"],
    }
    
    if display_name:
        body["displayName"] = display_name
    
    return make_request("POST", "/user", json=body)

@mcp.tool()
def delete_user(account_id: str) -> dict:
    """Delete a user."""
    params = {"accountId": account_id}
    return make_request("DELETE", "/user", params=params)

# ============================================================================
# GROUPS
# ============================================================================

@mcp.tool()
def get_group(group_id: Optional[str] = None, group_name: Optional[str] = None) -> dict:
    """Get group details."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    elif group_name:
        params["groupname"] = group_name
    
    return make_request("GET", "/group", params=params)

@mcp.tool()
def get_groups_bulk(
    group_ids: Optional[list] = None,
    group_names: Optional[list] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Get multiple groups."""
    params = {"startAt": start_at, "maxResults": max_results}
    
    if group_ids:
        params["groupId"] = group_ids
    if group_names:
        params["groupName"] = group_names
    
    return make_request("GET", "/group/bulk", params=params)

@mcp.tool()
def get_group_members(
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Get members of a group."""
    params = {"startAt": start_at, "maxResults": max_results}
    
    if group_id:
        params["groupId"] = group_id
    elif group_name:
        params["groupname"] = group_name
    
    return make_request("GET", "/group/member", params=params)

@mcp.tool()
def create_group(name: str) -> dict:
    """Create a new group."""
    return make_request("POST", "/group", json={"name": name})

@mcp.tool()
def delete_group(group_id: Optional[str] = None, group_name: Optional[str] = None) -> dict:
    """Delete a group."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    elif group_name:
        params["groupname"] = group_name
    
    return make_request("DELETE", "/group", params=params)

@mcp.tool()
def add_user_to_group(
    account_id: str,
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
) -> dict:
    """Add a user to a group."""
    params = {"accountId": account_id}
    
    if group_id:
        params["groupId"] = group_id
    elif group_name:
        params["groupname"] = group_name
    
    return make_request("POST", "/group/user", json={"accountId": account_id}, params=params)

@mcp.tool()
def remove_user_from_group(
    account_id: str,
    group_id: Optional[str] = None,
    group_name: Optional[str] = None,
) -> dict:
    """Remove a user from a group."""
    params = {"accountId": account_id}
    
    if group_id:
        params["groupId"] = group_id
    elif group_name:
        params["groupname"] = group_name
    
    return make_request("DELETE", "/group/user", params=params)

@mcp.tool()
def find_groups(query: str, max_results: int = 50) -> dict:
    """Find groups by name."""
    params = {"query": query, "maxResults": max_results}
    return make_request("GET", "/groups/picker", params=params)

# ============================================================================
# FILTERS
# ============================================================================

@mcp.tool()
def create_filter(
    name: str,
    jql: str,
    description: Optional[str] = None,
    favourite: bool = False,
) -> dict:
    """Create a new filter."""
    body = {
        "name": name,
        "jql": jql,
        "favourite": favourite,
    }
    
    if description:
        body["description"] = description
    
    return make_request("POST", "/filter", json=body)

@mcp.tool()
def get_filter(filter_id: str) -> dict:
    """Get a specific filter."""
    return make_request("GET", f"/filter/{filter_id}")

@mcp.tool()
def get_favorite_filters() -> dict:
    """Get user's favorite filters."""
    return make_request("GET", "/filter/favourite")

@mcp.tool()
def get_my_filters(include_favourites: bool = False) -> dict:
    """Get filters owned by the user."""
    params = {"includeFavourites": include_favourites}
    return make_request("GET", "/filter/my", params=params)

@mcp.tool()
def search_filters(
    filter_name: Optional[str] = None,
    owner_account_id: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Search for filters."""
    params = {"startAt": start_at, "maxResults": max_results}
    
    if filter_name:
        params["filterName"] = filter_name
    if owner_account_id:
        params["accountId"] = owner_account_id
    
    return make_request("GET", "/filter/search", params=params)

@mcp.tool()
def update_filter(
    filter_id: str,
    name: Optional[str] = None,
    jql: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a filter."""
    body = {}
    
    if name:
        body["name"] = name
    if jql:
        body["jql"] = jql
    if description:
        body["description"] = description
    
    return make_request("PUT", f"/filter/{filter_id}", json=body)

@mcp.tool()
def delete_filter(filter_id: str) -> dict:
    """Delete a filter."""
    return make_request("DELETE", f"/filter/{filter_id}")

@mcp.tool()
def add_filter_as_favorite(filter_id: str) -> dict:
    """Add a filter to favorites."""
    return make_request("PUT", f"/filter/{filter_id}/favourite", json={})

@mcp.tool()
def remove_filter_as_favorite(filter_id: str) -> dict:
    """Remove a filter from favorites."""
    return make_request("DELETE", f"/filter/{filter_id}/favourite")

# ============================================================================
# ISSUE TYPES
# ============================================================================

@mcp.tool()
def get_issue_types() -> dict:
    """Get all issue types."""
    return make_request("GET", "/issuetype")

@mcp.tool()
def get_issue_type(issue_type_id: str) -> dict:
    """Get a specific issue type."""
    return make_request("GET", f"/issuetype/{issue_type_id}")

# ============================================================================
# PRIORITIES
# ============================================================================

@mcp.tool()
def get_priorities() -> dict:
    """Get all priorities."""
    return make_request("GET", "/priority")

@mcp.tool()
def get_priority(priority_id: str) -> dict:
    """Get a specific priority."""
    return make_request("GET", f"/priority/{priority_id}")

# ============================================================================
# STATUSES
# ============================================================================

@mcp.tool()
def get_statuses() -> dict:
    """Get all statuses."""
    return make_request("GET", "/status")

@mcp.tool()
def get_status(status_id: str) -> dict:
    """Get a specific status."""
    return make_request("GET", f"/status/{status_id}")

# ============================================================================
# FIELDS
# ============================================================================

@mcp.tool()
def get_fields() -> dict:
    """Get all fields."""
    return make_request("GET", "/field")

@mcp.tool()
def create_custom_field(
    name: str,
    field_type: str,
    description: Optional[str] = None,
) -> dict:
    """Create a custom field."""
    body = {
        "name": name,
        "type": field_type,
    }
    
    if description:
        body["description"] = description
    
    return make_request("POST", "/field", json=body)

# ============================================================================
# ISSUE LINKS
# ============================================================================

@mcp.tool()
def create_issue_link(
    link_type: str,
    inward_issue: str,
    outward_issue: str,
) -> dict:
    """Create a link between two issues."""
    body = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue},
        "outwardIssue": {"key": outward_issue},
    }
    return make_request("POST", "/issueLink", json=body)

@mcp.tool()
def get_issue_link(link_id: str) -> dict:
    """Get a specific issue link."""
    return make_request("GET", f"/issueLink/{link_id}")

@mcp.tool()
def delete_issue_link(link_id: str) -> dict:
    """Delete an issue link."""
    return make_request("DELETE", f"/issueLink/{link_id}")

# ============================================================================
# ISSUE WATCHERS
# ============================================================================

@mcp.tool()
def get_issue_watchers(issue_key: str) -> dict:
    """Get watchers of an issue."""
    return make_request("GET", f"/issue/{issue_key}/watchers")

@mcp.tool()
def add_issue_watcher(issue_key: str, account_id: str) -> dict:
    """Add a watcher to an issue."""
    return make_request("POST", f"/issue/{issue_key}/watchers", json=account_id)

@mcp.tool()
def remove_issue_watcher(issue_key: str, account_id: str) -> dict:
    """Remove a watcher from an issue."""
    params = {"accountId": account_id}
    return make_request("DELETE", f"/issue/{issue_key}/watchers", params=params)

# ============================================================================
# ISSUE ATTACHMENTS
# ============================================================================

@mcp.tool()
def get_attachment(attachment_id: str) -> dict:
    """Get attachment metadata."""
    return make_request("GET", f"/attachment/{attachment_id}")

@mcp.tool()
def delete_attachment(attachment_id: str) -> dict:
    """Delete an attachment."""
    return make_request("DELETE", f"/attachment/{attachment_id}")

# ============================================================================
# ISSUE VOTES
# ============================================================================

@mcp.tool()
def get_issue_votes(issue_key: str) -> dict:
    """Get votes on an issue."""
    return make_request("GET", f"/issue/{issue_key}/votes")

@mcp.tool()
def add_issue_vote(issue_key: str) -> dict:
    """Vote for an issue."""
    return make_request("POST", f"/issue/{issue_key}/votes", json={})

@mcp.tool()
def remove_issue_vote(issue_key: str) -> dict:
    """Remove vote from an issue."""
    return make_request("DELETE", f"/issue/{issue_key}/votes")

# ============================================================================
# COMPONENTS
# ============================================================================

@mcp.tool()
def get_project_components(project_key: str) -> dict:
    """Get all components in a project."""
    return make_request("GET", f"/project/{project_key}/components")

@mcp.tool()
def get_component(component_id: str) -> dict:
    """Get a specific component."""
    return make_request("GET", f"/component/{component_id}")

@mcp.tool()
def create_component(
    project_key: str,
    name: str,
    description: Optional[str] = None,
) -> dict:
    """Create a component in a project."""
    body = {
        "name": name,
        "project": project_key,
    }
    
    if description:
        body["description"] = description
    
    return make_request("POST", "/component", json=body)

@mcp.tool()
def update_component(
    component_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a component."""
    body = {}
    
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    
    return make_request("PUT", f"/component/{component_id}", json=body)

@mcp.tool()
def delete_component(component_id: str) -> dict:
    """Delete a component."""
    return make_request("DELETE", f"/component/{component_id}")

# ============================================================================
# VERSIONS
# ============================================================================

@mcp.tool()
def get_project_versions(project_key: str) -> dict:
    """Get all versions in a project."""
    return make_request("GET", f"/project/{project_key}/versions")

@mcp.tool()
def get_version(version_id: str) -> dict:
    """Get a specific version."""
    return make_request("GET", f"/version/{version_id}")

@mcp.tool()
def create_version(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    released: bool = False,
    release_date: Optional[str] = None,
) -> dict:
    """Create a version in a project."""
    body = {
        "name": name,
        "project": project_key,
        "released": released,
    }
    
    if description:
        body["description"] = description
    if release_date:
        body["releaseDate"] = release_date
    
    return make_request("POST", "/version", json=body)

@mcp.tool()
def update_version(
    version_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    released: Optional[bool] = None,
    release_date: Optional[str] = None,
) -> dict:
    """Update a version."""
    body = {}
    
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    if released is not None:
        body["released"] = released
    if release_date:
        body["releaseDate"] = release_date
    
    return make_request("PUT", f"/version/{version_id}", json=body)

@mcp.tool()
def delete_version(version_id: str) -> dict:
    """Delete a version."""
    return make_request("DELETE", f"/version/{version_id}")

# ============================================================================
# ISSUE PROPERTIES
# ============================================================================

@mcp.tool()
def get_issue_property(issue_key: str, property_key: str) -> dict:
    """Get a property of an issue."""
    return make_request("GET", f"/issue/{issue_key}/properties/{property_key}")

@mcp.tool()
def set_issue_property(issue_key: str, property_key: str, value: Any) -> dict:
    """Set a property on an issue."""
    return make_request("PUT", f"/issue/{issue_key}/properties/{property_key}", json=value)

@mcp.tool()
def delete_issue_property(issue_key: str, property_key: str) -> dict:
    """Delete a property from an issue."""
    return make_request("DELETE", f"/issue/{issue_key}/properties/{property_key}")

# ============================================================================
# MYSELF
# ============================================================================

@mcp.tool()
def get_current_user() -> dict:
    """Get the current user's details."""
    return make_request("GET", "/myself")

# ============================================================================
# SERVER INFO
# ============================================================================

@mcp.tool()
def get_server_info() -> dict:
    """Get Jira server information."""
    return make_request("GET", "/serverInfo")

# ============================================================================
# ADDITIONAL ISSUE TYPE OPERATIONS
# ============================================================================

@mcp.tool()
def create_issue_type(
    name: str,
    issue_type: str = "standard",
    description: Optional[str] = None,
) -> dict:
    """Create a new issue type."""
    body = {
        "name": name,
        "type": issue_type,
    }
    
    if description:
        body["description"] = description
    
    return make_request("POST", "/issuetype", json=body)

@mcp.tool()
def update_issue_type(
    issue_type_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update an issue type."""
    body = {}
    
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    
    return make_request("PUT", f"/issuetype/{issue_type_id}", json=body)

@mcp.tool()
def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> dict:
    """Delete an issue type."""
    params = {}
    if alternative_issue_type_id:
        params["alternativeIssueTypeId"] = alternative_issue_type_id
    
    return make_request("DELETE", f"/issuetype/{issue_type_id}", params=params)

@mcp.tool()
def get_issue_types_for_project(project_id: int) -> dict:
    """Get issue types for a specific project."""
    params = {"projectId": project_id}
    return make_request("GET", "/issuetype/project", params=params)

@mcp.tool()
def get_alternative_issue_types(issue_type_id: str) -> dict:
    """Get alternative issue types that can replace the given issue type."""
    return make_request("GET", f"/issuetype/{issue_type_id}/alternatives")

# ============================================================================
# ADDITIONAL PRIORITY OPERATIONS
# ============================================================================

@mcp.tool()
def create_priority(
    name: str,
    description: Optional[str] = None,
) -> dict:
    """Create a new priority."""
    body = {"name": name}
    
    if description:
        body["description"] = description
    
    return make_request("POST", "/priority", json=body)

@mcp.tool()
def update_priority(
    priority_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a priority."""
    body = {}
    
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    
    return make_request("PUT", f"/priority/{priority_id}", json=body)

@mcp.tool()
def delete_priority(priority_id: str) -> dict:
    """Delete a priority."""
    return make_request("DELETE", f"/priority/{priority_id}")

# ============================================================================
# ISSUE CHANGELOG
# ============================================================================

@mcp.tool()
def get_issue_changelog(issue_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Get the changelog for an issue."""
    params = {"startAt": start_at, "maxResults": max_results}
    return make_request("GET", f"/issue/{issue_key}/changelog", params=params)

# ============================================================================
# ISSUE EDIT METADATA
# ============================================================================

@mcp.tool()
def get_issue_edit_metadata(issue_key: str) -> dict:
    """Get metadata for editing an issue."""
    return make_request("GET", f"/issue/{issue_key}/editmeta")

# ============================================================================
# ISSUE CREATE METADATA
# ============================================================================

@mcp.tool()
def get_create_issue_metadata(project_key: str, issue_type_id: Optional[str] = None) -> dict:
    """Get metadata for creating an issue."""
    if issue_type_id:
        return make_request("GET", f"/issue/createmeta/{project_key}/issuetypes/{issue_type_id}")
    else:
        return make_request("GET", f"/issue/createmeta/{project_key}/issuetypes")

# ============================================================================
# ISSUE BULK OPERATIONS
# ============================================================================

@mcp.tool()
def bulk_delete_issues(issue_ids_or_keys: list) -> dict:
    """Bulk delete issues."""
    body = {"issueIdsOrKeys": issue_ids_or_keys}
    return make_request("PUT", "/issue/archive", json=body)

@mcp.tool()
def bulk_edit_issues(
    issue_ids_or_keys: list,
    fields: dict,
) -> dict:
    """Bulk edit multiple issues."""
    body = {
        "issueIdsOrKeys": issue_ids_or_keys,
        "fields": fields,
    }
    return make_request("POST", "/issue/bulk", json=body)

# ============================================================================
# ISSUE LINK TYPES
# ============================================================================

@mcp.tool()
def get_issue_link_types() -> dict:
    """Get all issue link types."""
    return make_request("GET", "/issueLinkType")

@mcp.tool()
def get_issue_link_type(link_type_id: str) -> dict:
    """Get a specific issue link type."""
    return make_request("GET", f"/issueLinkType/{link_type_id}")

@mcp.tool()
def create_issue_link_type(
    name: str,
    inward: str,
    outward: str,
) -> dict:
    """Create a new issue link type."""
    body = {
        "name": name,
        "inward": inward,
        "outward": outward,
    }
    return make_request("POST", "/issueLinkType", json=body)

@mcp.tool()
def update_issue_link_type(
    link_type_id: str,
    name: Optional[str] = None,
    inward: Optional[str] = None,
    outward: Optional[str] = None,
) -> dict:
    """Update an issue link type."""
    body = {}
    
    if name:
        body["name"] = name
    if inward:
        body["inward"] = inward
    if outward:
        body["outward"] = outward
    
    return make_request("PUT", f"/issueLinkType/{link_type_id}", json=body)

@mcp.tool()
def delete_issue_link_type(link_type_id: str) -> dict:
    """Delete an issue link type."""
    return make_request("DELETE", f"/issueLinkType/{link_type_id}")

# ============================================================================
# RESOLUTIONS
# ============================================================================

@mcp.tool()
def get_resolutions() -> dict:
    """Get all resolutions."""
    return make_request("GET", "/resolution")

@mcp.tool()
def get_resolution(resolution_id: str) -> dict:
    """Get a specific resolution."""
    return make_request("GET", f"/resolution/{resolution_id}")

# ============================================================================
# LABELS
# ============================================================================

@mcp.tool()
def get_labels(start_at: int = 0, max_results: int = 50) -> dict:
    """Get all labels."""
    params = {"startAt": start_at, "maxResults": max_results}
    return make_request("GET", "/labels", params=params)

# ============================================================================
# PROJECT ROLES
# ============================================================================

@mcp.tool()
def get_project_roles(project_key: str) -> dict:
    """Get all roles in a project."""
    return make_request("GET", f"/project/{project_key}/roles")

@mcp.tool()
def get_project_role(project_key: str, role_id: str) -> dict:
    """Get a specific role in a project."""
    return make_request("GET", f"/project/{project_key}/roles/{role_id}")

@mcp.tool()
def add_user_to_project_role(
    project_key: str,
    role_id: str,
    account_id: str,
) -> dict:
    """Add a user to a project role."""
    body = {"user": [account_id]}
    return make_request("POST", f"/project/{project_key}/roles/{role_id}", json=body)

@mcp.tool()
def remove_user_from_project_role(
    project_key: str,
    role_id: str,
    account_id: str,
) -> dict:
    """Remove a user from a project role."""
    params = {"user": account_id}
    return make_request("DELETE", f"/project/{project_key}/roles/{role_id}", params=params)

# ============================================================================
# ISSUE SECURITY LEVELS
# ============================================================================

@mcp.tool()
def get_issue_security_levels(project_key: str) -> dict:
    """Get all security levels in a project."""
    return make_request("GET", f"/project/{project_key}/securitylevel")

if __name__ == "__main__":
    mcp.run()
