from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def issue_is_watching_bulk(issue_ids: List[str]) -> Dict[str, Any]:
    """POST /issue/watching - Get watched status for issues."""
    client = JiraClient()
    return client.request("POST", "/issue/watching", json_body={"issueIds": issue_ids})  # type: ignore[return-value]


def issue_watchers_get(issue_id_or_key: str) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/watchers - Get watchers."""
    client = JiraClient()
    return client.request("GET", f"/issue/{issue_id_or_key}/watchers")  # type: ignore[return-value]


def issue_watcher_add(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """POST /issue/{issueIdOrKey}/watchers - Add watcher.

    Jira expects a JSON string body containing the accountId.
    If account_id is None, adds the calling user.
    """
    client = JiraClient()
    # Send raw JSON string
    data = "null" if account_id is None else f"\"{account_id}\""
    return client.request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        data=data,
        content_type="application/json",
        accept="application/json",
    )  # type: ignore[return-value]


def issue_watcher_delete(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /issue/{issueIdOrKey}/watchers - Remove watcher."""
    client = JiraClient()
    params = clean_params({"accountId": account_id})
    return client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params=params)  # type: ignore[return-value]
