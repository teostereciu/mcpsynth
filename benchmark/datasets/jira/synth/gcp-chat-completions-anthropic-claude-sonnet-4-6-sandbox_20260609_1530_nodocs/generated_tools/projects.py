"""
MCP tools for Jira Projects.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-projects")


@mcp.tool()
def get_all_projects(
    expand: Optional[str] = None,
    recent: Optional[int] = None,
    properties: Optional[str] = None,
    keys: Optional[str] = None,
    type_key: Optional[str] = None,
    category_id: Optional[int] = None,
    action: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all projects visible to the authenticated user.

    Args:
        expand: Comma-separated list of entities to expand (e.g. 'description,lead,url,projectKeys').
        recent: Return only the most recently accessed N projects.
        properties: Comma-separated list of project properties to include.
        keys: Comma-separated list of project keys to filter by.
        type_key: Filter by project type: 'software', 'service_desk', 'business'.
        category_id: Filter by project category ID.
        action: Filter by action: 'view', 'browse', 'edit', 'create'.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties:
        params["properties"] = properties
    if keys:
        params["keys"] = keys
    if type_key:
        params["typeKey"] = type_key
    if category_id is not None:
        params["categoryId"] = category_id
    if action:
        params["action"] = action
    return jira_get("/project", params=params)


@mcp.tool()
def search_projects(
    query: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
    order_by: str = "key",
    expand: Optional[str] = None,
    status: Optional[str] = None,
    type_key: Optional[str] = None,
    category_id: Optional[int] = None,
    action: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for projects using pagination and filtering.

    Args:
        query: Text to search for in project name or key.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        order_by: Field to sort by (e.g. 'key', 'name', 'lastIssueUpdatedTime').
        expand: Comma-separated list of entities to expand.
        status: Filter by status: 'live', 'archived', 'deleted'.
        type_key: Filter by project type: 'software', 'service_desk', 'business'.
        category_id: Filter by project category ID.
        action: Filter by action: 'view', 'browse', 'edit', 'create'.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "orderBy": order_by,
    }
    if query:
        params["query"] = query
    if expand:
        params["expand"] = expand
    if status:
        params["status"] = status
    if type_key:
        params["typeKey"] = type_key
    if category_id is not None:
        params["categoryId"] = category_id
    if action:
        params["action"] = action
    return jira_get("/project/search", params=params)


@mcp.tool()
def get_project(
    project_id_or_key: str,
    expand: Optional[str] = None,
    properties: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get details of a specific project.

    Args:
        project_id_or_key: The project ID or key.
        expand: Comma-separated list of entities to expand (e.g. 'description,lead,issueTypes').
        properties: Comma-separated list of project properties to include.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if properties:
        params["properties"] = properties
    return jira_get(f"/project/{project_id_or_key}", params=params)


@mcp.tool()
def create_project(
    key: str,
    name: str,
    project_type_key: str = "software",
    project_template_key: Optional[str] = None,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
    url: Optional[str] = None,
    assignee_type: str = "UNASSIGNED",
    category_id: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Create a new Jira project.

    Args:
        key: Unique project key (e.g. 'MYPROJ'). Must be uppercase letters only.
        name: Project name.
        project_type_key: Project type: 'software', 'service_desk', 'business'.
        project_template_key: Template key (e.g. 'com.pyxis.greenhopper.jira:gh-scrum-template').
        description: Project description.
        lead_account_id: Account ID of the project lead.
        url: Project URL.
        assignee_type: Default assignee: 'PROJECT_LEAD' or 'UNASSIGNED'.
        category_id: Project category ID.
    """
    body: Dict[str, Any] = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type_key,
        "assigneeType": assignee_type,
    }
    if project_template_key:
        body["projectTemplateKey"] = project_template_key
    if description:
        body["description"] = description
    if lead_account_id:
        body["leadAccountId"] = lead_account_id
    if url:
        body["url"] = url
    if category_id is not None:
        body["categoryId"] = category_id
    return jira_post("/project", json=body)


