#!/usr/bin/env python3
"""
Jira Cloud MCP Server

This MCP server provides comprehensive coverage of the Jira Cloud REST API v3.
"""

import os
from typing import Any
import requests
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("jira")

# Base URL for Jira REST API
BASE_URL = os.environ.get("JIRA_BASE_URL", "https://your-org.atlassian.net").rstrip("/")

# Authentication headers
AUTH_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def make_request(method: str, endpoint: str, params: dict = None, data: dict = None) -> dict:
    """Make a request to the Jira REST API."""
    url = f"{BASE_URL}/rest/api/3{endpoint}"
    
    # Add authentication if credentials are provided
    email = os.environ.get("JIRA_EMAIL")
    api_token = os.environ.get("JIRA_API_TOKEN")
    
    auth = None
    if email and api_token:
        auth = (email, api_token)
    
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=AUTH_HEADERS,
            params=params,
            json=data,
            auth=auth
        )
        
        # Handle successful responses
        if response.status_code in (200, 201, 204):
            if response.status_code == 204:
                return {"success": True, "message": "Operation completed successfully"}
            try:
                return response.json()
            except ValueError:
                return {"success": True, "data": response.text}
        
        # Handle errors
        error_msg = f"API request failed with status {response.status_code}"
        try:
            error_data = response.json()
            error_msg += f": {error_data}"
        except ValueError:
            error_msg += f": {response.text}"
        
        return {"error": error_msg}
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# Projects
# ============================================================================

@mcp.tool()
def get_all_projects() -> dict:
    """Get all projects visible to the user. Deprecated, use get_projects_paginated instead."""
    return make_request("GET", "/project")


@mcp.tool()
def get_projects_paginated(start_at: int = 0, max_results: int = 50, query: str = None) -> dict:
    """Returns a paginated list of projects visible to the user."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if query:
        params["query"] = query
    return make_request("GET", "/project/search", params=params)


@mcp.tool()
def get_project(project_id_or_key: str) -> dict:
    """Returns the project details for a project."""
    return make_request("GET", f"/project/{project_id_or_key}")


@mcp.tool()
def create_project(
    name: str,
    key: str,
    project_type_key: str,
    project_template_key: str,
    description: str = None,
    assignee_type: str = None,
    lead_account_id: str = None,
    category_id: int = None
) -> dict:
    """Creates a project based on a project type template."""
    data = {
        "name": name,
        "key": key,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key
    }
    if description:
        data["description"] = description
    if assignee_type:
        data["assigneeType"] = assignee_type
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    if category_id:
        data["categoryId"] = category_id
    
    return make_request("POST", "/project", data=data)


@mcp.tool()
def update_project(project_id_or_key: str, name: str = None, description: str = None) -> dict:
    """Updates a project."""
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    
    return make_request("PUT", f"/project/{project_id_or_key}", data=data)


@mcp.tool()
def delete_project(project_id_or_key: str) -> dict:
    """Deletes a project."""
    return make_request("POST", f"/project/{project_id_or_key}/delete")


@mcp.tool()
def archive_project(project_id_or_key: str) -> dict:
    """Archives a project."""
    return make_request("POST", f"/project/{project_id_or_key}/archive")


@mcp.tool()
def restore_project(project_id_or_key: str) -> dict:
    """Restores a project."""
    return make_request("POST", f"/project/{project_id_or_key}/restore")


@mcp.tool()
def get_project_statuses(project_id_or_key: str) -> dict:
    """Returns the statuses available for a project."""
    return make_request("GET", f"/project/{project_id_or_key}/statuses")


# ============================================================================
# Issues
# ============================================================================

@mcp.tool()
def get_issue(issue_id_or_key: str) -> dict:
    """Returns an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}")


@mcp.tool()
def create_issue(
    project_id_or_key: str,
    summary: str,
    issue_type_id: str,
    description: str = None,
    assignee_id: str = None,
    priority_id: str = None,
    parent_id_or_key: str = None,
    fields: dict = None
) -> dict:
    """Creates an issue or subtask."""
    data = {
        "fields": {
            "project": {"id": project_id_or_key} if project_id_or_key.isdigit() else {"key": project_id_or_key},
            "summary": summary,
            "issuetype": {"id": issue_type_id}
        }
    }
    
    if description:
        data["fields"]["description"] = description
    if assignee_id:
        data["fields"]["assignee"] = {"id": assignee_id}
    if priority_id:
        data["fields"]["priority"] = {"id": priority_id}
    if parent_id_or_key:
        data["fields"]["parent"] = {"id": parent_id_or_key} if parent_id_or_key.isdigit() else {"key": parent_id_or_key}
    
    # Add any additional fields
    if fields:
        data["fields"].update(fields)
    
    return make_request("POST", "/issue", data=data)


