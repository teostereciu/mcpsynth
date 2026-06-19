from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_myself(client: JiraClient) -> Any:
    return client.request("GET", "/myself")


def get_user(client: JiraClient, account_id: str, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/user", params=params)


def find_users(client: JiraClient, query: str, max_results: int = 50, start_at: int = 0) -> Any:
    params = {"query": query, "maxResults": max_results, "startAt": start_at}
    return client.request("GET", "/user/search", params=params)


def get_users_assignable_to_project(client: JiraClient, project_key_or_id: str, query: Optional[str] = None, max_results: int = 50, start_at: int = 0) -> Any:
    params: Dict[str, Any] = {"project": project_key_or_id, "maxResults": max_results, "startAt": start_at}
    if query:
        params["query"] = query
    return client.request("GET", "/user/assignable/search", params=params)
