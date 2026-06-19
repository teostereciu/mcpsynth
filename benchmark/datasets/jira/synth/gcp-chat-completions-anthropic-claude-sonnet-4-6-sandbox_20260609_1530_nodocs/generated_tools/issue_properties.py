"""
MCP tools for Jira Issue Properties and Issue Security.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-issue-properties")


# ── Issue Properties ──────────────────────────────────────────────────────────

@mcp.tool()
def get_issue_properties(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get all property keys for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/properties")


@mcp.tool()
def get_issue_property(issue_id_or_key: str, property_key: str) -> Dict[str, Any]:
    """
    Get a specific property value for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        property_key: The property key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/properties/{property_key}")


@mcp.tool()
def set_issue_property(
    issue_id_or_key: str, property_key: str, value: Any
) -> Dict[str, Any]:
    """
    Set a property on an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        property_key: The property key.
        value: The property value (any JSON-serializable value).
    """
    return jira_put(f"/issue/{issue_id_or_key}/properties/{property_key}", json=value)


@mcp.tool()
def delete_issue_property(issue_id_or_key: str, property_key: str) -> Dict[str, Any]:
    """
    Delete a property from an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        property_key: The property key.
    """
    return jira_delete(f"/issue/{issue_id_or_key}/properties/{property_key}")


@mcp.tool()
def bulk_set_issue_properties(
    issues: List[str],
    properties: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Set properties on multiple issues in a single request.

    Args:
        issues: List of issue IDs or keys.
        properties: List of property dicts with 'key' and 'value' fields.
                    Example: [{"key": "myProp", "value": {"status": "active"}}]
    """
    return jira_post(
        "/issue/properties",
        json={"issues": issues, "properties": properties},
    )


@mcp.tool()
def bulk_delete_issue_properties(
    issues: List[str],
    property_key: str,
) -> Dict[str, Any]:
    """
    Delete a property from multiple issues.

    Args:
        issues: List of issue IDs or keys.
        property_key: The property key to delete.
    """
    return jira_delete(
        "/issue/properties",
        params={"propertyKey": property_key},
    )


# ── Issue Security ────────────────────────────────────────────────────────────

@mcp.tool()
def get_issue_security_schemes() -> Dict[str, Any]:
    """
    Get all issue security schemes.
    """
    return jira_get("/issuesecurityschemes")


@mcp.tool()
def get_issue_security_scheme(scheme_id: int) -> Dict[str, Any]:
    """
    Get a specific issue security scheme.

    Args:
        scheme_id: The security scheme ID.
    """
    return jira_get(f"/issuesecurityschemes/{scheme_id}")


@mcp.tool()
def get_issue_security_level(security_level_id: str) -> Dict[str, Any]:
    """
    Get details of a specific issue security level.

    Args:
        security_level_id: The security level ID.
    """
    return jira_get(f"/securitylevel/{security_level_id}")


@mcp.tool()
def get_project_issue_security_scheme(project_key_or_id: str) -> Dict[str, Any]:
    """
    Get the issue security scheme for a project.

    Args:
        project_key_or_id: The project key or ID.
    """
    return jira_get(f"/project/{project_key_or_id}/issuesecuritylevelscheme")


# ── Labels ────────────────────────────────────────────────────────────────────

@mcp.tool()
def get_all_labels(start_at: int = 0, max_results: int = 1000) -> Dict[str, Any]:
    """
    Get all labels used in Jira.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    return jira_get("/label", params={"startAt": start_at, "maxResults": max_results})


# ── Resolutions ───────────────────────────────────────────────────────────────

@mcp.tool()
def get_resolutions() -> Dict[str, Any]:
    """
    Get all issue resolutions (e.g. Fixed, Won't Fix, Duplicate, Cannot Reproduce).
    """
    return jira_get("/resolution")


@mcp.tool()
def get_resolution(resolution_id: str) -> Dict[str, Any]:
    """
    Get details of a specific resolution.

    Args:
        resolution_id: The resolution ID.
    """
    return jira_get(f"/resolution/{resolution_id}")


@mcp.tool()
def search_resolutions(
    start_at: int = 0,
    max_results: int = 50,
    id_: Optional[str] = None,
    only_default: bool = False,
) -> Dict[str, Any]:
    """
    Search for resolutions.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        id_: Comma-separated resolution IDs to filter by.
        only_default: Return only the default resolution.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "onlyDefault": only_default,
    }
    if id_:
        params["id"] = id_
    return jira_get("/resolution/search", params=params)