@mcp.tool()
def update_issue(issue_id_or_key: str, summary: str = None, description: str = None, fields: dict = None) -> dict:
    """Updates an issue."""
    data = {"fields": {}}
    
    if summary is not None:
        data["fields"]["summary"] = summary
    if description is not None:
        data["fields"]["description"] = description
    
    # Add any additional fields
    if fields:
        data["fields"].update(fields)
    
    return make_request("PUT", f"/issue/{issue_id_or_key}", data=data)


@mcp.tool()
def delete_issue(issue_id_or_key: str) -> dict:
    """Deletes an issue."""
    return make_request("DELETE", f"/issue/{issue_id_or_key}")


@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str) -> dict:
    """Assigns an issue to a user."""
    data = {"accountId": account_id}
    return make_request("PUT", f"/issue/{issue_id_or_key}/assignee", data=data)


@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str, fields: dict = None) -> dict:
    """Transitions an issue to a new status."""
    data = {"transition": {"id": transition_id}}
    
    if fields:
        data["fields"] = fields
    
    return make_request("POST", f"/issue/{issue_id_or_key}/transitions", data=data)


@mcp.tool()
def get_issue_transitions(issue_id_or_key: str) -> dict:
    """Gets available transitions for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/transitions")


@mcp.tool()
def archive_issues(issue_ids_or_keys: list) -> dict:
    """Archives issues by ID or key."""
    data = {"issueIdsOrKeys": issue_ids_or_keys}
    return make_request("PUT", "/issue/archive", data=data)


@mcp.tool()
def unarchive_issues(issue_ids_or_keys: list) -> dict:
    """Unarchives issues by ID or key."""
    data = {"issueIdsOrKeys": issue_ids_or_keys}
    return make_request("PUT", "/issue/unarchive", data=data)


@mcp.tool()
def get_issue_changelog(issue_id_or_key: str) -> dict:
    """Gets the changelog for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/changelog")


