from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def is_watching_issue_bulk(issue_ids: List[str]) -> Union[Dict[str, Any], list, str]:
    """POST /issue/watching"""
    client = JiraClient()
    return client.request("POST", "/issue/watching", json={"issueIds": issue_ids})


def get_issue_watchers(issue_id_or_key: str) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    return client.request("GET", f"/issue/{issue_id_or_key}/watchers")


def add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    # Body is a JSON string (accountId) or empty to add self.
    body: Any = account_id if account_id is not None else ""
    return client.request("POST", f"/issue/{issue_id_or_key}/watchers", json=body)


def delete_watcher(issue_id_or_key: str, account_id: Optional[str] = None, username: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    return client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params=params or None)
