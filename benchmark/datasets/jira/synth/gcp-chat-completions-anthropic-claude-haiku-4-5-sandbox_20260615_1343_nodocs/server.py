#!/usr/bin/env python3
"""
MCP Server for Jira Cloud REST API v3

Provides comprehensive tools for interacting with Jira Cloud, including:
- Issue management (create, read, update, delete, search)
- Project management
- User and group management
- Workflow transitions
- Comments and attachments
- And more
"""

import os
import json
import base64
from typing import Any, Optional, Dict, List
from urllib.parse import urljoin, quote

import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
server = FastMCP("jira-cloud")

# Configuration from environment
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# API base URL
API_BASE = f"{JIRA_BASE_URL}/rest/api/3"


def get_auth_header() -> Dict[str, str]:
    """Generate HTTP Basic Auth header for Jira API."""
    if not JIRA_EMAIL or not JIRA_API_TOKEN:
        return {}
    credentials = base64.b64encode(f"{JIRA_EMAIL}:{JIRA_API_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {credentials}"}


def make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make an HTTP request to the Jira API."""
    url = urljoin(API_BASE + "/", endpoint.lstrip("/"))
    
    req_headers = {"Content-Type": "application/json"}
    req_headers.update(get_auth_header())
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
        
        # Handle different response codes
        if response.status_code in (200, 201, 204):
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found", "status": 404}
        elif response.status_code == 400:
            try:
                return {"error": response.json(), "status": 400}
            except:
                return {"error": response.text, "status": 400}
        elif response.status_code == 401:
            return {"error": "Unauthorized - check credentials", "status": 401}
        elif response.status_code == 403:
            return {"error": "Forbidden", "status": 403}
        else:
            return {"error": f"HTTP {response.status_code}", "status": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# ISSUE OPERATIONS
# ============================================================================

@server.tool()
def create_issue(
    project_key: str,
    issue_type: str,
    summary: str,
    description: Optional[str] = None,
    assignee: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[List[str]] = None,
    components: Optional[List[str]] = None,
    custom_fields: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create a new issue in Jira.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
        issue_type: Issue type name (e.g., 'Bug', 'Task', 'Story')
        summary: Issue summary/title
        description: Issue description (optional)
        assignee: Assignee account ID (optional)
        priority: Priority name (e.g., 'High', 'Medium', 'Low')
        labels: List of labels (optional)
        components: List of component names (optional)
        custom_fields: Additional custom fields as dict (optional)
    
    Returns:
        Created issue details including key and ID
    """
    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": issue_type},
        "summary": summary,
    }
    
    if description:
        fields["description"] = {"version": 1, "type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}]}
    
    if assignee:
        fields["assignee"] = {"id": assignee}
    
    if priority:
        fields["priority"] = {"name": priority}
    
    if labels:
        fields["labels"] = labels
    
    if components:
        fields["components"] = [{"name": c} for c in components]
    
    if custom_fields:
        fields.update(custom_fields)
    
    return make_request("POST", "/issue", json_data={"fields": fields})


@server.tool()
def get_issue(issue_key: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get issue details by key.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        expand: Comma-separated list of fields to expand (e.g., 'changelog,transitions')
    
    Returns:
        Issue details
    """
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", f"/issue/{issue_key}", params=params)


@server.tool()
def update_issue(
    issue_key: str,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    assignee: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[List[str]] = None,
    custom_fields: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update an existing issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        summary: New summary (optional)
        description: New description (optional)
        assignee: New assignee account ID (optional)
        priority: New priority (optional)
        labels: New labels list (optional)
        custom_fields: Additional custom fields to update (optional)
    
    Returns:
        Update confirmation
    """
    fields = {}
    
    if summary is not None:
        fields["summary"] = summary
    
    if description is not None:
        fields["description"] = {"version": 1, "type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}]}
    
    if assignee is not None:
        fields["assignee"] = {"id": assignee}
    
    if priority is not None:
        fields["priority"] = {"name": priority}
    
    if labels is not None:
        fields["labels"] = labels
    
    if custom_fields:
        fields.update(custom_fields)
    
    return make_request("PUT", f"/issue/{issue_key}", json_data={"fields": fields})


@server.tool()
def delete_issue(issue_key: str) -> Dict[str, Any]:
    """
    Delete an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/issue/{issue_key}")


@server.tool()
def search_issues(
    jql: str,
    max_results: int = 50,
    start_at: int = 0,
    fields: Optional[List[str]] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for issues using JQL (Jira Query Language).
    
    Args:
        jql: JQL query string (e.g., 'project = PROJ AND status = Open')
        max_results: Maximum number of results (default 50)
        start_at: Starting index for pagination (default 0)
        fields: List of fields to return (optional)
        expand: Comma-separated fields to expand (optional)
    
    Returns:
        Search results with matching issues
    """
    params = {
        "jql": jql,
        "maxResults": max_results,
        "startAt": start_at,
    }
    
    if fields:
        params["fields"] = ",".join(fields)
    
    if expand:
        params["expand"] = expand
    
    return make_request("GET", "/search", params=params)


@server.tool()
def assign_issue(issue_key: str, assignee_id: str) -> Dict[str, Any]:
    """
    Assign an issue to a user.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        assignee_id: Assignee account ID
    
    Returns:
        Update confirmation
    """
    return make_request(
        "PUT",
        f"/issue/{issue_key}/assignee",
        json_data={"accountId": assignee_id}
    )


@server.tool()
def unassign_issue(issue_key: str) -> Dict[str, Any]:
    """
    Unassign an issue (remove assignee).
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        Update confirmation
    """
    return make_request(
        "PUT",
        f"/issue/{issue_key}/assignee",
        json_data={"accountId": None}
    )


@server.tool()
def transition_issue(
    issue_key: str,
    transition_id: str,
    comment: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Transition an issue to a different status.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        transition_id: Transition ID (get from get_issue with expand='transitions')
        comment: Optional comment to add during transition
    
    Returns:
        Transition confirmation
    """
    data = {"transition": {"id": transition_id}}
    
    if comment:
        data["update"] = {
            "comment": [
                {
                    "add": {
                        "body": {
                            "version": 1,
                            "type": "doc",
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
    
    return make_request("POST", f"/issue/{issue_key}/transitions", json_data=data)


@server.tool()
def get_issue_transitions(issue_key: str) -> Dict[str, Any]:
    """
    Get available transitions for an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of available transitions
    """
    return make_request("GET", f"/issue/{issue_key}/transitions")


# ============================================================================
# COMMENTS
# ============================================================================

@server.tool()
def add_comment(
    issue_key: str,
    comment_text: str,
    visibility: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a comment to an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        comment_text: Comment text
        visibility: Visibility restriction (e.g., 'group:developers')
    
    Returns:
        Created comment details
    """
    data = {
        "body": {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment_text}]
                }
            ]
        }
    }
    
    if visibility:
        data["visibility"] = {"type": "group", "value": visibility}
    
    return make_request("POST", f"/issue/{issue_key}/comments", json_data=data)


