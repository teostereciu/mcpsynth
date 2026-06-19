"""
MCP tools for Jira Permissions.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post

mcp = FastMCP("jira-permissions")


@mcp.tool()
def get_my_permissions(
    project_key: Optional[str] = None,
    project_id: Optional[str] = None,
    issue_key: Optional[str] = None,
    issue_id: Optional[str] = None,
    permissions: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get the permissions the current user has in a project or for an issue.

    Args:
        project_key: Project key to check permissions for.
        project_id: Project ID to check permissions for.
        issue_key: Issue key to check permissions for.
        issue_id: Issue ID to check permissions for.
        permissions: Comma-separated list of permissions to check
                     (e.g. 'BROWSE_PROJECTS,CREATE_ISSUES,EDIT_ISSUES').
                     If omitted, returns all permissions.
    """
    params: Dict[str, Any] = {}
    if project_key:
        params["projectKey"] = project_key
    if project_id:
        params["projectId"] = project_id
    if issue_key:
        params["issueKey"] = issue_key
    if issue_id:
        params["issueId"] = issue_id
    if permissions:
        params["permissions"] = permissions
    return jira_get("/mypermissions", params=params)


@mcp.tool()
def get_all_permissions() -> Dict[str, Any]:
    """
    Get all permissions defined in Jira (global and project permissions).
    """
    return jira_get("/permissions")


@mcp.tool()
def get_bulk_permissions(
    project_permissions: Optional[List[Dict[str, Any]]] = None,
    global_permissions: Optional[List[str]] = None,
    account_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Check permissions for multiple projects/issues in a single request.

    Args:
        project_permissions: List of dicts with 'permissions' (list of str) and
                             optionally 'projects' (list of int) and 'issues' (list of int).
                             Example: [{"permissions": ["EDIT_ISSUES"], "projects": [10001]}]
        global_permissions: List of global permission names to check.
        account_id: Account ID to check permissions for (admin only).
    """
    body: Dict[str, Any] = {}
    if project_permissions:
        body["projectPermissions"] = project_permissions
    if global_permissions:
        body["globalPermissions"] = global_permissions
    if account_id:
        body["accountId"] = account_id
    return jira_post("/permissions/check", json=body)


@mcp.tool()
def get_permitted_projects(permissions: List[str]) -> Dict[str, Any]:
    """
    Get all projects where the current user has the specified permissions.

    Args:
        permissions: List of permission names to check
                     (e.g. ['BROWSE_PROJECTS', 'CREATE_ISSUES']).
    """
    return jira_post("/permissions/project", json={"permissions": permissions})


@mcp.tool()
def get_permission_schemes(expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get all permission schemes.

    Args:
        expand: Comma-separated list of entities to expand (e.g. 'permissions,user,group,projectRole').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get("/permissionscheme", params=params)


@mcp.tool()
def get_permission_scheme(scheme_id: int, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a specific permission scheme.

    Args:
        scheme_id: The permission scheme ID.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/permissionscheme/{scheme_id}", params=params)


@mcp.tool()
def get_project_permission_scheme(
    project_id_or_key: str,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get the permission scheme associated with a project.

    Args:
        project_id_or_key: The project ID or key.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/project/{project_id_or_key}/permissionscheme", params=params)
