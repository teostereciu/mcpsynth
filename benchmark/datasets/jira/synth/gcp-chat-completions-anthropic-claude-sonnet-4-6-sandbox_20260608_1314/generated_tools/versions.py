"""Project version tools: get, create, update, delete versions."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_project_versions(project_id_or_key: str, start_at: int = 0,
                              max_results: int = 50, query: Optional[str] = None,
                              status: Optional[str] = None, order_by: Optional[str] = None) -> dict:
        """Get a paginated list of versions for a Jira project.
        status: 'released', 'unreleased', 'archived'"""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if status:
            params["status"] = status
        if order_by:
            params["orderBy"] = order_by
        r = session.get(f"{base}/project/{project_id_or_key}/version", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_project_versions_all(project_id_or_key: str) -> dict:
        """Get all versions for a Jira project (non-paginated)."""
        session, base = _client()
        r = session.get(f"{base}/project/{project_id_or_key}/versions")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_version(version_id: str) -> dict:
        """Get a specific Jira project version by ID."""
        session, base = _client()
        r = session.get(f"{base}/version/{version_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_version(project_id: int, name: str, description: Optional[str] = None,
                        release_date: Optional[str] = None, start_date: Optional[str] = None,
                        released: bool = False, archived: bool = False) -> dict:
        """Create a new version in a Jira project.
        release_date: ISO date string e.g. '2024-12-31'
        start_date: ISO date string e.g. '2024-01-01'"""
        session, base = _client()
        body: dict = {"projectId": project_id, "name": name, "released": released, "archived": archived}
        if description:
            body["description"] = description
        if release_date:
            body["releaseDate"] = release_date
        if start_date:
            body["startDate"] = start_date
        r = session.post(f"{base}/version", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_version(version_id: str, name: Optional[str] = None,
                        description: Optional[str] = None,
                        release_date: Optional[str] = None,
                        start_date: Optional[str] = None,
                        released: Optional[bool] = None,
                        archived: Optional[bool] = None) -> dict:
        """Update a Jira project version."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if release_date is not None:
            body["releaseDate"] = release_date
        if start_date is not None:
            body["startDate"] = start_date
        if released is not None:
            body["released"] = released
        if archived is not None:
            body["archived"] = archived
        r = session.put(f"{base}/version/{version_id}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None,
                        move_affected_issues_to: Optional[str] = None) -> dict:
        """Delete a Jira project version. Optionally move issues to another version."""
        session, base = _client()
        params: dict = {}
        if move_fix_issues_to:
            params["moveFixIssuesTo"] = move_fix_issues_to
        if move_affected_issues_to:
            params["moveAffectedIssuesTo"] = move_affected_issues_to
        r = session.delete(f"{base}/version/{version_id}", params=params)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def merge_versions(version_id: str, move_issues_to: str) -> dict:
        """Merge a Jira version into another version (deletes version_id, moves issues to move_issues_to)."""
        session, base = _client()
        r = session.put(f"{base}/version/{version_id}/mergeto/{move_issues_to}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_version_related_issue_counts(version_id: str) -> dict:
        """Get the count of issues related to a Jira version (fixed in, affected by)."""
        session, base = _client()
        r = session.get(f"{base}/version/{version_id}/relatedIssueCounts")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