@server.tool()
def get_issue_comments(issue_key: str) -> Dict[str, Any]:
    """
    Get all comments on an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of comments
    """
    return make_request("GET", f"/issue/{issue_key}/comments")


@server.tool()
def update_comment(
    issue_key: str,
    comment_id: str,
    comment_text: str,
) -> Dict[str, Any]:
    """
    Update a comment on an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        comment_id: Comment ID
        comment_text: New comment text
    
    Returns:
        Updated comment details
    """
    data = {
        "body": {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment_text}]
                }
            ]
        }
    }
    
    return make_request("PUT", f"/issue/{issue_key}/comments/{comment_id}", json_data=data)


@server.tool()
def delete_comment(issue_key: str, comment_id: str) -> Dict[str, Any]:
    """
    Delete a comment from an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        comment_id: Comment ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/issue/{issue_key}/comments/{comment_id}")


# ============================================================================
# WORKLOGS
# ============================================================================

@server.tool()
def add_worklog(
    issue_key: str,
    time_spent: str,
    comment: Optional[str] = None,
    started: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a worklog entry to an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        time_spent: Time spent (e.g., '2h 30m', '1d')
        comment: Optional comment about the work
        started: ISO 8601 timestamp when work started (optional)
    
    Returns:
        Created worklog details
    """
    data = {"timeSpent": time_spent}
    
    if comment:
        data["comment"] = {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment}]
                }
            ]
        }
    
    if started:
        data["started"] = started
    
    return make_request("POST", f"/issue/{issue_key}/worklog", json_data=data)