@mcp.tool()
def update_project(
    project_id_or_key: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
    url: Optional[str] = None,
    assignee_type: Optional[str] = None,
    category_id: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Update an existing Jira project.

    Args:
        project_id_or_key: The project ID or key.
        name: New project name.
        description: New project description.
        lead_account_id: Account ID of the new project lead.
        url: New project URL.
        assignee_type: Default assignee: 'PROJECT_LEAD' or 'UNASSIGNED'.
        category_id: New project category ID.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if lead_account_id is not None:
        body["leadAccountId"] = lead_account_id
    if url is not None:
        body["url"] = url
    if assignee_type is not None:
        body["assigneeType"] = assignee_type
    if category_id is not None:
        body["categoryId"] = category_id
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/project/{project_id_or_key}", json=body)


@mcp.tool()
def delete_project(project_id_or_key: str) -> Dict[str, Any]:
    """
    Delete a Jira project.

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_delete(f"/project/{project_id_or_key}")


@mcp.tool()
def archive_project(project_id_or_key: str) -> Dict[str, Any]:
    """
    Archive a Jira project.

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_post(f"/project/{project_id_or_key}/archive")


@mcp.tool()
def restore_project(project_id_or_key: str) -> Dict[str, Any]:
    """
    Restore an archived Jira project.

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_post(f"/project/{project_id_or_key}/restore")


@mcp.tool()
def get_project_statuses(project_id_or_key: str) -> Dict[str, Any]:
    """
    Get all issue statuses available in a project, grouped by issue type.

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_get(f"/project/{project_id_or_key}/statuses")


@mcp.tool()
def get_project_issue_types(project_id_or_key: str) -> Dict[str, Any]:
    """
    Get all issue types available in a project.

    Args:
        project_id_or_key: The project ID or key.
    """
    result = jira_get(f"/project/{project_id_or_key}", params={"expand": "issueTypes"})
    if "error" in result:
        return result
    return {"issueTypes": result.get("issueTypes", [])}


@mcp.tool()
def get_project_roles(project_id_or_key: str) -> Dict[str, Any]:
    """
    Get all roles for a project.

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_get(f"/project/{project_id_or_key}/role")


@mcp.tool()
def get_project_role(project_id_or_key: str, role_id: int) -> Dict[str, Any]:
    """
    Get details of a specific role in a project, including its members.

    Args:
        project_id_or_key: The project ID or key.
        role_id: The role ID.
    """
    return jira_get(f"/project/{project_id_or_key}/role/{role_id}")


@mcp.tool()
def add_actors_to_project_role(
    project_id_or_key: str,
    role_id: int,
    user_account_ids: Optional[List[str]] = None,
    group_names: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Add users or groups to a project role.

    Args:
        project_id_or_key: The project ID or key.
        role_id: The role ID.
        user_account_ids: List of user account IDs to add.
        group_names: List of group names to add.
    """
    body: Dict[str, Any] = {}
    if user_account_ids:
        body["user"] = user_account_ids
    if group_names:
        body["group"] = group_names
    return jira_post(f"/project/{project_id_or_key}/role/{role_id}", json=body)


@mcp.tool()
def delete_actor_from_project_role(
    project_id_or_key: str,
    role_id: int,
    account_id: Optional[str] = None,
    group_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Remove a user or group from a project role.

    Args:
        project_id_or_key: The project ID or key.
        role_id: The role ID.
        account_id: Account ID of the user to remove.
        group_name: Name of the group to remove.
    """
    params: Dict[str, Any] = {}
    if account_id:
        params["user"] = account_id
    if group_name:
        params["group"] = group_name
    return jira_delete(f"/project/{project_id_or_key}/role/{role_id}", params=params)


@mcp.tool()
def get_project_categories() -> Dict[str, Any]:
    """
    Get all project categories.
    """
    return jira_get("/projectCategory")


@mcp.tool()
def get_project_category(category_id: int) -> Dict[str, Any]:
    """
    Get a specific project category.

    Args:
        category_id: The project category ID.
    """
    return jira_get(f"/projectCategory/{category_id}")


@mcp.tool()
def create_project_category(name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new project category.

    Args:
        name: The category name.
        description: Optional description.
    """
    body: Dict[str, Any] = {"name": name}
    if description:
        body["description"] = description
    return jira_post("/projectCategory", json=body)


@mcp.tool()
def get_project_property(project_id_or_key: str, property_key: str) -> Dict[str, Any]:
    """
    Get a project property value.

    Args:
        project_id_or_key: The project ID or key.
        property_key: The property key.
    """
    return jira_get(f"/project/{project_id_or_key}/properties/{property_key}")


@mcp.tool()
def set_project_property(
    project_id_or_key: str, property_key: str, value: Any
) -> Dict[str, Any]:
    """
    Set a project property value.

    Args:
        project_id_or_key: The project ID or key.
        property_key: The property key.
        value: The property value (any JSON-serializable value).
    """
    return jira_put(f"/project/{project_id_or_key}/properties/{property_key}", json=value)


@mcp.tool()
def delete_project_property(project_id_or_key: str, property_key: str) -> Dict[str, Any]:
    """
    Delete a project property.

    Args:
        project_id_or_key: The project ID or key.
        property_key: The property key.
    """
    return jira_delete(f"/project/{project_id_or_key}/properties/{property_key}")
