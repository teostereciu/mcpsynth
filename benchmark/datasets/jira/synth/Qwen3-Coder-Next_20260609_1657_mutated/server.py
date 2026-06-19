#!/usr/bin/env python3
"""
Jira Cloud REST API MCP Server

An MCP server with comprehensive coverage of the Jira Cloud REST API v3.
"""

import os
import json
import requests
from typing import Any
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("jira")

# Base URL configuration
BASE_URL = os.getenv("JIRA_BASE_URL", "https://your-domain.atlassian.net").rstrip("/")

def _get_auth() -> tuple[str, str]:
    """Get authentication credentials from environment."""
    email = os.getenv("JIRA_EMAIL")
    api_token = os.getenv("JIRA_API_TOKEN")
    
    if not email or not api_token:
        raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set")
    
    return email, api_token

def _api_request(
    method: str,
    path: str,
    params: dict | None = None,
    data: dict | None = None,
    files: dict | None = None
) -> dict | list | str:
    """Make authenticated API request to Jira Cloud."""
    url = f"{BASE_URL}/rest/api/3{path}"
    auth = _get_auth()
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            json=data,
            files=files,
            headers=headers,
            auth=auth,
            timeout=60
        )
        
        # Handle success responses
        if response.status_code in (200, 201, 204):
            if response.status_code == 204:
                return {"message": "Operation successful"}
            try:
                return response.json()
            except ValueError:
                return response.text
        
        # Handle errors
        error_msg = f"API error: {response.status_code}"
        try:
            error_data = response.json()
            error_msg += f" - {error_data}"
        except:
            error_msg += f" - {response.text}"
        
        return {"error": error_msg}
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# PROJECTS
# ============================================================================