@mcp.tool()
def get_issue_editmeta(issue_id_or_key: str) -> dict:
    """Gets the edit metadata for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/editmeta")


@mcp.tool()
def get_issue_createmeta(project_id_or_key: str) -> dict:
    """Gets the create metadata for a project."""
    return make_request("GET", f"/issue/createmeta/{project_id_or_key}/issuetypes")


@mcp.tool()
def notify_issue(issue_id_or_key: str, subject: str, body: str, recipients: list = None) -> dict:
    """Sends a notification about an issue."""
    data = {
        "subject": subject,
        "body": body
    }
    if recipients:
        data["recipients"] = recipients
    
    return make_request("POST", f"/issue/{issue_id_or_key}/notify", data=data)


# ============================================================================
# Issue Comments
# ============================================================================

@mcp.tool()
def get_issue_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns all comments for an issue."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    return make_request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


@mcp.tool()
def create_issue_comment(issue_id_or_key: str, body: str, visibility_type: str = None, visibility_value: str = None) -> dict:
    """Adds a comment to an issue."""
    data = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": body
                        }
                    ]
                }
            ]
        }
    }
    
    if visibility_type and visibility_value:
        data["visibility"] = {
            "type": visibility_type,
            "identifier": visibility_value
        }
    
    return make_request("POST", f"/issue/{issue_id_or_key}/comment", data=data)


@mcp.tool()
def get_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """Returns a comment."""
    return make_request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}")


@mcp.tool()
def update_issue_comment(issue_id_or_key: str, comment_id: str, body: str = None, visibility_type: str = None, visibility_value: str = None) -> dict:
    """Updates a comment."""
    data = {}
    
    if body:
        data["body"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": body
                        }
                    ]
                }
            ]
        }
    
    if visibility_type and visibility_value:
        data["visibility"] = {
            "type": visibility_type,
            "identifier": visibility_value
        }
    
    return make_request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", data=data)


@mcp.tool()
def delete_issue_comment(issue_id_or_key: str, comment_id: str) -> dict:
    """Deletes a comment."""
    return make_request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


# ============================================================================
# Issue Worklogs
# ============================================================================

@mcp.tool()
def get_issue_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns worklogs for an issue."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    return make_request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)


@mcp.tool()
def create_issue_worklog(
    issue_id_or_key: str,
    time_spent: str,
    comment: str = None,
    started: str = None,
    time_spent_seconds: int = None
) -> dict:
    """Adds a worklog to an issue."""
    data = {
        "timeSpent": time_spent
    }
    
    if time_spent_seconds:
        data["timeSpentSeconds"] = time_spent_seconds
    
    if started:
        data["started"] = started
    
    if comment:
        data["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": comment
                        }
                    ]
                }
            ]
        }
    
    return make_request("POST", f"/issue/{issue_id_or_key}/worklog", data=data)


@mcp.tool()
def get_issue_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """Returns a worklog."""
    return make_request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}")


@mcp.tool()
def update_issue_worklog(
    issue_id_or_key: str,
    worklog_id: str,
    time_spent: str = None,
    comment: str = None,
    time_spent_seconds: int = None
) -> dict:
    """Updates a worklog."""
    data = {}
    
    if time_spent:
        data["timeSpent"] = time_spent
    
    if time_spent_seconds:
        data["timeSpentSeconds"] = time_spent_seconds
    
    if comment:
        data["comment"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": comment
                        }
                    ]
                }
            ]
        }
    
    return make_request("PUT", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", data=data)


@mcp.tool()
def delete_issue_worklog(issue_id_or_key: str, worklog_id: str) -> dict:
    """Deletes a worklog."""
    return make_request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}")


# ============================================================================
# Issue Attachments
# ============================================================================

@mcp.tool()
def get_attachment_metadata(attachment_id: str) -> dict:
    """Returns the metadata for an attachment."""
    return make_request("GET", f"/attachment/{attachment_id}")


@mcp.tool()
def get_attachment_content(attachment_id: str) -> dict:
    """Returns the contents of an attachment."""
    return make_request("GET", f"/attachment/content/{attachment_id}", params={"redirect": False})


@mcp.tool()
def get_attachment_thumbnail(attachment_id: str) -> dict:
    """Returns the thumbnail of an attachment."""
    return make_request("GET", f"/attachment/thumbnail/{attachment_id}", params={"redirect": False})


@mcp.tool()
def delete_attachment(attachment_id: str) -> dict:
    """Deletes an attachment."""
    return make_request("DELETE", f"/attachment/{attachment_id}")


# ============================================================================
# Issue Watchers
# ============================================================================

@mcp.tool()
def get_issue_watchers(issue_id_or_key: str) -> dict:
    """Returns the watchers for an issue."""
    return make_request("GET", f"/issue/{issue_id_or_key}/watchers")


@mcp.tool()
def add_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """Adds a user as a watcher of an issue."""
    data = account_id
    return make_request("POST", f"/issue/{issue_id_or_key}/watchers", data=data)


@mcp.tool()
def remove_issue_watcher(issue_id_or_key: str, account_id: str) -> dict:
    """Deletes a user as a watcher of an issue."""
    return make_request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


@mcp.tool()
def check_issues_watching(issue_ids: list) -> dict:
    """Returns the watching status for multiple issues."""
    data = {"issueIds": issue_ids}
    return make_request("POST", "/issue/watching", data=data)


# ============================================================================
# Issue Links
# ============================================================================

@mcp.tool()
def get_issue_link_types() -> dict:
    """Returns all issue link types."""
    return make_request("GET", "/issueLinkType")


@mcp.tool()
def create_issue_link(
    link_type_id: str,
    inward_issue_id_or_key: str,
    outward_issue_id_or_key: str,
    comment: str = None
) -> dict:
    """Creates an issue link."""
    data = {
        "linkType": {"id": link_type_id},
        "inwardIssue": {"id": inward_issue_id_or_key} if inward_issue_id_or_key.isdigit() else {"key": inward_issue_id_or_key},
        "outwardIssue": {"id": outward_issue_id_or_key} if outward_issue_id_or_key.isdigit() else {"key": outward_issue_id_or_key}
    }
    
    if comment:
        data["comment"] = {
            "body": comment
        }
    
    return make_request("POST", "/issueLink", data=data)


@mcp.tool()
def delete_issue_link(link_id: str) -> dict:
    """Deletes an issue link."""
    return make_request("DELETE", f"/issueLink/{link_id}")


# ============================================================================
# Issue Search (JQL)
# ============================================================================

@mcp.tool()
def search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: list = None,
    expand: str = None,
    validate_query: str = "validateIfPossible"
) -> dict:
    """Searches for issues using JQL."""
    data = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
        "validateQuery": validate_query
    }
    
    if fields:
        data["fields"] = fields
    
    if expand:
        data["expand"] = expand
    
    return make_request("POST", "/search", data=data)


@mcp.tool()
def search_issues_get(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: str = None,
    expand: str = None
) -> dict:
    """Searches for issues using JQL (GET version)."""
    params = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
        "validateQuery": "validateIfPossible"
    }
    
    if fields:
        params["fields"] = fields
    
    if expand:
        params["expand"] = expand
    
    return make_request("GET", "/search", params=params)


@mcp.tool()
def get_issue_picker_suggestions(query: str, current_jql: str = None) -> dict:
    """Returns issue suggestions for auto-completion."""
    params = {"query": query}
    if current_jql:
        params["currentJQL"] = current_jql
    
    return make_request("GET", "/issue/picker", params=params)


# ============================================================================
# Users
# ============================================================================

@mcp.tool()
def get_user(account_id: str = None, username: str = None, key: str = None) -> dict:
    """Returns a user."""
    params = {}
    if account_id:
        params["accountId"] = account_id
    if username:
        params["username"] = username
    if key:
        params["key"] = key
    
    return make_request("GET", "/user", params=params)


@mcp.tool()
def get_myself() -> dict:
    """Returns the current user."""
    return make_request("GET", "/myself")


@mcp.tool()
def search_users(query: str = None, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns a list of users matching a query."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if query:
        params["query"] = query
    
    return make_request("GET", "/users/search", params=params)


@mcp.tool()
def get_user_groups(account_id: str) -> dict:
    """Returns the groups a user belongs to."""
    return make_request("GET", "/user/groups", params={"accountId": account_id})


# ============================================================================
# Groups
# ============================================================================

@mcp.tool()
def get_group(group_id: str = None, group_name: str = None) -> dict:
    """Returns a group."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    
    return make_request("GET", "/group", params=params)


