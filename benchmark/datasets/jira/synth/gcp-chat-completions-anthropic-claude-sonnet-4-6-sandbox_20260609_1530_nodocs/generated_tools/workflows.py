"""
MCP tools for Jira Workflows and Workflow Schemes.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-workflows")


@mcp.tool()
def get_workflows(
    workflow_name: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all workflows.

    Args:
        workflow_name: Filter by workflow name.
        expand: Expand options (e.g. 'transitions,statuses').
    """
    params: Dict[str, Any] = {}
    if workflow_name:
        params["workflowName"] = workflow_name
    if expand:
        params["expand"] = expand
    return jira_get("/workflow", params=params)


@mcp.tool()
def search_workflows(
    start_at: int = 0,
    max_results: int = 50,
    workflow_name: Optional[str] = None,
    expand: Optional[str] = None,
    query_string: Optional[str] = None,
    order_by: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Search for workflows with pagination.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        workflow_name: Filter by workflow name (exact match).
        expand: Expand options.
        query_string: Filter by name (partial match).
        order_by: Field to sort by.
        is_active: Filter by active status.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if workflow_name:
        params["workflowName"] = workflow_name
    if expand:
        params["expand"] = expand
    if query_string:
        params["queryString"] = query_string
    if order_by:
        params["orderBy"] = order_by
    if is_active is not None:
        params["isActive"] = is_active
    return jira_get("/workflow/search", params=params)


@mcp.tool()
def get_workflow_transitions(workflow_name: str) -> Dict[str, Any]:
    """
    Get all transitions for a workflow.

    Args:
        workflow_name: The workflow name.
    """
    return jira_get("/workflow/transitions", params={"workflowName": workflow_name})


@mcp.tool()
def get_workflow_schemes(
    start_at: int = 0,
    max_results: int = 50,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all workflow schemes.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        expand: Expand options.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if expand:
        params["expand"] = expand
    return jira_get("/workflowscheme", params=params)


@mcp.tool()
def get_workflow_scheme(scheme_id: int, return_draft_if_exists: bool = False) -> Dict[str, Any]:
    """
    Get a specific workflow scheme.

    Args:
        scheme_id: The workflow scheme ID.
        return_draft_if_exists: Return the draft scheme if one exists.
    """
    params: Dict[str, Any] = {"returnDraftIfExists": return_draft_if_exists}
    return jira_get(f"/workflowscheme/{scheme_id}", params=params)


@mcp.tool()
def create_workflow_scheme(
    name: str,
    description: Optional[str] = None,
    default_workflow: Optional[str] = None,
    issue_type_mappings: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a new workflow scheme.

    Args:
        name: Workflow scheme name.
        description: Workflow scheme description.
        default_workflow: Name of the default workflow.
        issue_type_mappings: Dict mapping issue type IDs to workflow names.
                             Example: {"10001": "Software Simplified Workflow"}
    """
    body: Dict[str, Any] = {"name": name}
    if description:
        body["description"] = description
    if default_workflow:
        body["defaultWorkflow"] = default_workflow
    if issue_type_mappings:
        body["issueTypeMappings"] = issue_type_mappings
    return jira_post("/workflowscheme", json=body)


@mcp.tool()
def update_workflow_scheme(
    scheme_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    default_workflow: Optional[str] = None,
    issue_type_mappings: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update a workflow scheme.

    Args:
        scheme_id: The workflow scheme ID.
        name: New name.
        description: New description.
        default_workflow: New default workflow name.
        issue_type_mappings: New issue type to workflow mappings.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if default_workflow is not None:
        body["defaultWorkflow"] = default_workflow
    if issue_type_mappings is not None:
        body["issueTypeMappings"] = issue_type_mappings
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/workflowscheme/{scheme_id}", json=body)


@mcp.tool()
def delete_workflow_scheme(scheme_id: int) -> Dict[str, Any]:
    """
    Delete a workflow scheme.

    Args:
        scheme_id: The workflow scheme ID.
    """
    return jira_delete(f"/workflowscheme/{scheme_id}")


@mcp.tool()
def get_project_workflow_scheme(
    project_id_or_key: str,
    return_draft_if_exists: bool = False,
) -> Dict[str, Any]:
    """
    Get the workflow scheme associated with a project.

    Args:
        project_id_or_key: The project ID or key.
        return_draft_if_exists: Return the draft scheme if one exists.
    """
    return jira_get(
        f"/project/{project_id_or_key}/workflowscheme",
        params={"returnDraftIfExists": return_draft_if_exists},
    )


@mcp.tool()
def get_all_workflow_statuses() -> Dict[str, Any]:
    """
    Get all statuses used across all workflows.
    """
    return jira_get("/workflow/status")