@server.tool()
def get_issue_worklogs(issue_key: str) -> Dict[str, Any]:
    """
    Get all worklogs for an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of worklogs
    """
    return make_request("GET", f"/issue/{issue_key}/worklog")


@server.tool()
def delete_worklog(issue_key: str, worklog_id: str) -> Dict[str, Any]:
    """
    Delete a worklog entry.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        worklog_id: Worklog ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/issue/{issue_key}/worklog/{worklog_id}")


# ============================================================================
# ATTACHMENTS
# ============================================================================

@server.tool()
def add_attachment(
    issue_key: str,
    file_name: str,
    file_content: str,
) -> Dict[str, Any]:
    """
    Add an attachment to an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        file_name: Name of the file
        file_content: Base64-encoded file content
    
    Returns:
        Created attachment details
    """
    headers = get_auth_header()
    headers["X-Atlassian-Token"] = "no-check"
    
    url = urljoin(API_BASE + "/", f"issue/{issue_key}/attachments")
    
    try:
        files = {"file": (file_name, base64.b64decode(file_content))}
        response = requests.post(url, files=files, headers=headers, timeout=30)
        
        if response.status_code in (200, 201):
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}", "status": response.status_code}
    except Exception as e:
        return {"error": str(e)}


@server.tool()
def get_issue_attachments(issue_key: str) -> Dict[str, Any]:
    """
    Get all attachments for an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of attachments
    """
    result = get_issue(issue_key)
    if "error" in result:
        return result
    
    attachments = result.get("fields", {}).get("attachment", [])
    return {"attachments": attachments}


@server.tool()
def delete_attachment(attachment_id: str) -> Dict[str, Any]:
    """
    Delete an attachment.
    
    Args:
        attachment_id: Attachment ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/attachment/{attachment_id}")


# ============================================================================
# WATCHERS
# ============================================================================

@server.tool()
def add_watcher(issue_key: str, user_id: str) -> Dict[str, Any]:
    """
    Add a watcher to an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        user_id: User account ID
    
    Returns:
        Confirmation
    """
    return make_request("POST", f"/issue/{issue_key}/watchers", json_data={"accountId": user_id})


@server.tool()
def remove_watcher(issue_key: str, user_id: str) -> Dict[str, Any]:
    """
    Remove a watcher from an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
        user_id: User account ID
    
    Returns:
        Confirmation
    """
    return make_request("DELETE", f"/issue/{issue_key}/watchers", params={"accountId": user_id})


@server.tool()
def get_issue_watchers(issue_key: str) -> Dict[str, Any]:
    """
    Get all watchers for an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of watchers
    """
    return make_request("GET", f"/issue/{issue_key}/watchers")


# ============================================================================
# ISSUE LINKS
# ============================================================================

@server.tool()
def link_issues(
    inward_issue: str,
    outward_issue: str,
    link_type: str,
) -> Dict[str, Any]:
    """
    Create a link between two issues.
    
    Args:
        inward_issue: Inward issue key (e.g., 'PROJ-123')
        outward_issue: Outward issue key (e.g., 'PROJ-456')
        link_type: Link type name (e.g., 'relates to', 'blocks', 'is blocked by')
    
    Returns:
        Link confirmation
    """
    data = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue},
        "outwardIssue": {"key": outward_issue},
    }
    
    return make_request("POST", "/issueLink", json_data=data)


