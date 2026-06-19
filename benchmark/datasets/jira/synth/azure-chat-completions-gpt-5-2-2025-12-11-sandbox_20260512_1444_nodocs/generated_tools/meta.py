from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_server_info(client: JiraClient) -> Any:
    return client.request("GET", "/serverInfo")


def get_create_issue_metadata(client: JiraClient, project_ids: Optional[str] = None, project_keys: Optional[str] = None, issuetype_ids: Optional[str] = None, issuetype_names: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if project_ids:
        params["projectIds"] = project_ids
    if project_keys:
        params["projectKeys"] = project_keys
    if issuetype_ids:
        params["issuetypeIds"] = issuetype_ids
    if issuetype_names:
        params["issuetypeNames"] = issuetype_names
    if expand:
        params["expand"] = expand
    return client.request("GET", "/issue/createmeta", params=params)


def get_fields(client: JiraClient) -> Any:
    return client.request("GET", "/field")


def get_issue_types(client: JiraClient) -> Any:
    return client.request("GET", "/issuetype")


def get_priorities(client: JiraClient) -> Any:
    return client.request("GET", "/priority")


def get_statuses(client: JiraClient) -> Any:
    return client.request("GET", "/status")
