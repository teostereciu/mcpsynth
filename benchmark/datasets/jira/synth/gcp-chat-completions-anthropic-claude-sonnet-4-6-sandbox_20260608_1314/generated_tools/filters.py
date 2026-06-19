"""Filter management tools: create, get, update, delete, search filters."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def create_filter(name: str, jql: str, description: Optional[str] = None,
                       favourite: bool = False) -> dict:
        """Create a new Jira filter with a JQL query."""
        session, base = _client()
        body: dict = {"name": name, "jql": jql, "favourite": favourite}
        if description:
            body["description"] = description
        r = session.post(f"{base}/filter", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_filter(filter_id: str) -> dict:
        """Get a Jira filter by ID."""
        session, base = _client()
        r = session.get(f"{base}/filter/{filter_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_filter(filter_id: str, name: Optional[str] = None,
                       jql: Optional[str] = None, description: Optional[str] = None,
                       favourite: Optional[bool] = None) -> dict:
        """Update a Jira filter."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if jql:
            body["jql"] = jql
        if description is not None:
            body["description"] = description
        if favourite is not None:
            body["favourite"] = favourite
        r = session.put(f"{base}/filter/{filter_id}", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_filter(filter_id: str) -> dict:
        """Delete a Jira filter by ID."""
        session, base = _client()
        r = session.delete(f"{base}/filter/{filter_id}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_filters(filter_name: Optional[str] = None, account_id: Optional[str] = None,
                        project_id: Optional[int] = None, start_at: int = 0,
                        max_results: int = 50, order_by: Optional[str] = None) -> dict:
        """Search for Jira filters with optional filters."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if filter_name:
            params["filterName"] = filter_name
        if account_id:
            params["accountId"] = account_id
        if project_id:
            params["projectId"] = project_id
        if order_by:
            params["orderBy"] = order_by
        r = session.get(f"{base}/filter/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_favourite_filters() -> dict:
        """Get the current user's favourite Jira filters."""
        session, base = _client()
        r = session.get(f"{base}/filter/favourite")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_my_filters(include_favourites: bool = False) -> dict:
        """Get filters owned by the current user."""
        session, base = _client()
        params = {"includeFavourites": include_favourites}
        r = session.get(f"{base}/filter/my", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_filter_as_favourite(filter_id: str) -> dict:
        """Add a Jira filter to the current user's favourites."""
        session, base = _client()
        r = session.put(f"{base}/filter/{filter_id}/favourite")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def remove_filter_as_favourite(filter_id: str) -> dict:
        """Remove a Jira filter from the current user's favourites."""
        session, base = _client()
        r = session.delete(f"{base}/filter/{filter_id}/favourite")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