@server.tool()
def delete_issue_link(link_id: str) -> Dict[str, Any]:
    """
    Delete a link between issues.
    
    Args:
        link_id: Link ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/issueLink/{link_id}")


@server.tool()
def get_issue_links(issue_key: str) -> Dict[str, Any]:
    """
    Get all links for an issue.
    
    Args:
        issue_key: Issue key (e.g., 'PROJ-123')
    
    Returns:
        List of issue links
    """
    result = get_issue(issue_key)
    if "error" in result:
        return result
    
    links = result.get("fields", {}).get("issuelinks", [])
    return {"links": links}


# ============================================================================
# PROJECTS
# ============================================================================

@server.tool()
def get_project(project_key: str) -> Dict[str, Any]:
    """
    Get project details.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
    
    Returns:
        Project details
    """
    return make_request("GET", f"/project/{project_key}")


@server.tool()
def list_projects(
    expand: Optional[str] = None,
    recent: bool = False,
) -> Dict[str, Any]:
    """
    List all projects.
    
    Args:
        expand: Comma-separated fields to expand (optional)
        recent: Return only recently accessed projects (optional)
    
    Returns:
        List of projects
    """
    params = {}
    if expand:
        params["expand"] = expand
    if recent:
        params["recent"] = "true"
    
    return make_request("GET", "/project", params=params)


@server.tool()
def create_project(
    key: str,
    name: str,
    project_type: str = "software",
    template_key: str = "com.atlassian.jira-core-project-templates:jira-core-simplified-process-kanban",
) -> Dict[str, Any]:
    """
    Create a new project.
    
    Args:
        key: Project key (e.g., 'PROJ')
        name: Project name
        project_type: Project type ('software' or 'business')
        template_key: Template key for project
    
    Returns:
        Created project details
    """
    data = {
        "key": key,
        "name": name,
        "projectType": project_type,
        "projectTemplateKey": template_key,
    }
    
    return make_request("POST", "/project", json_data=data)


# ============================================================================
# COMPONENTS
# ============================================================================

@server.tool()
def get_project_components(project_key: str) -> Dict[str, Any]:
    """
    Get all components in a project.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
    
    Returns:
        List of components
    """
    return make_request("GET", f"/project/{project_key}/components")


@server.tool()
def create_component(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    lead_user_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a component in a project.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
        name: Component name
        description: Component description (optional)
        lead_user_id: Component lead account ID (optional)
    
    Returns:
        Created component details
    """
    data = {
        "name": name,
        "project": project_key,
    }
    
    if description:
        data["description"] = description
    
    if lead_user_id:
        data["leadUserName"] = lead_user_id
    
    return make_request("POST", "/component", json_data=data)


