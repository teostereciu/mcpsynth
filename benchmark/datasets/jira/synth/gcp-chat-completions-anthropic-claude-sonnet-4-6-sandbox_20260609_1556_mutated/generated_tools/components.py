"""Project component tools."""
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
    def get_project_components(
        project_id_or_key: str,
        start_at: int = 0,
        max_results: int = 50,
        query: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> dict:
        """Get components for a project (paginated)."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if order_by:
            params["orderBy"] = order_by
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/component", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_project_components_list(project_id_or_key: str) -> dict:
        """Get all components for a project (non-paginated list)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/project/{project_id_or_key}/components")
            r.raise_for_status()
            return {"components": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def create_component(
        project_key: str,
        name: str,
        description: Optional[str] = None,
        lead_account_id: Optional[str] = None,
        assignee_type: Optional[str] = None,
    ) -> dict:
        """Create a new project component."""
        s, base = _client()
        body: dict = {"project": project_key, "name": name}
        if description:
            body["description"] = description
        if lead_account_id:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        try:
            r = s.post(f"{base}/component", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_component(component_id: str) -> dict:
        """Get a project component by ID."""
        s, base = _client()
        try:
            r = s.get(f"{base}/component/{component_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_component(
        component_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        lead_account_id: Optional[str] = None,
        assignee_type: Optional[str] = None,
    ) -> dict:
        """Update a project component."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if lead_account_id is not None:
            body["leadAccountId"] = lead_account_id
        if assignee_type:
            body["assigneeType"] = assignee_type
        try:
            r = s.put(f"{base}/component/{component_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_component(component_id: str, move_issues_to: Optional[str] = None) -> dict:
        """Delete a project component. Optionally move issues to another component."""
        s, base = _client()
        params = {}
        if move_issues_to:
            params["moveIssuesTo"] = move_issues_to
        try:
            r = s.delete(f"{base}/component/{component_id}", params=params)
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_component_issue_counts(component_id: str) -> dict:
        """Get the count of issues for a component."""
        s, base = _client()
        try:
            r = s.get(f"{base}/component/{component_id}/relatedIssueCounts")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def find_components_for_projects(
        project_ids_or_keys: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
        query: Optional[str] = None,
    ) -> dict:
        """Find components across multiple projects."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if project_ids_or_keys:
            params["projectIdsOrKeys"] = project_ids_or_keys
        if query:
            params["query"] = query
        try:
            r = s.get(f"{base}/component", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