@mcp.tool()
def create_group(group_name: str) -> dict:
    """Creates a group."""
    data = {"name": group_name}
    return make_request("POST", "/group", data=data)


@mcp.tool()
def delete_group(group_id: str = None, group_name: str = None) -> dict:
    """Deletes a group."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    
    return make_request("DELETE", "/group", params=params)


@mcp.tool()
def get_group_members(group_id: str = None, group_name: str = None, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns users from a group."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    
    return make_request("GET", "/group/member", params=params)


@mcp.tool()
def add_user_to_group(group_id: str = None, group_name: str = None, account_id: str = None) -> dict:
    """Adds a user to a group."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    
    data = {}
    if account_id:
        data["accountId"] = account_id
    
    return make_request("POST", "/group/user", params=params, data=data)


@mcp.tool()
def remove_user_from_group(group_id: str = None, group_name: str = None, account_id: str = None) -> dict:
    """Removes a user from a group."""
    params = {}
    if group_id:
        params["groupId"] = group_id
    if group_name:
        params["groupname"] = group_name
    if account_id:
        params["accountId"] = account_id
    
    return make_request("DELETE", "/group/user", params=params)


@mcp.tool()
def find_groups(query: str = None, exclude: list = None, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns a list of groups matching a query."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if query:
        params["query"] = query
    if exclude:
        params["exclude"] = ",".join(exclude)
    
    return make_request("GET", "/groups/picker", params=params)


# ============================================================================
# Issue Types
# ============================================================================

@mcp.tool()
def get_issue_types() -> dict:
    """Returns all issue types."""
    return make_request("GET", "/issuetype")


@mcp.tool()
def create_issue_type(name: str, description: str = None, hierarchy_level: int = None) -> dict:
    """Creates an issue type."""
    data = {"name": name}
    
    if description:
        data["description"] = description
    if hierarchy_level is not None:
        data["hierarchyLevel"] = hierarchy_level
    
    return make_request("POST", "/issuetype", data=data)


@mcp.tool()
def update_issue_type(issue_type_id: str, name: str = None, description: str = None) -> dict:
    """Updates an issue type."""
    data = {}
    
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    
    return make_request("PUT", f"/issuetype/{issue_type_id}", data=data)


@mcp.tool()
def delete_issue_type(issue_type_id: str, alternative_issue_type_id: str = None) -> dict:
    """Deletes an issue type."""
    params = {}
    if alternative_issue_type_id:
        params["alternativeIssueTypeId"] = alternative_issue_type_id
    
    return make_request("DELETE", f"/issuetype/{issue_type_id}", params=params)


@mcp.tool()
def get_issue_type(issue_type_id: str) -> dict:
    """Returns an issue type."""
    return make_request("GET", f"/issuetype/{issue_type_id}")


@mcp.tool()
def get_issue_types_for_project(project_id: int) -> dict:
    """Returns issue types for a project."""
    params = {"projectId": project_id}
    return make_request("GET", "/issuetype/project", params=params)


@mcp.tool()
def get_alternative_issue_types(issue_type_id: str) -> dict:
    """Returns alternative issue types for an issue type."""
    return make_request("GET", f"/issuetype/{issue_type_id}/alternatives")


# ============================================================================
# Priorities
# ============================================================================

@mcp.tool()
def get_priorities() -> dict:
    """Returns all priorities."""
    return make_request("GET", "/priority")


@mcp.tool()
def create_priority(name: str, description: str = None, status_color: str = None) -> dict:
    """Creates a priority."""
    data = {"name": name}
    
    if description:
        data["description"] = description
    if status_color:
        data["statusColor"] = status_color
    
    return make_request("POST", "/priority", data=data)


@mcp.tool()
def update_priority(priority_id: str, name: str = None, description: str = None, status_color: str = None) -> dict:
    """Updates a priority."""
    data = {}
    
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if status_color:
        data["statusColor"] = status_color
    
    return make_request("PUT", f"/priority/{priority_id}", data=data)


@mcp.tool()
def delete_priority(priority_id: str) -> dict:
    """Deletes a priority."""
    return make_request("DELETE", f"/priority/{priority_id}")


@mcp.tool()
def get_priority(priority_id: str) -> dict:
    """Returns a priority."""
    return make_request("GET", f"/priority/{priority_id}")


# ============================================================================
# Statuses
# ============================================================================

@mcp.tool()
def get_statuses(status_ids: list) -> dict:
    """Returns statuses by ID."""
    params = {"id": status_ids}
    return make_request("GET", "/statuses", params=params)


@mcp.tool()
def search_statuses(project_id: str = None, search_string: str = None, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns a paginated list of statuses."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if project_id:
        params["projectId"] = project_id
    if search_string:
        params["searchString"] = search_string
    
    return make_request("GET", "/statuses/search", params=params)


@mcp.tool()
def get_statuses_by_name(names: list, project_id: str = None) -> dict:
    """Returns statuses by name."""
    params = {"name": names}
    if project_id:
        params["projectId"] = project_id
    
    return make_request("GET", "/statuses/byNames", params=params)


# ============================================================================
# Filters
# ============================================================================

@mcp.tool()
def create_filter(name: str, jql: str, description: str = None) -> dict:
    """Creates a filter."""
    data = {
        "name": name,
        "jql": jql
    }
    
    if description:
        data["description"] = description
    
    return make_request("POST", "/filter", data=data)


@mcp.tool()
def get_filter(filter_id: str) -> dict:
    """Returns a filter."""
    return make_request("GET", f"/filter/{filter_id}")


@mcp.tool()
def update_filter(filter_id: str, name: str = None, jql: str = None, description: str = None) -> dict:
    """Updates a filter."""
    data = {}
    
    if name:
        data["name"] = name
    if jql:
        data["jql"] = jql
    if description:
        data["description"] = description
    
    return make_request("PUT", f"/filter/{filter_id}", data=data)


@mcp.tool()
def delete_filter(filter_id: str) -> dict:
    """Deletes a filter."""
    return make_request("DELETE", f"/filter/{filter_id}")


@mcp.tool()
def get_my_filters(include_favourites: bool = True) -> dict:
    """Returns filters owned by the user."""
    params = {"includeFavourites": include_favourites}
    return make_request("GET", "/filter/my", params=params)


@mcp.tool()
def get_favorite_filters() -> dict:
    """Returns the user's favorite filters."""
    return make_request("GET", "/filter/favourite")


@mcp.tool()
def search_filters(
    filter_name: str = None,
    account_id: str = None,
    group_name: str = None,
    project_id: int = None,
    start_at: int = 0,
    max_results: int = 50
) -> dict:
    """Searches for filters."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    
    if filter_name:
        params["filterName"] = filter_name
    if account_id:
        params["accountId"] = account_id
    if group_name:
        params["groupname"] = group_name
    if project_id:
        params["projectId"] = project_id
    
    return make_request("GET", "/filter/search", params=params)


# ============================================================================
# Components
# ============================================================================

@mcp.tool()
def get_project_components(project_id_or_key: str, start_at: int = 0, max_results: int = 50) -> dict:
    """Returns all components for a project."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    return make_request("GET", f"/project/{project_id_or_key}/components", params=params)


@mcp.tool()
def create_component(
    project_id_or_key: str,
    name: str,
    description: str = None,
    lead_account_id: str = None
) -> dict:
    """Creates a component."""
    data = {
        "name": name
    }
    
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    
    return make_request("POST", f"/project/{project_id_or_key}/components", data=data)


@mcp.tool()
def get_component(component_id: str) -> dict:
    """Returns a component."""
    return make_request("GET", f"/component/{component_id}")


@mcp.tool()
def update_component(
    component_id: str,
    name: str = None,
    description: str = None,
    lead_account_id: str = None
) -> dict:
    """Updates a component."""
    data = {}
    
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    
    return make_request("PUT", f"/component/{component_id}", data=data)


@mcp.tool()
def delete_component(component_id: str, move_issues_to: str = None) -> dict:
    """Deletes a component."""
    params = {}
    if move_issues_to:
        params["moveIssuesTo"] = move_issues_to
    
    return make_request("DELETE", f"/component/{component_id}", params=params)


# ============================================================================
# Versions
# ============================================================================

@mcp.tool()
def get_project_versions(project_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: str = None) -> dict:
    """Returns all versions for a project."""
    params = {
        "startAt": start_at,
        "maxResults": max_results
    }
    if order_by:
        params["orderBy"] = order_by
    
    return make_request("GET", f"/project/{project_id_or_key}/versions", params=params)


@mcp.tool()
def create_version(
    project_id_or_key: str,
    name: str,
    description: str = None,
    start_date: str = None,
    release_date: str = None,
    archived: bool = False,
    released: bool = False
) -> dict:
    """Creates a version."""
    data = {
        "name": name,
        "archived": archived,
        "released": released
    }
    
    if description:
        data["description"] = description
    if start_date:
        data["startDate"] = start_date
    if release_date:
        data["releaseDate"] = release_date
    
    return make_request("POST", f"/project/{project_id_or_key}/versions", data=data)


@mcp.tool()
def get_version(version_id: str) -> dict:
    """Returns a version."""
    return make_request("GET", f"/version/{version_id}")


@mcp.tool()
def update_version(version_id: str, name: str = None, description: str = None, release_date: str = None) -> dict:
    """Updates a version."""
    data = {}
    
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if release_date:
        data["releaseDate"] = release_date
    
    return make_request("PUT", f"/version/{version_id}", data=data)


@mcp.tool()
def delete_version(version_id: str, move_issues_to: str = None) -> dict:
    """Deletes a version."""
    params = {}
    if move_issues_to:
        params["moveIssuesTo"] = move_issues_to
    
    return make_request("DELETE", f"/version/{version_id}", params=params)


# ============================================================================
# Utilities
# ============================================================================

@mcp.tool()
def get_server_info() -> dict:
    """Returns information about the Jira server."""
    return make_request("GET", "/serverInfo")


@mcp.tool()
def get_my_permissions() -> dict:
    """Returns all permissions the user has."""
    return make_request("GET", "/permissions")


@mcp.tool()
def get_time_tracking_options() -> dict:
    """Returns time tracking options."""
    return make_request("GET", "/timeTrackingOption")


# Run the server
if __name__ == "__main__":
    mcp.run()
