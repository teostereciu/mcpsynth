"""Filter management tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, List
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def create_filter(
        name: str,
        jql: str,
        description: Optional[str] = None,
        favourite: bool = False,
    ) -> dict:
        """Create a new saved filter."""
        s, base = _client()
        body: dict = {"name": name, "jql": jql, "favourite": favourite}
        if description:
            body["description"] = description
        try:
            r = s.post(f"{base}/filter", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_filter(filter_id: str, expand: Optional[str] = None) -> dict:
        """Get a filter by ID."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/filter/{filter_id}", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def update_filter(
        filter_id: str,
        name: Optional[str] = None,
        jql: Optional[str] = None,
        description: Optional[str] = None,
        favourite: Optional[bool] = None,
    ) -> dict:
        """Update an existing filter."""
        s, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if jql:
            body["jql"] = jql
        if description is not None:
            body["description"] = description
        if favourite is not None:
            body["favourite"] = favourite
        try:
            r = s.put(f"{base}/filter/{filter_id}", json=body)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_filter(filter_id: str) -> dict:
        """Delete a filter."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/filter/{filter_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_favourite_filters(expand: Optional[str] = None) -> dict:
        """Get the current user's favourite filters."""
        s, base = _client()
        params = {}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/filter/favourite", params=params)
            r.raise_for_status()
            return {"filters": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_my_filters(include_favourites: bool = False, expand: Optional[str] = None) -> dict:
        """Get filters owned by the current user."""
        s, base = _client()
        params: dict = {"includeFavourites": include_favourites}
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/filter/my", params=params)
            r.raise_for_status()
            return {"filters": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def search_filters(
        filter_name: Optional[str] = None,
        account_id: Optional[str] = None,
        project_id: Optional[int] = None,
        order_by: Optional[str] = None,
        start_at: int = 0,
        max_results: int = 50,
        expand: Optional[str] = None,
    ) -> dict:
        """Search for filters with various criteria."""
        s, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if filter_name:
            params["filterName"] = filter_name
        if account_id:
            params["accountId"] = account_id
        if project_id is not None:
            params["projectId"] = project_id
        if order_by:
            params["orderBy"] = order_by
        if expand:
            params["expand"] = expand
        try:
            r = s.get(f"{base}/filter/search", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_filter_as_favourite(filter_id: str) -> dict:
        """Mark a filter as a favourite."""
        s, base = _client()
        try:
            r = s.put(f"{base}/filter/{filter_id}/favourite")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def remove_filter_as_favourite(filter_id: str) -> dict:
        """Remove a filter from favourites."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/filter/{filter_id}/favourite")
            r.raise_for_status()
            return r.json() if r.content else {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_filter_columns(filter_id: str) -> dict:
        """Get the column configuration for a filter."""
        s, base = _client()
        try:
            r = s.get(f"{base}/filter/{filter_id}/columns")
            r.raise_for_status()
            return {"columns": r.json()}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def set_filter_columns(filter_id: str, columns: List[str]) -> dict:
        """Set the column configuration for a filter."""
        s, base = _client()
        try:
            r = s.put(f"{base}/filter/{filter_id}/columns", json=columns)
            if r.status_code == 200:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
