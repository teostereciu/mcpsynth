#!/usr/bin/env python3
"""
MCP Server for Jira Cloud REST API v3
Provides tools for managing issues, projects, users, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from base64 import b64encode
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("jira-server")

# Configuration from environment
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# API base URL
API_BASE = f"{JIRA_BASE_URL}/rest/api/3"

# Helper function to create auth header
def get_auth_header() -> dict:
    """Create HTTP Basic Auth header for Jira API."""
    credentials = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
    encoded = b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

# Helper function for API requests
def api_request(
    method: str,
    endpoint: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> dict:
    """Make an API request to Jira."""
    url = f"{API_BASE}{endpoint}"
    req_headers = get_auth_header()
    req_headers["Accept"] = "application/json"
    req_headers["Content-Type"] = "application/json"
    if headers:
        req_headers.update(headers)
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=req_headers, params=params, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, headers=req_headers, json=data, params=params, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=req_headers, json=data, params=params, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=req_headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {
                "error": f"HTTP {response.status_code}",
                "message": response.text[:500] if response.text else "No response body"
            }
        
        if response.status_code == 204:
            return {"success": True}
        
        try:
            return response.json()
        except:
            return {"success": True, "status_code": response.status_code}
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# ISSUES TOOLS
# ============================================================================

@server.tool()
def create_issue(
    project_id: str,
    issue_type: str,
    summary: str,
    description: Optional[str] = None,
    assignee_id: Optional[str] = None,
    priority_id: Optional[str] = None,
    labels: Optional[list] = None,
    components: Optional[list] = None,
    due_date: Optional[str] = None,
) -> dict:
    """Create a new issue in Jira."""
    fields = {
        "project": {"id": project_id},
        "issuetype": {"id": issue_type},
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
    
    if priority_id:
        fields["priority"] = {"id": priority_id}
    
    if labels:
        fields["labels"] = labels
    
    if components:
        fields["components"] = [{"id": c} for c in components]
    
    if due_date:
        fields["duedate"] = due_date
    
    return api_request("POST", "/issue", data={"fields": fields})

@server.tool()
def get_issue(issue_key: str, expand: Optional[str] = None) -> dict:
    """Get details of a specific issue."""
    params = {}
    if expand:
        params["expand"] = expand
    return api_request("GET", f"/issue/{issue_key}", params=params)

@server.tool()
def update_issue(
    issue_key: str,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    assignee_id: Optional[str] = None,
    priority_id: Optional[str] = None,
    labels: Optional[list] = None,
    status: Optional[str] = None,
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
    
    if priority_id:
        fields["priority"] = {"id": priority_id}
    
    if labels:
        fields["labels"] = labels
    
    return api_request("PUT", f"/issue/{issue_key}", data={"fields": fields})

@server.tool()
def delete_issue(issue_key: str) -> dict:
    """Delete an issue."""
    return api_request("DELETE", f"/issue/{issue_key}")

@server.tool()
def assign_issue(issue_key: str, assignee_id: str) -> dict:
    """Assign an issue to a user."""
    return api_request("PUT", f"/issue/{issue_key}/assignee", data={"accountId": assignee_id})

@server.tool()
def get_issue_transitions(issue_key: str) -> dict:
    """Get available transitions for an issue."""
    return api_request("GET", f"/issue/{issue_key}/transitions")

@server.tool()
def transition_issue(issue_key: str, transition_id: str, comment: Optional[str] = None) -> dict:
    """Transition an issue to a new status."""
    data = {"transition": {"id": transition_id}}
    
    if comment:
        data["update"] = {
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
    
    return api_request("POST", f"/issue/{issue_key}/transitions", data=data)

@server.tool()
def get_issue_changelog(issue_key: str) -> dict:
    """Get the changelog for an issue."""
    return api_request("GET", f"/issue/{issue_key}/changelog")

# ============================================================================
# ISSUE SEARCH TOOLS
# ============================================================================

@server.tool()
def search_issues(
    jql: str,
    start_index: int = 0,
    page_size: int = 50,
    fields: Optional[list] = None,
    expand: Optional[str] = None,
) -> dict:
    """Search for issues using JQL."""
    params = {
        "jql": jql,
        "startAt": start_index,
        "maxResults": page_size,
    }
    
    if fields:
        params["fields"] = ",".join(fields)
    
    if expand:
        params["expand"] = expand
    
    return api_request("GET", "/search", params=params)

@server.tool()
def count_issues(jql: str) -> dict:
    """Count issues matching a JQL query."""
    return api_request("POST", "/search/approximate-count", data={"jql": jql})

@server.tool()
def get_issue_picker_suggestions(query: str, current_jql: Optional[str] = None) -> dict:
    """Get issue picker suggestions for a query."""
    params = {"query": query}
    if current_jql:
        params["currentJQL"] = current_jql
    return api_request("GET", "/issue/picker", params=params)

# ============================================================================
# ISSUE COMMENTS TOOLS
# ============================================================================

@server.tool()
def add_comment(issue_key: str, comment_text: str, visibility: Optional[str] = None) -> dict:
    """Add a comment to an issue."""
    data = {
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
    
    if visibility:
        data["visibility"] = {"type": "role", "value": visibility}
    
    return api_request("POST", f"/issue/{issue_key}/comment", data=data)

@server.tool()
def get_issue_comments(issue_key: str) -> dict:
    """Get all comments for an issue."""
    return api_request("GET", f"/issue/{issue_key}/comment")

@server.tool()
def get_comment(issue_key: str, comment_id: str) -> dict:
    """Get a specific comment."""
    return api_request("GET", f"/issue/{issue_key}/comment/{comment_id}")

@server.tool()
def update_comment(issue_key: str, comment_id: str, comment_text: str) -> dict:
    """Update a comment."""
    data = {
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
    return api_request("PUT", f"/issue/{issue_key}/comment/{comment_id}", data=data)

@server.tool()
def delete_comment(issue_key: str, comment_id: str) -> dict:
    """Delete a comment."""
    return api_request("DELETE", f"/issue/{issue_key}/comment/{comment_id}")

# ============================================================================
# ISSUE WORKLOGS TOOLS
# ============================================================================

@server.tool()
def add_worklog(
    issue_key: str,
    time_spent: str,
    started: Optional[str] = None,
    comment: Optional[str] = None,
) -> dict:
    """Add a worklog entry to an issue."""
    data = {"timeSpent": time_spent}
    
    if started:
        data["started"] = started
    
    if comment:
        data["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    
    return api_request("POST", f"/issue/{issue_key}/worklog", data=data)

@server.tool()
def get_issue_worklogs(issue_key: str) -> dict:
    """Get all worklogs for an issue."""
    return api_request("GET", f"/issue/{issue_key}/worklog")

@server.tool()
def get_worklog(issue_key: str, worklog_id: str) -> dict:
    """Get a specific worklog entry."""
    return api_request("GET", f"/issue/{issue_key}/worklog/{worklog_id}")

@server.tool()
def update_worklog(
    issue_key: str,
    worklog_id: str,
    time_spent: Optional[str] = None,
    comment: Optional[str] = None,
) -> dict:
    """Update a worklog entry."""
    data = {}
    
    if time_spent:
        data["timeSpent"] = time_spent
    
    if comment:
        data["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    
    return api_request("PUT", f"/issue/{issue_key}/worklog/{worklog_id}", data=data)

@server.tool()
def delete_worklog(issue_key: str, worklog_id: str) -> dict:
    """Delete a worklog entry."""
    return api_request("DELETE", f"/issue/{issue_key}/worklog/{worklog_id}")

# ============================================================================
# ISSUE WATCHERS TOOLS
# ============================================================================

@server.tool()
def get_issue_watchers(issue_key: str) -> dict:
    """Get watchers for an issue."""
    return api_request("GET", f"/issue/{issue_key}/watchers")

@server.tool()
def add_watcher(issue_key: str, account_id: str) -> dict:
    """Add a watcher to an issue."""
    return api_request("POST", f"/issue/{issue_key}/watchers", data={"accountId": account_id})

@server.tool()
def remove_watcher(issue_key: str, account_id: str) -> dict:
    """Remove a watcher from an issue."""
    return api_request("DELETE", f"/issue/{issue_key}/watchers", params={"accountId": account_id})

# ============================================================================
# ISSUE LINKS TOOLS
# ============================================================================

@server.tool()
def create_issue_link(
    link_type: str,
    inward_issue: str,
    outward_issue: str,
) -> dict:
    """Create a link between two issues."""
    data = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue},
        "outwardIssue": {"key": outward_issue},
    }
    return api_request("POST", "/issueLink", data=data)

@server.tool()
def get_issue_link(link_id: str) -> dict:
    """Get details of an issue link."""
    return api_request("GET", f"/issueLink/{link_id}")

@server.tool()
def delete_issue_link(link_id: str) -> dict:
    """Delete an issue link."""
    return api_request("DELETE", f"/issueLink/{link_id}")

# ============================================================================
# ISSUE ATTACHMENTS TOOLS
# ============================================================================

@server.tool()
def get_attachment_metadata(attachment_id: str) -> dict:
    """Get metadata for an attachment."""
    return api_request("GET", f"/attachment/{attachment_id}")

@server.tool()
def delete_attachment(attachment_id: str) -> dict:
    """Delete an attachment."""
    return api_request("DELETE", f"/attachment/{attachment_id}")

# ============================================================================
# PROJECTS TOOLS
# ============================================================================

@server.tool()
def get_projects(expand: Optional[str] = None) -> dict:
    """Get all projects."""
    params = {}
    if expand:
        params["expand"] = expand
    return api_request("GET", "/project", params=params)

@server.tool()
def get_project(project_key: str, expand: Optional[str] = None) -> dict:
    """Get details of a specific project."""
    params = {}
    if expand:
        params["expand"] = expand
    return api_request("GET", f"/project/{project_key}", params=params)

@server.tool()
def create_project(
    key: str,
    name: str,
    project_type: str,
    description: Optional[str] = None,
) -> dict:
    """Create a new project."""
    data = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type,
    }
    
    if description:
        data["description"] = description
    
    return api_request("POST", "/project", data=data)

@server.tool()
def update_project(
    project_key: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a project."""
    data = {}
    
    if name:
        data["name"] = name
    
    if description:
        data["description"] = description
    
    return api_request("PUT", f"/project/{project_key}", data=data)