@mcp.tool()
def get_projects_paginated(
    start_index: int = 0,
    page_size: int = 50,
    query: str | None = None,
    type_key: str | None = None,
    category_id: int | None = None
) -> dict:
    """Get a paginated list of projects."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    if query:
        params["query"] = query
    if type_key:
        params["typeKey"] = type_key
    if category_id:
        params["categoryId"] = category_id
    
    return _api_request("GET", "/project/search", params=params)

@mcp.tool()
def get_project(project_id_or_key: str) -> dict:
    """Get project details by ID or key."""
    return _api_request("GET", f"/project/{project_id_or_key}")

@mcp.tool()
def create_project(
    name: str,
    key: str,
    project_type_key: str,
    project_template_key: str,
    description: str | None = None,
    leadAccountId: str | None = None,
    assignee_type: str | None = None,
    avatar_id: int | None = None,
    category_id: int | None = None,
    url: str | None = None
) -> dict:
    """Create a new project."""
    data = {
        "name": name,
        "key": key,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
        "assigneeType": assignee_type or "PROJECT_LEAD"
    }
    if description:
        data["description"] = description
    if leadAccountId:
        data["leadAccountId"] = leadAccountId
    if avatar_id:
        data["avatarId"] = avatar_id
    if category_id:
        data["categoryId"] = category_id
    if url:
        data["url"] = url
    
    return _api_request("POST", "/project", data=data)

@mcp.tool()
def update_project(project_id_or_key: str, **kwargs) -> dict:
    """Update project details."""
    return _api_request("PUT", f"/project/{project_id_or_key}", data=kwargs)

@mcp.tool()
def delete_project(project_id_or_key: str) -> dict:
    """Delete a project."""
    return _api_request("DELETE", f"/project/{project_id_or_key}")

@mcp.tool()
def archive_project(project_id_or_key: str) -> dict:
    """Archive a project."""
    return _api_request("POST", f"/project/{project_id_or_key}/archive")

@mcp.tool()
def restore_project(project_id_or_key: str) -> dict:
    """Restore an archived project."""
    return _api_request("POST", f"/project/{project_id_or_key}/restore")

# ============================================================================
# ISSUES
# ============================================================================

@mcp.tool()
def get_issue(issue_id_or_key: str, expand: str | None = None) -> dict:
    """Get an issue by ID or key."""
    params = {}
    if expand:
        params["expand"] = expand
    return _api_request("GET", f"/issue/{issue_id_or_key}", params=params)

@mcp.tool()
def create_issue(
    project_id_or_key: str,
    summary: str,
    issuetype_id: str,
    description: str | None = None,
    priority_id: str | None = None,
    assignee_id: str | None = None,
    reporter_id: str | None = None,
    components: list[str] | None = None,
    labels: list[str] | None = None,
    parent_id_or_key: str | None = None,
    **custom_fields
) -> dict:
    """Create a new issue."""
    data = {
        "update": {},
        "fields": {
            "project": {"id": project_id_or_key} if project_id_or_key.isdigit() else {"key": project_id_or_key},
            "summary": summary,
            "issuetype": {"id": issuetype_id} if issuetype_id.isdigit() else {"id": issuetype_id}
        }
    }
    
    if description:
        data["fields"]["description"] = description
    if priority_id:
        data["fields"]["priority"] = {"id": priority_id} if priority_id.isdigit() else {"id": priority_id}
    if assignee_id:
        data["fields"]["assignee"] = {"id": assignee_id}
    if reporter_id:
        data["fields"]["reporter"] = {"id": reporter_id}
    if components:
        data["fields"]["components"] = [{"id": c} if c.isdigit() else {"id": c} for c in components]
    if labels:
        data["fields"]["labels"] = labels
    if parent_id_or_key:
        data["fields"]["parent"] = {"id": parent_id_or_key} if parent_id_or_key.isdigit() else {"key": parent_id_or_key}
    
    # Add custom fields
    for field_name, field_value in custom_fields.items():
        if field_name.startswith("customfield_"):
            data["fields"][field_name] = field_value
    
    return _api_request("POST", "/issue", data=data)

@mcp.tool()
def update_issue(issue_id_or_key: str, **kwargs) -> dict:
    """Update issue fields."""
    return _api_request("PUT", f"/issue/{issue_id_or_key}", data={"fields": kwargs})

@mcp.tool()
def delete_issue(issue_id_or_key: str) -> dict:
    """Delete an issue."""
    return _api_request("DELETE", f"/issue/{issue_id_or_key}")

@mcp.tool()
def archive_issue(issue_id_or_key: str) -> dict:
    """Archive an issue."""
    return _api_request("PUT", "/issue/archive", data={"issueIdsOrKeys": [issue_id_or_key]})

@mcp.tool()
def unarchive_issue(issue_id_or_key: str) -> dict:
    """Unarchive an issue."""
    return _api_request("PUT", "/issue/unarchive", data={"issueIdsOrKeys": [issue_id_or_key]})

@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str) -> dict:
    """Assign an issue to a user."""
    return _api_request("PUT", f"/issue/{issue_id_or_key}/assignee", data={"accountId": account_id})

@mcp.tool()
def get_issue_transitions(issue_id_or_key: str) -> dict:
    """Get available transitions for an issue."""
    return _api_request("GET", f"/issue/{issue_id_or_key}/transitions")

@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str) -> dict:
    """Transition an issue to a new status."""
    return _api_request("POST", f"/issue/{issue_id_or_key}/transitions", data={"transition": {"id": transition_id}})

@mcp.tool()
def search_issues(
    jql: str,
    start_index: int = 0,
    page_size: int = 50,
    expand: str | None = None,
    fields: list[str] | None = None,
    validate_query: str = "warn"
) -> dict:
    """Search issues using JQL."""
    data = {
        "jql_query": jql,
        "start_index": start_index,
        "page_size": page_size,
        "validateQuery": validate_query
    }
    if expand:
        data["expand"] = expand
    if fields:
        data["include_fields"] = fields
    
    return _api_request("POST", "/search", data=data)

@mcp.tool()
def get_issue_comments(
    issue_id_or_key: str,
    start_index: int = 0,
    page_size: int = 50
) -> dict:
    """Get comments for an issue."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", f"/issue/{issue_id_or_key}/comment", params=params)

@mcp.tool()
def get_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """Get a specific comment."""
    return _api_request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}")

