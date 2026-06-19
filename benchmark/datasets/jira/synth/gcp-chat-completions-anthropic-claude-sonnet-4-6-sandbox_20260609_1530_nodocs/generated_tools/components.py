"""
MCP tools for Jira Project Components.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-components")


@mcp.tool()
def get_project_components(
    project_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    query: Optional[str] = None,
    order_by: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all components for a project (paginated).

    Args:
        project_id_or_key: The project ID or key.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        query: Filter components by name (partial match).
        order_by: Field to sort by (e.g. 'name', 'description', 'lead').
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if query:
        params["query"] = query
    if order_by:
        params["orderBy"] = order_by
    return jira_get(f"/project/{project_id_or_key}/component", params=params)


@mcp.tool()
def get_project_components_list(project_id_or_key: str) -> Dict[str, Any]:
    """
    Get all components for a project as a simple list (no pagination).

    Args:
        project_id_or_key: The project ID or key.
    """
    return jira_get(f"/project/{project_id_or_key}/components")


@mcp.tool()
def get_component(component_id: str) -> Dict[str, Any]:
    """
    Get details of a specific component.

    Args:
        component_id: The component ID.
    """
    return jira_get(f"/component/{component_id}")


@mcp.tool()
def create_component(
    project_key: str,
    name: str,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
    assignee_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new component in a project.

    Args:
        project_key: The project key.
        name: Component name.
        description: Component description.
        lead_account_id: Account ID of the component lead.
        assignee_type: Default assignee type: 'COMPONENT_LEAD', 'PROJECT_LEAD',
                       'PROJECT_DEFAULT', 'UNASSIGNED'.
    """
    body: Dict[str, Any] = {"project": project_key, "name": name}
    if description:
        body["description"] = description
    if lead_account_id:
        body["leadAccountId"] = lead_account_id
    if assignee_type:
        body["assigneeType"] = assignee_type
    return jira_post("/component", json=body)


@mcp.tool()
def update_component(
    component_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    lead_account_id: Optional[str] = None,
    assignee_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing component.

    Args:
        component_id: The component ID.
        name: New component name.
        description: New component description.
        lead_account_id: Account ID of the new component lead.
        assignee_type: Default assignee type: 'COMPONENT_LEAD', 'PROJECT_LEAD',
                       'PROJECT_DEFAULT', 'UNASSIGNED'.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if lead_account_id is not None:
        body["leadAccountId"] = lead_account_id
    if assignee_type is not None:
        body["assigneeType"] = assignee_type
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/component/{component_id}", json=body)


@mcp.tool()
def delete_component(
    component_id: str,
    move_issues_to: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Delete a component. Optionally move its issues to another component.

    Args:
        component_id: The component ID.
        move_issues_to: Component ID to move issues to after deletion.
    """
    params: Dict[str, Any] = {}
    if move_issues_to:
        params["moveIssuesTo"] = move_issues_to
    return jira_delete(f"/component/{component_id}", params=params)


@mcp.tool()
def get_component_issue_count(component_id: str) -> Dict[str, Any]:
    """
    Get the count of issues associated with a component.

    Args:
        component_id: The component ID.
    """
    return jira_get(f"/component/{component_id}/relatedIssueCounts")
