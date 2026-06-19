from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_issue_watchers(issueIdOrKey: str) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    return client.request("GET", f"/issue/{issueIdOrKey}/watchers")


def add_watcher(issueIdOrKey: str, *, accountId: Optional[str] = None) -> Any:
    """POST /rest/api/3/issue/{issueIdOrKey}/watchers

    Body is a JSON string of accountId, or empty to add self.
    """
    client = JiraClient()
    body = accountId if accountId is not None else ""
    return client.request(
        "POST",
        f"/issue/{issueIdOrKey}/watchers",
        headers={"Content-Type": "application/json"},
        data=f'"{body}"' if body != "" else '""',
    )


def remove_watcher(issueIdOrKey: str, *, accountId: str) -> Any:
    """DEL /rest/api/3/issue/{issueIdOrKey}/watchers?user_id={accountId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issueIdOrKey}/watchers", params={"user_id": accountId})


def bulk_is_watching(issueIds: List[str]) -> Any:
    """POST /rest/api/3/issue/watching"""
    client = JiraClient()
    return client.request("POST", "/issue/watching", json_body={"issueIds": issueIds})