@mcp.tool()
def add_comment(issue_id_or_key: str, body: str, visibility_type: str | None = None, visibility_value: str | None = None) -> dict:
    """Add a comment to an issue."""
    data = {
        "body": body
    }
    if visibility_type and visibility_value:
        data["visibility"] = {
            "type": visibility_type,
            "value": visibility_value
        }
    return _api_request("POST", f"/issue/{issue_id_or_key}/comment", data=data)

@mcp.tool()
def update_comment(issue_id_or_key: str, comment_id: str, body: str) -> dict:
    """Update a comment."""
    return _api_request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", data={"body": body})

@mcp.tool()
def delete_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """Delete a comment."""
    return _api_request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")

@mcp.tool()
def get_worklogs(issue_id_or_key: str, start_index: int = 0, page_size: int = 50) -> dict:
    """Get worklogs for an issue."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)

@mcp.tool()
def get_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """Get a specific worklog."""
    return _api_request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}")

@mcp.tool()
def add_worklog(
    issue_id_or_key: str,
    time_spent: str,
    comment: str | None = None,
    started: str | None = None,
    time_spent_seconds: int | None = None,
    visibility_type: str | None = None,
    visibility_value: str | None = None
) -> dict:
    """Add worklog to an issue."""
    data = {
        "timeSpent": time_spent
    }
    if time_spent_seconds:
        data["timeSpentSeconds"] = time_spent_seconds
    if comment:
        data["comment"] = {"content": [{"text": comment, "type": "text"}], "type": "doc", "version": 1}
    if started:
        data["started"] = started
    if visibility_type and visibility_value:
        data["visibility"] = {"type": visibility_type, "value": visibility_value}
    
    return _api_request("POST", f"/issue/{issue_id_or_key}/worklog", data=data)

@mcp.tool()
def update_worklog(
    issue_id_or_key: str,
    worklog_id: str,
    time_spent: str | None = None,
    comment: str | None = None,
    started: str | None = None,
    time_spent_seconds: int | None = None
) -> dict:
    """Update a worklog."""
    data = {}
    if time_spent:
        data["timeSpent"] = time_spent
    if time_spent_seconds:
        data["timeSpentSeconds"] = time_spent_seconds
    if comment:
        data["comment"] = {"content": [{"text": comment, "type": "text"}], "type": "doc", "version": 1}
    if started:
        data["started"] = started
    
    return _api_request("PUT", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", data=data)

@mcp.tool()
def delete_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """Delete a worklog."""
    return _api_request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}")

@mcp.tool()
def get_issue_watchers(issue_id_or_key: str) -> dict:
    """Get watchers for an issue."""
    return _api_request("GET", f"/issue/{issue_id_or_key}/watchers")

@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """Add a watcher to an issue."""
    return _api_request("POST", f"/issue/{issue_id_or_key}/watchers", data=account_id)

@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """Remove a watcher from an issue."""
    return _api_request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"user_id": account_id})

@mcp.tool()
def get_issue_remote_links(issue_id_or_key: str, global_id: str | None = None) -> dict:
    """Get remote links for an issue."""
    params = {}
    if global_id:
        params["globalId"] = global_id
    return _api_request("GET", f"/issue/{issue_id_or_key}/remotelink", params=params)

@mcp.tool()
def create_remote_link(
    issue_id_or_key: str,
    url: str,
    title: str,
    application_name: str | None = None,
    application_type: str | None = None,
    global_id: str | None = None,
    relationship: str | None = None
) -> dict:
    """Create a remote link for an issue."""
    data = {
        "object": {
            "url": url,
            "title": title
        }
    }
    if application_name:
        data["application"] = {"name": application_name}
    if application_type:
        data["application"]["type"] = application_type
    if global_id:
        data["globalId"] = global_id
    if relationship:
        data["relationship"] = relationship
    
    return _api_request("POST", f"/issue/{issue_id_or_key}/remotelink", data=data)

@mcp.tool()
def update_remote_link(issue_id_or_key: str, link_id: str, **kwargs) -> dict:
    """Update a remote link."""
    data = {"object": {}}
    for key, value in kwargs.items():
        if key in ["url", "title"]:
            data["object"][key] = value
        else:
            data[key] = value
    return _api_request("PUT", f"/issue/{issue_id_or_key}/remotelink/{link_id}", data=data)

@mcp.tool()
def delete_remote_link(issue_id_or_key: str, link_id: str) -> dict:
    """Delete a remote link."""
    return _api_request("DELETE", f"/issue/{issue_id_or_key}/remotelink/{link_id}")

@mcp.tool()
def get_issue_attachments(issue_id_or_key: str) -> dict:
    """Get attachments for an issue."""
    return _api_request("GET", f"/issue/{issue_id_or_key}/attachments")

@mcp.tool()
def add_attachment(issue_id_or_key: str, file_path: str, filename: str | None = None) -> dict:
    """Add an attachment to an issue."""
    if not filename:
        filename = os.path.basename(file_path)
    
    with open(file_path, 'rb') as f:
        files = {'file': (filename, f)}
        headers = {'X-Atlassian-Token': 'no-check'}
        return _api_request("POST", f"/issue/{issue_id_or_key}/attachments", headers=headers, files=files)

@mcp.tool()
def delete_attachment(attachment_id: str) -> dict:
    """Delete an attachment."""
    return _api_request("DELETE", f"/attachment/{attachment_id}")

@mcp.tool()
def get_attachment_content(attachment_id: str) -> dict:
    """Get attachment content URL."""
    return _api_request("GET", f"/attachment/content/{attachment_id}", params={"redirect": False})

# ============================================================================
# USERS
# ============================================================================

@mcp.tool()
def get_user(account_id: str | None = None, username: str | None = None) -> dict:
    """Get user details."""
    params = {}
    if account_id:
        params["user_id"] = account_id
    if username:
        params["username"] = username
    return _api_request("GET", "/user", params=params)

@mcp.tool()
def search_users(query: str, start_index: int = 0, page_size: int = 50) -> dict:
    """Search users."""
    params = {
        "start_index": start_index,
        "page_size": page_size,
        "query": query
    }
    return _api_request("GET", "/users/search", params=params)

@mcp.tool()
def get_user_groups(account_id: str) -> dict:
    """Get groups a user belongs to."""
    return _api_request("GET", "/user/groups", params={"user_id": account_id})

@mcp.tool()
def create_user(email: str, display_name: str, products: list[str] | None = None) -> dict:
    """Create a new user."""
    data = {
        "emailAddress": email,
        "displayName": display_name
    }
    if products:
        data["products"] = products
    return _api_request("POST", "/user", data=data)

@mcp.tool()
def delete_user(account_id: str) -> dict:
    """Delete a user."""
    return _api_request("DELETE", "/user", params={"user_id": account_id})

@mcp.tool()
def get_users_bulk(account_ids: list[str]) -> dict:
    """Get multiple users by account IDs."""
    params = {"user_id": account_ids}
    return _api_request("GET", "/user/bulk", params=params)

# ============================================================================
# PROJECTS - COMPONENTS
# ============================================================================

@mcp.tool()
def get_project_components(project_id_or_key: str, start_index: int = 0, page_size: int = 50) -> dict:
    """Get components for a project."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", f"/project/{project_id_or_key}/components", params=params)