@server.tool()
def delete_project(project_key: str) -> dict:
    """Delete a project."""
    return api_request("DELETE", f"/project/{project_key}")

@server.tool()
def get_project_statuses(project_key: str) -> dict:
    """Get all statuses for a project."""
    return api_request("GET", f"/project/{project_key}/statuses")

# ============================================================================
# PROJECT COMPONENTS TOOLS
# ============================================================================

@server.tool()
def get_project_components(project_key: str) -> dict:
    """Get all components for a project."""
    return api_request("GET", f"/project/{project_key}/components")

@server.tool()
def create_component(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
) -> dict:
    """Create a component in a project."""
    data = {
        "name": name,
        "project": project_key,
    }
    
    if description:
        data["description"] = description
    
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    
    return api_request("POST", "/component", data=data)

@server.tool()
def get_component(component_id: str) -> dict:
    """Get details of a component."""
    return api_request("GET", f"/component/{component_id}")

@server.tool()
def update_component(
    component_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a component."""
    data = {}
    
    if name:
        data["name"] = name
    
    if description:
        data["description"] = description
    
    return api_request("PUT", f"/component/{component_id}", data=data)

@server.tool()
def delete_component(component_id: str) -> dict:
    """Delete a component."""
    return api_request("DELETE", f"/component/{component_id}")

# ============================================================================
# PROJECT VERSIONS TOOLS
# ============================================================================

@server.tool()
def get_project_versions(project_key: str) -> dict:
    """Get all versions for a project."""
    return api_request("GET", f"/project/{project_key}/versions")

@server.tool()
def create_version(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    release_date: Optional[str] = None,
    released: bool = False,
) -> dict:
    """Create a version in a project."""
    data = {
        "name": name,
        "project": project_key,
        "released": released,
    }
    
    if description:
        data["description"] = description
    
    if release_date:
        data["releaseDate"] = release_date
    
    return api_request("POST", "/version", data=data)

@server.tool()
def get_version(version_id: str) -> dict:
    """Get details of a version."""
    return api_request("GET", f"/version/{version_id}")

@server.tool()
def update_version(
    version_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    released: Optional[bool] = None,
    release_date: Optional[str] = None,
) -> dict:
    """Update a version."""
    data = {}
    
    if name:
        data["name"] = name
    
    if description:
        data["description"] = description
    
    if released is not None:
        data["released"] = released
    
    if release_date:
        data["releaseDate"] = release_date
    
    return api_request("PUT", f"/version/{version_id}", data=data)

@server.tool()
def delete_version(version_id: str) -> dict:
    """Delete a version."""
    return api_request("DELETE", f"/version/{version_id}")

# ============================================================================
# USERS TOOLS
# ============================================================================

@server.tool()
def get_user(account_id: str) -> dict:
    """Get details of a user."""
    return api_request("GET", f"/user", params={"accountId": account_id})

@server.tool()
def create_user(
    email: str,
    display_name: str,
    password: Optional[str] = None,
) -> dict:
    """Create a new user."""
    data = {
        "emailAddress": email,
        "displayName": display_name,
    }
    
    if password:
        data["password"] = password
    
    return api_request("POST", "/user", data=data)

@server.tool()
def delete_user(account_id: str) -> dict:
    """Delete a user."""
    return api_request("DELETE", f"/user", params={"accountId": account_id})

@server.tool()
def get_all_users(start_at: int = 0, max_results: int = 50) -> dict:
    """Get all users."""
    params = {
        "startAt": start_at,
        "maxResults": max_results,
    }
    return api_request("GET", "/users/search", params=params)

@server.tool()
def get_user_groups(account_id: str) -> dict:
    """Get groups for a user."""
    return api_request("GET", f"/user/groups", params={"accountId": account_id})

# ============================================================================
# GROUPS TOOLS
# ============================================================================

@server.tool()
def create_group(group_name: str) -> dict:
    """Create a new group."""
    return api_request("POST", "/group", data={"name": group_name})

@server.tool()
def delete_group(group_name: str) -> dict:
    """Delete a group."""
    return api_request("DELETE", f"/group", params={"groupname": group_name})

@server.tool()
def get_group_members(group_name: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Get members of a group."""
    params = {
        "groupname": group_name,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return api_request("GET", "/group/member", params=params)

@server.tool()
def add_user_to_group(group_name: str, account_id: str) -> dict:
    """Add a user to a group."""
    return api_request("POST", f"/group/user", data={"groupname": group_name, "accountId": account_id})

@server.tool()
def remove_user_from_group(group_name: str, account_id: str) -> dict:
    """Remove a user from a group."""
    return api_request("DELETE", f"/group/user", params={"groupname": group_name, "accountId": account_id})

@server.tool()
def find_groups(query: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Find groups by name."""
    params = {
        "query": query,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return api_request("GET", "/groups/picker", params=params)

# ============================================================================
# FILTERS TOOLS
# ============================================================================

@server.tool()
def create_filter(
    name: str,
    jql: str,
    description: Optional[str] = None,
    favorite: bool = False,
) -> dict:
    """Create a new filter."""
    data = {
        "name": name,
        "jql": jql,
        "favorite": favorite,
    }
    
    if description:
        data["description"] = description
    
    return api_request("POST", "/filter", data=data)

@server.tool()
def get_filter(filter_id: str, expand: Optional[str] = None) -> dict:
    """Get details of a filter."""
    params = {}
    if expand:
        params["expand"] = expand
    return api_request("GET", f"/filter/{filter_id}", params=params)

@server.tool()
def update_filter(
    filter_id: str,
    name: Optional[str] = None,
    jql: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a filter."""
    data = {}
    
    if name:
        data["name"] = name
    
    if jql:
        data["jql"] = jql
    
    if description:
        data["description"] = description
    
    return api_request("PUT", f"/filter/{filter_id}", data=data)

@server.tool()
def delete_filter(filter_id: str) -> dict:
    """Delete a filter."""
    return api_request("DELETE", f"/filter/{filter_id}")

@server.tool()
def get_my_filters() -> dict:
    """Get filters owned by the current user."""
    return api_request("GET", "/filter/my")

@server.tool()
def get_favorite_filters() -> dict:
    """Get favorite filters for the current user."""
    return api_request("GET", "/filter/favourite")

@server.tool()
def add_filter_as_favorite(filter_id: str) -> dict:
    """Add a filter to favorites."""
    return api_request("PUT", f"/filter/{filter_id}/favourite", data={})

@server.tool()
def remove_filter_as_favorite(filter_id: str) -> dict:
    """Remove a filter from favorites."""
    return api_request("DELETE", f"/filter/{filter_id}/favourite")

# ============================================================================
# ISSUE TYPES TOOLS
# ============================================================================

@server.tool()
def get_all_issue_types() -> dict:
    """Get all issue types."""
    return api_request("GET", "/issuetype")

@server.tool()
def get_issue_type(issue_type_id: str) -> dict:
    """Get details of an issue type."""
    return api_request("GET", f"/issuetype/{issue_type_id}")

@server.tool()
def create_issue_type(
    name: str,
    issue_type_type: str,
    description: Optional[str] = None,
) -> dict:
    """Create a new issue type."""
    data = {
        "name": name,
        "type": issue_type_type,
    }
    
    if description:
        data["description"] = description
    
    return api_request("POST", "/issuetype", data=data)

@server.tool()
def update_issue_type(
    issue_type_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update an issue type."""
    data = {}
    
    if name:
        data["name"] = name
    
    if description:
        data["description"] = description
    
    return api_request("PUT", f"/issuetype/{issue_type_id}", data=data)

@server.tool()
def delete_issue_type(issue_type_id: str) -> dict:
    """Delete an issue type."""
    return api_request("DELETE", f"/issuetype/{issue_type_id}")

# ============================================================================
# PRIORITIES TOOLS
# ============================================================================

@server.tool()
def get_priorities() -> dict:
    """Get all priorities."""
    return api_request("GET", "/priority")

@server.tool()
def get_priority(priority_id: str) -> dict:
    """Get details of a priority."""
    return api_request("GET", f"/priority/{priority_id}")

# ============================================================================
# STATUSES TOOLS
# ============================================================================

@server.tool()
def get_all_statuses() -> dict:
    """Get all statuses."""
    return api_request("GET", "/status")

@server.tool()
def get_status(status_id: str) -> dict:
    """Get details of a status."""
    return api_request("GET", f"/status/{status_id}")

# ============================================================================
# SERVER INFO TOOLS
# ============================================================================

@server.tool()
def get_server_info() -> dict:
    """Get Jira server information."""
    return api_request("GET", "/serverInfo")

# ============================================================================
# MYSELF TOOLS
# ============================================================================

@server.tool()
def get_current_user() -> dict:
    """Get information about the current user."""
    return api_request("GET", "/myself")

# ============================================================================
# ADDITIONAL UTILITY TOOLS
# ============================================================================

@server.tool()
def get_comments_by_ids(comment_ids: list) -> dict:
    """Get multiple comments by their IDs."""
    return api_request("POST", "/comment/list", data={"ids": comment_ids})

@server.tool()
def search_filters(query: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Search for filters by name or description."""
    params = {
        "filterName": query,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return api_request("GET", "/filter/search", params=params)

@server.tool()
def get_issue_edit_metadata(issue_key: str) -> dict:
    """Get metadata for editing an issue."""
    return api_request("GET", f"/issue/{issue_key}/editmeta")

@server.tool()
def get_create_issue_metadata(project_key: str) -> dict:
    """Get metadata for creating issues in a project."""
    params = {"projectKeys": project_key}
    return api_request("GET", "/issue/createmeta", params=params)

@server.tool()
def send_issue_notification(
    issue_key: str,
    subject: str,
    body: str,
    recipients: Optional[list] = None,
) -> dict:
    """Send a notification about an issue."""
    data = {
        "subject": subject,
        "textBody": body,
    }
    
    if recipients:
        data["to"] = {"users": [{"accountId": r} for r in recipients]}
    
    return api_request("POST", f"/issue/{issue_key}/notify", data=data)

@server.tool()
def get_issue_types_for_project(project_key: str) -> dict:
    """Get issue types available for a project."""
    return api_request("GET", f"/issue/createmeta/{project_key}/issuetypes")

@server.tool()
def get_create_field_metadata(project_key: str, issue_type_id: str) -> dict:
    """Get field metadata for creating issues of a specific type."""
    return api_request("GET", f"/issue/createmeta/{project_key}/issuetypes/{issue_type_id}")

@server.tool()
def get_project_recent() -> dict:
    """Get recently viewed projects."""
    return api_request("GET", "/project/recent")

@server.tool()
def search_projects(
    query: str = "",
    start_at: int = 0,
    max_results: int = 50,
) -> dict:
    """Search for projects by name or key."""
    params = {
        "query": query,
        "startAt": start_at,
        "maxResults": max_results,
    }
    return api_request("GET", "/project/search", params=params)

@server.tool()
def get_component_issues_count(component_id: str) -> dict:
    """Get count of issues for a component."""
    return api_request("GET", f"/component/{component_id}/relatedIssueCounts")

@server.tool()
def get_version_related_issues_count(version_id: str) -> dict:
    """Get count of issues related to a version."""
    return api_request("GET", f"/version/{version_id}/relatedIssueCounts")

@server.tool()
def bulk_get_users(user_ids: list) -> dict:
    """Get multiple users by their account IDs."""
    params = {"user_id": user_ids}
    return api_request("GET", "/user/bulk", params=params)

@server.tool()
def get_user_email(account_id: str) -> dict:
    """Get email address for a user."""
    params = {"accountId": account_id}
    return api_request("GET", "/user/email", params=params)

@server.tool()
def get_user_emails_bulk(account_ids: list) -> dict:
    """Get email addresses for multiple users."""
    params = {"accountId": account_ids}
    return api_request("GET", "/user/email/bulk", params=params)

@server.tool()
def check_issues_against_jql(issue_ids: list, jql_queries: list) -> dict:
    """Check which issues match given JQL queries."""
    data = {
        "issueIds": issue_ids,
        "jqls": jql_queries,
    }
    return api_request("POST", "/jql_query/match", data=data)

@server.tool()
def get_issue_votes(issue_key: str) -> dict:
    """Get vote information for an issue."""
    return api_request("GET", f"/issue/{issue_key}/votes")

@server.tool()
def add_issue_vote(issue_key: str) -> dict:
    """Vote for an issue."""
    return api_request("POST", f"/issue/{issue_key}/votes", data={})

@server.tool()
def remove_issue_vote(issue_key: str) -> dict:
    """Remove vote from an issue."""
    return api_request("DELETE", f"/issue/{issue_key}/votes")

@server.tool()
def get_issue_remote_links(issue_key: str) -> dict:
    """Get remote links for an issue."""
    return api_request("GET", f"/issue/{issue_key}/remotelink")

@server.tool()
def create_issue_remote_link(
    issue_key: str,
    url: str,
    title: str,
    summary: Optional[str] = None,
) -> dict:
    """Create a remote link for an issue."""
    data = {
        "object": {
            "url": url,
            "title": title,
        }
    }
    
    if summary:
        data["object"]["summary"] = summary
    
    return api_request("POST", f"/issue/{issue_key}/remotelink", data=data)

@server.tool()
def delete_issue_remote_link(issue_key: str, link_id: str) -> dict:
    """Delete a remote link from an issue."""
    return api_request("DELETE", f"/issue/{issue_key}/remotelink/{link_id}")

@server.tool()
def get_project_notification_scheme(project_key: str) -> dict:
    """Get notification scheme for a project."""
    return api_request("GET", f"/project/{project_key}/notificationscheme")

@server.tool()
def get_project_issue_type_hierarchy(project_key: str) -> dict:
    """Get issue type hierarchy for a project."""
    return api_request("GET", f"/project/{project_key}/hierarchy")

if __name__ == "__main__":
    server.run()
