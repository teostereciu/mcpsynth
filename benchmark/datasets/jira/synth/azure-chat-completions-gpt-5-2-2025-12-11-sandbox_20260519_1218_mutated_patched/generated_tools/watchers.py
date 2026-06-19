from typing import Any, Dict, List, Optional

from ._client import JiraClient


def get_watchers(client: JiraClient, issue_id_or_key: str) -> Any:
    return client.request("GET", f"/issue/{issue_id_or_key}/watchers")


def add_watcher(client: JiraClient, issue_id_or_key: str, *, account_id: Optional[str] = None) -> Any:
    # Body is a JSON string (accountId) or empty to add self.
    body = account_id if account_id is not None else ""
    return client.request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        headers={"Content-Type": "application/json"},
        data=f"\"{body}\"" if body != "" else "\"\"",
    )


def remove_watcher(client: JiraClient, issue_id_or_key: str, *, account_id: str) -> Any:
    # Docs show user_id query param; in Cloud this is accountId.
    return client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


def is_watching_bulk(client: JiraClient, issue_ids: List[str]) -> Any:
    return client.request("POST", "/issue/watching", json={"issueIds": issue_ids})