@mcp.tool()
def create_component(
    name: str,
    project_id_or_key: str,
    description: str | None = None,
    lead_account_id: str | None = None,
    assignee_type: str | None = None
) -> dict:
    """Create a project component."""
    data = {
        "name": name,
        "project": project_id_or_key
    }
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    if assignee_type:
        data["assigneeType"] = assignee_type
    
    return _api_request("POST", "/component", data=data)

@mcp.tool()
def update_component(component_id: str, **kwargs) -> dict:
    """Update a component."""
    return _api_request("PUT", f"/component/{component_id}", data=kwargs)

@mcp.tool()
def delete_component(component_id: str, move_issues_to: str | None = None) -> dict:
    """Delete a component."""
    params = {}
    if move_issues_to:
        params["moveIssuesTo"] = move_issues_to
    return _api_request("DELETE", f"/component/{component_id}", params=params)

# ============================================================================
# ISSUES - TYPES
# ============================================================================

@mcp.tool()
def get_issue_types() -> dict:
    """Get all issue types."""
    return _api_request("GET", "/issuetype")

@mcp.tool()
def get_issue_type(issue_type_id: str) -> dict:
    """Get an issue type."""
    return _api_request("GET", f"/issuetype/{issue_type_id}")

@mcp.tool()
def create_issue_type(name: str, description: str | None = None, hierarchy_level: int = 0) -> dict:
    """Create a new issue type."""
    data = {"name": name, "hierarchyLevel": hierarchy_level}
    if description:
        data["description"] = description
    return _api_request("POST", "/issuetype", data=data)

