from typing import Any, Dict, List, Optional

from jira_client import JiraClient


def jql_search(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    """GET /search"""
    client = JiraClient()
    params: Dict[str, Any] = {"jql": jql, "startAt": start_at, "maxResults": max_results}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    return client.request("GET", "/search", params=params)
