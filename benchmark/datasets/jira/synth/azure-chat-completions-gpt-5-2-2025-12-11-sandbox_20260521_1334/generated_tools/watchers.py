from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_issue_watchers(issue_id_or_key: str) -> Any:
    """GET /issue/{issueIdOrKey}/watchers"""
    return JiraClient().request("GET", f"/issue/{issue_id_or_key}/watchers")


def add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    """POST /issue/{issueIdOrKey}/watchers

    Body is a JSON string containing the accountId.
    """
    # Jira expects a JSON string, not an object.
    body = account_id or ""
    return JiraClient().request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        data=f"\"{body}\"",
        headers={"Content-Type": "application/json"},
    )


def delete_watcher(issue_id_or_key: str, account_id: str) -> Any:
    """DELETE /issue/{issueIdOrKey}/watchers"""
    params = {"accountId": account_id}
    return JiraClient().request("DELETE", f"/issue/{issue_id_or_key}/watchers", params=params)


def get_is_watching_issue_bulk(issue_ids: List[str]) -> Any:
    """POST /issue/watching"""
    return JiraClient().request("POST", "/issue/watching", json_body={"issueIds": issue_ids})