@mcp.tool()
def update_issue_type(issue_type_id: str, **kwargs) -> dict:
    """Update an issue type."""
    return _api_request("PUT", f"/issuetype/{issue_type_id}", data=kwargs)

@mcp.tool()
def delete_issue_type(issue_type_id: str, alternative_id: str | None = None) -> dict:
    """Delete an issue type."""
    params = {}
    if alternative_id:
        params["alternativeIssueTypeId"] = alternative_id
    return _api_request("DELETE", f"/issuetype/{issue_type_id}", params=params)

# ============================================================================
# ISSUES - PRIORITIES
# ============================================================================

@mcp.tool()
def get_priorities() -> dict:
    """Get all priorities."""
    return _api_request("GET", "/priority")

@mcp.tool()
def get_priority(priority_id: str) -> dict:
    """Get a priority."""
    return _api_request("GET", f"/priority/{priority_id}")

# ============================================================================
# ISSUES - STATUS
# ============================================================================

@mcp.tool()
def get_statuses(status_ids: list[str]) -> dict:
    """Get statuses by IDs."""
    params = {"id": status_ids}
    return _api_request("GET", "/statuses", params=params)

@mcp.tool()
def search_statuses(project_id: str | None = None, start_index: int = 0, page_size: int = 50, search_string: str | None = None) -> dict:
    """Search statuses."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    if project_id:
        params["projectId"] = project_id
    if search_string:
        params["searchString"] = search_string
    return _api_request("GET", "/statuses/search", params=params)

# ============================================================================
# GROUPS
# ============================================================================

@mcp.tool()
def get_groups(query: str | None = None, start_index: int = 0, page_size: int = 50) -> dict:
    """Get groups."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    if query:
        params["query"] = query
    return _api_request("GET", "/group/bulk", params=params)

