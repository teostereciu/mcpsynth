from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def jql_search(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None, expand: Optional[List[str]] = None) -> Dict[str, Any]:
    """POST /search"""
    client = JiraClient()
    payload: Dict[str, Any] = {"jql": jql, "startAt": start_at, "maxResults": max_results}
    if fields is not None:
        payload["fields"] = fields
    if expand is not None:
        payload["expand"] = expand
    return client.request("POST", "/search", json=payload)
