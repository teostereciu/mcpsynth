"""
MCP tools for Jira Project Versions (Releases).
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-versions")


@mcp.tool()
def get_project_versions(
    project_id_or_key: str,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get all versions for a project.

    Args:
        project_id_or_key: The project ID or key.
        expand: Comma-separated list of entities to expand (e.g. 'issuesstatus').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/project/{project_id_or_key}/versions", params=params)


@mcp.tool()
def get_project_versions_paginated(
    project_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
    order_by: Optional[str] = None,
    query: Optional[str] = None,
    status: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get versions for a project with pagination and filtering.

    Args:
        project_id_or_key: The project ID or key.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        order_by: Field to sort by (e.g. 'sequence', 'name', 'startDate', 'releaseDate').
        query: Filter versions by name (partial match).
        status: Filter by status: 'released', 'unreleased', 'archived'.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if query:
        params["query"] = query
    if status:
        params["status"] = status
    if expand:
        params["expand"] = expand
    return jira_get(f"/project/{project_id_or_key}/version", params=params)


@mcp.tool()
def get_version(version_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Get details of a specific version.

    Args:
        version_id: The version ID.
        expand: Comma-separated list of entities to expand (e.g. 'issuesstatus').
    """
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return jira_get(f"/version/{version_id}", params=params)


@mcp.tool()
def create_version(
    project_id: str,
    name: str,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    released: bool = False,
    archived: bool = False,
) -> Dict[str, Any]:
    """
    Create a new version in a project.

    Args:
        project_id: The project ID (numeric, not key).
        name: Version name (e.g. '1.0.0', 'Sprint 5').
        description: Version description.
        start_date: Start date in YYYY-MM-DD format.
        release_date: Release date in YYYY-MM-DD format.
        released: Whether the version is released.
        archived: Whether the version is archived.
    """
    body: Dict[str, Any] = {
        "projectId": int(project_id),
        "name": name,
        "released": released,
        "archived": archived,
    }
    if description:
        body["description"] = description
    if start_date:
        body["startDate"] = start_date
    if release_date:
        body["releaseDate"] = release_date
    return jira_post("/version", json=body)


@mcp.tool()
def update_version(
    version_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    start_date: Optional[str] = None,
    release_date: Optional[str] = None,
    released: Optional[bool] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update an existing version.

    Args:
        version_id: The version ID.
        name: New version name.
        description: New version description.
        start_date: New start date in YYYY-MM-DD format.
        release_date: New release date in YYYY-MM-DD format.
        released: Whether the version is released.
        archived: Whether the version is archived.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if start_date is not None:
        body["startDate"] = start_date
    if release_date is not None:
        body["releaseDate"] = release_date
    if released is not None:
        body["released"] = released
    if archived is not None:
        body["archived"] = archived
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/version/{version_id}", json=body)


@mcp.tool()
def delete_version(
    version_id: str,
    move_fix_issues_to: Optional[str] = None,
    move_affected_issues_to: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Delete a version. Optionally move associated issues to another version.

    Args:
        version_id: The version ID.
        move_fix_issues_to: Version ID to move fix-version issues to.
        move_affected_issues_to: Version ID to move affected-version issues to.
    """
    params: Dict[str, Any] = {}
    if move_fix_issues_to:
        params["moveFixIssuesTo"] = move_fix_issues_to
    if move_affected_issues_to:
        params["moveAffectedIssuesTo"] = move_affected_issues_to
    return jira_delete(f"/version/{version_id}", params=params)


@mcp.tool()
def merge_versions(version_id: str, move_issues_to_version_id: str) -> Dict[str, Any]:
    """
    Merge a version into another version (moves all issues and deletes the source version).

    Args:
        version_id: The source version ID to merge from.
        move_issues_to_version_id: The target version ID to merge into.
    """
    return jira_put(f"/version/{version_id}/mergeto/{move_issues_to_version_id}")


@mcp.tool()
def get_version_related_issues(version_id: str) -> Dict[str, Any]:
    """
    Get counts of issues related to a version (fixed in, affected by).

    Args:
        version_id: The version ID.
    """
    return jira_get(f"/version/{version_id}/relatedIssueCounts")


@mcp.tool()
def get_version_unresolved_issue_count(version_id: str) -> Dict[str, Any]:
    """
    Get the count of unresolved issues for a version.

    Args:
        version_id: The version ID.
    """
    return jira_get(f"/version/{version_id}/unresolvedIssueCount")


@mcp.tool()
def move_version(
    version_id: str,
    after: Optional[str] = None,
    position: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Move a version to a different position in the project's version list.

    Args:
        version_id: The version ID.
        after: The URL of the version to place this version after.
        position: Position to move to: 'Earlier', 'Later', 'First', 'Last'.
    """
    body: Dict[str, Any] = {}
    if after:
        body["after"] = after
    if position:
        body["position"] = position
    return jira_post(f"/version/{version_id}/move", json=body)
