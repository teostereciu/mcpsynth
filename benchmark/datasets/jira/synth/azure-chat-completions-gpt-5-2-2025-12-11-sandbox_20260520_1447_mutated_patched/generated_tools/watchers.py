from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_issue_watchers(issueIdOrKey: str):
    """GET /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    return client.request("GET", f"/issue/{issueIdOrKey}/watchers")


def add_watcher(issueIdOrKey: str, accountId: Optional[str] = None):
    """POST /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    # API expects a JSON string body (accountId). If None, add calling user.
    return client.request("POST", f"/issue/{issueIdOrKey}/watchers", json=accountId)


def delete_watcher(issueIdOrKey: str, user_id: Optional[str] = None, username: Optional[str] = None):
    """DELETE /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if user_id is not None:
        params["accountId"] = user_id
    if username is not None:
        params["username"] = username
    return client.request("DELETE", f"/issue/{issueIdOrKey}/watchers", params=params or None)


def bulk_is_watching(issueIds: List[str]):
    """POST /issue/watching"""
    client = JiraClient()
    return client.request("POST", "/issue/watching", json={"issueIds": issueIds})
