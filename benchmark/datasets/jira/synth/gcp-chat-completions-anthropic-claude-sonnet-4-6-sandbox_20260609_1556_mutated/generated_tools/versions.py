"""Project version tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_project_versions(
        project_id_or_key: str,
        start_at: int = 0,
        max_results: int = 50,
        order_by: Optional[str] = None,
        query: Optional[str] = None,
        status: Optional[str] = None,
        expand: Optional[str] = None,
    ) -> dict:
        """Get versions for a project (paginated)."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if order_by:
            params["orderBy"] = order_by
        if query:
            params["query"] = query
        if status:
            params["status"] = status
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/version", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_versions_list(project_id_or_key: str, expand: Optional[str] = None) -> dict:
        """Get all versions for a project (non-paginated)."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/versions", params=params)
            r.raise_for_status()
            return {"versions": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_version(
        project_id: int,
        name: str,
        description: Optional[str] = None,
        release_date: Optional[str] = None,
        start_date: Optional[str] = None,
        released: bool = False,
        archived: bool = False,
    ) -> dict:
        """Create a new project version. release_date format: YYYY-MM-DD."""
        s, base = _client()
        body: dict = {"projectId": project_id, "name": name, "released": released, "archived": archived}
        if description:
            body["description"] = description
        if release_date:
            body["releaseDate"] = release_date
        if start_date:
            body["startDate"] = start_date
        try:
            r = s.post(f"{base}/version", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_version(version_id: str, expand: Optional[str] = None) -> dict:
        """Get a project version by ID."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/version/{version_id}", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_version(
        version_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        release_date: Optional[str] = None,
        start_date: Optional[str] = None,
        released: Optional[bool] = None,
        archived: Optional[bool] = None,
    ) -> dict:
        """Update a project version."""
        s, base = _client()
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
        try:
            r = s.put(f"{base}/version/{version_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_version(
        version_id: str,
        move_fix_issues_to: Optional[str] = None,
        move_affected_issues_to: Optional[str] = None,
    ) -> dict:
        """Delete a project version."""
        s, base = _client()
        params = {}
        if move_fix_issues_to:
            params["moveFixIssuesTo"] = move_fix_issues_to
        if move_affected_issues_to:
            params["moveAffectedIssuesTo"] = move_affected_issues_to
        try:
            r = s.delete(f"{base}/version/{version_id}", params=params)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def merge_versions(version_id: str, move_issues_to: str) -> dict:
        """Merge a version into another version."""
        s, base = _client()
        try:
            r = s.put(f"{base}/version/{version_id}/mergeto/{move_issues_to}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def move_version(
        version_id: str,
        after: Optional[str] = None,
        position: Optional[str] = None,
    ) -> dict:
        """Move a version to a different position in the project. position: 'First', 'Last', 'Earlier', 'Later'."""
        s, base = _client()
        body: dict = {}
        if after:
            body["after"] = after
        if position:
            body["position"] = position
        try:
            r = s.post(f"{base}/version/{version_id}/move", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_version_related_issue_counts(version_id: str) -> dict:
        """Get the count of issues related to a version."""
        s, base = _client()
        try:
            r = s.get(f"{base}/version/{version_id}/relatedIssueCounts")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_version_unresolved_issue_count(version_id: str) -> dict:
        """Get the count of unresolved issues for a version."""
        s, base = _client()
        try:
            r = s.get(f"{base}/version/{version_id}/unresolvedIssueCount")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
