"""JQL tools: parse, validate, autocomplete, and convert JQL queries."""
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
    def get_jql_autocomplete_data() -> dict:
        """Get JQL field reference data for building queries (field names, operators, functions)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/jql/autocompletedata")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_jql_field_suggestions(
        field_name: str,
        field_value: Optional[str] = None,
        predicate_name: Optional[str] = None,
        predicate_value: Optional[str] = None,
    ) -> dict:
        """Get JQL autocomplete suggestions for a specific field."""
        s, base = _client()
        params: dict = {"fieldName": field_name}
        if field_value:
            params["fieldValue"] = field_value
        if predicate_name:
            params["predicateName"] = predicate_name
        if predicate_value:
            params["predicateValue"] = predicate_value
        try:
            r = s.get(f"{base}/jql/autocompletedata/suggestions", params=params)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def parse_jql_queries(queries: List[str], validation: str = "strict") -> dict:
        """Parse and validate JQL queries. validation: 'strict', 'warn', or 'none'."""
        s, base = _client()
        try:
            r = s.post(f"{base}/jql/parse", json={"queries": queries}, params={"validation": validation})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def convert_jql_user_identifiers(query_strings: List[str]) -> dict:
        """Convert JQL queries with usernames/user keys to use account IDs (GDPR compliance)."""
        s, base = _client()
        try:
            r = s.post(f"{base}/jql/pdcleaner", json={"queryStrings": query_strings})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_all_labels(start_at: int = 0, max_results: int = 1000) -> dict:
        """Get all available labels for the global label field."""
        s, base = _client()
        try:
            r = s.get(f"{base}/label", params={"startAt": start_at, "maxResults": max_results})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def check_issues_against_jql(issue_ids: List[int], jqls: List[str]) -> dict:
        """Check whether issues match one or more JQL queries."""
        s, base = _client()
        try:
            r = s.post(f"{base}/jql/match", json={"issueIds": issue_ids, "jqls": jqls})
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