@server.tool()
def update_component(
    component_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a component.
    
    Args:
        component_id: Component ID
        name: New component name (optional)
        description: New description (optional)
    
    Returns:
        Updated component details
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    
    if description is not None:
        data["description"] = description
    
    return make_request("PUT", f"/component/{component_id}", json_data=data)


@server.tool()
def delete_component(component_id: str) -> Dict[str, Any]:
    """
    Delete a component.
    
    Args:
        component_id: Component ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/component/{component_id}")


# ============================================================================
# VERSIONS
# ============================================================================

@server.tool()
def get_project_versions(project_key: str) -> Dict[str, Any]:
    """
    Get all versions in a project.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
    
    Returns:
        List of versions
    """
    return make_request("GET", f"/project/{project_key}/versions")


@server.tool()
def create_version(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    released: bool = False,
    release_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a version in a project.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
        name: Version name
        description: Version description (optional)
        released: Whether version is released (optional)
        release_date: Release date in YYYY-MM-DD format (optional)
    
    Returns:
        Created version details
    """
    data = {
        "name": name,
        "project": project_key,
        "released": released,
    }
    
    if description:
        data["description"] = description
    
    if release_date:
        data["releaseDate"] = release_date
    
    return make_request("POST", "/version", json_data=data)


@server.tool()
def update_version(
    version_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    released: Optional[bool] = None,
    release_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a version.
    
    Args:
        version_id: Version ID
        name: New version name (optional)
        description: New description (optional)
        released: Whether version is released (optional)
        release_date: Release date in YYYY-MM-DD format (optional)
    
    Returns:
        Updated version details
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    
    if description is not None:
        data["description"] = description
    
    if released is not None:
        data["released"] = released
    
    if release_date is not None:
        data["releaseDate"] = release_date
    
    return make_request("PUT", f"/version/{version_id}", json_data=data)


@server.tool()
def delete_version(version_id: str) -> Dict[str, Any]:
    """
    Delete a version.
    
    Args:
        version_id: Version ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/version/{version_id}")


# ============================================================================
# USERS
# ============================================================================

@server.tool()
def get_user(user_id: str) -> Dict[str, Any]:
    """
    Get user details by account ID.
    
    Args:
        user_id: User account ID
    
    Returns:
        User details
    """
    return make_request("GET", f"/user", params={"accountId": user_id})


@server.tool()
def search_users(
    query: str,
    max_results: int = 50,
    start_at: int = 0,
) -> Dict[str, Any]:
    """
    Search for users.
    
    Args:
        query: Search query (name or email)
        max_results: Maximum results (default 50)
        start_at: Starting index (default 0)
    
    Returns:
        List of matching users
    """
    params = {
        "query": query,
        "maxResults": max_results,
        "startAt": start_at,
    }
    
    return make_request("GET", "/user/search", params=params)


@server.tool()
def get_project_users(project_key: str) -> Dict[str, Any]:
    """
    Get all users in a project.
    
    Args:
        project_key: Project key (e.g., 'PROJ')
    
    Returns:
        List of project users
    """
    return make_request("GET", f"/project/{project_key}/users")


# ============================================================================
# GROUPS
# ============================================================================

@server.tool()
def get_group(group_name: str) -> Dict[str, Any]:
    """
    Get group details.
    
    Args:
        group_name: Group name
    
    Returns:
        Group details
    """
    return make_request("GET", "/group", params={"groupname": group_name})


@server.tool()
def search_groups(query: str) -> Dict[str, Any]:
    """
    Search for groups.
    
    Args:
        query: Search query
    
    Returns:
        List of matching groups
    """
    return make_request("GET", "/groups/picker", params={"query": query})


@server.tool()
def add_user_to_group(user_id: str, group_name: str) -> Dict[str, Any]:
    """
    Add a user to a group.
    
    Args:
        user_id: User account ID
        group_name: Group name
    
    Returns:
        Confirmation
    """
    return make_request(
        "POST",
        "/group/user",
        params={"groupname": group_name},
        json_data={"accountId": user_id}
    )


@server.tool()
def remove_user_from_group(user_id: str, group_name: str) -> Dict[str, Any]:
    """
    Remove a user from a group.
    
    Args:
        user_id: User account ID
        group_name: Group name
    
    Returns:
        Confirmation
    """
    return make_request(
        "DELETE",
        "/group/user",
        params={"groupname": group_name, "accountId": user_id}
    )


# ============================================================================
# FILTERS
# ============================================================================

@server.tool()
def get_filter(filter_id: str) -> Dict[str, Any]:
    """
    Get filter details.
    
    Args:
        filter_id: Filter ID
    
    Returns:
        Filter details
    """
    return make_request("GET", f"/filter/{filter_id}")


@server.tool()
def list_filters(
    expand: Optional[str] = None,
    filter_type: str = "my",
) -> Dict[str, Any]:
    """
    List filters.
    
    Args:
        expand: Comma-separated fields to expand (optional)
        filter_type: Filter type ('my', 'shared', 'starred', 'search')
    
    Returns:
        List of filters
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    endpoint = f"/filter/{filter_type}"
    return make_request("GET", endpoint, params=params)


@server.tool()
def create_filter(
    name: str,
    jql: str,
    description: Optional[str] = None,
    favorite: bool = False,
) -> Dict[str, Any]:
    """
    Create a filter.
    
    Args:
        name: Filter name
        jql: JQL query
        description: Filter description (optional)
        favorite: Mark as favorite (optional)
    
    Returns:
        Created filter details
    """
    data = {
        "name": name,
        "jql": jql,
        "favourite": favorite,
    }
    
    if description:
        data["description"] = description
    
    return make_request("POST", "/filter", json_data=data)


@server.tool()
def update_filter(
    filter_id: str,
    name: Optional[str] = None,
    jql: Optional[str] = None,
    description: Optional[str] = None,
    favorite: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update a filter.
    
    Args:
        filter_id: Filter ID
        name: New filter name (optional)
        jql: New JQL query (optional)
        description: New description (optional)
        favorite: Mark as favorite (optional)
    
    Returns:
        Updated filter details
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    
    if jql is not None:
        data["jql"] = jql
    
    if description is not None:
        data["description"] = description
    
    if favorite is not None:
        data["favourite"] = favorite
    
    return make_request("PUT", f"/filter/{filter_id}", json_data=data)


@server.tool()
def delete_filter(filter_id: str) -> Dict[str, Any]:
    """
    Delete a filter.
    
    Args:
        filter_id: Filter ID
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/filter/{filter_id}")


# ============================================================================
# ISSUE TYPES
# ============================================================================

@server.tool()
def list_issue_types() -> Dict[str, Any]:
    """
    List all issue types.
    
    Returns:
        List of issue types
    """
    return make_request("GET", "/issuetype")


@server.tool()
def get_issue_type(issue_type_id: str) -> Dict[str, Any]:
    """
    Get issue type details.
    
    Args:
        issue_type_id: Issue type ID
    
    Returns:
        Issue type details
    """
    return make_request("GET", f"/issuetype/{issue_type_id}")


# ============================================================================
# PRIORITIES
# ============================================================================

@server.tool()
def list_priorities() -> Dict[str, Any]:
    """
    List all priorities.
    
    Returns:
        List of priorities
    """
    return make_request("GET", "/priority")


@server.tool()
def get_priority(priority_id: str) -> Dict[str, Any]:
    """
    Get priority details.
    
    Args:
        priority_id: Priority ID
    
    Returns:
        Priority details
    """
    return make_request("GET", f"/priority/{priority_id}")


# ============================================================================
# STATUSES
# ============================================================================

@server.tool()
def list_statuses() -> Dict[str, Any]:
    """
    List all statuses.
    
    Returns:
        List of statuses
    """
    return make_request("GET", "/status")


@server.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """
    Get status details.
    
    Args:
        status_id: Status ID
    
    Returns:
        Status details
    """
    return make_request("GET", f"/status/{status_id}")


# ============================================================================
# FIELDS
# ============================================================================

@server.tool()
def list_fields() -> Dict[str, Any]:
    """
    List all fields.
    
    Returns:
        List of fields with their configurations
    """
    return make_request("GET", "/field")


@server.tool()
def search_field(field_name: str) -> Dict[str, Any]:
    """
    Search for a field by name.
    
    Args:
        field_name: Field name or key
    
    Returns:
        Matching field details
    """
    result = list_fields()
    if "error" in result:
        return result
    
    fields = result if isinstance(result, list) else result.get("fields", [])
    matching = [f for f in fields if field_name.lower() in f.get("name", "").lower() or field_name.lower() in f.get("key", "").lower()]
    
    return {"fields": matching}


# ============================================================================
# DASHBOARDS
# ============================================================================

@server.tool()
def list_dashboards(
    max_results: int = 50,
    start_at: int = 0,
) -> Dict[str, Any]:
    """
    List all dashboards.
    
    Args:
        max_results: Maximum results (default 50)
        start_at: Starting index (default 0)
    
    Returns:
        List of dashboards
    """
    params = {
        "maxResults": max_results,
        "startAt": start_at,
    }
    
    return make_request("GET", "/dashboard", params=params)


@server.tool()
def get_dashboard(dashboard_id: str) -> Dict[str, Any]:
    """
    Get dashboard details.
    
    Args:
        dashboard_id: Dashboard ID
    
    Returns:
        Dashboard details
    """
    return make_request("GET", f"/dashboard/{dashboard_id}")


# ============================================================================
# RESOLUTIONS
# ============================================================================

@server.tool()
def list_resolutions() -> Dict[str, Any]:
    """
    List all resolutions.
    
    Returns:
        List of resolutions
    """
    return make_request("GET", "/resolution")


@server.tool()
def get_resolution(resolution_id: str) -> Dict[str, Any]:
    """
    Get resolution details.
    
    Args:
        resolution_id: Resolution ID
    
    Returns:
        Resolution details
    """
    return make_request("GET", f"/resolution/{resolution_id}")


# ============================================================================
# CONFIGURATION
# ============================================================================

@server.tool()
def get_server_info() -> Dict[str, Any]:
    """
    Get Jira server information.
    
    Returns:
        Server details including version and capabilities
    """
    return make_request("GET", "/serverInfo")


@server.tool()
def get_myself() -> Dict[str, Any]:
    """
    Get current user information.
    
    Returns:
        Current user details
    """
    return make_request("GET", "/myself")


if __name__ == "__main__":
    server.run()
