from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_myself() -> Any:
    """GET /myself"""
    client = JiraClient()
    return client.request("GET", "/myself")


def get_user(account_id: str, expand: Optional[str] = None) -> Any:
    """GET /user"""
    client = JiraClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/user", params=params)


def find_users(query: str, max_results: int = 50) -> Any:
    """GET /user/search"""
    client = JiraClient()
    return client.request("GET", "/user/search", params={"query": query, "maxResults": max_results})


def find_assignable_users(project: Optional[str] = None, issue_key: Optional[str] = None, query: Optional[str] = None, max_results: int = 50) -> Any:
    """GET /user/assignable/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"maxResults": max_results}
    if project:
        params["project"] = project
    if issue_key:
        params["issueKey"] = issue_key
    if query:
        params["query"] = query
    return client.request("GET", "/user/assignable/search", params=params)
