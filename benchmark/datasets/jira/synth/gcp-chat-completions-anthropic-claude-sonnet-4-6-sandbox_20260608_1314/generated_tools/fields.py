"""Issue field tools: get, create, update, delete fields."""
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
    def get_fields() -> dict:
        """Get all Jira issue fields (system and custom) visible to the current user."""
        session, base = _client()
        r = session.get(f"{base}/field")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def search_fields(query: Optional[str] = None, field_type: Optional[str] = None,
                       start_at: int = 0, max_results: int = 50,
                       order_by: Optional[str] = None) -> dict:
        """Search for Jira fields (paginated). field_type: 'custom' or 'system'."""
        session, base = _client()
        params: dict = {"startAt": start_at, "maxResults": max_results}
        if query:
            params["query"] = query
        if field_type:
            params["type"] = [field_type]
        if order_by:
            params["orderBy"] = order_by
        r = session.get(f"{base}/field/search", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def create_custom_field(name: str, field_type: str, description: Optional[str] = None,
                             searcher_key: Optional[str] = None) -> dict:
        """Create a new custom field in Jira.
        field_type: e.g. 'com.atlassian.jira.plugin.system.customfieldtypes:textfield'
        searcher_key: e.g. 'com.atlassian.jira.plugin.system.customfieldtypes:textsearcher'"""
        session, base = _client()
        body: dict = {"name": name, "type": field_type}
        if description:
            body["description"] = description
        if searcher_key:
            body["searcherKey"] = searcher_key
        r = session.post(f"{base}/field", json=body)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def update_custom_field(field_id: str, name: Optional[str] = None,
                             description: Optional[str] = None,
                             searcher_key: Optional[str] = None) -> dict:
        """Update a custom field's name, description, or searcher key."""
        session, base = _client()
        body: dict = {}
        if name:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if searcher_key:
            body["searcherKey"] = searcher_key
        r = session.put(f"{base}/field/{field_id}", json=body)
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_custom_field(field_id: str) -> dict:
        """Delete a custom field by ID (asynchronous operation)."""
        session, base = _client()
        r = session.delete(f"{base}/field/{field_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_jql_autocomplete_data() -> dict:
        """Get JQL autocomplete reference data: field names, operators, and functions."""
        session, base = _client()
        r = session.get(f"{base}/jql/autocompletedata")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_jql_field_suggestions(field_name: str, field_value: Optional[str] = None) -> dict:
        """Get JQL autocomplete suggestions for a specific field name and optional partial value."""
        session, base = _client()
        params: dict = {"fieldName": field_name}
        if field_value:
            params["fieldValue"] = field_value
        r = session.get(f"{base}/jql/autocompletedata/suggestions", params=params)
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def parse_jql_queries(queries: List[str], validation: str = "strict") -> dict:
        """Parse and validate one or more JQL queries.
        validation: 'strict', 'warn', or 'none'"""
        session, base = _client()
        r = session.post(f"{base}/jql/parse", params={"validation": validation},
                         json={"queries": queries})
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
