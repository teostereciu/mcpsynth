"""
MCP tools for Jira Server Info, Application Roles, and Audit Log.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post

mcp = FastMCP("jira-server-info")


@mcp.tool()
def get_server_info() -> Dict[str, Any]:
    """
    Get information about the Jira instance (version, build number, base URL, etc.).
    """
    return jira_get("/serverInfo")


@mcp.tool()
def get_application_roles() -> Dict[str, Any]:
    """
    Get all application roles (e.g. jira-software, jira-servicedesk).
    """
    return jira_get("/applicationrole")


@mcp.tool()
def get_application_role(role_key: str) -> Dict[str, Any]:
    """
    Get details of a specific application role.

    Args:
        role_key: The application role key (e.g. 'jira-software').
    """
    return jira_get(f"/applicationrole/{role_key}")


@mcp.tool()
def get_audit_records(
    offset: int = 0,
    limit: int = 1000,
    filter_: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get audit log records (requires admin permissions).

    Args:
        offset: Index of the first record to return.
        limit: Maximum number of records to return.
        filter_: Text to filter audit records by.
        from_date: Start date in ISO 8601 format (e.g. '2024-01-01').
        to_date: End date in ISO 8601 format.
    """
    params: Dict[str, Any] = {"offset": offset, "limit": limit}
    if filter_:
        params["filter"] = filter_
    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date
    return jira_get("/auditing/record", params=params)


@mcp.tool()
def get_configuration() -> Dict[str, Any]:
    """
    Get the global Jira configuration (voting, watching, issue linking, etc.).
    """
    return jira_get("/configuration")


@mcp.tool()
def get_global_settings() -> Dict[str, Any]:
    """
    Get global Jira settings including time tracking configuration.
    """
    return jira_get("/settings/columns")


@mcp.tool()
def get_time_tracking_configuration() -> Dict[str, Any]:
    """
    Get the time tracking configuration (working hours per day/week, format).
    """
    return jira_get("/configuration/timetracking")


@mcp.tool()
def get_time_tracking_providers() -> Dict[str, Any]:
    """
    Get all available time tracking providers.
    """
    return jira_get("/configuration/timetracking/list")


@mcp.tool()
def get_avatars(entity_type: str, entity_id: str) -> Dict[str, Any]:
    """
    Get avatars for a project or user.

    Args:
        entity_type: The entity type: 'project' or 'user'.
        entity_id: The entity ID (project ID or user account ID).
    """
    return jira_get(f"/universal_avatar/type/{entity_type}/owner/{entity_id}")


@mcp.tool()
def get_system_avatars(avatar_type: str) -> Dict[str, Any]:
    """
    Get all system avatars for a given type.

    Args:
        avatar_type: The avatar type: 'issuetype', 'project', or 'user'.
    """
    return jira_get(f"/avatar/{avatar_type}/system")


@mcp.tool()
def get_issue_navigator_default_columns() -> Dict[str, Any]:
    """
    Get the default columns for the issue navigator.
    """
    return jira_get("/settings/columns")


@mcp.tool()
def get_my_preferences() -> Dict[str, Any]:
    """
    Get the current user's preferences.
    """
    return jira_get("/mypreferences")


@mcp.tool()
def get_locale() -> Dict[str, Any]:
    """
    Get the locale of the current user.
    """
    return jira_get("/mypreferences/locale")


@mcp.tool()
def get_notification_schemes(
    start_at: int = 0,
    max_results: int = 50,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all notification schemes.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        expand: Expand options (e.g. 'all', 'field', 'group', 'notificationSchemeEvents',
                'projectRole', 'user').
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if expand:
        params["expand"] = expand
    return jira_get("/notificationscheme", params=params)


@mcp.tool()
def get_notification_scheme(scheme_id: int, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a specific notification scheme.

    Args:
        scheme_id: The notification scheme ID.
        expand: Expand options.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/notificationscheme/{scheme_id}", params=params)


@mcp.tool()
def get_project_notification_scheme(
    project_id_or_key: str,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get the notification scheme for a project.

    Args:
        project_id_or_key: The project ID or key.
        expand: Expand options.
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/project/{project_id_or_key}/notificationscheme", params=params)
