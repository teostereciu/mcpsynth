from typing import Any, Dict, Optional

from .jira_client import JiraClient


def list_issue_types() -> Any:
    """GET /issuetype"""
    client = JiraClient()
    return client.request("GET", "/issuetype")


def list_priorities() -> Any:
    """GET /priority"""
    client = JiraClient()
    return client.request("GET", "/priority")


def list_statuses() -> Any:
    """GET /status"""
    client = JiraClient()
    return client.request("GET", "/status")


def list_fields() -> Any:
    """GET /field"""
    client = JiraClient()
    return client.request("GET", "/field")


def get_create_meta(project_keys: Optional[str] = None, issuetype_names: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/createmeta"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if project_keys:
        params["projectKeys"] = project_keys
    if issuetype_names:
        params["issuetypeNames"] = issuetype_names
    if expand:
        params["expand"] = expand
    return client.request("GET", "/issue/createmeta", params=params)
