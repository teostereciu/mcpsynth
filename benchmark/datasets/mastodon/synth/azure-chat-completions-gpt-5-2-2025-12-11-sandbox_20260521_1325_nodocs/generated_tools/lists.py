from typing import Any, Dict, Optional

from .client import MastodonClient


def list_lists(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/lists")


def get_list(client: MastodonClient, list_id: str) -> Any:
    return client.request("GET", f"/api/v1/lists/{list_id}")


def create_list(client: MastodonClient, title: str, replies_policy: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    return client.request("POST", "/api/v1/lists", json=payload)


def update_list(client: MastodonClient, list_id: str, title: Optional[str] = None, replies_policy: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    return client.request("PUT", f"/api/v1/lists/{list_id}", json=payload)


def delete_list(client: MastodonClient, list_id: str) -> Any:
    return client.request("DELETE", f"/api/v1/lists/{list_id}")


def add_accounts_to_list(client: MastodonClient, list_id: str, account_ids: list) -> Any:
    return client.request("POST", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})


def remove_accounts_from_list(client: MastodonClient, list_id: str, account_ids: list) -> Any:
    return client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})


def get_list_accounts(client: MastodonClient, list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/api/v1/lists/{list_id}/accounts", params=params or None)
