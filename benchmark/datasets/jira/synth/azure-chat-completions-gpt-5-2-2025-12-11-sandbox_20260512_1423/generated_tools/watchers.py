from typing import Any, Dict, List, Optional

from ._client import get_client


def get_issue_watchers(issue_id_or_key: str) -> Any:
    """GET /issue/{issueIdOrKey}/watchers"""
    return get_client().request("GET", f"/issue/{issue_id_or_key}/watchers")


def add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    """POST /issue/{issueIdOrKey}/watchers"""
    # Body is a JSON string (accountId). If omitted, adds current user.
    body = account_id if account_id is not None else ""
    return get_client().request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        json_body=body if account_id is not None else None,
        headers={"Content-Type": "application/json"},
    )


def remove_watcher(issue_id_or_key: str, account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    """DELETE /issue/{issueIdOrKey}/watchers"""
    params: Dict[str, Any] = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    return get_client().request("DELETE", f"/issue/{issue_id_or_key}/watchers", params=params or None)


def bulk_is_watching(issue_ids: List[str]) -> Any:
    """POST /issue/watching"""
    return get_client().request("POST", "/issue/watching", json_body={"issueIds": issue_ids})