@mcp.tool()
def get_group_members(group_id: str, include_inactive: bool = False, start_index: int = 0, page_size: int = 50) -> dict:
    """Get members of a group."""
    params = {
        "groupId": group_id,
        "includeInactiveUsers": include_inactive,
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", "/group/member", params=params)

@mcp.tool()
def add_user_to_group(group_id: str, account_id: str) -> dict:
    """Add a user to a group."""
    return _api_request("POST", "/group/user", params={"groupId": group_id}, data={"user_id": account_id})

@mcp.tool()
def remove_user_from_group(group_id: str, account_id: str) -> dict:
    """Remove a user from a group."""
    return _api_request("DELETE", "/group/user", params={"groupId": group_id, "user_id": account_id})

# ============================================================================
# JQL
# ============================================================================

@mcp.tool()
def jql_autocomplete(field_name: str, field_value: str | None = None) -> dict:
    """Get JQL autocomplete suggestions."""
    params = {"fieldName": field_name}
    if field_value:
        params["fieldValue"] = field_value
    return _api_request("GET", "/jql_query/autocompletedata/suggestions", params=params)

@mcp.tool()
def jql_parse(queries: list[str], validation: str = "strict") -> dict:
    """Parse and validate JQL queries."""
    data = {"queries": queries}
    return _api_request("POST", "/jql_query/parse", params={"validation": validation}, data=data)

# ============================================================================
# FIELDS
# ============================================================================

@mcp.tool()
def get_fields() -> dict:
    """Get all fields."""
    return _api_request("GET", "/field")

@mcp.tool()
def search_fields(
    start_index: int = 0,
    page_size: int = 50,
    query: str | None = None,
    type_: str = "all"
) -> dict:
    """Search fields."""
    params = {
        "start_index": start_index,
        "page_size": page_size,
        "type": type_
    }
    if query:
        params["query"] = query
    return _api_request("GET", "/field/search", params=params)

@mcp.tool()
def create_custom_field(name: str, description: str | None = None, searcher_key: str | None = None, field_type: str = "text") -> dict:
    """Create a custom field."""
    data = {
        "name": name,
        "type": field_type
    }
    if description:
        data["description"] = description
    if searcher_key:
        data["searcherKey"] = searcher_key
    return _api_request("POST", "/field", data=data)

@mcp.tool()
def update_custom_field(field_id: str, **kwargs) -> dict:
    """Update a custom field."""
    return _api_request("PUT", f"/field/{field_id}", data=kwargs)

@mcp.tool()
def delete_custom_field(field_id: str) -> dict:
    """Delete a custom field."""
    return _api_request("DELETE", f"/field/{field_id}")

# ============================================================================
# MYSELF
# ============================================================================

@mcp.tool()
def get_myself() -> dict:
    """Get current user details."""
    return _api_request("GET", "/myself")

# ============================================================================
# VERSIONS
# ============================================================================

@mcp.tool()
def get_project_versions(project_id_or_key: str, start_index: int = 0, page_size: int = 50) -> dict:
    """Get versions for a project."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", f"/project/{project_id_or_key}/versions", params=params)

@mcp.tool()
def create_version(
    name: str,
    project_id_or_key: str,
    description: str | None = None,
    release_date: str | None = None,
    start_date: str | None = None
) -> dict:
    """Create a project version."""
    data = {
        "name": name,
        "project": project_id_or_key
    }
    if description:
        data["description"] = description
    if release_date:
        data["releaseDate"] = release_date
    if start_date:
        data["startDate"] = start_date
    return _api_request("POST", "/version", data=data)

# ============================================================================
# Filters
# ============================================================================

@mcp.tool()
def get_filters(start_index: int = 0, page_size: int = 50) -> dict:
    """Get user's filters."""
    params = {
        "start_index": start_index,
        "page_size": page_size
    }
    return _api_request("GET", "/filter/my", params=params)

@mcp.tool()
def create_filter(name: str, jql: str, description: str | None = None) -> dict:
    """Create a filter."""
    data = {
        "name": name,
        "jql_query": jql
    }
    if description:
        data["description"] = description
    return _api_request("POST", "/filter", data=data)

@mcp.tool()
def get_filter(filter_id: str) -> dict:
    """Get a filter by ID."""
    return _api_request("GET", f"/filter/{filter_id}")

@mcp.tool()
def update_filter(filter_id: str, **kwargs) -> dict:
    """Update a filter."""
    return _api_request("PUT", f"/filter/{filter_id}", data=kwargs)

@mcp.tool()
def delete_filter(filter_id: str) -> dict:
    """Delete a filter."""
    return _api_request("DELETE", f"/filter/{filter_id}")

# ============================================================================
# Issue links
# ============================================================================

@mcp.tool()
def create_issue_link(
    inward_issue: str,
    outward_issue: str,
    link_type_name: str = "Duplicate",
    comment: str | None = None
) -> dict:
    """Create an issue link."""
    data = {
        "inwardIssue": {"key": inward_issue},
        "outwardIssue": {"key": outward_issue},
        "type": {"name": link_type_name}
    }
    if comment:
        data["comment"] = {
            "body": comment,
            "visibility": {"type": "group", "value": "jira-users"}
        }
    return _api_request("POST", "/issueLink", data=data)

@mcp.tool()
def get_issue_link(link_id: str) -> dict:
    """Get an issue link by ID."""
    return _api_request("GET", f"/issueLink/{link_id}")

@mcp.tool()
def delete_issue_link(link_id: str) -> dict:
    """Delete an issue link."""
    return _api_request("DELETE", f"/issueLink/{link_id}")

# ============================================================================
# Server metadata
# ============================================================================

@mcp.tool()
def get_server_info() -> dict:
    """Get Jira server information."""
    return _api_request("GET", "/serverInfo")

if __name__ == "__main__":
    mcp.run()
