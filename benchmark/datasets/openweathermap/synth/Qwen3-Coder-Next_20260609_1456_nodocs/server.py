import os
import requests
from typing import Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("jira")

# Jira base URL
JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "https://your-org.atlassian.net").rstrip("/")


def get_auth() -> tuple[str, str]:
    """Get Jira authentication credentials."""
    email = os.environ.get("JIRA_EMAIL")
    api_token = os.environ.get("JIRA_API_TOKEN")
    if not email or not api_token:
        raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set")
    return email, api_token


def jira_request(
    method: str,
    endpoint: str,
    params: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
    files: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Make a request to the Jira REST API."""
    try:
        url = f"{JIRA_BASE_URL}/rest/api/3{endpoint}"
        email, api_token = get_auth()
        
        headers = {"Accept": "application/json"}
        if files:
            headers.pop("Content-Type", None)  # Let requests set multipart content type
        
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            files=files,
            headers=headers,
            auth=(email, api_token),
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
    except ValueError as e:
        return {"error": str(e)}


@mcp.tool()
def get_issue(issueIdOrKey: str) -> dict[str, Any]:
    """Get an issue by ID or key.
    
    Args:
        issueIdOrKey: The issue ID or key (e.g., "PROJ-123" or "12345")
    
    Returns:
        Issue details including fields, transitions, etc.
    """
    return jira_request("GET", f"/issue/{issueIdOrKey}")


@mcp.tool()
def update_issue(issueIdOrKey: str, update: dict[str, Any], fields: dict[str, Any] | None = None, update_history: bool = True) -> dict[str, Any]:
    """Update an issue.
    
    Args:
        issueIdOrKey: The issue ID or key
        update: Issue update operations (e.g., {"summary": [{"set": "New summary"}]})
        fields: Issue fields to update (e.g., {"summary": "New summary"})
        update_history: Whether to update the issue history
    
    Returns:
        Updated issue details
    """
    data = {"update": update, "fields": fields or {}, "updateHistory": update_history}
    return jira_request("PUT", f"/issue/{issueIdOrKey}", json=data)


@mcp.tool()
def delete_issue(issueIdOrKey: str, delete_subtasks: bool = True) -> dict[str, Any]:
    """Delete an issue.
    
    Args:
        issueIdOrKey: The issue ID or key
        delete_subtasks: Whether to delete subtasks
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/issue/{issueIdOrKey}", params={"deleteSubtasks": str(delete_subtasks).lower()})


@mcp.tool()
def create_issue(
    fields: dict[str, Any],
    update: dict[str, Any] | None = None,
    update_history: bool = True,
    properties: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Create a new issue.
    
    Args:
        fields: Issue fields (summary, description, project, issuetype, etc.)
        update: Issue update operations
        update_history: Whether to update the issue history
        properties: Issue properties to set
    
    Returns:
        Created issue details with key and ID
    """
    data = {
        "fields": fields,
        "update": update or {},
        "updateHistory": update_history,
        "properties": properties or [],
    }
    return jira_request("POST", "/issue", json=data)


@mcp.tool()
def search_issues_jql(
    jql: str,
    start: int = 0,
    max_results: int = 50,
    validate_query: str = "warn",
    fields: list[str] | None = None,
    expand: list[str] | None = None,
    properties: list[str] | None = None,
    language: str = "jql",
) -> dict[str, Any]:
    """Search issues using JQL query.
    
    Args:
        jql: JQL query string
        start: Starting index for pagination
        max_results: Maximum number of results
        validate_query: Validation behavior (strict, warn, log, ignore)
        fields: List of fields to return
        expand: Fields to expand (changelog, renderings, etc.)
        properties: Issue properties to include
        language: Query language (defaults to jql)
    
    Returns:
        Search results with issues and metadata
    """
    data = {
        "jql": jql,
        "start": start,
        "maxResults": max_results,
        "validateQuery": validate_query,
        "fields": fields or ["*all"],
        "expand": expand or [],
        "properties": properties or [],
        "language": language,
    }
    return jira_request("POST", "/search", json=data)


@mcp.tool()
def get_project(projectIdOrKey: str) -> dict[str, Any]:
    """Get project details.
    
    Args:
        projectIdOrKey: Project ID or key
    
    Returns:
        Project details including lead, assignee, etc.
    """
    return jira_request("GET", f"/project/{projectIdOrKey}")


@mcp.tool()
def list_projects(
    start: int = 0,
    max_results: int = 50,
    expand: str | None = None,
    status: list[str] | None = None,
) -> dict[str, Any]:
    """List projects.
    
    Args:
        start: Starting index for pagination
        max_results: Maximum number of results
        expand: Fields to expand
        status: Filter by project status
    
    Returns:
        List of projects with metadata
    """
    params = {
        "start": start,
        "maxResults": max_results,
        "expand": expand or "description,lead,projectKeys",
    }
    if status:
        params["status"] = status
    return jira_request("GET", "/project", params=params)


@mcp.tool()
def create_project(
    key: str,
    name: str,
    description: str = "",
    lead_id: str | None = None,
    lead_account_id: str | None = None,
    assignee_type: str = "PROJECT_LEAD",
    project_type: str = "business",
    project_style: str = "classic",
    avatar_id: str | None = None,
    notification_scheme: str | None = None,
    permission_scheme: str | None = None,
    issue_security_scheme: str | None = None,
    category_id: str | None = None,
) -> dict[str, Any]:
    """Create a new project.
    
    Args:
        key: Project key (e.g., "PROJ")
        name: Project name
        description: Project description
        lead_id: User ID of project lead (legacy)
        lead_account_id: Account ID of project lead
        assignee_type: Who can be assigned to issues
        project_type: Type of project (business, service, software, knowledge)
        project_style: Project style (classic or next-gen)
        avatar_id: ID of project avatar
        notification_scheme: Notification scheme ID
        permission_scheme: Permission scheme ID
        issue_security_scheme: Security scheme ID
        category_id: Category ID
    
    Returns:
        Created project details
    """
    data = {
        "key": key,
        "name": name,
        "description": description,
        "leadAccountId": lead_account_id,
        "assigneeType": assignee_type,
        "projectTypeKey": project_type,
        "projectStyle": project_style,
        "avatarId": avatar_id,
        "notificationScheme": notification_scheme,
        "permissionScheme": permission_scheme,
        "issueSecurityScheme": issue_security_scheme,
        "categoryId": category_id,
    }
    if lead_id:
        data["leadId"] = lead_id
    return jira_request("POST", "/project", json=data)


@mcp.tool()
def update_project(
    projectIdOrKey: str,
    name: str | None = None,
    description: str | None = None,
    lead_id: str | None = None,
    lead_account_id: str | None = None,
    assignee_type: str | None = None,
    project_type: str | None = None,
    project_style: str | None = None,
    avatar_id: str | None = None,
    notification_scheme: str | None = None,
    permission_scheme: str | None = None,
    issue_security_scheme: str | None = None,
    category_id: str | None = None,
) -> dict[str, Any]:
    """Update project details.
    
    Args:
        projectIdOrKey: Project ID or key
        name: New project name
        description: New description
        lead_id: New project lead ID
        lead_account_id: New project lead account ID
        assignee_type: New assignee type
        project_type: New project type
        project_style: New project style
        avatar_id: New avatar ID
        notification_scheme: New notification scheme ID
        permission_scheme: New permission scheme ID
        issue_security_scheme: New security scheme ID
        category_id: New category ID
    
    Returns:
        Updated project details
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if lead_account_id is not None:
        data["leadAccountId"] = lead_account_id
    if lead_id is not None:
        data["leadId"] = lead_id
    if assignee_type is not None:
        data["assigneeType"] = assignee_type
    if project_type is not None:
        data["projectTypeKey"] = project_type
    if project_style is not None:
        data["projectStyle"] = project_style
    if avatar_id is not None:
        data["avatarId"] = avatar_id
    if notification_scheme is not None:
        data["notificationScheme"] = notification_scheme
    if permission_scheme is not None:
        data["permissionScheme"] = permission_scheme
    if issue_security_scheme is not None:
        data["issueSecurityScheme"] = issue_security_scheme
    if category_id is not None:
        data["categoryId"] = category_id
    
    return jira_request("PUT", f"/project/{projectIdOrKey}", json=data)


@mcp.tool()
def delete_project(projectIdOrKey: str) -> dict[str, Any]:
    """Delete a project.
    
    Args:
        projectIdOrKey: Project ID or key
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/project/{projectIdOrKey}")


@mcp.tool()
def assign_issue(issueIdOrKey: str, accountId: str | None = None, key: str | None = None) -> dict[str, Any]:
    """Assign an issue to a user.
    
    Args:
        issueIdOrKey: Issue ID or key
        accountId: Account ID of user to assign to
        key: Username (legacy)
    
    Returns:
        Assignment result
    """
    data = {}
    if accountId is not None:
        data["accountId"] = accountId
    if key is not None:
        data["key"] = key
    
    if not data:
        return {"error": "Either accountId or key must be provided"}
    
    return jira_request("POST", f"/issue/{issueIdOrKey}/assignee", json=data)


@mcp.tool()
def transition_issue(
    issueIdOrKey: str,
    transition_id: str,
    update: dict[str, Any] | None = None,
    fields: dict[str, Any] | None = None,
    comment: str | None = None,
) -> dict[str, Any]:
    """Transition an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        transition_id: Transition ID
        update: Issue update operations
        fields: Issue fields to set during transition
        comment: Optional comment to add during transition
    
    Returns:
        Transition result
    """
    data = {
        "transition": {"id": transition_id},
    }
    if update:
        data["update"] = update
    if fields:
        data["fields"] = fields
    if comment:
        data["comment"] = {"body": comment}
    
    return jira_request("POST", f"/issue/{issueIdOrKey}/transitions", json=data)


@mcp.tool()
def add_comment(
    issueIdOrKey: str,
    body: str,
    visibility: dict[str, str] | None = None,
    properties: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Add a comment to an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        body: Comment body text
        visibility: Comment visibility (type, value)
        properties: Comment properties
    
    Returns:
        Created comment details
    """
    data = {"body": body}
    if visibility:
        data["visibility"] = visibility
    if properties:
        data["properties"] = properties
    
    return jira_request("POST", f"/issue/{issueIdOrKey}/comment", json=data)


@mcp.tool()
def update_comment(
    issueIdOrKey: str,
    commentId: str,
    body: str,
    visibility: dict[str, str] | None = None,
    properties: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Update a comment.
    
    Args:
        issueIdOrKey: Issue ID or key
        commentId: Comment ID
        body: New comment body
        visibility: New visibility
        properties: New properties
    
    Returns:
        Updated comment details
    """
    data = {"body": body}
    if visibility:
        data["visibility"] = visibility
    if properties:
        data["properties"] = properties
    
    return jira_request("PUT", f"/issue/{issueIdOrKey}/comment/{commentId}", json=data)


@mcp.tool()
def delete_comment(issueIdOrKey: str, commentId: str) -> dict[str, Any]:
    """Delete a comment.
    
    Args:
        issueIdOrKey: Issue ID or key
        commentId: Comment ID
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/issue/{issueIdOrKey}/comment/{commentId}")


@mcp.tool()
def add_worklog(
    issueIdOrKey: str,
    comment: str | None = None,
    adjust_estimate: str | None = None,
    new_estimate: str | None = None,
    reduce_by: str | None = None,
    started: str | None = None,
    time_spent: str | None = None,
) -> dict[str, Any]:
    """Add a worklog to an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        comment: Optional worklog comment
        adjust_estimate: Estimate adjustment (new, leave, manual)
        new_estimate: New estimate value
        reduce_by: Amount to reduce by
        started: Worklog start time (ISO 8601)
        time_spent: Time spent (e.g., "1h 30m")
    
    Returns:
        Created worklog details
    """
    data = {}
    if comment:
        data["comment"] = comment
    if adjust_estimate:
        data["adjustEstimate"] = adjust_estimate
    if new_estimate:
        data["newEstimate"] = new_estimate
    if reduce_by:
        data["reduceBy"] = reduce_by
    if started:
        data["started"] = started
    if time_spent:
        data["timeSpent"] = time_spent
    
    return jira_request("POST", f"/issue/{issueIdOrKey}/worklog", json=data)


@mcp.tool()
def update_worklog(
    issueIdOrKey: str,
    worklogId: str,
    comment: str | None = None,
    adjust_estimate: str | None = None,
    new_estimate: str | None = None,
    reduce_by: str | None = None,
    started: str | None = None,
    time_spent: str | None = None,
) -> dict[str, Any]:
    """Update a worklog.
    
    Args:
        issueIdOrKey: Issue ID or key
        worklogId: Worklog ID
        comment: New comment
        adjust_estimate: Estimate adjustment
        new_estimate: New estimate
        reduce_by: Amount to reduce by
        started: New start time
        time_spent: New time spent
    
    Returns:
        Updated worklog details
    """
    data = {}
    if comment:
        data["comment"] = comment
    if adjust_estimate:
        data["adjustEstimate"] = adjust_estimate
    if new_estimate:
        data["newEstimate"] = new_estimate
    if reduce_by:
        data["reduceBy"] = reduce_by
    if started:
        data["started"] = started
    if time_spent:
        data["timeSpent"] = time_spent
    
    return jira_request("PUT", f"/issue/{issueIdOrKey}/worklog/{worklogId}", json=data)


@mcp.tool()
def delete_worklog(issueIdOrKey: str, worklogId: str) -> dict[str, Any]:
    """Delete a worklog.
    
    Args:
        issueIdOrKey: Issue ID or key
        worklogId: Worklog ID
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/issue/{issueIdOrKey}/worklog/{worklogId}")


@mcp.tool()
def add_attachment(issueIdOrKey: str, filename: str, file_content: bytes) -> dict[str, Any]:
    """Add an attachment to an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        filename: Name of the file
        file_content: Binary content of the file
    
    Returns:
        Created attachment details
    """
    try:
        import base64
        import io
        
        # Create multipart form data
        import requests
        url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issueIdOrKey}/attachments"
        email, api_token = get_auth()
        
        files = {
            "file": (filename, io.BytesIO(file_content)),
        }
        
        response = requests.post(
            url=url,
            headers={"Accept": "application/json"},
            auth=(email, api_token),
            files=files,
        )
        
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def add_watcher(issueIdOrKey: str, accountId: str) -> dict[str, Any]:
    """Add a watcher to an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        accountId: Account ID of watcher
    
    Returns:
        Success message or error
    """
    data = {"accountId": accountId}
    return jira_request("POST", f"/issue/{issueIdOrKey}/watchers", json=data)


@mcp.tool()
def remove_watcher(issueIdOrKey: str, accountId: str) -> dict[str, Any]:
    """Remove a watcher from an issue.
    
    Args:
        issueIdOrKey: Issue ID or key
        accountId: Account ID of watcher to remove
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/issue/{issueIdOrKey}/watchers", params={"accountId": accountId})


@mcp.tool()
def get_users_by_project(projectIdOrKey: str, start: int = 0, max_results: int = 50) -> dict[str, Any]:
    """Get users in a project.
    
    Args:
        projectIdOrKey: Project ID or key
        start: Starting index
        max_results: Maximum results
    
    Returns:
        List of users with metadata
    """
    params = {
        "start": start,
        "maxResults": max_results,
    }
    return jira_request("GET", f"/project/{projectIdOrKey}/users", params=params)


@mcp.tool()
def get_issue_types(start: int = 0, max_results: int = 50, expand: str | None = None) -> dict[str, Any]:
    """Get all issue types.
    
    Args:
        start: Starting index
        max_results: Maximum results
        expand: Fields to expand
    
    Returns:
        List of issue types
    """
    params = {
        "start": start,
        "maxResults": max_results,
        "expand": expand or "icon",
    }
    return jira_request("GET", "/issuetype", params=params)


@mcp.tool()
def get_priorities(start: int = 0, max_results: int = 50, expand: str | None = None) -> dict[str, Any]:
    """Get all priorities.
    
    Args:
        start: Starting index
        max_results: Maximum results
        expand: Fields to expand
    
    Returns:
        List of priorities
    """
    params = {
        "start": start,
        "maxResults": max_results,
        "expand": expand or "icon",
    }
    return jira_request("GET", "/priority", params=params)


@mcp.tool()
def get_statuses(start: int = 0, max_results: int = 50, expand: str | None = None) -> dict[str, Any]:
    """Get all statuses.
    
    Args:
        start: Starting index
        max_results: Maximum results
        expand: Fields to expand
    
    Returns:
        List of statuses
    """
    params = {
        "start": start,
        "maxResults": max_results,
        "expand": expand or "icon",
    }
    return jira_request("GET", "/status", params=params)


@mcp.tool()
def get_issue_type(id: str) -> dict[str, Any]:
    """Get an issue type by ID.
    
    Args:
        id: Issue type ID
    
    Returns:
        Issue type details
    """
    return jira_request("GET", f"/issuetype/{id}")


@mcp.tool()
def get_priority(id: str) -> dict[str, Any]:
    """Get a priority by ID.
    
    Args:
        id: Priority ID
    
    Returns:
        Priority details
    """
    return jira_request("GET", f"/priority/{id}")


@mcp.tool()
def get_status(id: str) -> dict[str, Any]:
    """Get a status by ID.
    
    Args:
        id: Status ID
    
    Returns:
        Status details
    """
    return jira_request("GET", f"/status/{id}")


@mcp.tool()
def get_version(id: str) -> dict[str, Any]:
    """Get a version by ID.
    
    Args:
        id: Version ID
    
    Returns:
        Version details
    """
    return jira_request("GET", f"/version/{id}")


@mcp.tool()
def create_version(
    name: str,
    project_id_or_key: str,
    description: str = "",
    release_date: str | None = None,
    overdue: bool = False,
    user_start_date: str | None = None,
    user_release_date: str | None = None,
    start_date: str | None = None,
    archived: bool = False,
    released: bool = False,
    move_unfixed_issues_to: str | None = None,
) -> dict[str, Any]:
    """Create a version.
    
    Args:
        name: Version name
        project_id_or_key: Project ID or key
        description: Version description
        release_date: Release date (YYYY-MM-DD)
        overdue: Whether version is overdue
        user_start_date: User start date
        user_release_date: User release date
        start_date: Start date
        archived: Whether version is archived
        released: Whether version is released
        move_unfixed_issues_to: Move unfixed issues to this version
    
    Returns:
        Created version details
    """
    data = {
        "name": name,
        "description": description,
        "archived": archived,
        "released": released,
        "projectId": project_id_or_key,
    }
    if release_date:
        data["releaseDate"] = release_date
    if overdue:
        data["overdue"] = overdue
    if user_start_date:
        data["userStartDate"] = user_start_date
    if user_release_date:
        data["userReleaseDate"] = user_release_date
    if start_date:
        data["startDate"] = start_date
    if move_unfixed_issues_to:
        data["moveUnfixedIssuesTo"] = move_unfixed_issues_to
    
    return jira_request("POST", "/version", json=data)


@mcp.tool()
def update_version(
    id: str,
    name: str | None = None,
    description: str | None = None,
    release_date: str | None = None,
    overdue: bool | None = None,
    user_start_date: str | None = None,
    user_release_date: str | None = None,
    start_date: str | None = None,
    archived: bool | None = None,
    released: bool | None = None,
    move_unfixed_issues_to: str | None = None,
) -> dict[str, Any]:
    """Update a version.
    
    Args:
        id: Version ID
        name: New name
        description: New description
        release_date: New release date
        overdue: New overdue status
        user_start_date: New user start date
        user_release_date: New user release date
        start_date: New start date
        archived: New archived status
        released: New released status
        move_unfixed_issues_to: New move unfixed issues to version
    
    Returns:
        Updated version details
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if release_date is not None:
        data["releaseDate"] = release_date
    if overdue is not None:
        data["overdue"] = overdue
    if user_start_date is not None:
        data["userStartDate"] = user_start_date
    if user_release_date is not None:
        data["userReleaseDate"] = user_release_date
    if start_date is not None:
        data["startDate"] = start_date
    if archived is not None:
        data["archived"] = archived
    if released is not None:
        data["released"] = released
    if move_unfixed_issues_to is not None:
        data["moveUnfixedIssuesTo"] = move_unfixed_issues_to
    
    return jira_request("PUT", f"/version/{id}", json=data)


@mcp.tool()
def delete_version(id: str, move_unfixed_issues_to: str | None = None) -> dict[str, Any]:
    """Delete a version.
    
    Args:
        id: Version ID
        move_unfixed_issues_to: Move unfixed issues to this version before deleting
    
    Returns:
        Success message or error
    """
    params = {}
    if move_unfixed_issues_to:
        params["moveUnfixedIssuesTo"] = move_unfixed_issues_to
    return jira_request("DELETE", f"/version/{id}", params=params)


@mcp.tool()
def get_components(projectIdOrKey: str, start: int = 0, max_results: int = 50) -> dict[str, Any]:
    """Get components for a project.
    
    Args:
        projectIdOrKey: Project ID or key
        start: Starting index
        max_results: Maximum results
    
    Returns:
        List of components
    """
    params = {
        "start": start,
        "maxResults": max_results,
    }
    return jira_request("GET", f"/project/{projectIdOrKey}/components", params=params)


@mcp.tool()
def create_component(
    name: str,
    project_id_or_key: str,
    description: str = "",
    lead_id: str | None = None,
    lead_account_id: str | None = None,
    assignee_type: str | None = None,
    archiver_account_id: str | None = None,
) -> dict[str, Any]:
    """Create a component.
    
    Args:
        name: Component name
        project_id_or_key: Project ID or key
        description: Component description
        lead_id: Component lead ID
        lead_account_id: Component lead account ID
        assignee_type: Assignee type
        archiver_account_id: Archiver account ID
    
    Returns:
        Created component details
    """
    data = {
        "name": name,
        "description": description,
        "projectId": project_id_or_key,
    }
    if lead_id:
        data["leadAccountId"] = lead_id
    if lead_account_id:
        data["leadAccountId"] = lead_account_id
    if assignee_type:
        data["assigneeType"] = assignee_type
    if archiver_account_id:
        data["archiverAccountId"] = archiver_account_id
    
    return jira_request("POST", f"/project/{project_id_or_key}/components", json=data)


@mcp.tool()
def update_component(
    id: str,
    name: str | None = None,
    description: str | None = None,
    lead_id: str | None = None,
    lead_account_id: str | None = None,
    assignee_type: str | None = None,
    archiver_account_id: str | None = None,
) -> dict[str, Any]:
    """Update a component.
    
    Args:
        id: Component ID
        name: New name
        description: New description
        lead_id: New lead ID
        lead_account_id: New lead account ID
        assignee_type: New assignee type
        archiver_account_id: New archiver account ID
    
    Returns:
        Updated component details
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if lead_account_id is not None:
        data["leadAccountId"] = lead_account_id
    if lead_id is not None:
        data["leadAccountId"] = lead_id
    if assignee_type is not None:
        data["assigneeType"] = assignee_type
    if archiver_account_id is not None:
        data["archiverAccountId"] = archiver_account_id
    
    return jira_request("PUT", f"/component/{id}", json=data)


@mcp.tool()
def delete_component(id: str) -> dict[str, Any]:
    """Delete a component.
    
    Args:
        id: Component ID
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/component/{id}")


@mcp.tool()
def create_filter(
    name: str,
    description: str = "",
    jql: str = "",
    shared_with: str | None = None,
    favourite: bool = False,
) -> dict[str, Any]:
    """Create a filter.
    
    Args:
        name: Filter name
        description: Filter description
        jql: JQL query
        shared_with: Who to share with ("all" or "logged-in")
        favourite: Whether to mark as favourite
    
    Returns:
        Created filter details
    """
    data = {
        "name": name,
        "description": description,
        "jql": jql,
        "favourite": favourite,
    }
    if shared_with:
        data["sharedWith"] = {"type": shared_with}
    
    return jira_request("POST", "/filter", json=data)


@mcp.tool()
def get_filter(id: str) -> dict[str, Any]:
    """Get a filter by ID.
    
    Args:
        id: Filter ID
    
    Returns:
        Filter details including JQL, owner, etc.
    """
    return jira_request("GET", f"/filter/{id}")


@mcp.tool()
def update_filter(
    id: str,
    name: str | None = None,
    description: str | None = None,
    jql: str | None = None,
    favourite: bool | None = None,
    shared_with: str | None = None,
) -> dict[str, Any]:
    """Update a filter.
    
    Args:
        id: Filter ID
        name: New name
        description: New description
        jql: New JQL query
        favourite: New favourite status
        shared_with: New share type
    
    Returns:
        Updated filter details
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if jql is not None:
        data["jql"] = jql
    if favourite is not None:
        data["favourite"] = favourite
    if shared_with is not None:
        data["sharedWith"] = {"type": shared_with}
    
    return jira_request("PUT", f"/filter/{id}", json=data)


@mcp.tool()
def delete_filter(id: str) -> dict[str, Any]:
    """Delete a filter.
    
    Args:
        id: Filter ID
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/filter/{id}")


@mcp.tool()
def get_groups(start: int = 0, max_results: int = 50, exclude: list[str] | None = None) -> dict[str, Any]:
    """Get groups.
    
    Args:
        start: Starting index
        max_results: Maximum results
        exclude: Groups to exclude
    
    Returns:
        List of groups with metadata
    """
    params = {
        "start": start,
        "maxResults": max_results,
    }
    if exclude:
        params["exclude"] = ",".join(exclude)
    return jira_request("GET", "/group", params=params)


@mcp.tool()
def create_group(name: str) -> dict[str, Any]:
    """Create a group.
    
    Args:
        name: Group name
    
    Returns:
        Created group details
    """
    data = {"name": name}
    return jira_request("POST", "/group", json=data)


@mcp.tool()
def add_user_to_group(
    group_name: str,
    account_id: str | None = None,
    username: str | None = None,
) -> dict[str, Any]:
    """Add a user to a group.
    
    Args:
        group_name: Group name
        account_id: User account ID
        username: Username (legacy)
    
    Returns:
        Success message or error
    """
    if not account_id and not username:
        return {"error": "Either accountId or username must be provided"}
    
    data = {}
    if account_id:
        data["accountId"] = account_id
    if username:
        data["name"] = username
    
    return jira_request("POST", "/group/user", json=data, params={"groupname": group_name})


@mcp.tool()
def remove_user_from_group(
    group_name: str,
    account_id: str | None = None,
    username: str | None = None,
) -> dict[str, Any]:
    """Remove a user from a group.
    
    Args:
        group_name: Group name
        account_id: User account ID
        username: Username (legacy)
    
    Returns:
        Success message or error
    """
    params = {"groupname": group_name}
    if account_id:
        params["accountId"] = account_id
    if username:
        params["username"] = username
    
    return jira_request("DELETE", "/group/user", params=params)


@mcp.tool()
def get_user(
    account_id: str | None = None,
    username: str | None = None,
    key: str | None = None,
    expand: str | None = None,
) -> dict[str, Any]:
    """Get user details.
    
    Args:
        account_id: User account ID
        username: Username (legacy)
        key: User key (legacy)
        expand: Fields to expand
    
    Returns:
        User details
    """
    params = {}
    if account_id:
        params["accountId"] = account_id
    if username:
        params["username"] = username
    if key:
        params["key"] = key
    if expand:
        params["expand"] = expand
    
    return jira_request("GET", "/user", params=params)


@mcp.tool()
def search_users(
    query: str,
    start: int = 0,
    max_results: int = 50,
    active: bool | None = None,
    exclude: list[str] | None = None,
) -> dict[str, Any]:
    """Search users.
    
    Args:
        query: Search query
        start: Starting index
        max_results: Maximum results
        active: Filter by active status
        exclude: Users to exclude
    
    Returns:
        List of matching users
    """
    params = {
        "query": query,
        "start": start,
        "maxResults": max_results,
    }
    if active is not None:
        params["active"] = str(active).lower()
    if exclude:
        params["exclude"] = ",".join(exclude)
    
    return jira_request("GET", "/user/search", params=params)


@mcp.tool()
def create_issue_link(
    type_id: str,
    inward_issue_id: str,
    outward_issue_id: str,
    comment: str | None = None,
) -> dict[str, Any]:
    """Create an issue link.
    
    Args:
        type_id: Issue link type ID
        inward_issue_id: Inward issue ID
        outward_issue_id: Outward issue ID
        comment: Optional comment
    
    Returns:
        Created issue link details
    """
    data = {
        "type": {"id": type_id},
        "inwardIssue": {"id": inward_issue_id},
        "outwardIssue": {"id": outward_issue_id},
    }
    if comment:
        data["comment"] = {"body": comment}
    
    return jira_request("POST", "/issueLink", json=data)


@mcp.tool()
def get_issue_links(issueLinkId: str) -> dict[str, Any]:
    """Get an issue link by ID.
    
    Args:
        issueLinkId: Issue link ID
    
    Returns:
        Issue link details
    """
    return jira_request("GET", f"/issueLink/{issueLinkId}")


@mcp.tool()
def delete_issue_link(issueLinkId: str) -> dict[str, Any]:
    """Delete an issue link.
    
    Args:
        issueLinkId: Issue link ID
    
    Returns:
        Success message or error
    """
    return jira_request("DELETE", f"/issueLink/{issueLinkId}")


# Run the server
if __name__ == "__main__":
    mcp.run()
