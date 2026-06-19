from typing import Any, Dict, List, Optional

from ._client import JiraClient


def get_user(
    client: JiraClient,
    *,
    account_id: Optional[str] = None,
    username: Optional[str] = None,
    key: Optional[str] = None,
    expand: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    if key is not None:
        params["key"] = key
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/user", params=params or None)


def create_user(client: JiraClient, user: Dict[str, Any]) -> Any:
    return client.request("POST", "/user", json=user)


def delete_user(
    client: JiraClient,
    *,
    account_id: str,
) -> Any:
    return client.request("DELETE", "/user", params={"accountId": account_id})


def bulk_get_users(
    client: JiraClient,
    account_ids: List[str],
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {"accountId": account_ids}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", "/user/bulk", params=params)


def get_user_groups(client: JiraClient, *, account_id: str) -> Any:
    return client.request("GET", "/user/groups", params={"accountId": account_id})


def search_users(
    client: JiraClient,
    query: str,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {"query": query}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", "/users/search", params=params)


def get_myself(client: JiraClient) -> Any:
    return client.request("GET", "/myself")
